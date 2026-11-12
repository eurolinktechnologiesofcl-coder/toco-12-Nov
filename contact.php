<?php
/**
 * TOCO Technologies UAE — Enquiry Form Handler
 * Compatible with Linux / cPanel PHP 7.4+ and 8.x hosting.
 */
declare(strict_types=1);

header('Content-Type: application/json; charset=UTF-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store, no-cache, must-revalidate');

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    http_response_code(405);
    echo json_encode([
        'ok' => false,
        'message' => 'Method not allowed. Please submit the form from the website.'
    ]);
    exit;
}

// Parse JSON or standard URL-encoded / multipart POST body
$rawBody = file_get_contents('php://input');
$input = [];
if (!empty($_POST)) {
    $input = $_POST;
} elseif (!empty($rawBody)) {
    $decoded = json_decode($rawBody, true);
    if (is_array($decoded)) {
        $input = $decoded;
    }
}

function str_len_utf8(string $s): int {
    return function_exists('mb_strlen') ? mb_strlen($s, 'UTF-8') : strlen($s);
}

function str_sub_utf8(string $s, int $start, int $len): string {
    return function_exists('mb_substr') ? mb_substr($s, $start, $len, 'UTF-8') : substr($s, $start, $len);
}

/**
 * Strip header injection characters and normalize whitespace.
 */
function clean_single_line(string $val, int $maxLen = 160): string {
    $val = str_replace(["\r", "\n", "%0a", "%0d", "%0A", "%0D", "\0"], ' ', $val);
    $val = preg_replace('/\s+/u', ' ', trim($val)) ?? trim($val);
    return str_sub_utf8($val, 0, $maxLen);
}

function clean_multiline(string $val, int $maxLen = 3000): string {
    $val = str_replace(["\r\n", "\r", "\0"], ["\n", "\n", ''], trim($val));
    return str_sub_utf8($val, 0, $maxLen);
}

// 1. Spam Protection — Honeypot check
$honeypot = trim((string)($input['website_url'] ?? ''));
if ($honeypot !== '') {
    http_response_code(422);
    echo json_encode([
        'ok' => false,
        'message' => 'Spam submission rejected.'
    ]);
    exit;
}

// 2. Spam Protection — Form timing check (blocks instant bot POSTs)
$formTs = isset($input['form_ts']) ? (int)$input['form_ts'] : 0;
$nowMs  = (int)round(microtime(true) * 1000);
if ($formTs > 0) {
    $elapsedMs = $nowMs - $formTs;
    if ($elapsedMs < 1500 || $elapsedMs > 86400000) {
        http_response_code(422);
        echo json_encode([
            'ok' => false,
            'message' => 'Form session expired or submitted too quickly. Please refresh the page and try again.'
        ]);
        exit;
    }
}

// 3. Spam Protection — Lightweight per-IP rate limiting (max 5 requests / 15 minutes)
$clientIp = $_SERVER['REMOTE_ADDR'] ?? '0.0.0.0';
$rateFile = rtrim(sys_get_temp_dir(), DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . 'toco_rate_' . md5($clientIp) . '.json';
$windowSec = 900;
$maxRequests = 5;
$nowSec = time();
$timestamps = [];

if (is_file($rateFile)) {
    $stored = @file_get_contents($rateFile);
    $parsed = $stored ? json_decode($stored, true) : [];
    if (is_array($parsed)) {
        foreach ($parsed as $ts) {
            if (is_int($ts) && ($nowSec - $ts) < $windowSec) {
                $timestamps[] = $ts;
            }
        }
    }
}

if (count($timestamps) >= $maxRequests) {
    http_response_code(429);
    echo json_encode([
        'ok' => false,
        'message' => 'Too many enquiries sent recently. Please call us on +971 4 577 0725 or message us on WhatsApp.'
    ]);
    exit;
}

// 4. Extract & Validate Fields
$fullName = clean_single_line((string)($input['full_name'] ?? ''), 120);
$email    = clean_single_line((string)($input['email'] ?? ''), 160);
$phone    = clean_single_line((string)($input['phone'] ?? ''), 40);
$company  = clean_single_line((string)($input['company'] ?? ''), 140);
$service  = clean_single_line((string)($input['service'] ?? ''), 120);
$message  = clean_multiline((string)($input['message'] ?? ''), 3000);

$errors = [];

if (str_len_utf8($fullName) < 2) {
    $errors['full_name'] = 'Please enter your full name.';
}

if ($email === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors['email'] = 'Please enter a valid business email address.';
}

$digitsOnly = preg_replace('/\D+/', '', $phone) ?? '';
if (strlen($digitsOnly) < 7 || strlen($digitsOnly) > 16 || !preg_match('/^[+\d\s().\-]{7,24}$/', $phone)) {
    $errors['phone'] = 'Please enter a valid UAE or international phone number.';
}

$allowedServices = [
    'Website Design & Development',
    'Mobile Application Development',
    'E-Commerce Development',
    'Custom Software & ERP Solutions',
    'Search Engine Optimization (SEO)',
    'Digital Marketing',
    'Social Media Management',
    'Branding & Graphic Design',
    'Website Maintenance & Support',
    'Other / General Consultation'
];
if ($service === '' || !in_array($service, $allowedServices, true)) {
    $errors['service'] = 'Please select the service required.';
}

if (str_len_utf8($message) < 15) {
    $errors['message'] = 'Please briefly describe your project requirements (at least 15 characters).';
}

// Reject excessive URL spam in message body
if (preg_match_all('/https?:\/\//i', $message) > 3) {
    $errors['message'] = 'Please remove multiple external links from your project description.';
}

if (!empty($errors)) {
    http_response_code(422);
    echo json_encode([
        'ok' => false,
        'message' => 'Please check the highlighted fields and try again.',
        'errors' => $errors
    ]);
    exit;
}

// 5. Compose & Send Enquiry Email to Verified TOCO Business Inbox
$recipient = 'info@tocoplus.com';
$host = preg_replace('/[^a-zA-Z0-9.\-]/', '', $_SERVER['SERVER_NAME'] ?? 'tocotechnologies.ae');
if ($host === '' || $host === 'localhost' || filter_var($host, FILTER_VALIDATE_IP)) {
    $host = 'tocotechnologies.ae';
}
$fromAddress = 'noreply@' . $host;
$subject = 'New Project Enquiry [' . $service . '] — ' . $fullName;

$safeName    = htmlspecialchars($fullName, ENT_QUOTES, 'UTF-8');
$safeEmail   = htmlspecialchars($email, ENT_QUOTES, 'UTF-8');
$safePhone   = htmlspecialchars($phone, ENT_QUOTES, 'UTF-8');
$safeCompany = htmlspecialchars($company !== '' ? $company : 'Not specified', ENT_QUOTES, 'UTF-8');
$safeService = htmlspecialchars($service, ENT_QUOTES, 'UTF-8');
$safeMessage = nl2br(htmlspecialchars($message, ENT_QUOTES, 'UTF-8'));
$submittedAt = gmdate('Y-m-d H:i:s') . ' UTC';

$htmlBody = <<<HTML
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"></head>
<body style="margin:0;padding:24px;background:#F5F7FB;font-family:Arial,Helvetica,sans-serif;color:#111827;">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="max-width:620px;margin:0 auto;background:#FFFFFF;border:1px solid #E2E8F0;border-radius:10px;overflow:hidden;">
    <tr>
      <td style="background:#0B1220;padding:22px 28px;color:#FFFFFF;">
        <div style="font-size:12px;letter-spacing:1.2px;text-transform:uppercase;color:#397BFF;font-weight:bold;">TOCO Technologies UAE</div>
        <h1 style="margin:6px 0 0;font-size:20px;font-weight:700;color:#FFFFFF;">New Website Project Enquiry</h1>
      </td>
    </tr>
    <tr>
      <td style="padding:24px 28px;">
        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;font-size:14px;">
          <tr><td style="padding:8px 0;color:#64748B;width:150px;">Full Name</td><td style="padding:8px 0;font-weight:600;color:#111827;">{$safeName}</td></tr>
          <tr><td style="padding:8px 0;color:#64748B;">Business Email</td><td style="padding:8px 0;"><a href="mailto:{$safeEmail}" style="color:#2563EB;text-decoration:none;">{$safeEmail}</a></td></tr>
          <tr><td style="padding:8px 0;color:#64748B;">Phone Number</td><td style="padding:8px 0;"><a href="tel:{$safePhone}" style="color:#2563EB;text-decoration:none;">{$safePhone}</a></td></tr>
          <tr><td style="padding:8px 0;color:#64748B;">Company Name</td><td style="padding:8px 0;color:#111827;">{$safeCompany}</td></tr>
          <tr><td style="padding:8px 0;color:#64748B;">Service Required</td><td style="padding:8px 0;font-weight:600;color:#2563EB;">{$safeService}</td></tr>
        </table>
        <div style="margin-top:18px;padding:16px;background:#F5F7FB;border-left:3px solid #2563EB;border-radius:4px;">
          <div style="font-size:12px;font-weight:700;text-transform:uppercase;color:#64748B;margin-bottom:8px;">Project Description</div>
          <div style="font-size:14px;line-height:1.6;color:#111827;">{$safeMessage}</div>
        </div>
        <p style="margin:20px 0 0;font-size:12px;color:#64748B;">Submitted on {$submittedAt} from tocotechnologies.ae</p>
      </td>
    </tr>
  </table>
</body>
</html>
HTML;

$headers = [
    'MIME-Version: 1.0',
    'Content-Type: text/html; charset=UTF-8',
    'From: TOCO Technologies Website <' . $fromAddress . '>',
    'Reply-To: ' . $fullName . ' <' . $email . '>',
    'X-Mailer: TOCO-Web-Handler/1.0'
];

$encodedSubject = '=?UTF-8?B?' . base64_encode($subject) . '?=';
$sent = @mail($recipient, $encodedSubject, $htmlBody, implode("\r\n", $headers));

if (!$sent) {
    http_response_code(500);
    echo json_encode([
        'ok' => false,
        'message' => 'Our mail server could not dispatch your message right now. Please contact us directly at info@tocoplus.com, call +971 4 577 0725, or message us on WhatsApp.'
    ]);
    exit;
}

// Record rate-limit timestamp only on successful dispatch
$timestamps[] = $nowSec;
@file_put_contents($rateFile, json_encode($timestamps), LOCK_EX);

echo json_encode([
    'ok' => true,
    'message' => 'Thank you, ' . $fullName . '. Your project enquiry has been sent to our Dubai team. We will get back to you promptly.'
]);

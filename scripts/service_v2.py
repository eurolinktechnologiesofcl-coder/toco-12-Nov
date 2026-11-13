#!/usr/bin/env python3
"""
TOCO Technologies — Service Page Template v2 (High-Variety Premium Layout)

Currently applied to /services/ai-automation as a single-page design preview.
Replaces uniform box grids with interactive Department Workflow Studio,
asymmetric bento modules, split comparison consoles, and distinct feature cards.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_data import SERVICES_DATA
from build_full_site import (
    SITE_BASE, ROOT_DIR, render_head_tags, render_header, render_footer,
    render_breadcrumbs, make_breadcrumb_schema, make_faq_schema, render_cta_band,
)
from icons import svg, EMOJI_MAP
from bento_data import SERVICE_META, get_bento_html

V2_SLUGS = [
    "ai-automation",
    "ai-business-automation",
    "mobile-app-development",
    "website-and-software-development",
    "digital-marketing",
    "seo",
    "ecommerce-development",
    "erp-and-custom-software",
    "social-media-management",
    "branding-and-ui-ux-design",
]

EXTRA = {
    "ai-automation": {
        "pill": "AI Automation • Dubai, UAE",
        "pill_note": "Autonomous Workflow Execution",
        "h1_html": 'AI Automation &amp; <span class="grad-text">Autonomous Agents</span> for Dubai Businesses',
        "hero_points": ["Human-in-the-loop approvals", "UAE data residency options", "30-day post-launch warranty"],
        "integrations": [
            "OpenAI GPT-4o", "Anthropic Claude", "WhatsApp Cloud API", "Microsoft 365",
            "Google Workspace", "Zoho ERP", "HubSpot", "PostgreSQL", "SAP", "AWS UAE"
        ],
        "console": [
            ("file-text", "Invoice received", "accounts@supplier.ae · PDF attached", "done", "Done"),
            ("search", "Data extracted", "Vendor TRN, line items, 5% VAT", "done", "Done"),
            ("layers", "Matched against ERP", "Checking PO #9481 & Goods Receipt", "run", "Running"),
            ("message", "Manager approval", "One-tap sign-off on WhatsApp", "wait", "Queued"),
        ],
        "before": [
            "Staff manually re-key invoices, bills, and purchase orders into ERP",
            "Approvals stall in buried email threads and unanswered phone calls",
            "Discrepancies and math errors surface only at month-end closing",
            "Operations completely halt after 6:00 PM, on weekends, and holidays",
            "Zero centralized audit trail of who modified records, when, or why",
        ],
        "after": [
            "Documents are ingested, verified, and posted to ERP in under 5 seconds",
            "Instant manager sign-offs sent directly to WhatsApp with 1-tap approval",
            "Pre-posting validation rules catch discrepancies before records commit",
            "Autonomous agents run 24/7/365 through nights, weekends, and holidays",
            "Cryptographic audit log records every prompt, decision, and ERP write",
        ],
        "durations": ["Days 1–5", "Days 6–14", "Weeks 3–4", "Launch + 30 Days"],
        "departments": [
            {
                "id": "finance",
                "label": "Finance & Accounts",
                "icon": "wallet",
                "badge": "Finance & Accounts Automation",
                "headline": "Close month-end 4x faster with self-processing invoices and instant 3-way reconciliation.",
                "desc": "Eliminate manual data entry from supplier invoices, utility bills, and purchase orders. Our AI agents extract Arabic and English text, verify UAE TRNs against Federal Tax Authority rules, check goods receipts in your ERP, and draft payment schedules.",
                "metrics": [
                    ("zap", "18.5 hrs saved / week"),
                    ("badge-check", "99.8% extraction precision")
                ],
                "steps": [
                    "Ingests incoming PDF invoices from supplier emails and WhatsApp",
                    "Extracts vendor details, line items, and calculates 5% UAE VAT",
                    "Matches against Purchase Orders (PO) and Goods Received Notes (GRN)",
                    "Dispatches WhatsApp approval for invoices exceeding threshold",
                    "Posts approved transaction directly to ERP accounting ledger"
                ],
                "sim_title": "toco-agent / finance-sentinel",
                "sim_status": "Validated",
                "sim_rows": [
                    ("Scanned Document", "INV-2024-8902 · Al Futtaim Engineering LLC", "normal"),
                    ("TRN Check", "100293849100003 · Validated via FTA UAE Registry", "ok"),
                    ("Subtotal", "AED 14,200.00", "normal"),
                    ("VAT (5%)", "AED 710.00", "accent"),
                    ("Total Amount", "AED 14,910.00", "normal"),
                    ("3-Way Match", "PO #PO-4410 Matched (100% Item & Price Alignment)", "ok")
                ],
                "sim_footer_speed": "3.4s",
                "sim_footer_status": "Ready to Post to ERP"
            },
            {
                "id": "logistics",
                "label": "Logistics & Operations",
                "icon": "truck",
                "badge": "Logistics & Dispatch Automation",
                "headline": "Keep drivers, dispatchers, and clients in sync with real-time POD capture and manifest OCR.",
                "desc": "Delivery notes, customs clearance forms, and bills of lading are ingested instantly. Drivers upload delivery photos via WhatsApp, and our agent extracts the signature, stamps time & GPS coordinates, updates the dispatch console, and notifies the client.",
                "metrics": [
                    ("zap", "12 mins saved per delivery"),
                    ("badge-check", "Zero lost delivery slips")
                ],
                "steps": [
                    "Parses scanned delivery notes, customs bills, and shipping manifests",
                    "Extracts driver signatures and proof of delivery (POD) from photos",
                    "Live updates shipment status in your fleet management system",
                    "Sends automatic WhatsApp delivery confirmation to the recipient",
                    "Triggers instant customer billing upon verified delivery"
                ],
                "sim_title": "toco-agent / dispatch-telemetry",
                "sim_status": "POD Confirmed",
                "sim_rows": [
                    ("Shipment Ref", "Shipment #DXB-9921 · JAFZA South Zone 4", "normal"),
                    ("Driver Upload", "Delivery Note #DN-5541 (WhatsApp Photo Received)", "normal"),
                    ("Signature OCR", "Customer Signature Verified & Time-stamped (14:32 GST)", "ok"),
                    ("Warehouse ERP", "Inventory Decremented & Manifest Closed", "ok"),
                    ("Client Alert", "WhatsApp delivery confirmation dispatched with signed POD", "accent")
                ],
                "sim_footer_speed": "2.1s",
                "sim_footer_status": "Dispatch Status: Delivered"
            },
            {
                "id": "sales",
                "label": "Sales & Inquiries",
                "icon": "message",
                "badge": "Sales & Pipeline Automation",
                "headline": "Qualify, quote, and schedule warm inbound inquiries within 20 seconds, 24 hours a day.",
                "desc": "Never lose a prospective client to delayed follow-ups. Our sales agents respond instantly across WhatsApp, web forms, and email, answer technical product questions, qualify budget and timeline, and draft tailored PDF quotations.",
                "metrics": [
                    ("zap", "18-second response latency"),
                    ("trending-up", "3.2x higher consultation booking rate")
                ],
                "steps": [
                    "Instant conversational greeting and intent detection on WhatsApp",
                    "Intelligent qualification based on service scope, budget, and urgency",
                    "Real-time calendar availability check and meeting booking",
                    "Instant quotation PDF generation based on pricing matrix",
                    "Automatic CRM contact and deal stage creation"
                ],
                "sim_title": "toco-agent / sales-concierge",
                "sim_status": "Response: 18s",
                "sim_rows": [
                    ("Client Inquiry", "Hi, we need custom ERP software for 40 users in Business Bay", "normal"),
                    ("AI Response", "Hello! We engineer custom ERPs with UAE VAT & WPS. What is your rollout timeline?", "accent"),
                    ("Qualification Score", "92/100 (Enterprise Tier, High Intent)", "ok"),
                    ("Action Taken", "Meeting booked on Senior Engineer calendar", "ok"),
                    ("CRM Update", "Deal created in Zoho CRM (AED 35,000 Pipeline)", "normal")
                ],
                "sim_footer_speed": "18s",
                "sim_footer_status": "Calendar Invite Dispatched"
            },
            {
                "id": "hr",
                "label": "HR & Administration",
                "icon": "users",
                "badge": "HR & Workforce Automation",
                "headline": "Eliminate repetitive paperwork, visa tracking, and compliance checks from your HR desk.",
                "desc": "Automate Emirates ID renewals, visa expiries, and MOHRE labour compliance. New joiners upload their documents via a simple link, and our agent verifies validity, generates employment contracts, and provisions company accounts.",
                "metrics": [
                    ("zap", "100% On-time visa renewals"),
                    ("shield", "Zero MOHRE fines")
                ],
                "steps": [
                    "Automated Emirates ID & passport expiry sentinel monitoring",
                    "Document OCR extraction for new hire onboarding paperwork",
                    "Automated MOHRE labour contract drafting & compliance verification",
                    "Instant leave request routing and balance calculation",
                    "Employee policy Q&A assistant trained on your staff handbook"
                ],
                "sim_title": "toco-agent / hr-compliance",
                "sim_status": "Sentinel Active",
                "sim_rows": [
                    ("Expiry Detection", "Emirates ID for 3 employees expiring in < 30 days", "normal"),
                    ("Action Triggered", "Automated WhatsApp renewal checklist sent to employee", "accent"),
                    ("Document Upload", "Passport copy & photo received and verified via OCR", "ok"),
                    ("MOHRE Check", "WPS salary compliance validated for upcoming cycle", "ok"),
                    ("HR Dossier", "Renewal dossier compiled and assigned to PRO for submission", "normal")
                ],
                "sim_footer_speed": "Continuous",
                "sim_footer_status": "0 Non-Compliance Violations"
            }
        ]
    },

    # -------------------------------------------------------------------------
    "ai-business-automation": {
        "pill": "AI Sales Automation • Dubai, UAE",
        "pill_note": "Lead Capture & Conversion Engine",
        "h1_html": 'AI Business Automation for <span class="grad-text">High-Impact Conversions</span> in Dubai',
        "hero_points": ["18-second WhatsApp response", "Automated CRM sync", "30-day post-launch warranty"],
        "integrations": [
            "WhatsApp Business API", "HubSpot CRM", "Zoho CRM", "Salesforce",
            "OpenAI GPT-4o", "Google Calendar", "Calendly", "Twilio", "Mailchimp", "Slack"
        ],
        "console": [
            ("message", "Inquiry received", "ahmed@example.ae · Website form", "done", "Done"),
            ("search", "Intent classified", "ERP software · 40 users · Business Bay", "done", "Done"),
            ("zap", "AI response sent", "Personalized WhatsApp reply dispatched in 18s", "run", "Running"),
            ("calendar", "Meeting booked", "Senior Engineer slot confirmed", "wait", "Queued"),
        ],
        "before": [
            "Leads sit unread in email inboxes for hours or even days",
            "Sales reps manually qualify every inquiry over long phone calls",
            "No follow-up system — high-intent leads go cold and choose competitors",
            "CRM entries are created inconsistently and miss deal details",
            "Team capacity limits responses to UAE business hours only",
        ],
        "after": [
            "Every inquiry gets an intelligent, personalized reply in under 18 seconds",
            "AI qualifies lead intent, budget, and urgency automatically",
            "Warm leads are nurtured with follow-up sequences until booking confirmed",
            "CRM deal, contact, and pipeline stage created instantly and accurately",
            "Conversion engine runs 24/7 — evenings, weekends, and UAE public holidays",
        ],
        "durations": ["Days 1–3", "Days 4–10", "Weeks 2–3", "Launch + 30 Days"],
        "departments": [
            {
                "id": "inbound",
                "label": "Inbound Lead Capture",
                "icon": "message",
                "badge": "Inbound Lead Automation",
                "headline": "Capture and qualify every web, WhatsApp, and email inquiry within 18 seconds.",
                "desc": "Our AI sales concierge responds to inquiries across all channels instantly. It identifies the service needed, extracts key qualification signals (budget, timeline, company size), and routes hot prospects directly to your senior sales team.",
                "metrics": [
                    ("zap", "18-second average response"),
                    ("trending-up", "3.2x higher booking rate"),
                ],
                "steps": [
                    "AI monitors WhatsApp, website form, and email channels simultaneously",
                    "Detects inquiry intent and service category from natural language",
                    "Sends personalized response with relevant case studies and pricing range",
                    "Scores lead quality (budget, urgency, decision authority) on a 100-point scale",
                    "Routes high-score leads to senior engineer calendar for instant booking",
                ],
                "sim_title": "toco-agent / sales-concierge",
                "sim_status": "Response: 18s",
                "sim_rows": [
                    ("Inquiry Source", "WhatsApp · +971 55 234 5678", "normal"),
                    ("Message", "Need CRM for our 25-person real estate agency in JLT", "normal"),
                    ("Intent Score", "91/100 — High Intent, Real Estate CRM", "ok"),
                    ("AI Reply Sent", "Personalized solution overview dispatched in 16s", "ok"),
                    ("CRM Deal Created", "AED 28,000 pipeline · Zoho CRM stage: Qualified", "accent"),
                ],
                "sim_footer_speed": "16s",
                "sim_footer_status": "Meeting Invite Dispatched",
            },
            {
                "id": "followup",
                "label": "Automated Follow-Up",
                "icon": "trending-up",
                "badge": "Lead Nurture Automation",
                "headline": "Re-engage cold leads automatically until they book a consultation.",
                "desc": "Most leads need 3-7 touch points before converting. Our AI nurture sequences send personalized follow-ups at optimal intervals, reference past conversations, and pivot message tone based on engagement signals.",
                "metrics": [
                    ("badge-check", "68% re-engagement rate"),
                    ("zap", "5-touchpoint automated sequence"),
                ],
                "steps": [
                    "Tags leads as warm, cold, or dormant based on engagement patterns",
                    "Dispatches day-3, day-7, and day-14 follow-up messages via WhatsApp",
                    "Personalizes each message referencing the original inquiry context",
                    "Escalates highly engaged leads to live sales rep intervention",
                    "Removes opted-out contacts and maintains clean GDPR-safe data",
                ],
                "sim_title": "toco-agent / nurture-sequence",
                "sim_status": "Day 7 Follow-Up",
                "sim_rows": [
                    ("Lead Status", "Cold — no reply after initial outreach", "normal"),
                    ("Trigger", "Day-7 nurture sequence activated", "accent"),
                    ("Message Sent", "Hi Ahmed, still exploring ERP options? We built one for a Dubai logistics firm last month.", "normal"),
                    ("Engagement", "Read receipt confirmed · Link opened (3 times)", "ok"),
                    ("Re-escalated", "Lead moved to Active — booked intro call", "ok"),
                ],
                "sim_footer_speed": "Automated",
                "sim_footer_status": "Lead Reactivated",
            },
            {
                "id": "quotation",
                "label": "AI Quotation Engine",
                "icon": "file-text",
                "badge": "Automated Proposal Generation",
                "headline": "Generate professional UAE-formatted quotation PDFs in under 60 seconds.",
                "desc": "Once a lead is qualified, our AI generates a branded PDF proposal with the client's name, project scope, UAE VAT-inclusive pricing, timeline, and terms — dispatched via WhatsApp instantly without human effort.",
                "metrics": [
                    ("zap", "60-second proposal generation"),
                    ("badge-check", "UAE VAT 5% auto-calculated"),
                ],
                "steps": [
                    "Extracts project scope from the qualification conversation history",
                    "Looks up pricing matrix for selected service tier and add-ons",
                    "Calculates UAE VAT 5% and generates AED-denominated line items",
                    "Renders branded PDF with TOCO letterhead, logo, and payment terms",
                    "Sends PDF directly to client WhatsApp and CC's the account manager",
                ],
                "sim_title": "toco-agent / proposal-generator",
                "sim_status": "PDF Ready",
                "sim_rows": [
                    ("Client", "Khalid Al-Mansouri · Prestige Properties LLC", "normal"),
                    ("Service", "Real Estate CRM · 15 Users · 90-Day Build", "normal"),
                    ("Subtotal", "AED 42,000.00", "normal"),
                    ("VAT (5%)", "AED 2,100.00", "accent"),
                    ("Total", "AED 44,100.00 · Terms: 50/50 Milestone", "ok"),
                ],
                "sim_footer_speed": "58s",
                "sim_footer_status": "Proposal Dispatched via WhatsApp",
            },
        ],
    },

    # -------------------------------------------------------------------------
    "mobile-app-development": {
        "pill": "Mobile App Development • Dubai, UAE",
        "pill_note": "iOS & Android Engineering",
        "h1_html": 'Mobile App <span class="grad-text">Software Engineering</span> in Dubai, UAE',
        "hero_points": ["Flutter & Native iOS/Android", "Arabic RTL & bilingual UX", "30-day post-launch warranty"],
        "integrations": [
            "Flutter", "Swift", "Kotlin", "Firebase", "AWS UAE",
            "Stripe", "Tabby", "WhatsApp API", "Google Maps", "Apple Pay"
        ],
        "console": [
            ("smartphone", "Sprint 1 complete", "Authentication & onboarding flow", "done", "Done"),
            ("layers", "API integration", "REST endpoints connected to ERP backend", "done", "Done"),
            ("zap", "App Store build", "iOS & Android builds compiling", "run", "Running"),
            ("badge-check", "QA testing", "Device matrix testing queued", "wait", "Queued"),
        ],
        "before": [
            "Business processes rely on manual WhatsApp messages and Excel spreadsheets",
            "Field teams have no real-time visibility into inventory or job status",
            "Customer communication is slow, inconsistent, and entirely manual",
            "No branded mobile presence — competitors have polished consumer apps",
            "Data is siloed across email threads and cannot be analysed centrally",
        ],
        "after": [
            "Staff and customers interact via a branded, purpose-built mobile app",
            "Field teams get live job assignments, GPS navigation, and instant POD capture",
            "Push notifications keep customers informed at every stage of their order",
            "Managers monitor live KPIs on an in-app analytics dashboard",
            "All data syncs to your cloud ERP in real time for unified reporting",
        ],
        "durations": ["Days 1–7", "Weeks 2–5", "Weeks 6–10", "Launch + 30 Days"],
        "departments": [
            {
                "id": "consumer",
                "label": "Consumer Apps",
                "icon": "smartphone",
                "badge": "Consumer Mobile Engineering",
                "headline": "Launch a polished, App Store–ready consumer app in under 12 weeks.",
                "desc": "From e-commerce platforms to on-demand service marketplaces, we engineer native-quality Flutter apps with seamless UAE payment gateways (Tabby, Apple Pay, Stripe), Arabic RTL layouts, and sub-second load performance.",
                "metrics": [
                    ("zap", "12-week average delivery"),
                    ("badge-check", "4.8★ App Store average rating"),
                ],
                "steps": [
                    "UX wireframes and Arabic/English bilingual design system creation",
                    "Flutter development with clean MVVM architecture and state management",
                    "Tabby BNPL, Apple Pay, and UAE card payment gateway integration",
                    "Firebase push notifications, analytics, and crash monitoring setup",
                    "App Store Connect and Google Play submission with full ASO metadata",
                ],
                "sim_title": "toco-build / consumer-app",
                "sim_status": "Release Ready",
                "sim_rows": [
                    ("Platform", "iOS 17+ · Android 12+ · Flutter 3.19", "normal"),
                    ("Screen Count", "42 screens implemented and QA approved", "ok"),
                    ("Payment Flow", "Apple Pay + Tabby BNPL + Card — all tested", "ok"),
                    ("Lighthouse Score", "98/100 · LCP 1.2s · CLS 0.01", "ok"),
                    ("Store Submission", "App Store & Play Store — both live", "accent"),
                ],
                "sim_footer_speed": "11.5 weeks",
                "sim_footer_status": "Live in Both App Stores",
            },
            {
                "id": "enterprise",
                "label": "Enterprise Field Apps",
                "icon": "building",
                "badge": "Enterprise Mobile Engineering",
                "headline": "Equip field teams with real-time dispatch, job tracking, and POD capture apps.",
                "desc": "We build high-reliability enterprise mobile apps for logistics drivers, field service technicians, and sales reps — with offline-first capability, biometric login, GPS live tracking, and direct ERP sync.",
                "metrics": [
                    ("zap", "Real-time ERP sync in 200ms"),
                    ("shield", "Biometric auth + offline mode"),
                ],
                "steps": [
                    "Role-based access design for field staff, supervisors, and admin",
                    "Offline-first SQLite caching with intelligent background sync",
                    "GPS tracking, geofencing, and route optimization integration",
                    "Camera-powered POD capture with OCR signature extraction",
                    "ERP REST API sync with conflict resolution and retry logic",
                ],
                "sim_title": "toco-build / field-operations-app",
                "sim_status": "Synced",
                "sim_rows": [
                    ("Driver", "Mohamed Al-Rashid · Vehicle DXB-4421", "normal"),
                    ("Job Assigned", "Delivery #DXB-9921 · Al Quoz Industrial 4", "normal"),
                    ("GPS Status", "On route · ETA 14 mins", "ok"),
                    ("POD Captured", "Customer signature extracted · Time-stamped", "ok"),
                    ("ERP Update", "Delivery closed · Invoice triggered in 200ms", "accent"),
                ],
                "sim_footer_speed": "200ms",
                "sim_footer_status": "ERP Synced & Invoice Triggered",
            },
            {
                "id": "saas",
                "label": "SaaS Dashboards",
                "icon": "bar-chart",
                "badge": "SaaS Product Engineering",
                "headline": "Launch a subscription SaaS product with multi-tenant isolation and in-app billing.",
                "desc": "We engineer full-stack SaaS mobile products with Stripe or Payfort subscription billing, multi-tenant data isolation, in-app analytics dashboards, and automated onboarding flows to reduce churn from day one.",
                "metrics": [
                    ("trending-up", "Full subscription billing"),
                    ("badge-check", "Multi-tenant isolation"),
                ],
                "steps": [
                    "SaaS pricing tier design and subscription plan architecture",
                    "Stripe / Payfort recurring billing integration with webhook sync",
                    "Multi-tenant database schema with strict row-level security",
                    "In-app usage analytics dashboard with exportable reports",
                    "Automated trial-to-paid conversion email and push sequence",
                ],
                "sim_title": "toco-build / saas-platform",
                "sim_status": "Subscription Active",
                "sim_rows": [
                    ("Tenant", "Gulf Logistics Solutions LLC · Plan: Enterprise", "normal"),
                    ("Billing", "AED 1,200 / month · Stripe recurring", "accent"),
                    ("Active Users", "34 / 50 seats · Onboarded last 48h", "ok"),
                    ("Usage", "API calls: 48,210 this month · Under quota", "ok"),
                    ("Churn Risk", "Low — 100% feature engagement score", "ok"),
                ],
                "sim_footer_speed": "Real-time",
                "sim_footer_status": "Subscription Renewed Automatically",
            },
        ],
    },

    # -------------------------------------------------------------------------
    "website-and-software-development": {
        "pill": "Web Development • Dubai, UAE",
        "pill_note": "Enterprise Websites & Software",
        "h1_html": 'Website & Custom Software <span class="grad-text">Engineering</span> in Dubai, UAE',
        "hero_points": ["Sub-380ms TTFB on UAE CDN", "Core Web Vitals 90+ score", "30-day post-launch warranty"],
        "integrations": [
            "Next.js", "React", "Node.js", "PostgreSQL", "Cloudflare",
            "AWS UAE", "Stripe", "Tabby", "Google Analytics 4", "HubSpot"
        ],
        "console": [
            ("globe", "Domain & SSL configured", "tocotechnologies.ae · Cloudflare CDN", "done", "Done"),
            ("zap", "Build deployed", "Static site 98/100 Lighthouse · 320ms TTFB", "done", "Done"),
            ("search", "SEO audit passed", "Schema markup & Core Web Vitals validated", "run", "Running"),
            ("bar-chart", "Analytics live", "GA4 event tracking going live", "wait", "Queued"),
        ],
        "before": [
            "Website loads in 6+ seconds — users bounce before the page appears",
            "No clear contact journey — visitors leave without converting to leads",
            "Site is not indexed on Google for Dubai or UAE service keywords",
            "Outdated WordPress install with security vulnerabilities and plugin bloat",
            "Mobile layout is broken — 60%+ of UAE traffic is mobile-first users",
        ],
        "after": [
            "Sub-380ms TTFB from UAE edge nodes — faster than 98% of competitors",
            "Conversion-optimised layout drives 3x more consultation bookings",
            "Full technical SEO with structured data, sitemap, and Core Web Vitals green",
            "Zero-dependency static architecture — no plugins, no maintenance overhead",
            "Perfect mobile-first responsive design tested across 20+ UAE device profiles",
        ],
        "durations": ["Days 1–5", "Days 6–18", "Days 19–25", "Launch + 30 Days"],
        "departments": [
            {
                "id": "corporate",
                "label": "Corporate Websites",
                "icon": "globe",
                "badge": "Corporate Web Engineering",
                "headline": "Launch a 99/100 Lighthouse corporate website that ranks, converts, and loads instantly.",
                "desc": "We engineer static-first corporate websites using modern JAMstack — sub-second loading from UAE CDN edge nodes, semantic HTML5, complete structured data, and conversion-optimised section design that turns visitors into consultation bookings.",
                "metrics": [
                    ("zap", "Sub-380ms TTFB from UAE edge"),
                    ("badge-check", "98–100 Lighthouse score"),
                ],
                "steps": [
                    "Discovery sprint — competitor SEO audit and conversion architecture planning",
                    "Figma wireframes and mobile-first responsive design system creation",
                    "Static HTML/CSS/JS build with zero dependencies and Cloudflare CDN deployment",
                    "Full technical SEO: structured data, canonical tags, sitemap, robots.txt",
                    "GA4 event tracking, heatmap setup, and 30-day monitoring handover",
                ],
                "sim_title": "toco-build / corporate-site",
                "sim_status": "Live",
                "sim_rows": [
                    ("Lighthouse Performance", "99 / 100", "ok"),
                    ("TTFB (UAE CDN)", "318ms · Cloudflare Middle East", "ok"),
                    ("Core Web Vitals", "LCP 1.1s · CLS 0.00 · INP 42ms — all Green", "ok"),
                    ("SEO Score", "98 / 100 · 0 broken links · schema validated", "ok"),
                    ("Mobile Score", "98 / 100 · tested on 20 UAE device profiles", "accent"),
                ],
                "sim_footer_speed": "318ms",
                "sim_footer_status": "Live — 99/100 Lighthouse",
            },
            {
                "id": "portal",
                "label": "Client Portals",
                "icon": "layout",
                "badge": "Web App & Portal Engineering",
                "headline": "Build secure client portals, dashboards, and B2B SaaS platforms for UAE enterprises.",
                "desc": "From vendor portals to real estate client dashboards, we engineer authenticated web applications with role-based access, encrypted data storage, full audit trails, and seamless ERP/CRM integration built for the UAE regulatory environment.",
                "metrics": [
                    ("shield", "RBAC & AES-256 encryption"),
                    ("zap", "Real-time ERP data sync"),
                ],
                "steps": [
                    "Role and permission architecture design for all user types",
                    "React or Next.js frontend with TypeScript and design system",
                    "Node.js REST API with PostgreSQL database and JWT authentication",
                    "ERP or CRM integration via webhook or REST API endpoints",
                    "Security audit, penetration testing, and production deployment on AWS UAE",
                ],
                "sim_title": "toco-build / client-portal",
                "sim_status": "Portal Active",
                "sim_rows": [
                    ("Logged In As", "Omar Al-Farouq · Vendor Manager · Role: Finance", "normal"),
                    ("Invoice Upload", "INV-2024-882 uploaded and auto-processed", "ok"),
                    ("Approval Status", "Pending CFO sign-off via WhatsApp", "accent"),
                    ("Audit Trail", "Action logged: 2026-11-13 09:42 GST", "ok"),
                    ("ERP Sync", "SAP updated — PO #7821 matched", "ok"),
                ],
                "sim_footer_speed": "Real-time",
                "sim_footer_status": "Portal Live — 0 Incidents",
            },
            {
                "id": "api",
                "label": "API & Integrations",
                "icon": "code",
                "badge": "API Engineering & Integration",
                "headline": "Connect your disconnected business systems with clean REST APIs and webhook pipelines.",
                "desc": "We architect and build production-grade REST and GraphQL APIs that connect your website, ERP, CRM, payment gateway, and third-party platforms — eliminating data silos and manual re-keying across your UAE enterprise stack.",
                "metrics": [
                    ("zap", "API response < 80ms median"),
                    ("badge-check", "Zero data silos guaranteed"),
                ],
                "steps": [
                    "System audit — map all integration touchpoints and data flows",
                    "OpenAPI schema design and sandbox environment provisioning",
                    "REST or GraphQL API engineering with rate limiting and auth",
                    "Webhook pipelines for real-time cross-system event propagation",
                    "Load testing to 10,000 req/s and production deployment on AWS UAE",
                ],
                "sim_title": "toco-build / api-gateway",
                "sim_status": "API Healthy",
                "sim_rows": [
                    ("Endpoint", "POST /api/v2/invoices/process", "normal"),
                    ("Response Time", "62ms p50 · 94ms p95 · 0 errors", "ok"),
                    ("Throughput", "2,841 requests in last 60 seconds", "normal"),
                    ("ERP Sync", "Zoho Books updated via webhook in 180ms", "ok"),
                    ("Uptime", "99.97% last 90 days · 0 P1 incidents", "accent"),
                ],
                "sim_footer_speed": "62ms",
                "sim_footer_status": "API Uptime 99.97%",
            },
        ],
    },

    # -------------------------------------------------------------------------
    "digital-marketing": {
        "pill": "Digital Marketing • Dubai, UAE",
        "pill_note": "Paid Media & Lead Generation",
        "h1_html": 'Performance Digital Marketing & <span class="grad-text">Paid Acquisition</span> in Dubai',
        "hero_points": ["Google Ads certified team", "GA4 & multi-touch attribution", "30-day performance review"],
        "integrations": [
            "Google Ads", "Meta Ads", "GA4", "Google Tag Manager", "HubSpot",
            "Hotjar", "LinkedIn Ads", "TikTok Ads", "Zoho CRM", "Mailchimp"
        ],
        "console": [
            ("trending-up", "Campaign launched", "Google Search · Dubai ERP Software keywords", "done", "Done"),
            ("bar-chart", "First conversions", "12 form fills · AED 94 avg CPL", "done", "Done"),
            ("zap", "Bid optimisation", "Smart bidding adjusting based on conversion data", "run", "Running"),
            ("badge-check", "ROAS tracking", "Return on ad spend dashboard live", "wait", "Queued"),
        ],
        "before": [
            "Ad budget is spent with no clear attribution to actual revenue generated",
            "Generic keywords waste AED thousands on irrelevant clicks and tourists",
            "Competitor ads appear above yours for every valuable UAE service keyword",
            "Leads from ads never reach sales team due to broken form or CRM setup",
            "No monthly reporting — campaign performance is a black box",
        ],
        "after": [
            "Every AED spent is tracked from ad click to signed contract via GA4",
            "Hyper-targeted Dubai and UAE campaigns eliminate wasted impressions",
            "Top-of-page positions secured for your highest-converting search terms",
            "Instant lead routing from ad form to WhatsApp and CRM simultaneously",
            "Live dashboard and monthly executive performance report delivered",
        ],
        "durations": ["Days 1–5", "Days 6–14", "Month 2+", "Quarterly"],
        "departments": [
            {
                "id": "ppc",
                "label": "Google PPC Ads",
                "icon": "trending-up",
                "badge": "Google Ads Management",
                "headline": "Drive high-intent B2B and B2C leads from Google Search at the lowest UAE CPL.",
                "desc": "We engineer data-driven Google Search and Display campaigns targeting buyers actively searching for your services in Dubai, Abu Dhabi, and across the GCC. Full negative keyword hygiene, UAE-specific bid adjustments, and conversion tracking from click to CRM deal.",
                "metrics": [
                    ("zap", "AED 80–120 avg B2B CPL"),
                    ("badge-check", "Google Partner certified team"),
                ],
                "steps": [
                    "Competitive keyword research for high-intent UAE service searches",
                    "Campaign and ad group architecture with single theme ad groups (STAGs)",
                    "Ad copy A/B testing with UAE-localised English and Arabic extensions",
                    "Smart bidding configuration tuned to target CPA or ROAS goals",
                    "Weekly optimisation — negative keywords, bid adjustments, landing page CRO",
                ],
                "sim_title": "toco-ads / google-search",
                "sim_status": "Active",
                "sim_rows": [
                    ("Campaign", "UAE ERP Software · Dubai Search — Exact Match", "normal"),
                    ("Impressions (7d)", "14,820 · Impression Share: 72%", "normal"),
                    ("Clicks (7d)", "482 · CTR: 3.25%", "ok"),
                    ("Conversions (7d)", "38 leads · Conv. Rate: 7.9%", "ok"),
                    ("CPL", "AED 94.21 · Budget remaining: AED 2,840", "accent"),
                ],
                "sim_footer_speed": "Real-time",
                "sim_footer_status": "On Target — ROAS 4.2x",
            },
            {
                "id": "social",
                "label": "Meta & Social Ads",
                "icon": "users",
                "badge": "Meta Paid Social Management",
                "headline": "Build brand awareness and generate leads across Instagram and Facebook in the UAE.",
                "desc": "We create high-converting Meta Ads campaigns using UAE audience segments, retargeting pixel events, and scroll-stopping creative content — including short-form video reels that capture attention in an oversaturated Dubai social feed.",
                "metrics": [
                    ("zap", "3.5% avg CTR on UAE campaigns"),
                    ("trending-up", "2.8x ROAS on lead gen campaigns"),
                ],
                "steps": [
                    "Meta Pixel installation and custom event configuration via GTM",
                    "UAE audience research — interests, lookalike and custom audiences",
                    "Creative brief and production: static ads, carousel, and 15s video reels",
                    "Full-funnel campaign setup: awareness → retarget → conversion",
                    "Weekly reporting on CPL, ROAS, frequency, and creative fatigue",
                ],
                "sim_title": "toco-ads / meta-social",
                "sim_status": "Running",
                "sim_rows": [
                    ("Campaign", "UAE Real Estate CRM — IG/FB Lead Ads", "normal"),
                    ("Reach (7d)", "142,000 unique UAE users · Freq: 2.1", "normal"),
                    ("Leads (7d)", "52 form fills · CPL: AED 71.40", "ok"),
                    ("Creative Winner", "15s reel — 4.1% CTR (vs 1.8% static avg)", "ok"),
                    ("ROAS", "2.8x · AED 18,400 revenue attributed", "accent"),
                ],
                "sim_footer_speed": "Real-time",
                "sim_footer_status": "ROAS 2.8x — Scaling Budget",
            },
            {
                "id": "analytics",
                "label": "Analytics & Attribution",
                "icon": "bar-chart",
                "badge": "GA4 & Attribution Setup",
                "headline": "Know exactly which ad, keyword, or channel drove each closed deal.",
                "desc": "We implement Google Analytics 4, server-side GTM, and CRM attribution pipelines so your marketing team can see the full journey from first ad impression to signed invoice — with AED revenue tied to every campaign and touchpoint.",
                "metrics": [
                    ("badge-check", "Full multi-touch attribution"),
                    ("zap", "GA4 + CRM revenue sync"),
                ],
                "steps": [
                    "GA4 property setup with enhanced e-commerce and custom event taxonomy",
                    "Server-side Google Tag Manager deployment for first-party data accuracy",
                    "CRM integration to pass offline conversion data back to Google Ads",
                    "Looker Studio executive dashboard build with live AED revenue data",
                    "Monthly attribution deep-dive report with channel efficiency scoring",
                ],
                "sim_title": "toco-analytics / attribution",
                "sim_status": "Full Coverage",
                "sim_rows": [
                    ("Conversion Event", "consultation_booked · AED 2,800 avg deal value", "normal"),
                    ("Top Channel", "Google Search · 62% of attributed revenue", "ok"),
                    ("Assisted Channel", "Meta Retargeting · 28% assist rate", "ok"),
                    ("CRM Sync", "41 offline conversions uploaded to Google Ads", "accent"),
                    ("ROAS (blended)", "5.2x across all paid channels this month", "ok"),
                ],
                "sim_footer_speed": "Real-time",
                "sim_footer_status": "Attribution 100% — 0 Data Gaps",
            },
        ],
    },

    # -------------------------------------------------------------------------
    "seo": {
        "pill": "Technical SEO • Dubai, UAE",
        "pill_note": "Organic Search Growth Engine",
        "h1_html": 'Technical SEO & <span class="grad-text">Search Optimization</span> in Dubai, UAE',
        "hero_points": ["Core Web Vitals green-pass", "Structured data & rich results", "30-day ranking review"],
        "integrations": [
            "Google Search Console", "Semrush", "Screaming Frog", "Ahrefs",
            "GA4", "Google Tag Manager", "Schema.org", "Cloudflare", "Surfer SEO", "HubSpot"
        ],
        "console": [
            ("search", "Technical audit complete", "0 critical errors · 3 warnings resolved", "done", "Done"),
            ("zap", "Core Web Vitals", "LCP 1.1s · CLS 0.00 · INP 40ms — all Green", "done", "Done"),
            ("trending-up", "Rank tracking live", "42 target keywords monitored daily", "run", "Running"),
            ("badge-check", "Schema implemented", "LocalBusiness, FAQPage, BreadcrumbList", "wait", "Queued"),
        ],
        "before": [
            "Website doesn't appear on page 1 for any Dubai or UAE service keywords",
            "Core Web Vitals are failing — Google is suppressing the site's visibility",
            "No structured data markup — zero rich results in Google SERPs",
            "Duplicate content and missing canonical tags confuse search crawlers",
            "Backlink profile is weak — competitors outrank on every target keyword",
        ],
        "after": [
            "Page 1 rankings for 20+ high-intent Dubai commercial search queries",
            "Core Web Vitals green across all metrics — Google reward factor satisfied",
            "Rich snippet FAQ, breadcrumb, and local business results in Google SERPs",
            "Clean crawl architecture with proper canonicalisation and sitemap structure",
            "Monthly authority link acquisition from UAE and GCC industry domains",
        ],
        "durations": ["Days 1–7", "Days 8–21", "Month 2–3", "Month 4+"],
        "departments": [
            {
                "id": "technical",
                "label": "Technical Audit",
                "icon": "code",
                "badge": "Technical SEO Engineering",
                "headline": "Fix every crawl error, speed bottleneck, and indexing issue blocking your UAE rankings.",
                "desc": "We run a forensic technical SEO audit across your site architecture, page speed, crawl budget, duplicate content, internal link equity, hreflang implementation, and mobile rendering — then systematically fix every issue in priority order.",
                "metrics": [
                    ("zap", "Full-site audit in 48 hours"),
                    ("badge-check", "Zero critical errors guaranteed"),
                ],
                "steps": [
                    "Screaming Frog full-site crawl — 200+ technical signals analysed",
                    "Core Web Vitals audit: LCP, CLS, INP on mobile and desktop",
                    "Duplicate content detection and canonical tag remediation",
                    "Internal link equity flow analysis and orphan page detection",
                    "Priority fix implementation with before/after rank change tracking",
                ],
                "sim_title": "toco-seo / technical-audit",
                "sim_status": "Audit Complete",
                "sim_rows": [
                    ("Pages Crawled", "1,842 URLs · 0 server errors", "ok"),
                    ("Critical Issues", "0 — all resolved (was 14 pre-audit)", "ok"),
                    ("Core Web Vitals", "LCP 1.1s · CLS 0.00 · INP 40ms — Green", "ok"),
                    ("Duplicate Content", "12 canonicals fixed · 3 redirects added", "accent"),
                    ("Crawl Budget", "Sitemap pruned to 180 priority pages", "normal"),
                ],
                "sim_footer_speed": "48h audit",
                "sim_footer_status": "0 Critical Issues Remaining",
            },
            {
                "id": "content",
                "label": "Content & On-Page",
                "icon": "file-text",
                "badge": "Content SEO & On-Page",
                "headline": "Engineer UAE search content that ranks for buyer-intent keywords and converts visitors.",
                "desc": "We research high-value search intent clusters for your Dubai services, write semantically rich service pages and blog content, implement NLP-optimised on-page signals, and structure internal links to maximise topical authority.",
                "metrics": [
                    ("trending-up", "3x organic traffic in 90 days"),
                    ("badge-check", "Intent-mapped content architecture"),
                ],
                "steps": [
                    "Keyword research — map buyer intent clusters for each UAE service",
                    "Content gap analysis against top-3 ranking competitors in Dubai",
                    "Service page rewrite with semantic NLP signals and FAQ structured data",
                    "Blog content calendar targeting informational UAE search queries",
                    "Internal linking strategy to pass equity from high-DA pages to targets",
                ],
                "sim_title": "toco-seo / content-strategy",
                "sim_status": "Rankings Rising",
                "sim_rows": [
                    ("Target Keyword", "ERP software Dubai — was Position 44", "normal"),
                    ("After Optimisation", "ERP software Dubai — now Position 7", "ok"),
                    ("Rich Snippet", "FAQ schema firing · 3 questions in SERP", "ok"),
                    ("Organic Clicks", "+218% vs same period last quarter", "accent"),
                    ("Page Authority", "DA 32 → 41 after link building campaign", "ok"),
                ],
                "sim_footer_speed": "90 days",
                "sim_footer_status": "Ranking Top 10 on 18 Target Keywords",
            },
            {
                "id": "local",
                "label": "Local & GBP SEO",
                "icon": "map-pin",
                "badge": "Local SEO & Google Business",
                "headline": "Dominate Google Maps and local pack results for Dubai service area searches.",
                "desc": "We optimise your Google Business Profile, build UAE-specific citation signals, implement LocalBusiness structured data, and engineer a review acquisition strategy to push your listing into the Google Maps 3-Pack for every target service area.",
                "metrics": [
                    ("zap", "Google Maps 3-Pack targeting"),
                    ("badge-check", "Full LocalBusiness schema"),
                ],
                "steps": [
                    "Google Business Profile audit and category, photo, and NAP optimisation",
                    "LocalBusiness JSON-LD schema with Dubai geo-coordinates and opening hours",
                    "UAE citation building across Yellow Pages, Bayut, and local directories",
                    "Review acquisition playbook — WhatsApp-based review request automation",
                    "Monthly GBP post schedule and local search performance reporting",
                ],
                "sim_title": "toco-seo / local-gbp",
                "sim_status": "Maps 3-Pack",
                "sim_rows": [
                    ("GBP Status", "Verified · Port Saeed, Deira, Dubai", "ok"),
                    ("Search Appearance", "3-Pack: 'AI automation Dubai' — Position 2", "ok"),
                    ("Review Score", "4.8 ★ (142 reviews) · +34 new this quarter", "ok"),
                    ("Profile Views", "+184% vs prior quarter · 2,840 views/month", "accent"),
                    ("Direction Requests", "482 directions requests this month", "normal"),
                ],
                "sim_footer_speed": "Ongoing",
                "sim_footer_status": "Google Maps 3-Pack — Position 2",
            },
        ],
    },

    # -------------------------------------------------------------------------
    "ecommerce-development": {
        "pill": "E-Commerce Development • Dubai, UAE",
        "pill_note": "High-Converting Online Stores",
        "h1_html": 'E-Commerce Development & <span class="grad-text">Storefront Architecture</span> in Dubai',
        "hero_points": ["Tabby & Tamara BNPL ready", "UAE VAT invoicing built-in", "30-day post-launch warranty"],
        "integrations": [
            "Shopify Plus", "WooCommerce", "Next.js", "Tabby", "Tamara",
            "PayTabs", "Network International", "Aramex API", "Fetchr", "Zoho Inventory"
        ],
        "console": [
            ("shopping-bag", "Store configured", "12 product collections · Arabic RTL ready", "done", "Done"),
            ("credit-card", "Payment gateways live", "Tabby · Apple Pay · Card via PayTabs", "done", "Done"),
            ("zap", "Shipping rules active", "Aramex & Fetchr live rate calculation", "run", "Running"),
            ("bar-chart", "Analytics wired", "GA4 enhanced e-commerce · Meta Pixel live", "wait", "Queued"),
        ],
        "before": [
            "Products are sold over WhatsApp with no order tracking or inventory system",
            "International payment cards fail — UAE customers abandon checkout",
            "No BNPL option: Tabby or Tamara needed for high-AED cart conversions",
            "Manual shipping quotes delay orders and frustrate GCC customers",
            "Zero analytics — no visibility into what products, pages, or traffic source converts",
        ],
        "after": [
            "Professional storefront with 1-click checkout and order tracking portal",
            "Network International, Apple Pay, and card accepted seamlessly",
            "Tabby and Tamara BNPL reduces checkout abandonment on high-value orders",
            "Live Aramex and Fetchr shipping rates calculated in cart — zero manual work",
            "Full GA4 enhanced e-commerce funnel from product view to revenue tracked",
        ],
        "durations": ["Days 1–7", "Days 8–21", "Days 22–30", "Launch + 30 Days"],
        "departments": [
            {
                "id": "shopify",
                "label": "Shopify & Headless",
                "icon": "shopping-bag",
                "badge": "Shopify Plus & Headless Commerce",
                "headline": "Launch a Shopify Plus store with UAE payment gateways, BNPL, and Arabic RTL in under 30 days.",
                "desc": "We configure and customise Shopify Plus with UAE-specific payment processors (PayTabs, Network International), Tabby and Tamara BNPL, bilingual Arabic/English product pages, VAT 5% invoicing, and live shipping rate APIs for Aramex and Fetchr.",
                "metrics": [
                    ("zap", "30-day launch guarantee"),
                    ("badge-check", "UAE VAT 5% auto-calculated"),
                ],
                "steps": [
                    "Shopify Plus store setup with UAE tax rules and multi-currency (AED/USD)",
                    "Custom theme development with Arabic RTL and mobile-first design",
                    "Tabby BNPL, Apple Pay, and PayTabs card payment gateway integration",
                    "Aramex and Fetchr live shipping rate calculation at checkout",
                    "GA4 enhanced e-commerce and Meta Pixel tracking configuration",
                ],
                "sim_title": "toco-build / shopify-store",
                "sim_status": "Store Live",
                "sim_rows": [
                    ("Checkout Conversion", "4.8% — above UAE average of 2.9%", "ok"),
                    ("BNPL Orders", "31% via Tabby · avg AOV AED 820", "ok"),
                    ("UAE VAT", "5% auto-applied · Tax invoice generated per order", "ok"),
                    ("Shipping", "Aramex live rates active · avg AED 25 to Dubai", "accent"),
                    ("Mobile Revenue", "72% of orders on mobile · LCP 1.2s", "ok"),
                ],
                "sim_footer_speed": "28 days",
                "sim_footer_status": "Store Live — 4.8% Checkout Conversion",
            },
            {
                "id": "custom",
                "label": "Custom Storefront",
                "icon": "code",
                "badge": "Custom Headless E-Commerce",
                "headline": "Build a fully custom headless storefront for complex product catalogues and B2B ordering.",
                "desc": "For enterprise UAE brands with custom pricing logic, B2B account tiers, subscription products, or complex product configurators, we engineer a bespoke Next.js headless storefront with your own backend API and full data ownership.",
                "metrics": [
                    ("zap", "100% custom checkout logic"),
                    ("shield", "Full data ownership & control"),
                ],
                "steps": [
                    "Commerce architecture design: headless vs. Shopify vs. hybrid evaluation",
                    "Next.js storefront engineering with server-side rendering for SEO",
                    "Custom pricing engine with B2B tier discounts and volume pricing",
                    "Order management system with real-time inventory sync to warehouse",
                    "ERP integration: auto-generate purchase orders and delivery manifests",
                ],
                "sim_title": "toco-build / custom-headless",
                "sim_status": "API Active",
                "sim_rows": [
                    ("Architecture", "Next.js 14 · Node.js API · PostgreSQL", "normal"),
                    ("Product Catalogue", "12,420 SKUs · real-time inventory sync", "ok"),
                    ("B2B Pricing", "5 tier groups · volume discounts applied live", "ok"),
                    ("API Latency", "Product page SSR: 180ms · Checkout: 290ms", "ok"),
                    ("ERP Sync", "SAP PO generated on every confirmed order", "accent"),
                ],
                "sim_footer_speed": "180ms",
                "sim_footer_status": "Custom Storefront — 12,420 SKUs Live",
            },
            {
                "id": "cro",
                "label": "CRO & Conversion",
                "icon": "trending-up",
                "badge": "Conversion Rate Optimisation",
                "headline": "Turn existing traffic into more revenue by optimising every step of the checkout funnel.",
                "desc": "We audit your store's conversion funnel with heatmaps, session recordings, and cohort analysis — then run structured A/B tests on product pages, checkout steps, pricing presentation, and trust signals to systematically increase your revenue per visitor.",
                "metrics": [
                    ("trending-up", "+35% CVR improvement avg"),
                    ("badge-check", "A/B tested changes only"),
                ],
                "steps": [
                    "GA4 funnel analysis — identify where visitors drop off in checkout",
                    "Hotjar heatmap and session recording audit of top 10 product pages",
                    "Hypothesis backlog creation ranked by impact × confidence × effort",
                    "A/B test engineering: product images, pricing, CTA copy, trust badges",
                    "Statistical significance monitoring and winning variant deployment",
                ],
                "sim_title": "toco-cro / checkout-optimisation",
                "sim_status": "Test Running",
                "sim_rows": [
                    ("Hypothesis", "Adding Tabby BNPL messaging above-fold increases CVR", "normal"),
                    ("Test Split", "50/50 · 4,820 sessions per variant", "normal"),
                    ("Variant A (Control)", "CVR 2.9% — no BNPL messaging", "normal"),
                    ("Variant B (Test)", "CVR 4.1% — BNPL messaging visible — winner", "ok"),
                    ("Revenue Uplift", "+AED 28,400 / month projected at current traffic", "accent"),
                ],
                "sim_footer_speed": "14-day test",
                "sim_footer_status": "Winning Variant Deployed — +41% CVR",
            },
        ],
    },

    # -------------------------------------------------------------------------
    "erp-and-custom-software": {
        "pill": "Custom ERP Development • Dubai, UAE",
        "pill_note": "Enterprise Software Engineering",
        "h1_html": 'Custom ERP & Enterprise <span class="grad-text">Software Platforms</span> in Dubai',
        "hero_points": ["UAE VAT & WPS compliance built-in", "Arabic RTL bilingual interface", "30-day post-launch warranty"],
        "integrations": [
            "PostgreSQL", "Node.js", "React", "Docker", "AWS UAE",
            "WhatsApp Business API", "FTA UAE API", "Aramex API", "Zoho", "PayTabs"
        ],
        "console": [
            ("database", "Schema deployed", "42 tables · UAE VAT rules seeded", "done", "Done"),
            ("layers", "Module integration", "CRM ↔ Inventory ↔ Finance synced", "done", "Done"),
            ("zap", "Live ERP processing", "Purchase orders and dispatch running live", "run", "Running"),
            ("shield", "Compliance check", "FTA TRN validation and WPS payroll queued", "wait", "Queued"),
        ],
        "before": [
            "Operations managed via Excel spreadsheets and disconnected WhatsApp threads",
            "Finance team manually reconciles invoices against purchase orders every month",
            "No live inventory visibility — stock-outs happen without warning",
            "Dispatch and logistics have no real-time tracking or manifest automation",
            "Payroll is calculated manually and WPS SIF files are built by hand",
        ],
        "after": [
            "Single unified ERP dashboard connects every operational department",
            "3-way PO-GRN-Invoice matching executes automatically with discrepancy alerts",
            "Live inventory levels across all warehouses with low-stock auto-reorder",
            "Dispatch console with driver assignment, GPS tracking, and POD capture",
            "One-click WPS payroll with automated gratuity and MOHRE SIF generation",
        ],
        "durations": ["Days 1–10", "Weeks 2–6", "Weeks 7–10", "Launch + 30 Days"],
        "departments": [
            {
                "id": "operations",
                "label": "Operations & Dispatch",
                "icon": "truck",
                "badge": "Operations & Logistics ERP",
                "headline": "Unify procurement, inventory, dispatch, and invoicing in one bespoke ERP platform.",
                "desc": "We engineer full dispatch management systems — from purchase order creation through goods receipt, warehouse management, driver assignment, live GPS tracking, automated delivery confirmation, and instant billing upon POD capture.",
                "metrics": [
                    ("zap", "Real-time across all warehouses"),
                    ("badge-check", "Zero manual dispatch paperwork"),
                ],
                "steps": [
                    "Business process mapping across procurement, warehouse, and logistics",
                    "Database schema design for multi-warehouse, multi-currency operations",
                    "Procurement module: PO creation, approval workflows, and GRN matching",
                    "Dispatch console: driver assignment, GPS tracking, and POD capture",
                    "Automated invoicing upon delivery confirmation via WhatsApp",
                ],
                "sim_title": "toco-erp / dispatch-module",
                "sim_status": "Live Operations",
                "sim_rows": [
                    ("Open Purchase Orders", "142 POs · AED 2.4M total value", "normal"),
                    ("3-Way Match", "138 matched auto · 4 flagged for review", "ok"),
                    ("Active Deliveries", "28 drivers tracked live across Dubai", "ok"),
                    ("POD Today", "91 deliveries confirmed · AED 840,000 invoiced", "accent"),
                    ("Inventory Accuracy", "99.4% — zero phantom stock in 30 days", "ok"),
                ],
                "sim_footer_speed": "Real-time",
                "sim_footer_status": "Live — 0 Manual Steps Remaining",
            },
            {
                "id": "finance",
                "label": "Finance & UAE Compliance",
                "icon": "wallet",
                "badge": "Finance & Tax Compliance ERP",
                "headline": "Automate UAE VAT invoicing, FTA TRN validation, and WPS payroll compliance.",
                "desc": "Our finance modules handle UAE-specific requirements: 5% VAT calculation on every transaction, FTA Tax Registration Number validation, automated Emirates NBD WPS salary transfer file (SIF) generation, and real-time P&L and cash flow dashboards.",
                "metrics": [
                    ("shield", "FTA VAT 5% auto-compliant"),
                    ("badge-check", "1-click WPS SIF generation"),
                ],
                "steps": [
                    "Chart of accounts setup with UAE VAT tax code mapping",
                    "FTA TRN API integration for real-time vendor number validation",
                    "Automated 5% VAT calculation, collection, and return report generation",
                    "WPS payroll module: salary, leave balance, and gratuity calculation",
                    "One-click SIF file generation in Emirates NBD/ADCB-approved format",
                ],
                "sim_title": "toco-erp / finance-module",
                "sim_status": "VAT Compliant",
                "sim_rows": [
                    ("Monthly Revenue", "AED 1,840,000 · 12,420 transactions", "normal"),
                    ("VAT Collected", "AED 92,000 · FTA return prepared", "ok"),
                    ("TRN Validation", "2,841 vendor TRNs verified via FTA API", "ok"),
                    ("WPS Payroll", "84 employees · SIF file generated and submitted", "accent"),
                    ("Month-End Close", "2.5 hours — was 3 days manual process", "ok"),
                ],
                "sim_footer_speed": "2.5 hours close",
                "sim_footer_status": "FTA Compliant — 0 Penalty Exposure",
            },
            {
                "id": "crm",
                "label": "CRM & Sales Pipeline",
                "icon": "bar-chart",
                "badge": "Built-in CRM & Deal Management",
                "headline": "Manage your entire UAE sales pipeline from lead capture to signed contract inside the ERP.",
                "desc": "We build fully integrated CRM modules into your ERP — with WhatsApp lead intake, automated follow-up sequences, pipeline stage management, quotation generation, contract e-signing, and revenue reporting all in a single system.",
                "metrics": [
                    ("trending-up", "2.4x faster deal cycle"),
                    ("zap", "WhatsApp lead intake automated"),
                ],
                "steps": [
                    "CRM data model design: contacts, companies, deals, and activities",
                    "WhatsApp Business API integration for automatic lead capture",
                    "AI qualification agent routes and scores every inbound inquiry",
                    "PDF quotation engine with UAE VAT, AED pricing, and branded template",
                    "One-click deal-to-PO conversion for seamless sales-to-operations handover",
                ],
                "sim_title": "toco-erp / crm-module",
                "sim_status": "Pipeline Active",
                "sim_rows": [
                    ("Pipeline Value", "AED 4.2M across 38 open deals", "normal"),
                    ("New Leads (7d)", "24 · Source: WhatsApp (18), Web (6)", "ok"),
                    ("Proposals Sent", "14 quotations · avg value AED 42,000", "ok"),
                    ("Won This Month", "8 deals · AED 320,000 revenue", "accent"),
                    ("Sales Cycle", "12 days avg — was 28 days before ERP", "ok"),
                ],
                "sim_footer_speed": "Real-time",
                "sim_footer_status": "Pipeline AED 4.2M — 8 Closed This Month",
            },
        ],
    },

    # -------------------------------------------------------------------------
    "social-media-management": {
        "pill": "Social Media Management • Dubai, UAE",
        "pill_note": "B2B Brand Growth & Engagement",
        "h1_html": 'Strategic Social Media Management & <span class="grad-text">Brand Growth</span> in Dubai',
        "hero_points": ["Arabic & English content", "Professional video reels production", "Monthly performance reports"],
        "integrations": [
            "LinkedIn", "Instagram", "TikTok", "Facebook", "X (Twitter)",
            "Meta Business Suite", "Canva Pro", "Adobe Premiere", "Buffer", "Hootsuite"
        ],
        "console": [
            ("camera", "Content shoot done", "8 posts · 2 reels · 1 carousel batch", "done", "Done"),
            ("zap", "Copy approved", "English & Arabic captions reviewed", "done", "Done"),
            ("calendar", "Posts scheduled", "12 posts queued · Mon/Wed/Fri cadence", "run", "Running"),
            ("bar-chart", "Analytics report", "Monthly engagement performance queued", "wait", "Queued"),
        ],
        "before": [
            "Social accounts post inconsistently — once every few weeks when someone remembers",
            "Content is low-quality phone photos with no brand consistency or visual identity",
            "No Arabic content — 40%+ of UAE audience speaks Arabic as first language",
            "Zero strategy behind posts — no hashtags, no audience research, no CTA",
            "Competitor brands look 10x more professional on the same platforms",
        ],
        "after": [
            "Consistent 3x/week posting cadence with premium photo and video content",
            "On-brand visual design system with Arabic/English bilingual captions",
            "Full Arabic content written by native bilingual copywriters",
            "Strategic hashtag mix, optimal posting times, and engagement-driving CTAs",
            "Monthly report with follower growth, reach, impressions, and engagement rate",
        ],
        "durations": ["Week 1", "Weeks 2–3", "Month 2+", "Quarterly"],
        "departments": [
            {
                "id": "linkedin",
                "label": "LinkedIn B2B Growth",
                "icon": "users",
                "badge": "LinkedIn B2B Strategy",
                "headline": "Build executive authority and generate B2B inbound leads from LinkedIn in the UAE.",
                "desc": "We manage LinkedIn pages and personal executive profiles for UAE B2B brands — combining thought leadership articles, company case study posts, and targeted outreach sequences to generate qualified enterprise inbound inquiries.",
                "metrics": [
                    ("trending-up", "+420% follower growth avg (6 months)"),
                    ("zap", "12–18 B2B leads / month from LinkedIn"),
                ],
                "steps": [
                    "LinkedIn page and executive profile audit and optimisation",
                    "Content strategy: thought leadership, case studies, and industry news",
                    "10–12 posts/month: carousels, documents, and native video",
                    "Hashtag and audience targeting strategy for UAE B2B sectors",
                    "Monthly analytics: impressions, reach, follower growth, and lead count",
                ],
                "sim_title": "toco-social / linkedin-manager",
                "sim_status": "Post Scheduled",
                "sim_rows": [
                    ("Post Type", "Carousel: 5 AI automation wins from Dubai clients", "normal"),
                    ("Scheduled", "Tuesday 8:00 AM GST — peak UAE B2B window", "ok"),
                    ("Last Post Reach", "14,820 impressions · 480 reactions · 38 reposts", "ok"),
                    ("Follower Growth", "+342 followers this month · 4.2% engagement rate", "accent"),
                    ("Leads Generated", "14 connection requests from decision-makers", "ok"),
                ],
                "sim_footer_speed": "3 posts/week",
                "sim_footer_status": "14 B2B Leads This Month via LinkedIn",
            },
            {
                "id": "instagram",
                "label": "Instagram & Reels",
                "icon": "camera",
                "badge": "Instagram Content Production",
                "headline": "Grow your UAE brand on Instagram with high-production reels, stories, and feed content.",
                "desc": "We produce, edit, and publish premium Instagram content for UAE brands — including 30-second product reels, behind-the-scenes brand stories, and highly shareable carousel educational posts in Arabic and English.",
                "metrics": [
                    ("zap", "30-second reels in 5 days"),
                    ("trending-up", "4–8% engagement rate avg"),
                ],
                "steps": [
                    "Instagram profile optimisation: bio, highlights, link-in-bio, and CTA",
                    "Monthly content brief: 12 posts, 4 reels, and 8 stories per month",
                    "Professional photo and video shoot coordination in Dubai",
                    "Reel production with branded intro, B-roll, text overlays, and CTA",
                    "Bilingual Arabic/English captions with hashtag research and scheduling",
                ],
                "sim_title": "toco-social / instagram-manager",
                "sim_status": "Reel Published",
                "sim_rows": [
                    ("Reel", "Before/After: ERP transformation at Dubai logistics firm", "normal"),
                    ("Views (24h)", "28,420 · Shares: 184 · Saves: 342", "ok"),
                    ("Profile Visits", "+840 from reel viewers this week", "ok"),
                    ("Engagement Rate", "7.2% — above UAE average of 2.8%", "ok"),
                    ("Follower Change", "+218 followers in last 7 days", "accent"),
                ],
                "sim_footer_speed": "5-day reel turnaround",
                "sim_footer_status": "7.2% Engagement Rate — Above UAE Average",
            },
            {
                "id": "content",
                "label": "Content Strategy",
                "icon": "file-text",
                "badge": "Arabic & English Content Strategy",
                "headline": "Build a 90-day content calendar that tells your brand story in Arabic and English.",
                "desc": "We define your social brand voice, create an audience persona based on your UAE target market, map content pillars, and produce a 90-day publishing calendar across all channels — with Arabic and English versions ready for every post.",
                "metrics": [
                    ("badge-check", "Native Arabic copywriting"),
                    ("zap", "90-day calendar delivered in week 1"),
                ],
                "steps": [
                    "Brand voice and tone guide for social media: UAE market nuance included",
                    "Audience persona research for primary UAE decision-maker segments",
                    "4-pillar content strategy: educate, inspire, engage, convert",
                    "90-day post calendar with platform-specific formats and Arabic/English copy",
                    "Monthly content performance review and calendar adjustment session",
                ],
                "sim_title": "toco-social / content-calendar",
                "sim_status": "Calendar Live",
                "sim_rows": [
                    ("Month Coverage", "November 2026 · 36 posts planned", "normal"),
                    ("Platforms", "LinkedIn · Instagram · X · Facebook", "normal"),
                    ("Arabic Posts", "18 / 36 posts bilingual Arabic + English", "ok"),
                    ("Reels Planned", "4 reels · production brief sent to team", "ok"),
                    ("Approval Status", "All 36 posts client-approved and queued", "accent"),
                ],
                "sim_footer_speed": "36 posts/month",
                "sim_footer_status": "90-Day Calendar Approved & Scheduled",
            },
        ],
    },

    # -------------------------------------------------------------------------
    "branding-and-ui-ux-design": {
        "pill": "Branding & UI/UX Design • Dubai, UAE",
        "pill_note": "Corporate Identity & Digital Design",
        "h1_html": 'Corporate Branding & <span class="grad-text">UI/UX Product Design</span> in Dubai',
        "hero_points": ["Full Figma design system", "Arabic RTL product design", "30-day revision warranty"],
        "integrations": [
            "Figma", "Adobe Illustrator", "Adobe Photoshop", "Framer",
            "Lottie", "Storybook", "Zeroheight", "Notion", "Linear", "Miro"
        ],
        "console": [
            ("pen-tool", "Brand discovery done", "Visual direction, moodboard & brief approved", "done", "Done"),
            ("layout", "Wireframes delivered", "48 screens wireframed in Figma", "done", "Done"),
            ("zap", "High-fidelity UI", "Pixel-perfect components being built", "run", "Running"),
            ("badge-check", "Design handoff", "Developer-ready Figma with tokens queued", "wait", "Queued"),
        ],
        "before": [
            "Logo was made in Canva and looks unprofessional next to competitor brands",
            "No consistent visual identity — colors, fonts, and icons differ on every asset",
            "No design system — developers make visual decisions independently each sprint",
            "Mobile app or website UX is confusing — users can't find key actions easily",
            "Arabic version of the product is broken RTL with English font fallbacks",
        ],
        "after": [
            "Professional UAE-market corporate identity that commands B2B trust",
            "Cohesive design language applied consistently across every digital touchpoint",
            "Component design system in Figma — developers build from one source of truth",
            "Research-validated UX flows with 92%+ task completion rates in usability testing",
            "Perfect Arabic RTL design with carefully selected bilingual type pairings",
        ],
        "durations": ["Days 1–7", "Days 8–21", "Days 22–35", "Delivery + 30 Days"],
        "departments": [
            {
                "id": "identity",
                "label": "Brand Identity",
                "icon": "pen-tool",
                "badge": "Corporate Identity Design",
                "headline": "Create a UAE-market brand identity that commands B2B credibility and market trust.",
                "desc": "We design complete corporate brand identities for UAE businesses — logo system (primary, secondary, favicon), colour palette with cultural appropriateness for the GCC market, bilingual Arabic/English typography pairs, and a 60-page brand standards guide.",
                "metrics": [
                    ("zap", "Full identity in 21 days"),
                    ("badge-check", "60-page brand guidelines delivered"),
                ],
                "steps": [
                    "Brand discovery workshop: positioning, values, audience, and competitive audit",
                    "Moodboard and visual direction deck — 3 distinct creative directions presented",
                    "Logo system design: primary, horizontal, stacked, monochrome, and favicon versions",
                    "Colour palette, typography system, and Arabic/English bilingual type pairs",
                    "60-page brand standards PDF with usage guidelines, do/don'ts, and assets",
                ],
                "sim_title": "toco-design / brand-identity",
                "sim_status": "Brand Approved",
                "sim_rows": [
                    ("Logo Formats", "SVG · PNG · AI · EPS · Favicon.ico — all delivered", "ok"),
                    ("Colour System", "Primary: #0049D0 · 12-token design palette", "ok"),
                    ("Typography", "Space Grotesk (EN) + Noto Kufi (AR) paired", "ok"),
                    ("Brand Guide", "64 pages · PDF + Figma library delivered", "ok"),
                    ("Social Templates", "24 branded post templates ready in Canva", "accent"),
                ],
                "sim_footer_speed": "19 days",
                "sim_footer_status": "Brand Identity Approved — All Assets Delivered",
            },
            {
                "id": "product",
                "label": "Product UI/UX Design",
                "icon": "layout",
                "badge": "Product UI/UX Engineering",
                "headline": "Design a pixel-perfect product UI with a Figma component system your engineers will love.",
                "desc": "We design and prototype every screen of your web or mobile product in Figma — from information architecture and wireframes through high-fidelity UI with auto-layout components, design tokens, and developer handoff documentation that eliminates back-and-forth.",
                "metrics": [
                    ("zap", "Full Figma component system"),
                    ("badge-check", "Developer-ready handoff in 35 days"),
                ],
                "steps": [
                    "User flow mapping and information architecture diagram for all screen paths",
                    "Low-fidelity wireframes in Figma for all 40–80 product screens",
                    "Design system setup: 400+ auto-layout components with design tokens",
                    "High-fidelity UI design with micro-interactions and animation specs",
                    "Developer handoff: Figma inspect, Zeroheight docs, and asset export",
                ],
                "sim_title": "toco-design / product-ui",
                "sim_status": "Handoff Ready",
                "sim_rows": [
                    ("Screens Designed", "64 screens · 100% of user flows covered", "ok"),
                    ("Components Built", "420 components · 8 variant states each", "ok"),
                    ("Design Tokens", "142 tokens: colour, spacing, typography, shadow", "ok"),
                    ("Prototype", "Interactive prototype · 92% task completion in testing", "ok"),
                    ("Arabic RTL", "All 64 screens fully mirrored for Arabic layout", "accent"),
                ],
                "sim_footer_speed": "32 days",
                "sim_footer_status": "Figma System Ready — 420 Components",
            },
            {
                "id": "ux",
                "label": "UX Research & Testing",
                "icon": "search",
                "badge": "UX Research & Usability Testing",
                "headline": "Validate every design decision with real UAE user testing before a single line of code is written.",
                "desc": "We plan and execute moderated usability testing sessions with real UAE users — testing task completion rates, heatmapping prototype clicks, and running 5-second first impression tests to ensure your product is intuitive before development starts.",
                "metrics": [
                    ("badge-check", "92%+ task completion rate"),
                    ("zap", "Real UAE user testing"),
                ],
                "steps": [
                    "Research plan and task scenario design for 5–8 user testing sessions",
                    "Prototype-based moderated testing with 5–8 real UAE target users",
                    "Eye-tracking heatmap analysis on key product screens",
                    "Usability findings report with severity ranking and actionable recommendations",
                    "Prototype iteration based on findings before engineering sprint begins",
                ],
                "sim_title": "toco-design / ux-research",
                "sim_status": "Research Complete",
                "sim_rows": [
                    ("Participants", "8 users · UAE English and Arabic speakers", "normal"),
                    ("Task Completion", "Task 1: 94% · Task 2: 88% · Task 3: 96%", "ok"),
                    ("Critical Issues", "2 — navigation label ambiguity (fixed)", "normal"),
                    ("Net Usability Score", "82 / 100 — above enterprise benchmark of 68", "ok"),
                    ("Iteration", "3 screens redesigned based on findings", "accent"),
                ],
                "sim_footer_speed": "5-day turnaround",
                "sim_footer_status": "NUS 82/100 — Above Enterprise Benchmark",
            },
        ],
    },
}


def _svc(slug):
    return next(s for s in SERVICES_DATA if s["slug"] == slug)


def _ico(emoji_or_name):
    name = EMOJI_MAP.get(emoji_or_name.replace("\ufe0f", ""), emoji_or_name)
    return svg(name)


def build(slug):
    svc, x = _svc(slug), EXTRA[slug]
    url = f"/services/{slug}"
    canonical = f"{SITE_BASE}{url}"
    short = svc["h1"].split(" in ")[0]
    crumbs = [("Home", "/"), ("Services", "/services"), (short, "")]

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": f"{canonical}#service",
                "name": svc["h1"],
                "serviceType": short,
                "description": svc["meta_desc"],
                "provider": {
                    "@type": "LocalBusiness",
                    "name": "TOCO Technologies",
                    "telephone": "+971-4-577-0725",
                    "email": "info@tocoplus.com",
                    "address": {
                        "@type": "PostalAddress",
                        "streetAddress": "Port Saeed",
                        "addressLocality": "Dubai",
                        "addressCountry": "AE"
                    },
                },
                "areaServed": [
                    {"@type": "City", "name": "Dubai"},
                    {"@type": "City", "name": "Abu Dhabi"},
                    {"@type": "Country", "name": "United Arab Emirates"}
                ],
            },
            make_breadcrumb_schema(crumbs),
            make_faq_schema(svc["faqs"]),
        ],
    }

    check = svg("check")
    arrow = '<svg class="arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

    # Hero points
    points = "".join(f"<span>{check}{p}</span>" for p in x["hero_points"])

    # Hero console nodes
    nodes = ""
    for ico, title, sub, st, label in x["console"]:
        nodes += f'''                <div class="sv-node{' is-run' if st == 'run' else ''}">
                  <div class="sv-node-ico">{svg(ico)}</div>
                  <div><b>{title}</b><small>{sub}</small></div>
                  <span class="st {st}">{label}</span>
                </div>\n'''

    # Integrations Marquee
    integrations_items = "".join(f'<span class="sv-stack-chip">{svg("zap")}{i}</span>' for i in x["integrations"])
    integrations_html = integrations_items + integrations_items.replace('<span class="sv-stack-chip">', '<span class="sv-stack-chip" aria-hidden="true">')

    # Bento Grid Capabilities
    bento_html = get_bento_html(slug)

    # Before / After Split Console
    x_ico = svg("x")
    before_lis = "".join(f'<li><span class="cross-mk">{x_ico}</span><span>{t}</span></li>' for t in x["before"])
    after_lis = "".join(f'<li><span class="check-mk">{check}</span><span>{t}</span></li>' for t in x["after"])

    # Implementation Timeline
    steps = ""
    for i, s_ in enumerate(svc["steps"]):
        steps += f'''          <div class="sv-step rv">
            <div class="dot">{s_["num"]}</div>
            <span class="when">{x["durations"][i]}</span>
            <h3>{s_["title"]}</h3>
            <p>{s_["desc"]}</p>
          </div>\n'''

    # Results command center
    results = "".join(
        f'<div class="sv-res rv"><b>{b["metric"]}</b><h3>{b["title"]}</h3><p>{b["desc"]}</p></div>'
        for b in svc["benefits"]
    )

    # Department Workflow Studio (Replaces 4 uniform boxes from Screenshot 1)
    studio_tabs = ""
    studio_panels = ""
    for i, dept in enumerate(x["departments"]):
        is_first = (i == 0)
        active_class = " active" if is_first else ""
        selected_attr = "true" if is_first else "false"
        tabindex_attr = "0" if is_first else "-1"
        hidden_attr = "" if is_first else " hidden"

        studio_tabs += f'''        <button class="sv-tab-btn{active_class}" type="button" role="tab" id="tab-{dept["id"]}" aria-controls="panel-{dept["id"]}" aria-selected="{selected_attr}" tabindex="{tabindex_attr}" data-tab="panel-{dept["id"]}">
          {svg(dept["icon"])}
          <span>{dept["label"]}</span>
        </button>\n'''

        metrics_html = "".join(f'<span class="sv-metric-chip">{svg(m_ico)}<span>{m_lbl}</span></span>' for m_ico, m_lbl in dept["metrics"])
        steps_html = "".join(f'''              <div class="sv-studio-step">
                <span class="step-idx">{idx:02d}</span>
                <span>{step_text}</span>
              </div>\n''' for idx, step_text in enumerate(dept["steps"], 1))

        sim_rows_html = ""
        for k, v, tone in dept["sim_rows"]:
            tone_class = f" {tone}" if tone != "normal" else ""
            sim_rows_html += f'''                <div class="sv-sim-row">
                  <span class="k">{k}</span>
                  <span class="v{tone_class}">{v}</span>
                </div>\n'''

        studio_panels += f'''        <div class="sv-studio-panel{active_class}" id="panel-{dept["id"]}" role="tabpanel" aria-labelledby="tab-{dept["id"]}"{hidden_attr}>
          <!-- Left Pane: Department Overview & Workflow Steps -->
          <div class="sv-pane-content">
            <div>
              <span class="sv-studio-badge">{svg(dept["icon"])} {dept["badge"]}</span>
              <h3>{dept["headline"]}</h3>
              <p class="sv-studio-desc">{dept["desc"]}</p>
              <div class="sv-studio-metrics">
                {metrics_html}
              </div>
              <div class="sv-studio-steps">
                {steps_html}
              </div>
            </div>
            <a href="/contact" class="sv-studio-link">
              <span>Discuss this workflow with an engineer</span>
              {svg("arrow-up-right")}
            </a>
          </div>

          <!-- Right Pane: Live Department Simulation Console -->
          <div class="sv-pane-preview" aria-hidden="true">
            <div class="sv-sim-card">
              <div class="sv-sim-header">
                <div class="sv-sim-dots">
                  <span></span><span></span><span></span>
                </div>
                <div style="font-family:ui-monospace,monospace;color:#94A3B8;font-size:11.5px;">{dept["sim_title"]}</div>
                <span class="sv-sim-badge">{dept["sim_status"]}</span>
              </div>
              <div class="sv-sim-body">
{sim_rows_html}              </div>
              <div class="sv-sim-footer">
                <span>Speed: <strong class="speed">{dept["sim_footer_speed"]}</strong></span>
                <span>Status: <strong>{dept["sim_footer_status"]}</strong></span>
              </div>
            </div>
          </div>
        </div>\n'''

    # FAQs
    faqs = ""
    for i, q in enumerate(svc["faqs"]):
        first = (i == 0)
        faqs += f'''            <div class="faq-item{' open' if first else ''}">
              <button class="faq-q" type="button" aria-expanded="{'true' if first else 'false'}"><span>{q["q"]}</span><i></i></button>
              <div class="faq-a" style="{'max-height:260px;' if first else ''}"><div class="faq-a-inner"><p>{q["a"]}</p></div></div>
            </div>\n'''

    meta = SERVICE_META.get(slug, {})

    # Related Services & Products
    related_cards = ""
    for r in svc.get("related", []):
        r_url = r["url"]
        is_prod = "/products/" in r_url
        tag = f'{"PRODUCT" if is_prod else "SERVICE"} &bull; ECOSYSTEM'
        card_class = "is-featured" if is_prod else "is-tech"
        action_text = "Explore Product" if is_prod else "Explore Service"
        related_cards += f'''          <a href="{r_url}" class="sv-rel-card {card_class} rv">
            <div>
              <span class="rel-tag">{svg("zap")} {tag}</span>
              <h3>{r["title"]}</h3>
              <p>{r["desc"]}</p>
              <div class="rel-mockup">
                <div style="display:flex;align-items:center;gap:8px;font-family:ui-monospace,monospace;font-size:11px;color:#334155;">
                  <span style="width:7px;height:7px;border-radius:50%;background:#10B981;display:inline-block;"></span>
                  <span>Integrated with {short} &bull; Live in UAE</span>
                </div>
              </div>
            </div>
            <span class="rel-action"><span>{action_text}</span>{svg("arrow-up-right")}</span>
          </a>\n'''
    related_html = f'''        <div class="sv-rel-grid">
{related_cards}        </div>'''

    f1 = meta.get("float1", ("shield", "30-Day Launch Warranty", "Full guarantee"))
    f2 = meta.get("float2", ("clock", "Port Saeed, Dubai HQ", "Engineering hub"))
    console_file = meta.get("console_file", "system / workflow.py")
    hero_cta = meta.get("hero_cta", "Book a Free Consultation")
    cap_heading = meta.get("cap_heading", "Enterprise Capabilities Engineered for UAE Scale")
    cap_sub = meta.get("cap_sub", "Production-grade digital systems and software engineered around how UAE enterprises actually operate.")
    studio_heading = meta.get("studio_heading", "Use Cases by Department")
    studio_sub = meta.get("studio_sub", "Select an operational discipline below to explore how custom engineering accelerates operations.")
    faq_help_title = meta.get("faq_help_title", "Have a custom workflow in mind?")
    faq_help_desc = meta.get("faq_help_desc", "Talk directly with an engineer in Port Saeed, Dubai. We reply within one business day.")
    cta_title = meta.get("cta_title", "Ready to Build Your Next Digital Advantage?")
    cta_sub = meta.get("cta_sub", "Partner with TOCO Technologies in Dubai to architect high-performance software solutions.")

    html = f'''{render_head_tags(svc["title"], svc["meta_desc"], canonical, schema)}
{render_header("services")}

  <main id="main-content">
    <!-- HERO SECTION -->
    <section class="page-hero sv-hero">
      <div class="wrap">
        {render_breadcrumbs(crumbs)}
        <div class="sv-hero-grid">
          <div>
            <span class="sv-pill"><b>{x["pill"]}</b>{x["pill_note"]}</span>
            <h1>{x["h1_html"]}</h1>
            <p class="lede">{svc["lede"]}</p>
            <div class="sv-cta">
              <a href="/contact" class="btn btn-primary"><span>{hero_cta}</span>{arrow}</a>
              <a href="https://wa.me/97145770725" target="_blank" rel="noopener" class="btn btn-ghost"><span>Chat on WhatsApp</span></a>
            </div>
            <div class="sv-points">{points}</div>
          </div>

          <div class="sv-visual" aria-hidden="true">
            <div class="sv-console">
              <div class="sv-console-bar"><i></i><i></i><i></i><span>{console_file}</span><span class="live">Live</span></div>
              <div class="sv-flow">
{nodes}              </div>
              <div class="sv-progress"><span></span></div>
            </div>
            <div class="sv-float f1">{svg(f1[0])}<div>{f1[1]}<small>{f1[2]}</small></div></div>
            <div class="sv-float f2">{svg(f2[0])}<div>{f2[1]}<small>{f2[2]}</small></div></div>
          </div>
        </div>
      </div>
    </section>

    <!-- INTEGRATIONS TICKER -->
    <section class="sv-strip theme-light">
      <div class="wrap">
        <span class="sv-strip-label">Connects with your stack</span>
        <div class="sv-strip-track">
          <div class="sv-strip-inner">
            {integrations_html}
          </div>
        </div>
      </div>
    </section>

    <!-- ENTERPRISE CAPABILITIES (ASYMMETRIC BENTO GRID) -->
    <section class="sv-sec theme-light" id="capabilities">
      <div class="wrap">
        <div class="sv-head">
          <div>
            <div class="eyebrow">Enterprise Capabilities</div>
            <h2>{cap_heading}</h2>
          </div>
          <p>{cap_sub}</p>
        </div>
{bento_html}
      </div>
    </section>

    <!-- OPERATIONAL COMPARISON: BEFORE VS AFTER -->
    <section class="sv-sec theme-alt" id="the-difference">
      <div class="wrap">
        <div class="sv-head center">
          <div>
            <div class="eyebrow">The Difference</div>
            <h2>From Manual Bottlenecks to Hands-Free Velocity</h2>
          </div>
          <p>What changes for your operational team on day one of going live.</p>
        </div>
        <div class="sv-compare-console">
          <div class="sv-compare-card is-before rv">
            <div class="compare-badge is-before">{svg("x")} TODAY &bull; MANUAL PROCESS</div>
            <h3>Fragile Manual Operations</h3>
            <ul class="compare-list">
              {before_lis}
            </ul>
          </div>

          <div class="sv-compare-divider">
            <span class="compare-trans-icon">{svg("zap")}</span>
            <span class="compare-trans-lbl">AI Shift</span>
          </div>

          <div class="sv-compare-card is-after rv">
            <div class="compare-badge is-after">{svg("check")} WITH TOCO &bull; AUTONOMOUS AI</div>
            <h3>Intelligent Agent Workflows</h3>
            <ul class="compare-list">
              {after_lis}
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- USE CASES: THE DEPARTMENT WORKFLOW STUDIO -->
    <section class="sv-sec theme-light" id="use-cases">
      <div class="wrap">
        <div class="sv-head">
          <div>
            <div class="eyebrow">Use Cases &amp; Disciplines</div>
            <h2>{studio_heading}</h2>
          </div>
          <p>{studio_sub}</p>
        </div>

        <div class="sv-studio">
          <!-- Segmented Tab Navigation -->
          <div class="sv-studio-nav" role="tablist" aria-label="Department Automations">
{studio_tabs}          </div>

          <!-- Studio Canvas & Dynamic Showcase -->
          <div class="sv-studio-canvas">
{studio_panels}          </div>
        </div>
      </div>
    </section>

    <!-- IMPLEMENTATION METHODOLOGY -->
    <section class="sv-sec theme-dark" id="how-it-works">
      <div class="wrap">
        <div class="sv-head">
          <div>
            <div class="eyebrow">How It Works</div>
            <h2>Live in Weeks, Not Quarters</h2>
          </div>
          <p>A phased rollout with a working sandbox pilot first, ensuring proven ROI before full commitment.</p>
        </div>
        <div class="sv-timeline">
{steps}        </div>
      </div>
    </section>

    <!-- MEASURABLE RESULTS -->
    <section class="sv-sec theme-blue" id="results">
      <div class="wrap">
        <div class="sv-head">
          <div>
            <div class="eyebrow">Measurable Outcomes</div>
            <h2>Verified Impact on Operational Numbers</h2>
          </div>
          <p>The commercial metrics we engineer and guarantee every engagement against.</p>
        </div>
        <div class="sv-results">{results}</div>
      </div>
    </section>

    <!-- FREQUENTLY ASKED QUESTIONS -->
    <section class="sv-sec theme-alt" id="faq">
      <div class="wrap sv-faq">
        <div>
          <div class="eyebrow">Commercial FAQs</div>
          <h2 style="font-size:clamp(30px,3.6vw,46px);margin-top:14px;letter-spacing:-.03em;">Questions We Hear from Dubai Teams</h2>
          <div class="sv-help">
            <h3>{faq_help_title}</h3>
            <p>{faq_help_desc}</p>
            <a href="https://wa.me/97145770725" target="_blank" rel="noopener" class="btn btn-primary btn-sm"><span>Message us on WhatsApp</span>{arrow}</a>
          </div>
        </div>
        <div class="faq-wrap">
{faqs}        </div>
      </div>
    </section>

    <!-- RELATED SERVICES & PRODUCTS (HIGH-VARIETY CARDS) -->
    <section class="sv-sec theme-light" id="related">
      <div class="wrap">
        <div class="sv-head">
          <div>
            <div class="eyebrow">Explore the Ecosystem</div>
            <h2>Related Services &amp; Enterprise Software</h2>
          </div>
          <p>Connect your workflows across our unified digital and software ecosystem.</p>
        </div>
{related_html}
      </div>
    </section>

    {render_cta_band(cta_title, cta_sub)}
  </main>

{render_footer()}
</body>
</html>'''

    out = os.path.join(ROOT_DIR, "services", slug, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Generated v2 service page: {url}")


def main():
    for slug in V2_SLUGS:
        build(slug)


if __name__ == "__main__":
    main()

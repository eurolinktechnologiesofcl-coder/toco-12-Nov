#!/usr/bin/env python3
"""
TOCO Technologies UAE — Complete Static Site Builder
Generates all 26 static pages, sitemap.xml, and robots.txt.
"""

import os
import sys
import json

# Ensure scratch directory is on path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_data import SERVICES_DATA, PRODUCTS_DATA
from product_bento_data import render_bento_capabilities

SITE_BASE = "https://tocotechnologies.ae"
ROOT_DIR = "/Users/mac/Downloads/toco 12 nov"

# -----------------------------------------------------------------------------
# Reusable HTML Templates
# -----------------------------------------------------------------------------

def render_header(active_nav=""):
    return f'''  <!-- Top Navigation Bar -->
  <header class="nav" id="main-nav">
    <div class="wrap">
      <a href="/" class="brand" aria-label="TOCO Technologies Homepage">
        <img src="/assets/images/logo.webp" alt="TOCO Technologies logo" width="40" height="40" class="logo-img">
        <span class="brand-text"><span class="brand-name">TOCO Technologies</span><span class="brand-sub">Dubai &bull; UAE</span></span>
      </a>

      <!-- Desktop Navigation Links -->
      <ul class="nav-links" role="menubar">
        <li role="none"><a href="/" role="menuitem" class="{'active' if active_nav == 'home' else ''}">Home</a></li>
        <li role="none"><a href="/about" role="menuitem" class="{'active' if active_nav == 'about' else ''}">About</a></li>

        <!-- Services Mega Menu -->
        <li class="dd" role="none">
          <a href="/services" role="menuitem" class="{'active' if active_nav == 'services' else ''}" aria-haspopup="true" aria-expanded="false">
            Services
            <svg class="chev" width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M2.5 4.5L6 8L9.5 4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <div class="dd-panel mega" role="menu" aria-label="Services Submenu">
            <a href="/services/ai-automation" class="dd-item" role="menuitem">
              <span class="mi">🤖</span>
              <div>
                <b>AI Automation &amp; Agents</b>
                <small>Autonomous workflow execution &amp; LLM agents</small>
              </div>
            </a>
            <a href="/services/ai-business-automation" class="dd-item" role="menuitem">
              <span class="mi">⚡</span>
              <div>
                <b>AI Business Conversions</b>
                <small>Lead capture, qualification &amp; sales automation</small>
              </div>
            </a>
            <a href="/services/mobile-app-development" class="dd-item" role="menuitem">
              <span class="mi">📱</span>
              <div>
                <b>Mobile Application Software</b>
                <small>High-concurrency iOS &amp; Android platforms</small>
              </div>
            </a>
            <a href="/services/website-and-software-development" class="dd-item" role="menuitem">
              <span class="mi">💻</span>
              <div>
                <b>Website &amp; Custom Software</b>
                <small>Enterprise web platforms &amp; cloud systems</small>
              </div>
            </a>
            <a href="/services/digital-marketing" class="dd-item" role="menuitem">
              <span class="mi">📈</span>
              <div>
                <b>Digital Marketing &amp; PPC</b>
                <small>Google Ads, Meta funnels &amp; GA4 attribution</small>
              </div>
            </a>
            <a href="/services/seo" class="dd-item" role="menuitem">
              <span class="mi">🔍</span>
              <div>
                <b>Technical SEO &amp; Dubai Search</b>
                <small>Core Web Vitals &amp; GCC high-intent ranking</small>
              </div>
            </a>
            <a href="/services/ecommerce-development" class="dd-item" role="menuitem">
              <span class="mi">🛍️</span>
              <div>
                <b>E-Commerce Development</b>
                <small>Shopify, custom stores &amp; UAE payment gateways</small>
              </div>
            </a>
            <a href="/services/erp-and-custom-software" class="dd-item" role="menuitem">
              <span class="mi">🏢</span>
              <div>
                <b>Custom ERP &amp; Business Systems</b>
                <small>Dispatch suites, portals &amp; API integrations</small>
              </div>
            </a>
            <a href="/services/social-media-management" class="dd-item" role="menuitem">
              <span class="mi">📣</span>
              <div>
                <b>Social Media Management</b>
                <small>B2B LinkedIn, video reels &amp; GCC growth</small>
              </div>
            </a>
            <a href="/services/branding-and-ui-ux-design" class="dd-item" role="menuitem">
              <span class="mi">🎨</span>
              <div>
                <b>Branding &amp; UI/UX Design</b>
                <small>Design systems, Figma &amp; brand identities</small>
              </div>
            </a>
          </div>
        </li>

        <!-- Products Mega Menu -->
        <li class="dd" role="none">
          <a href="/products" role="menuitem" class="{'active' if active_nav == 'products' else ''}" aria-haspopup="true" aria-expanded="false">
            Products
            <svg class="chev" width="12" height="12" viewBox="0 0 12 12" fill="none"><path d="M2.5 4.5L6 8L9.5 4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <div class="dd-panel mega" role="menu" aria-label="Products Submenu">
            <a href="/products/elearning-platform" class="dd-item" role="menuitem">
              <span class="mi">🎓</span>
              <div>
                <b>E-Learning Platform <span class="tag-badge live">Live</span></b>
                <small>Enterprise LMS platform &amp; training portal</small>
              </div>
            </a>
            <a href="/products/interior-quote-automation" class="dd-item" role="menuitem">
              <span class="mi">📐</span>
              <div>
                <b>Interior Quote Automation <span class="tag-badge live">Live</span></b>
                <small>Interior quote &amp; sales automation platform</small>
              </div>
            </a>
            <a href="/products/ai-erp-platform" class="dd-item" role="menuitem">
              <span class="mi">📊</span>
              <div>
                <b>AI-Powered ERP <span class="tag-badge live">Live</span></b>
                <small>Intelligent operations &amp; deal conversion</small>
              </div>
            </a>
            <a href="/products/payroll-automation" class="dd-item" role="menuitem">
              <span class="mi">💼</span>
              <div>
                <b>Payroll Automation <span class="tag-badge live">Live</span></b>
                <small>Automated UAE payroll &amp; WPS compliance</small>
              </div>
            </a>
            <a href="/products/analytics-tracking" class="dd-item" role="menuitem">
              <span class="mi">📉</span>
              <div>
                <b>Analytics Tracking Suite</b>
                <small>Multi-touch customer journey analytics</small>
              </div>
            </a>
            <a href="/products/real-estate-crm" class="dd-item" role="menuitem">
              <span class="mi">🏙️</span>
              <div>
                <b>Real Estate CRM</b>
                <small>Gulf brokerage &amp; WhatsApp lead acceleration</small>
              </div>
            </a>
          </div>
        </li>

        <li role="none"><a href="/industries" role="menuitem" class="{'active' if active_nav == 'industries' else ''}">Industries</a></li>
        <li role="none"><a href="/portfolio" role="menuitem" class="{'active' if active_nav == 'portfolio' else ''}">Portfolio</a></li>
        <li role="none"><a href="/contact" role="menuitem" class="{'active' if active_nav == 'contact' else ''}">Contact</a></li>
      </ul>

      <!-- Direct Phone & CTA -->
      <div class="nav-actions">
        <a href="tel:+97145770725" class="nav-phone" aria-label="Call TOCO Technologies Dubai">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span>+971 4 577 0725</span>
        </a>
        <a href="/contact" class="btn btn-primary btn-sm">
          <span>Book an Intro</span>
          <svg class="arr" width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
        <button class="mob-toggle" type="button" aria-label="Toggle navigation menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Slide-In Navigation -->
  <aside class="mobile-menu" aria-label="Mobile Navigation">
    <div class="mobile-menu-head">
      <a href="/" class="brand">
        <img src="/assets/images/logo.webp" alt="TOCO Technologies logo" width="40" height="40" class="logo-img">
        <span class="brand-text"><span class="brand-name">TOCO Technologies</span><span class="brand-sub">Dubai &bull; UAE</span></span>
      </a>
      <button class="mobile-close" type="button" aria-label="Close navigation menu">✕</button>
    </div>
    <div class="mobile-menu-body">
      <ul class="mobile-nav-list">
        <li><a href="/" class="mobile-link">Home</a></li>
        <li><a href="/about" class="mobile-link">About Us</a></li>
        
        <li class="mobile-nav-group">
          <button class="mobile-nav-title" type="button" aria-expanded="false">
            <span>Services (10)</span>
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 5l4 4 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
          </button>
          <ul class="mobile-sub-list">
            <li><a href="/services/ai-automation">🤖 AI Automation &amp; Agents</a></li>
            <li><a href="/services/ai-business-automation">⚡ AI Business Conversions</a></li>
            <li><a href="/services/mobile-app-development">📱 Mobile Application Software</a></li>
            <li><a href="/services/website-and-software-development">💻 Website &amp; Custom Software</a></li>
            <li><a href="/services/digital-marketing">📈 Performance Digital Marketing</a></li>
            <li><a href="/services/seo">🔍 Technical SEO &amp; Dubai Search</a></li>
            <li><a href="/services/ecommerce-development">🛍️ E-Commerce Development</a></li>
            <li><a href="/services/erp-and-custom-software">🏢 Custom ERP &amp; Business Systems</a></li>
            <li><a href="/services/social-media-management">📣 Social Media Management</a></li>
            <li><a href="/services/branding-and-ui-ux-design">🎨 Branding &amp; UI/UX Design</a></li>
          </ul>
        </li>

        <li class="mobile-nav-group">
          <button class="mobile-nav-title" type="button" aria-expanded="false">
            <span>Products (6)</span>
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 5l4 4 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
          </button>
          <ul class="mobile-sub-list">
            <li><a href="/products/elearning-platform">🎓 E-Learning Platform</a></li>
            <li><a href="/products/interior-quote-automation">📐 Interior Quote Automation</a></li>
            <li><a href="/products/ai-erp-platform">📊 AI-Powered ERP</a></li>
            <li><a href="/products/payroll-automation">💼 Payroll Automation (WPS)</a></li>
            <li><a href="/products/analytics-tracking">📉 Analytics Tracking Suite</a></li>
            <li><a href="/products/real-estate-crm">🏙️ Real Estate CRM</a></li>
          </ul>
        </li>

        <li><a href="/industries" class="mobile-link">Industries</a></li>
        <li><a href="/portfolio" class="mobile-link">Portfolio &amp; Case Studies</a></li>
        <li><a href="/contact" class="mobile-link">Contact Dubai HQ</a></li>
      </ul>
      <div class="mobile-menu-footer">
        <a href="https://wa.me/97145770725" target="_blank" rel="noopener" class="btn btn-primary" style="width:100%;justify-content:center;">
          <span>Chat on WhatsApp</span>
        </a>
        <div style="margin-top:14px;font-size:13px;color:var(--ink-3);text-align:center;">
          Port Saeed, Dubai, UAE • +971 4 577 0725
        </div>
      </div>
    </div>
  </aside>'''


def render_footer():
    return '''  <!-- Corporate Rich Footer -->
  <footer class="footer">
    <div class="wrap">
      <div class="foot-grid">
        <!-- Col 1: Brand & Contact -->
        <div class="foot-col brand-col">
          <a href="/" class="brand" aria-label="TOCO Technologies">
            <img src="/assets/images/logo.webp" alt="TOCO Technologies logo" width="40" height="40" class="logo-img">
        <span class="brand-text"><span class="brand-name">TOCO Technologies</span><span class="brand-sub">Dubai &bull; UAE</span></span>
          </a>
          <p class="foot-tagline">
            Engineering high-impact AI business automation, enterprise web &amp; mobile software, custom ERP platforms, and performance digital systems for businesses in Dubai and across the UAE.
          </p>
          <div class="foot-contact-info">
            <div class="f-info-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              <span>Port Saeed, Deira, Dubai, United Arab Emirates</span>
            </div>
            <div class="f-info-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
              <a href="tel:+97145770725">+971 4 577 0725</a>
            </div>
            <div class="f-info-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
              <a href="mailto:info@tocoplus.com">info@tocoplus.com</a>
            </div>
            <div class="f-info-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              <span>Mon – Sat: 9:00 AM – 6:00 PM GST</span>
            </div>
          </div>
        </div>

        <!-- Col 2: Services -->
        <div class="foot-col">
          <h4>Engineering Services</h4>
          <ul class="foot-links">
            <li><a href="/services/ai-automation">AI Automation &amp; Agents</a></li>
            <li><a href="/services/ai-business-automation">AI Business Conversions</a></li>
            <li><a href="/services/mobile-app-development">Mobile Application Software</a></li>
            <li><a href="/services/website-and-software-development">Website &amp; Software Development</a></li>
            <li><a href="/services/digital-marketing">Digital Marketing &amp; Ads</a></li>
            <li><a href="/services/seo">Technical SEO &amp; Dubai Search</a></li>
            <li><a href="/services/ecommerce-development">E-Commerce Development</a></li>
            <li><a href="/services/erp-and-custom-software">Custom ERP &amp; Business Systems</a></li>
            <li><a href="/services/social-media-management">Social Media Management</a></li>
            <li><a href="/services/branding-and-ui-ux-design">Branding &amp; UI/UX Design</a></li>
          </ul>
        </div>

        <!-- Col 3: Proprietary Products -->
        <div class="foot-col">
          <h4>Our Products</h4>
          <ul class="foot-links">
            <li><a href="/products/elearning-platform">E-Learning Platform</a></li>
            <li><a href="/products/interior-quote-automation">Interior Quote Automation</a></li>
            <li><a href="/products/ai-erp-platform">AI-Powered ERP</a></li>
            <li><a href="/products/payroll-automation">Payroll Automation</a></li>
            <li><a href="/products/analytics-tracking">Analytics Tracking Suite</a></li>
            <li><a href="/products/real-estate-crm">Real Estate CRM</a></li>
            <li><a href="/products">All Products Hub</a></li>
          </ul>
        </div>

        <!-- Col 4: Corporate & Industries -->
        <div class="foot-col">
          <h4>Company &amp; Industry</h4>
          <ul class="foot-links">
            <li><a href="/about">About TOCO Technologies</a></li>
            <li><a href="/industries">Industries We Serve</a></li>
            <li><a href="/portfolio">Portfolio &amp; Client Impact</a></li>
            <li><a href="/contact">Contact &amp; Dubai Office</a></li>
            <li><a href="https://wa.me/97145770725" target="_blank" rel="noopener">WhatsApp Direct Support</a></li>
            <li><a href="/privacy-policy">Privacy Policy (UAE PDP Law)</a></li>
            <li><a href="/terms-of-service">Terms of Service &amp; SLA</a></li>
            <li><a href="/sitemap.xml">XML Sitemap</a></li>
          </ul>
        </div>
      </div>

      <div class="foot-bar">
        <p>&copy; <span class="current-year">2026</span> TOCO Technologies UAE. All rights reserved. Registered in Dubai, United Arab Emirates.</p>
        <div class="foot-bar-links">
          <a href="/privacy-policy">Privacy</a>
          <span>•</span>
          <a href="/terms-of-service">Terms &amp; SLA</a>
          <span>•</span>
          <a href="/contact">Dubai HQ</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Floating Back to Top Button -->
  <button id="back-to-top" class="back-to-top" type="button" aria-label="Scroll back to top">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg>
  </button>

  <script src="/assets/js/main.js" defer></script>'''


def render_head_tags(title, desc, canonical, schema_json):
    return f'''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="author" content="TOCO Technologies">
  <meta name="theme-color" content="#060911">
  <meta name="geo.region" content="AE-DU">
  <meta name="geo.placename" content="Port Saeed, Dubai">
  <meta name="geo.position" content="25.249344;55.331351">
  <meta name="ICBM" content="25.249344, 55.331351">

  <link rel="canonical" href="{canonical}">
  <link rel="icon" type="image/svg+xml" href="/assets/images/favicon.svg">
  <link rel="apple-touch-icon" href="/assets/images/logo.webp">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="TOCO Technologies">
  <meta property="og:locale" content="en_AE">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{SITE_BASE}/assets/images/og-cover.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@TocoTechnologies">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{SITE_BASE}/assets/images/og-cover.jpg">

  <!-- Google Fonts Preconnect -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">

  <!-- Core Stylesheet -->
  <link rel="stylesheet" href="/assets/css/style.css">

  <!-- Structured Data JSON-LD -->
  <script type="application/ld+json">
{json.dumps(schema_json, indent=2)}
  </script>
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>
'''

def render_cta_band(title="Ready to Build Your Next Digital Advantage?", subtitle="Partner with TOCO Technologies in Dubai to architect high-performance AI automation, web applications, and scalable software solutions."):
    return f'''  <!-- Full Width CTA Band -->
  <section class="sec" style="padding-top:40px;">
    <div class="wrap">
      <div class="card cta-band rv">
        <div>
          <h2 style="font-size:clamp(26px, 3.2vw, 42px);margin-bottom:12px;">{title}</h2>
          <p style="color:var(--ink-2);max-width:620px;font-size:16px;line-height:1.6;">
            {subtitle}
          </p>
        </div>
        <div class="cta-actions" style="display:flex;gap:12px;flex-wrap:wrap;">
          <a href="/contact" class="btn btn-primary">
            <span>Schedule Discovery Call</span>
            <svg class="arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="https://wa.me/97145770725" target="_blank" rel="noopener" class="btn btn-ghost">
            <span>Chat via WhatsApp</span>
          </a>
        </div>
      </div>
    </div>
  </section>'''

def render_breadcrumbs(crumbs):
    crumb_items = []
    for label, url in crumbs:
        if url:
            crumb_items.append(f'<a href="{url}">{label}</a>')
        else:
            crumb_items.append(f'<span>{label}</span>')
    sep = '<span class="sep">/</span>'
    return f'<nav class="crumbs" aria-label="Breadcrumb">{sep.join(crumb_items)}</nav>'

def make_breadcrumb_schema(crumbs):
    elements = []
    for i, (label, url) in enumerate(crumbs):
        item_id = f"{SITE_BASE}{url}" if url and url.startswith('/') else (url if url else f"{SITE_BASE}")
        elements.append({
            "@type": "ListItem",
            "position": i + 1,
            "name": label,
            "item": item_id
        })
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elements
    }

def make_faq_schema(faq_items):
    entities = []
    for item in faq_items:
        entities.append({
            "@type": "Question",
            "name": item["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["a"]
            }
        })
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }

# -----------------------------------------------------------------------------
# Generate Individual Service Page
# -----------------------------------------------------------------------------
def generate_service_page(svc):
    slug = svc["slug"]
    url = f"/services/{slug}"
    canonical = f"{SITE_BASE}{url}"
    
    crumbs = [("Home", "/"), ("Services", "/services"), (svc["h1"].split(" in ")[0], "")]
    
    # JSON-LD Schema
    schema_graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": f"{canonical}#service",
                "name": svc["h1"],
                "serviceType": svc["h1"],
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
                    }
                },
                "areaServed": [
                    {"@type": "City", "name": "Dubai"},
                    {"@type": "City", "name": "Abu Dhabi"},
                    {"@type": "Country", "name": "United Arab Emirates"}
                ]
            },
            make_breadcrumb_schema(crumbs),
            make_faq_schema(svc["faqs"])
        ]
    }

    # Features HTML
    features_html = ""
    for f in svc["features"]:
        features_html += f'''        <div class="card feature-box rv">
          <div class="f-ico">{f["icon"]}</div>
          <h4>{f["title"]}</h4>
          <p>{f["desc"]}</p>
        </div>\n'''

    # Steps HTML
    steps_html = ""
    for s in svc["steps"]:
        steps_html += f'''        <div class="card step-card rv">
          <div class="step-num">{s["num"]}</div>
          <h3 style="font-size:20px;margin-bottom:10px;font-family:var(--font-display);">{s["title"]}</h3>
          <p style="color:var(--ink-2);font-size:14.5px;line-height:1.6;">{s["desc"]}</p>
        </div>\n'''

    # Benefits HTML
    benefits_html = ""
    for b in svc["benefits"]:
        benefits_html += f'''        <div class="card stat-card rv">
          <div class="stat-num">{b["metric"]}</div>
          <div class="stat-lbl" style="font-size:16px;font-weight:700;color:var(--ink);margin-bottom:6px;">{b["title"]}</div>
          <p style="color:var(--ink-3);font-size:13.5px;line-height:1.5;">{b["desc"]}</p>
        </div>\n'''

    # Tech Stack HTML
    tech_html = "".join([f'<span class="t-chip">{tech}</span>' for tech in svc["tech_stack"]])

    # FAQs HTML
    faqs_html = ""
    for i, faq in enumerate(svc["faqs"]):
        is_first = (i == 0)
        faqs_html += f'''        <div class="faq-item{' open' if is_first else ''}">
          <button class="faq-q" type="button" aria-expanded="{'true' if is_first else 'false'}">
            <span>{faq["q"]}</span>
            <i></i>
          </button>
          <div class="faq-a" style="{'max-height:200px;' if is_first else ''}">
            <div class="faq-a-inner">
              <p>{faq["a"]}</p>
            </div>
          </div>
        </div>\n'''

    # Related Services HTML
    related_html = ""
    for rel in svc["related"]:
        related_html += f'''        <a href="{rel["url"]}" class="card rv" style="text-decoration:none;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
            <h4 style="font-size:18px;color:var(--ink);">{rel["title"]}</h4>
            <span style="color:var(--cyan);font-size:18px;">↗</span>
          </div>
          <p style="font-size:14px;color:var(--ink-2);line-height:1.5;">{rel["desc"]}</p>
        </a>\n'''

    html_content = f'''{render_head_tags(svc["title"], svc["meta_desc"], canonical, schema_graph)}
{render_header("services")}

  <main id="main-content">
    <!-- Inner Page Hero -->
    <section class="page-hero">
      <div class="wrap">
        {render_breadcrumbs(crumbs)}
        <div style="max-width:820px;">
          <div class="eyebrow">Enterprise Service • Dubai &amp; UAE</div>
          <h1>{svc["h1"]}</h1>
          <p class="lede">{svc["lede"]}</p>
          <div style="display:flex;gap:12px;margin-top:28px;flex-wrap:wrap;">
            <a href="/contact" class="btn btn-primary">
              <span>Book Strategy Consultation</span>
              <svg class="arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
            <a href="https://wa.me/97145770725" target="_blank" rel="noopener" class="btn btn-ghost">
              <span>WhatsApp Direct Line</span>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Capabilities / What's Included Grid -->
    <section class="sec">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Enterprise Capabilities</div>
          <h2>What's Included in Our Engineering Suite</h2>
          <p>End-to-end deliverables designed for high performance, commercial reliability, and long-term maintainability.</p>
        </div>
        <div class="grid-3">
{features_html}        </div>
      </div>
    </section>

    <!-- How It Works / Process -->
    <section class="sec" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Implementation Methodology</div>
          <h2>How We Engineer and Deploy in Dubai</h2>
          <p>A proven, phased delivery framework ensuring transparency, rapid velocity, and zero business disruption.</p>
        </div>
        <div class="grid-4">
{steps_html}        </div>
      </div>
    </section>

    <!-- Measurable Business Benefits -->
    <section class="sec">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Measurable Commercial Impact</div>
          <h2>Proven Outcomes for UAE Enterprises</h2>
          <p>We measure success not in vanity statistics, but in verified operational velocity and commercial revenue.</p>
        </div>
        <div class="grid-4">
{benefits_html}        </div>
      </div>
    </section>

    <!-- Tech Stack -->
    <section class="sec" style="padding-top:10px;padding-bottom:50px;">
      <div class="wrap">
        <div class="card" style="padding:clamp(24px, 4vw, 36px);text-align:center;">
          <h3 style="font-size:20px;margin-bottom:14px;font-family:var(--font-display);">Production-Grade Technology Stack</h3>
          <p style="color:var(--ink-2);max-width:640px;margin:0 auto 20px;font-size:14.5px;">
            Engineered with modern, battle-tested frameworks that ensure high concurrency, ironclad security, and zero vendor lock-in.
          </p>
          <div class="tech-chips" style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;">
            {tech_html}
          </div>
        </div>
      </div>
    </section>

    <!-- Frequently Asked Questions -->
    <section class="sec" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Commercial FAQs</div>
          <h2>Frequently Asked Questions in Dubai &amp; UAE</h2>
          <p>Transparent answers regarding timelines, data security, compliance, and ongoing maintenance.</p>
        </div>
        <div class="faq-wrap">
{faqs_html}        </div>
      </div>
    </section>

    <!-- Related Services -->
    <section class="sec">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Explore Further</div>
          <h2>Complementary Engineering &amp; Growth Solutions</h2>
          <p>Connect your workflows across our unified digital and software ecosystem.</p>
        </div>
        <div class="grid-3">
{related_html}        </div>
      </div>
    </section>

    {render_cta_band("Ready to Accelerate Your Business in Dubai?", "Connect with TOCO Technologies' senior engineers in Port Saeed, Dubai. We'll review your project scope and provide a fixed-price proposal within 24 hours.")}
  </main>

{render_footer()}
</body>
</html>'''

    out_dir = os.path.join(ROOT_DIR, "services", slug)
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated service page: {url}")


# -----------------------------------------------------------------------------
# Generate Individual Product Page
# -----------------------------------------------------------------------------
def render_product_capabilities(prod, features_html):
    slug = prod["slug"]
    bento = render_bento_capabilities(slug)
    if bento:
        return bento
    return f'''    <!-- Platform Features -->
    <section class="sec">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Platform Capabilities</div>
          <h2>Engineered for High-Velocity Business Execution</h2>
          <p>Every feature is designed to reduce friction, eliminate operational error, and accelerate commercial workflow.</p>
        </div>
        <div class="grid-3">
{features_html}        </div>
      </div>
    </section>'''


def generate_product_page(prod):
    slug = prod["slug"]
    url = f"/products/{slug}"
    canonical = f"{SITE_BASE}{url}"
    is_waitlist = prod.get("is_waitlist", False)

    crumbs = [("Home", "/"), ("Products", "/products"), (prod["h1"].split(" — ")[0], "")]

    # JSON-LD Schema
    schema_graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "SoftwareApplication",
                "@id": f"{canonical}#software",
                "name": prod["h1"],
                "applicationCategory": "BusinessApplication",
                "operatingSystem": "Cloud, Web, Mobile",
                "description": prod["meta_desc"],
                "creator": {
                    "@type": "Organization",
                    "name": "TOCO Technologies",
                    "url": SITE_BASE
                }
            },
            make_breadcrumb_schema(crumbs),
            make_faq_schema(prod["faqs"])
        ]
    }

    # Features HTML
    features_html = ""
    for f in prod["features"]:
        features_html += f'''        <div class="card feature-box rv">
          <div class="f-ico">{f["icon"]}</div>
          <h4>{f["title"]}</h4>
          <p>{f["desc"]}</p>
        </div>\n'''

    # Steps HTML
    steps_html = ""
    for s in prod["steps"]:
        steps_html += f'''        <div class="card step-card rv">
          <div class="step-num">{s["num"]}</div>
          <h3 style="font-size:20px;margin-bottom:10px;font-family:var(--font-display);">{s["title"]}</h3>
          <p style="color:var(--ink-2);font-size:14.5px;line-height:1.6;">{s["desc"]}</p>
        </div>\n'''

    # Benefits HTML
    benefits_html = ""
    for b in prod["benefits"]:
        benefits_html += f'''        <div class="card stat-card rv">
          <div class="stat-num">{b["metric"]}</div>
          <div class="stat-lbl" style="font-size:16px;font-weight:700;color:var(--ink);margin-bottom:6px;">{b["title"]}</div>
          <p style="color:var(--ink-3);font-size:13.5px;line-height:1.5;">{b["desc"]}</p>
        </div>\n'''

    # Tech Stack HTML
    tech_html = "".join([f'<span class="t-chip">{tech}</span>' for tech in prod["tech_stack"]])

    # FAQs HTML
    faqs_html = ""
    for i, faq in enumerate(prod["faqs"]):
        is_first = (i == 0)
        faqs_html += f'''        <div class="faq-item{' open' if is_first else ''}">
          <button class="faq-q" type="button" aria-expanded="{'true' if is_first else 'false'}">
            <span>{faq["q"]}</span>
            <i></i>
          </button>
          <div class="faq-a" style="{'max-height:200px;' if is_first else ''}">
            <div class="faq-a-inner">
              <p>{faq["a"]}</p>
            </div>
          </div>
        </div>\n'''

    # Hero Action / Waitlist Form
    if is_waitlist:
        hero_action = '''        <form class="waitlist-form" style="margin-top:24px;">
          <input type="email" class="form-control" placeholder="Enter corporate email for VIP early access" required>
          <button type="submit" class="btn btn-primary">
            <span>Join VIP Waitlist</span>
            <svg class="arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
          <div class="waitlist-status"></div>
        </form>
        <p style="font-size:13px;color:var(--ink-3);margin-top:10px;">Private beta invitations rolling out to Dubai &amp; GCC enterprises in Q3 2026.</p>'''
    else:
        hero_action = '''        <div style="display:flex;gap:12px;margin-top:28px;flex-wrap:wrap;">
          <a href="/contact" class="btn btn-primary">
            <span>Request Platform Demo</span>
            <svg class="arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="https://wa.me/97145770725" target="_blank" rel="noopener" class="btn btn-ghost">
            <span>WhatsApp Product Specialist</span>
          </a>
        </div>'''

    # Related Links
    related_html = ""
    for rel in prod["related"]:
        related_html += f'''        <a href="{rel["url"]}" class="card rv" style="text-decoration:none;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
            <h4 style="font-size:18px;color:var(--ink);">{rel["title"]}</h4>
            <span style="color:var(--cyan);font-size:18px;">↗</span>
          </div>
          <p style="font-size:14px;color:var(--ink-2);line-height:1.5;">{rel["desc"]}</p>
        </a>\n'''

    capabilities_html = render_product_capabilities(prod, features_html)

    html_content = f'''{render_head_tags(prod["title"], prod["meta_desc"], canonical, schema_graph)}
{render_header("products")}

  <main id="main-content">
    <!-- Product Hero -->
    <section class="page-hero">
      <div class="wrap">
        {render_breadcrumbs(crumbs)}
        <div style="max-width:840px;">
          <div class="eyebrow" style="color:var(--cyan);">{prod["status_badge"]}</div>
          <h1>{prod["h1"]}</h1>
          <p class="lede">{prod["lede"]}</p>
{hero_action}
        </div>
      </div>
    </section>

{capabilities_html}

    <!-- Architecture & Process -->
    <section class="sec" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Enterprise Delivery</div>
          <h2>Deployment &amp; Onboarding Roadmap</h2>
          <p>From initial provisioning to enterprise team adoption, our engineers ensure a frictionless launch.</p>
        </div>
        <div class="grid-4">
{steps_html}        </div>
      </div>
    </section>

    <!-- Measurable Benefits -->
    <section class="sec">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Platform Value</div>
          <h2>Demonstrated Impact on Business Performance</h2>
          <p>Real-world metrics observed across active enterprise installations in the UAE.</p>
        </div>
        <div class="grid-4">
{benefits_html}        </div>
      </div>
    </section>

    <!-- Tech Stack -->
    <section class="sec" style="padding-top:10px;padding-bottom:50px;">
      <div class="wrap">
        <div class="card" style="padding:clamp(24px, 4vw, 36px);text-align:center;">
          <h3 style="font-size:20px;margin-bottom:14px;font-family:var(--font-display);">Underlying Technology Stack</h3>
          <p style="color:var(--ink-2);max-width:640px;margin:0 auto 20px;font-size:14.5px;">
            High-concurrency microservices, encrypted databases, and compliant cloud hosting within UAE borders.
          </p>
          <div class="tech-chips" style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;">
            {tech_html}
          </div>
        </div>
      </div>
    </section>

    <!-- FAQs -->
    <section class="sec" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Product Questions</div>
          <h2>Frequently Asked Questions</h2>
          <p>Clear details regarding licensing, deployment models, integrations, and compliance.</p>
        </div>
        <div class="faq-wrap">
{faqs_html}        </div>
      </div>
    </section>

    <!-- Related Links -->
    <section class="sec">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Explore Ecosystem</div>
          <h2>Related Software &amp; Capabilities</h2>
          <p>Connect this platform with custom engineering and growth systems.</p>
        </div>
        <div class="grid-3">
{related_html}        </div>
      </div>
    </section>

    {render_cta_band("Experience the Power of Proprietary TOCO Software", "Schedule a private demonstration with our product engineering team in Dubai, UAE.")}
  </main>

{render_footer()}
</body>
</html>'''

    out_dir = os.path.join(ROOT_DIR, "products", slug)
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated product page: {url}")


print("Service and Product generator functions defined.")

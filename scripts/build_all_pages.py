#!/usr/bin/env python3
"""
TOCO Technologies UAE — Static Site Builder (Full 26-Page Suite)
Builds all 26 static pages, sitemap.xml, and robots.txt.
"""

import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_data import SERVICES_DATA, PRODUCTS_DATA
from build_full_site import generate_service_page, generate_product_page

SITE_BASE = "https://tocotechnologies.ae"
ROOT_DIR = "/Users/mac/Downloads/toco 12 nov"

# -----------------------------------------------------------------------------
# Common UI Helpers
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
# 1. Generate Services Overview Hub (/services/index.html)
# -----------------------------------------------------------------------------
def build_services_hub():
    url = "/services"
    canonical = f"{SITE_BASE}{url}"
    title = "Engineering Services in Dubai | TOCO Technologies"
    desc = "Explore our 10 specialized digital & software engineering services in Dubai, UAE: AI automation, mobile apps, web engineering, ERP, and SEO."
    crumbs = [("Home", "/"), ("Services", "")]

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "@id": f"{canonical}#webpage",
                "name": title,
                "description": desc,
                "url": canonical
            },
            make_breadcrumb_schema(crumbs)
        ]
    }

    cards_html = ""
    for svc in SERVICES_DATA:
        cards_html += f'''        <a href="/services/{svc["slug"]}" class="card rv" style="text-decoration:none;display:flex;flex-direction:column;justify-content:space-between;">
          <div>
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:14px;">
              <span style="font-size:28px;">{svc["features"][0]["icon"]}</span>
              <span style="color:var(--cyan);font-size:20px;font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">{svc["h1"].split(" in ")[0]}</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:16px;">{svc["lede"][:135]}...</p>
          </div>
          <div class="tags" style="display:flex;gap:6px;flex-wrap:wrap;">
            <span class="t-chip" style="font-size:11px;padding:3px 8px;">{svc["tech_stack"][0]}</span>
            <span class="t-chip" style="font-size:11px;padding:3px 8px;">{svc["tech_stack"][1]}</span>
            <span class="t-chip" style="font-size:11px;padding:3px 8px;">{svc["tech_stack"][2]}</span>
          </div>
        </a>\n'''

    content = f'''{render_head_tags(title, desc, canonical, schema)}
{render_header("services")}
  <main id="main-content">
    <section class="page-hero">
      <div class="wrap">
        {render_breadcrumbs(crumbs)}
        <div style="max-width:820px;">
          <div class="eyebrow">Enterprise Offerings • Dubai &amp; Across UAE</div>
          <h1>End-to-End Digital &amp; Software Engineering Services</h1>
          <p class="lede">
            From autonomous AI agents and enterprise web platforms to bespoke ERP systems and high-converting performance marketing, we engineer technology that delivers demonstrable business advantage.
          </p>
        </div>
      </div>
    </section>

    <section class="sec">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Complete Service Catalog</div>
          <h2>Our 10 Core Engineering &amp; Growth Disciplines</h2>
          <p>Every offering is backed by our senior engineering team in Port Saeed, Dubai, and guaranteed by our 30-day post-launch warranty.</p>
        </div>
        <div class="grid-3">
{cards_html}        </div>
      </div>
    </section>

    {render_cta_band("Need a Custom Technology Solution for Your Business?", "Schedule a discovery meeting with our Dubai leadership to explore how our engineering capabilities fit your exact operational requirements.")}
  </main>
{render_footer()}
</body>
</html>'''

    out_dir = os.path.join(ROOT_DIR, "services")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated Services Hub: /services")


# -----------------------------------------------------------------------------
# 2. Generate Products Overview Hub (/products/index.html)
# -----------------------------------------------------------------------------
def build_products_hub():
    url = "/products"
    canonical = f"{SITE_BASE}{url}"
    title = "Proprietary Software Platforms & Products | TOCO Technologies"
    desc = "Explore software products engineered by TOCO Technologies in Dubai: e-learning, interior quote automation, AI-powered ERP and UAE payroll automation."
    crumbs = [("Home", "/"), ("Products", "")]

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "@id": f"{canonical}#webpage",
                "name": title,
                "description": desc,
                "url": canonical
            },
            make_breadcrumb_schema(crumbs)
        ]
    }

    cards_html = ""
    for prod in PRODUCTS_DATA:
        is_dev = prod.get("is_waitlist", False)
        badge_cls = "dev" if is_dev else "live"
        badge_txt = "In Development" if is_dev else "Live Platform"
        cards_html += f'''        <a href="/products/{prod["slug"]}" class="card rv" style="text-decoration:none;display:flex;flex-direction:column;justify-content:space-between;">
          <div>
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
              <span class="tag-badge {badge_cls}">{badge_txt}</span>
              <span style="color:var(--cyan);font-size:20px;font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">{prod["h1"].split(" — ")[0]}</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:16px;">{prod["lede"][:135]}...</p>
          </div>
          <div class="tags" style="display:flex;gap:6px;flex-wrap:wrap;">
            <span class="t-chip" style="font-size:11px;padding:3px 8px;">{prod["tech_stack"][0]}</span>
            <span class="t-chip" style="font-size:11px;padding:3px 8px;">{prod["tech_stack"][1]}</span>
            <span class="t-chip" style="font-size:11px;padding:3px 8px;">{prod["tech_stack"][2]}</span>
          </div>
        </a>\n'''

    content = f'''{render_head_tags(title, desc, canonical, schema)}
{render_header("products")}
  <main id="main-content">
    <section class="page-hero">
      <div class="wrap">
        {render_breadcrumbs(crumbs)}
        <div style="max-width:820px;">
          <div class="eyebrow">Proprietary Software • Built by TOCO</div>
          <h1>Proprietary Software Platforms &amp; AI Products</h1>
          <p class="lede">
            In addition to custom client engineering, TOCO Technologies architects purpose-built proprietary SaaS platforms designed for key regional industries across Dubai and the Arabian Gulf.
          </p>
        </div>
      </div>
    </section>

    <section class="sec">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Product Portfolio</div>
          <h2>Production Platforms &amp; Next-Gen Solutions</h2>
          <p>Explore our battle-tested live platforms or explore our upcoming business intelligence and CRM suites.</p>
        </div>
        <div class="grid-3">
{cards_html}        </div>
      </div>
    </section>

    {render_cta_band("Looking to License or White-Label Our Products?", "Speak with TOCO Technologies' product team about enterprise deployment, multi-tenant white-labeling, or dedicated on-premise installation.")}
  </main>
{render_footer()}
</body>
</html>'''

    out_dir = os.path.join(ROOT_DIR, "products")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated Products Hub: /products")


# -----------------------------------------------------------------------------
# 3. Generate About Page (/about/index.html)
# -----------------------------------------------------------------------------
def build_about_page():
    url = "/about"
    canonical = f"{SITE_BASE}{url}"
    title = "About TOCO Technologies | Dubai UAE Software Engineering"
    desc = "About TOCO Technologies UAE. Headquartered in Port Saeed, Dubai. We engineer AI automation, custom software, and digital solutions for Gulf enterprises."
    crumbs = [("Home", "/"), ("About Us", "")]

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "AboutPage",
                "@id": f"{canonical}#about",
                "name": title,
                "description": desc,
                "url": canonical
            },
            make_breadcrumb_schema(crumbs)
        ]
    }

    content = f'''{render_head_tags(title, desc, canonical, schema)}
{render_header("about")}
  <main id="main-content">
    <section class="page-hero">
      <div class="wrap">
        {render_breadcrumbs(crumbs)}
        <div style="max-width:840px;">
          <div class="eyebrow">About TOCO Technologies UAE</div>
          <h1>Engineering High-Impact Software &amp; AI Systems in Dubai</h1>
          <p class="lede">
            Headquartered in Port Saeed, Deira, Dubai, TOCO Technologies is a premier software engineering and artificial intelligence consultancy. We partner with Gulf enterprises, fast-scaling startups, and government entities to build resilient digital platforms.
          </p>
        </div>
      </div>
    </section>

    <!-- Company Story & Purpose -->
    <section class="sec">
      <div class="wrap">
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;">
          <div>
            <div class="eyebrow">Our Mission &amp; Heritage</div>
            <h2 style="font-size:clamp(26px, 3.2vw, 38px);margin-bottom:16px;">Technology That Moves Your Business Forward</h2>
            <p style="color:var(--ink-2);font-size:15.5px;line-height:1.65;margin-bottom:16px;">
              Founded with the belief that UAE businesses deserve engineering excellence without the overhead or complexity of generic global agencies, TOCO Technologies brings together senior software architects, AI researchers, and UX designers based locally in Dubai.
            </p>
            <p style="color:var(--ink-2);font-size:15.5px;line-height:1.65;margin-bottom:24px;">
              We don't sell bloated templates or lock clients into opaque vendor agreements. Every line of code, database schema, and automated agent pipeline is engineered for clean performance, high concurrency, and complete intellectual property ownership.
            </p>
            <div style="display:flex;gap:16px;flex-wrap:wrap;">
              <a href="/contact" class="btn btn-primary">
                <span>Visit Dubai Office</span>
                <svg class="arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </a>
              <a href="/portfolio" class="btn btn-ghost">
                <span>View Client Case Studies</span>
              </a>
            </div>
          </div>
          <div>
            <div class="card" style="padding:12px;overflow:hidden;border-radius:var(--radius);">
              <img src="/assets/images/about-office.webp" alt="TOCO Technologies Engineering Hub Dubai" width="600" height="400" style="width:100%;height:auto;border-radius:calc(var(--radius) - 8px);display:block;">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Core Engineering Principles -->
    <section class="sec" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Engineering Standards</div>
          <h2>Our Core Technical Commitments</h2>
          <p>The engineering principles that guide every architecture we design, build, and deploy.</p>
        </div>
        <div class="grid-4">
          <div class="card rv">
            <div style="font-size:32px;margin-bottom:14px;">⚡</div>
            <h3 style="font-size:19px;margin-bottom:8px;font-family:var(--font-display);">Performance-First Architecture</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Sub-second page speeds, Core Web Vitals dominance, and lightweight codebases built without bloated third-party dependencies.
            </p>
          </div>
          <div class="card rv">
            <div style="font-size:32px;margin-bottom:14px;">🛡️</div>
            <h3 style="font-size:19px;margin-bottom:8px;font-family:var(--font-display);">Data Sovereignty &amp; Security</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Strict adherence to UAE Federal Decree-Law No. 45 on Personal Data Protection, offering private cloud and on-premise deployments.
            </p>
          </div>
          <div class="card rv">
            <div style="font-size:32px;margin-bottom:14px;">🔓</div>
            <h3 style="font-size:19px;margin-bottom:8px;font-family:var(--font-display);">Zero Vendor Lock-In</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Complete transfer of all intellectual property, source repositories, documentation, and credentials upon project completion.
            </p>
          </div>
          <div class="card rv">
            <div style="font-size:32px;margin-bottom:14px;">🤝</div>
            <h3 style="font-size:19px;margin-bottom:8px;font-family:var(--font-display);">30-Day Launch Warranty</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Every deployment includes 30 days of comprehensive engineering warranty and live SLA monitoring at zero additional cost.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Leadership & Physical Presence in Dubai -->
    <section class="sec">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Local Presence</div>
          <h2>Serving Businesses Across Dubai &amp; the UAE</h2>
          <p>Based in Port Saeed, Deira, we provide direct in-person consultation and technical support across all Emirates.</p>
        </div>
        <div class="grid-3">
          <div class="card rv">
            <div style="font-size:24px;color:var(--blue-bright);margin-bottom:10px;">📍</div>
            <h4 style="font-size:18px;margin-bottom:8px;">Port Saeed, Dubai HQ</h4>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Conveniently located in Port Saeed, Deira, minutes away from Dubai International Airport and central business corridors.
            </p>
          </div>
          <div class="card rv">
            <div style="font-size:24px;color:var(--cyan);margin-bottom:10px;">📞</div>
            <h4 style="font-size:18px;margin-bottom:8px;">Direct Engineering Line</h4>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Call +971 4 577 0725 or message our technical leadership on WhatsApp for urgent architectural reviews.
            </p>
          </div>
          <div class="card rv">
            <div style="font-size:24px;color:var(--emerald);margin-bottom:10px;">⏱️</div>
            <h4 style="font-size:18px;margin-bottom:8px;">GST Operating Hours</h4>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Monday through Saturday: 9:00 AM – 6:00 PM Gulf Standard Time, with 24/7 on-call emergency SLA support for enterprise clients.
            </p>
          </div>
        </div>
      </div>
    </section>

    {render_cta_band("Ready to Meet Our Dubai Engineering Team?", "Schedule a consultation at our Port Saeed office or book a video strategy session.")}
  </main>
{render_footer()}
</body>
</html>'''

    out_dir = os.path.join(ROOT_DIR, "about")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated About Page: /about")


# -----------------------------------------------------------------------------
# 4. Generate Industries Page (/industries/index.html)
# -----------------------------------------------------------------------------
def build_industries_page():
    url = "/industries"
    canonical = f"{SITE_BASE}{url}"
    title = "Industries We Serve in Dubai UAE | TOCO Technologies"
    desc = "Specialized technology solutions for UAE industries: Logistics, Luxury Retail, Real Estate, Healthcare, E-Learning, and Professional Services."
    crumbs = [("Home", "/"), ("Industries", "")]

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"{canonical}#webpage",
                "name": title,
                "description": desc,
                "url": canonical
            },
            make_breadcrumb_schema(crumbs)
        ]
    }

    industries_list = [
        {
            "num": "01",
            "title": "Logistics &amp; Dispatch",
            "desc": "Real-time fleet tracking, automated manifests, and multi-courier dispatch consoles for UAE distribution.",
            "link": "/services/erp-and-custom-software",
            "svg": '''<svg viewBox="0 0 200 120" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="20" y="55" width="100" height="45" rx="2" stroke="currentColor" stroke-width="1.5"/>
              <rect x="120" y="65" width="60" height="35" rx="2" stroke="currentColor" stroke-width="1.5"/>
              <line x1="20" y1="75" x2="120" y2="75" stroke="currentColor" stroke-width="1.5"/>
              <circle cx="45" cy="102" r="8" stroke="currentColor" stroke-width="1.5"/>
              <circle cx="90" cy="102" r="8" stroke="currentColor" stroke-width="1.5"/>
              <circle cx="150" cy="102" r="8" stroke="currentColor" stroke-width="1.5"/>
              <rect x="135" y="40" width="30" height="25" rx="1" fill="#4ADE80" fill-opacity="0.3" stroke="currentColor" stroke-width="1.5"/>
            </svg>'''
        },
        {
            "num": "02",
            "title": "Luxury Retail &amp; E-Commerce",
            "desc": "High-converting storefronts with Apple Pay, Tabby / Tamara, and multi-currency GCC checkout.",
            "link": "/services/ecommerce-development",
            "svg": '''<svg viewBox="0 0 200 120" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="30" y="20" width="140" height="90" rx="3" stroke="currentColor" stroke-width="1.5"/>
              <rect x="30" y="20" width="140" height="22" rx="3" stroke="currentColor" stroke-width="1.5" fill="currentColor" fill-opacity="0.06"/>
              <rect x="50" y="52" width="40" height="40" rx="2" stroke="currentColor" stroke-width="1.5"/>
              <rect x="100" y="52" width="55" height="8" rx="1" stroke="currentColor" stroke-width="1.5"/>
              <rect x="100" y="78" width="55" height="8" rx="1" fill="#4ADE80" fill-opacity="0.3" stroke="currentColor" stroke-width="1.5"/>
              <circle cx="38" cy="31" r="4" fill="currentColor" fill-opacity="0.2" stroke="currentColor" stroke-width="1"/>
              <circle cx="52" cy="31" r="4" fill="currentColor" fill-opacity="0.2" stroke="currentColor" stroke-width="1"/>
            </svg>'''
        },
        {
            "num": "03",
            "title": "Real Estate &amp; Property",
            "desc": "Off-plan inventory management, WhatsApp lead intake, and interactive client presentation portals.",
            "link": "/products/real-estate-crm",
            "svg": '''<svg viewBox="0 0 200 120" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="25" y="45" width="60" height="65" rx="2" stroke="currentColor" stroke-width="1.5"/>
              <rect x="35" y="55" width="12" height="12" rx="1" stroke="currentColor" stroke-width="1.2"/>
              <rect x="55" y="55" width="12" height="12" rx="1" stroke="currentColor" stroke-width="1.2"/>
              <rect x="38" y="93" width="24" height="17" stroke="currentColor" stroke-width="1.2"/>
              <rect x="90" y="30" width="85" height="80" rx="2" stroke="currentColor" stroke-width="1.5"/>
              <rect x="100" y="40" width="20" height="20" rx="1" stroke="currentColor" stroke-width="1.2"/>
              <rect x="130" y="40" width="20" height="20" rx="1" stroke="currentColor" stroke-width="1.2"/>
              <circle cx="150" cy="22" r="6" fill="#4ADE80" fill-opacity="0.4" stroke="currentColor" stroke-width="1.2"/>
              <circle cx="168" cy="22" r="6" fill="#4ADE80" fill-opacity="0.4" stroke="currentColor" stroke-width="1.2"/>
            </svg>'''
        },
        {
            "num": "04",
            "title": "Healthcare &amp; Medical",
            "desc": "Patient appointment portals, WhatsApp reminder sequences, and secure EMR database sync.",
            "link": "/services/website-and-software-development",
            "svg": '''<svg viewBox="0 0 200 120" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="30" y="30" width="140" height="80" rx="4" stroke="currentColor" stroke-width="1.5"/>
              <rect x="30" y="30" width="140" height="22" rx="4" stroke="currentColor" stroke-width="1.5" fill="currentColor" fill-opacity="0.05"/>
              <rect x="50" y="65" width="30" height="30" rx="2" stroke="currentColor" stroke-width="1.2"/>
              <line x1="65" y1="70" x2="65" y2="90" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
              <line x1="55" y1="80" x2="75" y2="80" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
              <rect x="95" y="62" width="60" height="8" rx="2" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.08"/>
              <rect x="95" y="76" width="45" height="8" rx="2" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.05"/>
              <rect x="95" y="90" width="52" height="8" rx="2" fill="#4ADE80" fill-opacity="0.3" stroke="currentColor" stroke-width="1.2"/>
            </svg>'''
        },
        {
            "num": "05",
            "title": "Education &amp; e-Learning",
            "desc": "Bilingual LMS portals, DRM video streaming, automated grading, and digital completion certificates.",
            "link": "/products/elearning-platform",
            "svg": '''<svg viewBox="0 0 200 120" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="20" y="25" width="160" height="75" rx="3" stroke="currentColor" stroke-width="1.5"/>
              <rect x="20" y="25" width="45" height="75" rx="3" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.04"/>
              <line x1="65" y1="25" x2="65" y2="100" stroke="currentColor" stroke-width="1"/>
              <rect x="30" y="38" width="25" height="4" rx="1" fill="currentColor" fill-opacity="0.3"/>
              <rect x="30" y="48" width="25" height="4" rx="1" fill="currentColor" fill-opacity="0.2"/>
              <circle cx="112" cy="58" r="22" stroke="currentColor" stroke-width="1.5"/>
              <polygon points="104,48 104,68 128,58" fill="#4ADE80" fill-opacity="0.5" stroke="currentColor" stroke-width="1.2"/>
              <rect x="75" y="88" width="90" height="8" rx="2" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.05"/>
            </svg>'''
        },
        {
            "num": "06",
            "title": "Professional &amp; Financial",
            "desc": "Corporate portals, encrypted document exchange, automated billing, and compliance workflow trackers.",
            "link": "/services/erp-and-custom-software",
            "svg": '''<svg viewBox="0 0 200 120" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="25" y="20" width="150" height="90" rx="3" stroke="currentColor" stroke-width="1.5"/>
              <rect x="25" y="20" width="150" height="18" rx="3" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-width="1.5"/>
              <line x1="25" y1="38" x2="175" y2="38" stroke="currentColor" stroke-width="1"/>
              <line x1="25" y1="60" x2="175" y2="60" stroke="currentColor" stroke-width="0.8" stroke-dasharray="3 3" stroke-opacity="0.4"/>
              <line x1="25" y1="78" x2="175" y2="78" stroke="currentColor" stroke-width="0.8" stroke-dasharray="3 3" stroke-opacity="0.4"/>
              <rect x="35" y="45" width="50" height="8" rx="1" fill="currentColor" fill-opacity="0.15"/>
              <rect x="130" y="45" width="30" height="8" rx="1" fill="#4ADE80" fill-opacity="0.35" stroke="currentColor" stroke-width="1"/>
              <rect x="130" y="63" width="30" height="8" rx="1" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="1"/>
              <rect x="35" y="63" width="40" height="8" rx="1" fill="currentColor" fill-opacity="0.1"/>
              <rect x="35" y="81" width="55" height="8" rx="1" fill="currentColor" fill-opacity="0.1"/>
            </svg>'''
        },
        {
            "num": "07",
            "title": "AI &amp; Automation",
            "desc": "Intelligent workflow agents, document OCR, WhatsApp bots, and AI-powered ERP integrations.",
            "link": "/services/ai-automation",
            "svg": '''<svg viewBox="0 0 200 120" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="100" cy="60" r="28" stroke="currentColor" stroke-width="1.5"/>
              <circle cx="100" cy="60" r="12" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.08"/>
              <circle cx="100" cy="32" r="6" stroke="currentColor" stroke-width="1.2" fill="#4ADE80" fill-opacity="0.4"/>
              <circle cx="124" cy="46" r="6" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.1"/>
              <circle cx="124" cy="74" r="6" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.1"/>
              <circle cx="100" cy="88" r="6" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.1"/>
              <circle cx="76" cy="74" r="6" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.1"/>
              <circle cx="76" cy="46" r="6" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.1"/>
              <line x1="100" y1="38" x2="100" y2="48" stroke="currentColor" stroke-width="1.2"/>
              <line x1="118" y1="49" x2="110" y2="54" stroke="currentColor" stroke-width="1.2"/>
              <line x1="82" y1="49" x2="90" y2="54" stroke="currentColor" stroke-width="1.2"/>
            </svg>'''
        },
        {
            "num": "08",
            "title": "Mobile Apps &amp; SaaS",
            "desc": "iOS and Android apps, SaaS platform dashboards, and scalable subscription product development.",
            "link": "/services/mobile-app-development",
            "svg": '''<svg viewBox="0 0 200 120" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="55" y="10" width="55" height="100" rx="8" stroke="currentColor" stroke-width="1.5"/>
              <rect x="62" y="22" width="41" height="62" rx="2" stroke="currentColor" stroke-width="1.2" fill="currentColor" fill-opacity="0.04"/>
              <rect x="72" y="12" width="21" height="4" rx="2" fill="currentColor" fill-opacity="0.3"/>
              <circle cx="82" cy="102" r="5" stroke="currentColor" stroke-width="1.2"/>
              <rect x="68" y="30" width="30" height="12" rx="2" fill="#4ADE80" fill-opacity="0.3" stroke="currentColor" stroke-width="1"/>
              <rect x="68" y="48" width="20" height="6" rx="1" fill="currentColor" fill-opacity="0.15"/>
              <rect x="68" y="58" width="28" height="6" rx="1" fill="currentColor" fill-opacity="0.1"/>
            </svg>'''
        },
        {
            "num": "09",
            "title": "Digital Marketing &amp; SEO",
            "desc": "Performance campaigns, UAE search positioning, social media systems, and conversion-rate optimization.",
            "link": "/services/digital-marketing",
            "svg": '''<svg viewBox="0 0 200 120" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect x="20" y="80" width="22" height="30" rx="1" stroke="currentColor" stroke-width="1.5" fill="#4ADE80" fill-opacity="0.3"/>
              <rect x="50" y="60" width="22" height="50" rx="1" stroke="currentColor" stroke-width="1.5" fill="currentColor" fill-opacity="0.08"/>
              <rect x="80" y="45" width="22" height="65" rx="1" stroke="currentColor" stroke-width="1.5" fill="currentColor" fill-opacity="0.08"/>
              <rect x="110" y="30" width="22" height="80" rx="1" stroke="currentColor" stroke-width="1.5" fill="currentColor" fill-opacity="0.08"/>
              <rect x="140" y="15" width="22" height="95" rx="1" stroke="currentColor" stroke-width="1.5" fill="currentColor" fill-opacity="0.08"/>
              <polyline points="31,80 61,60 91,45 121,30 151,15" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
              <circle cx="151" cy="15" r="4" fill="#4ADE80"/>
              <line x1="20" y1="110" x2="175" y2="110" stroke="currentColor" stroke-width="1.2" stroke-opacity="0.4"/>
            </svg>'''
        },
    ]

    # Build bordered grid HTML (endcap.design style: shared borders, no radius)
    cards_html = ""
    for ind in industries_list:
        link_href = ind.get("link", "/contact")
        cards_html += f'''        <a href="{link_href}" class="ind-cell rv">
          <div class="ind-cell-visual">
            {ind["svg"]}
          </div>
          <div class="ind-cell-body">
            <span class="ind-num">{ind["num"]}</span>
            <h3 class="ind-title">{ind["title"]}</h3>
            <p class="ind-desc">{ind["desc"]}</p>
          </div>
          <span class="ind-arrow" aria-hidden="true">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 13L13 3M13 3H6M13 3v7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
        </a>\n'''

    content = f'''{render_head_tags(title, desc, canonical, schema)}
{render_header("industries")}
  <main id="main-content">
    <section class="page-hero">
      <div class="wrap">
        {render_breadcrumbs(crumbs)}
        <div style="max-width:720px;">
          <div class="eyebrow">Sector Capabilities &bull; Dubai &amp; UAE</div>
          <h1>Industries We Build For</h1>
          <p class="lede">
            Specialized software, AI automation, and digital systems across nine UAE commercial verticals.
          </p>
        </div>
      </div>
    </section>

    <section class="sec" style="padding-top:30px;padding-bottom:70px;">
      <div class="wrap">
        <div class="ind-grid">
{cards_html}        </div>
      </div>
    </section>

    {render_cta_band("Need Specialized Engineering for Your Industry?", "Our Dubai engineering team will analyze your specific sector workflows and build a custom solution.")}
  </main>
{render_footer()}
</body>
</html>'''
    out_dir = os.path.join(ROOT_DIR, "industries")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated Industries Page: /industries")


# -----------------------------------------------------------------------------
# 5. Generate Portfolio Page (/portfolio/index.html)
# -----------------------------------------------------------------------------
def build_portfolio_page():
    url = "/portfolio"
    canonical = f"{SITE_BASE}{url}"
    title = "Portfolio & Client Case Studies Dubai | TOCO Technologies"
    desc = "Explore verified case studies from TOCO Technologies in Dubai: iKart Express ERP, MŌJ Luxury E-Commerce, GlobalEdge, and Indoroot Supply Chain."
    crumbs = [("Home", "/"), ("Portfolio", "")]

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "@id": f"{canonical}#portfolio",
                "name": title,
                "description": desc,
                "url": canonical
            },
            make_breadcrumb_schema(crumbs)
        ]
    }

    case_studies = [
        {
            "img": "/assets/images/portfolio/ikart-erp.webp",
            "title": "iKart Express — Custom Logistics & Dispatch ERP",
            "tag": "Logistics & ERP",
            "desc": "Engineered a bespoke dispatch console and fleet management ERP handling over 15,000 monthly deliveries across Dubai, Abu Dhabi, and Sharjah.",
            "results": ["65% reduction in dispatch latency", "Real-time driver GPS telemetry", "Zero missed delivery SLAs"]
        },
        {
            "img": "/assets/images/portfolio/moj-ecommerce.webp",
            "title": "MŌJ Perfume — Luxury E-Commerce Storefront",
            "tag": "Luxury Retail",
            "desc": "Crafted an ultra-fast, high-converting digital perfume boutique integrated with UAE payment gateways, Tabby installments, and live inventory sync.",
            "results": ["+42% increase in mobile conversion", "0.7s average page load speed", "Automated UAE VAT invoicing"]
        },
        {
            "img": "/assets/images/portfolio/globaledge-platform.webp",
            "title": "GlobalEdge — Scalable International Web Platform",
            "tag": "Enterprise Web",
            "desc": "Architected an international corporate web platform built for high concurrency, multi-language localization, and sub-second global response.",
            "results": ["99.9% uptime SLA recorded", "Core Web Vitals score of 98", "Complete SEO re-architecture"]
        },
        {
            "img": "/assets/images/portfolio/indoroot-supply.webp",
            "title": "Indoroot — B2B Wholesale Supply Chain Portal",
            "tag": "B2B Commerce",
            "desc": "Developed a wholesale ordering portal connecting regional agricultural suppliers directly to UAE supermarkets and hospitality groups.",
            "results": ["Over AED 8M quarterly volume processed", "Automated recurring procurement", "Tiered wholesale pricing engine"]
        },
        {
            "img": "/assets/images/portfolio/spaceown-dashboard.webp",
            "title": "Spaceown — Commercial Spatial Analytics Dashboard",
            "tag": "SaaS Platform",
            "desc": "High-performance commercial property dashboard tracking footfall analytics, lease valuations, and tenant contract renewals.",
            "results": ["Interactive spatial floor maps", "Automated lease expiry alerts", "Exportable investor reports"]
        },
        {
            "img": "/assets/images/portfolio/kai-digital.webp",
            "title": "KAI Digital — Corporate Brand System & Web Presence",
            "tag": "Branding & Web",
            "desc": "Comprehensive corporate brand identity guidelines, interactive Figma design tokens, and a lightning-fast responsive web architecture.",
            "results": ["Bespoke vector design system", "100% WCAG AA accessibility", "High-converting B2B inquiry funnels"]
        }
    ]

    cards_html = ""
    for cs in case_studies:
        results_html = "".join([f'<li style="font-size:13px;color:var(--ink-2);margin-bottom:4px;">✓ {r}</li>' for r in cs["results"]])
        cards_html += f'''        <div class="card rv" style="padding:0;overflow:hidden;display:flex;flex-direction:column;">
          <img src="{cs["img"]}" alt="{cs["title"]}" width="600" height="340" style="width:100%;height:220px;object-fit:cover;border-bottom:1px solid var(--line);">
          <div style="padding:24px;flex:1;display:flex;flex-direction:column;justify-content:space-between;">
            <div>
              <span class="tag-badge live" style="margin-bottom:10px;">{cs["tag"]}</span>
              <h3 style="font-size:19px;margin-bottom:8px;font-family:var(--font-display);color:var(--ink);">{cs["title"]}</h3>
              <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:16px;">{cs["desc"]}</p>
            </div>
            <ul style="list-style:none;padding:0;border-top:1px solid var(--line);padding-top:12px;">
              {results_html}
            </ul>
          </div>
        </div>\n'''

    content = f'''{render_head_tags(title, desc, canonical, schema)}
{render_header("portfolio")}
  <main id="main-content">
    <section class="page-hero">
      <div class="wrap">
        {render_breadcrumbs(crumbs)}
        <div style="max-width:820px;">
          <div class="eyebrow">Demonstrated Results • Dubai &amp; Across UAE</div>
          <h1>Verified Client Case Studies &amp; Engineering Impact</h1>
          <p class="lede">
            Inspect genuine case studies demonstrating how TOCO Technologies helped Dubai companies scale revenue, automate operational dispatch, and achieve Core Web Vitals dominance.
          </p>
        </div>
      </div>
    </section>

    <section class="sec">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Client Case Studies</div>
          <h2>Production Platforms Built for Leading Regional Brands</h2>
          <p>Real projects, genuine client feedback, and verifiable commercial results across Dubai and the UAE.</p>
        </div>
        <div class="grid-3">
{cards_html}        </div>
      </div>
    </section>

    {render_cta_band("Ready to Achieve Similar Results for Your Business?", "Connect with our Dubai engineering leadership to discuss your upcoming project requirements.")}
  </main>
{render_footer()}
</body>
</html>'''

    out_dir = os.path.join(ROOT_DIR, "portfolio")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated Portfolio Page: /portfolio")


# -----------------------------------------------------------------------------
# 6. Generate Contact Page (/contact/index.html)
# -----------------------------------------------------------------------------
def build_contact_page():
    url = "/contact"
    canonical = f"{SITE_BASE}{url}"
    title = "Contact TOCO Technologies | Dubai Port Saeed Office & Support"
    desc = "Contact TOCO Technologies Dubai. Phone +971 4 577 0725, email info@tocoplus.com, Port Saeed, Deira, Dubai, UAE. Book a project strategy call."
    crumbs = [("Home", "/"), ("Contact", "")]

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["ContactPage", "LocalBusiness"],
                "@id": f"{canonical}#contact",
                "name": "TOCO Technologies Dubai Office",
                "description": desc,
                "url": canonical,
                "telephone": "+971-4-577-0725",
                "email": "info@tocoplus.com",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "Port Saeed, Deira",
                    "addressLocality": "Dubai",
                    "addressRegion": "Dubai",
                    "addressCountry": "AE"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 25.249344,
                    "longitude": 55.331351
                },
                "openingHoursSpecification": [
                    {
                        "@type": "OpeningHoursSpecification",
                        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                        "opens": "09:00",
                        "closes": "18:00"
                    }
                ]
            },
            make_breadcrumb_schema(crumbs)
        ]
    }

    content = f'''{render_head_tags(title, desc, canonical, schema)}
{render_header("contact")}
  <main id="main-content">
    <section class="page-hero">
      <div class="wrap">
        {render_breadcrumbs(crumbs)}
        <div style="max-width:820px;">
          <div class="eyebrow">Connect With Our Team • Port Saeed, Dubai</div>
          <h1>Speak Directly With Our Dubai Engineering Leadership</h1>
          <p class="lede">
            Have a project in mind, need custom AI automation, or exploring a proprietary software deployment? Contact our technical leadership in Dubai for a prompt, transparent discussion.
          </p>
        </div>
      </div>
    </section>

    <section class="sec">
      <div class="wrap">
        <div style="display:grid;grid-template-columns:1fr 1.25fr;gap:40px;align-items:flex-start;">
          <!-- Contact Details Col -->
          <div>
            <div class="eyebrow">Dubai Headquarters</div>
            <h2 style="font-size:28px;margin-bottom:16px;">We're Here to Help Your Business Grow</h2>
            <p style="color:var(--ink-2);font-size:15px;line-height:1.6;margin-bottom:28px;">
              Visit us in Port Saeed, Deira, or connect via phone or WhatsApp. We reply to all commercial enquiries within 24 hours.
            </p>

            <div class="foot-contact-info" style="gap:18px;">
              <div class="f-info-item" style="font-size:15px;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                <span>Port Saeed, Deira, Dubai, United Arab Emirates</span>
              </div>
              <div class="f-info-item" style="font-size:15px;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                <a href="tel:+97145770725" style="color:var(--ink);font-weight:600;">+971 4 577 0725</a>
              </div>
              <div class="f-info-item" style="font-size:15px;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                <a href="mailto:info@tocoplus.com" style="color:var(--ink);font-weight:600;">info@tocoplus.com</a>
              </div>
              <div class="f-info-item" style="font-size:15px;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                <span>Monday – Saturday: 9:00 AM – 6:00 PM GST</span>
              </div>
            </div>

            <div style="margin-top:32px;">
              <a href="https://wa.me/97145770725" target="_blank" rel="noopener" class="btn btn-primary" style="width:100%;justify-content:center;">
                <span>Chat Instantly on WhatsApp</span>
                <svg class="arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </a>
            </div>

            <!-- Map View -->
            <div class="card" style="margin-top:28px;padding:0;overflow:hidden;border-radius:var(--radius);">
              <iframe title="TOCO Technologies Dubai Office Location" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14434.697412759887!2d55.32259585!3d25.24934445!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e5f5d21a2c3a51f%3A0x6b6c2d1c67d3!2sPort%20Saeed%20-%20Dubai!5e0!3m2!1sen!2sae!4v1700000000000" width="100%" height="240" style="border:0;display:block;" allowfullscreen="" loading="lazy"></iframe>
            </div>
          </div>

          <!-- Contact Form Col -->
          <div>
            <div class="form-card">
              <h3 style="font-size:24px;margin-bottom:8px;font-family:var(--font-display);">Send Project Specification</h3>
              <p style="color:var(--ink-2);font-size:14px;line-height:1.5;margin-bottom:24px;">
                Complete this form and our technical team will review your requirements and provide an initial feasibility assessment within 24 hours.
              </p>

              <form id="contact-form" novalidate>
                <!-- Honeypot Bot Trap -->
                <input type="text" name="company_website_url" class="hp-field" tabindex="-1" autocomplete="off">

                <div class="form-grid">
                  <div class="form-group">
                    <label class="form-label" for="cf-name">Full Name *</label>
                    <input type="text" id="cf-name" class="form-control" placeholder="e.g. Tariq Al-Mansoor" required>
                  </div>
                  <div class="form-group">
                    <label class="form-label" for="cf-email">Corporate Email *</label>
                    <input type="email" id="cf-email" class="form-control" placeholder="tariq@company.ae" required>
                  </div>
                  <div class="form-group">
                    <label class="form-label" for="cf-phone">UAE Mobile / Phone *</label>
                    <input type="tel" id="cf-phone" class="form-control" placeholder="+971 50 123 4567" required>
                  </div>
                  <div class="form-group">
                    <label class="form-label" for="cf-service">Primary Service Interest *</label>
                    <select id="cf-service" class="form-control" required style="appearance:auto;">
                      <option value="" disabled selected>Select an offering...</option>
                      <option value="AI Automation & Agents">AI Automation &amp; Agents</option>
                      <option value="AI Business Conversions">AI Business Conversions</option>
                      <option value="Mobile App Development">Mobile Application Software</option>
                      <option value="Website & Custom Software">Website &amp; Custom Software</option>
                      <option value="Custom ERP & Business Systems">Custom ERP &amp; Business Systems</option>
                      <option value="Digital Marketing & PPC">Digital Marketing &amp; PPC</option>
                      <option value="Technical SEO">Technical SEO &amp; Search</option>
                      <option value="E-Commerce Development">E-Commerce Development</option>
                      <option value="Software Products">Proprietary Software Products</option>
                      <option value="Other Technology Requirement">Other Consultation</option>
                    </select>
                  </div>
                  <div class="form-group full">
                    <label class="form-label" for="cf-message">Project Brief &amp; Scope *</label>
                    <textarea id="cf-message" class="form-control" placeholder="Describe your operational goals, estimated timeline, and current software stack..." required></textarea>
                  </div>
                </div>

                <div style="margin-top:20px;">
                  <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;">
                    <span>Send Project Enquiry</span>
                    <svg class="arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
                  </button>
                </div>

                <div class="form-status"></div>
                <p style="font-size:12px;color:var(--ink-3);margin-top:12px;text-align:center;">
                  🔒 We protect your data under UAE PDP Law. Non-disclosure agreements (NDAs) signed upon request.
                </p>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
{render_footer()}
</body>
</html>'''

    out_dir = os.path.join(ROOT_DIR, "contact")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated Contact Page: /contact")


# -----------------------------------------------------------------------------
# 7. Generate Privacy Policy & Terms of Service & 404
# -----------------------------------------------------------------------------
def build_legal_and_404():
    # Privacy Policy
    p_url = "/privacy-policy"
    p_canonical = f"{SITE_BASE}{p_url}"
    p_title = "Privacy Policy | TOCO Technologies UAE"
    p_desc = "Privacy policy of TOCO Technologies UAE, compliant with UAE Federal Decree-Law No. 45 of 2021 regarding Personal Data Protection (UAE PDP Law)."
    p_crumbs = [("Home", "/"), ("Privacy Policy", "")]
    p_schema = {"@context": "https://schema.org", "@type": "WebPage", "name": p_title, "url": p_canonical}

    p_content = f'''{render_head_tags(p_title, p_desc, p_canonical, p_schema)}
{render_header()}
  <main id="main-content">
    <section class="page-hero">
      <div class="wrap">
        {render_breadcrumbs(p_crumbs)}
        <div style="max-width:800px;">
          <div class="eyebrow">Regulatory Compliance • UAE PDP Law</div>
          <h1>Privacy Policy</h1>
          <p class="lede">Last updated: January 2026. This policy outlines how TOCO Technologies collects, uses, and safeguards personal and corporate data in compliance with UAE Federal Decree-Law No. 45 of 2021.</p>
        </div>
      </div>
    </section>

    <section class="sec">
      <div class="wrap" style="max-width:840px;">
        <div class="card" style="padding:clamp(24px, 4vw, 40px);line-height:1.75;color:var(--ink-2);font-size:15px;">
          <h2 style="color:var(--ink);margin-bottom:12px;font-size:22px;">1. Information We Collect</h2>
          <p style="margin-bottom:18px;">When you submit an enquiry through our website, communicate via WhatsApp, or engage our engineering services, we collect contact information including your full name, corporate email, UAE phone number, company name, and project scope.</p>

          <h2 style="color:var(--ink);margin-bottom:12px;font-size:22px;">2. Legal Basis for Processing</h2>
          <p style="margin-bottom:18px;">We process your data strictly under the provisions of UAE Federal Decree-Law No. 45 of 2021 on Personal Data Protection to provide engineering proposals, fulfill contractual deliverables, and comply with statutory financial audits.</p>

          <h2 style="color:var(--ink);margin-bottom:12px;font-size:22px;">3. Data Sovereignty &amp; Security</h2>
          <p style="margin-bottom:18px;">We implement bank-grade encryption (AES-256 at rest, TLS 1.3 in transit). Client repositories and production databases are deployed in ISO 27001-certified data centers or local UAE AWS cloud regions to preserve national data sovereignty.</p>

          <h2 style="color:var(--ink);margin-bottom:12px;font-size:22px;">4. Third-Party Sharing</h2>
          <p style="margin-bottom:18px;">TOCO Technologies never sells, rents, or monetizes client data to third-party advertisers. Data is shared exclusively with designated infrastructure providers (e.g. AWS UAE, official WhatsApp Cloud API) required to operate your services.</p>

          <h2 style="color:var(--ink);margin-bottom:12px;font-size:22px;">5. Your Rights Under UAE Law</h2>
          <p style="margin-bottom:18px;">You retain the right to access, rectify, or request erasure of your personal data at any time by contacting our Data Protection Officer at <a href="mailto:info@tocoplus.com" style="color:var(--cyan);text-decoration:underline;">info@tocoplus.com</a>.</p>

          <h2 style="color:var(--ink);margin-bottom:12px;font-size:22px;">6. Office Details</h2>
          <p>TOCO Technologies, Port Saeed, Deira, Dubai, United Arab Emirates. Telephone: +971 4 577 0725.</p>
        </div>
      </div>
    </section>
  </main>
{render_footer()}
</body>
</html>'''

    p_dir = os.path.join(ROOT_DIR, "privacy-policy")
    os.makedirs(p_dir, exist_ok=True)
    with open(os.path.join(p_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(p_content)
    print("Generated Privacy Policy: /privacy-policy")

    # Terms of Service
    t_url = "/terms-of-service"
    t_canonical = f"{SITE_BASE}{t_url}"
    t_title = "Terms of Service & SLA Warranty | TOCO Technologies UAE"
    t_desc = "Terms of Service, intellectual property transfer terms, and 30-day post-launch warranty agreement for TOCO Technologies Dubai, UAE."
    t_crumbs = [("Home", "/"), ("Terms of Service", "")]
    t_schema = {"@context": "https://schema.org", "@type": "WebPage", "name": t_title, "url": t_canonical}

    t_content = f'''{render_head_tags(t_title, t_desc, t_canonical, t_schema)}
{render_header()}
  <main id="main-content">
    <section class="page-hero">
      <div class="wrap">
        {render_breadcrumbs(t_crumbs)}
        <div style="max-width:800px;">
          <div class="eyebrow">Master Engineering Agreement</div>
          <h1>Terms of Service &amp; SLA</h1>
          <p class="lede">Last updated: January 2026. Standard commercial delivery terms, intellectual property ownership guarantees, and 30-day post-launch warranty provisions.</p>
        </div>
      </div>
    </section>

    <section class="sec">
      <div class="wrap" style="max-width:840px;">
        <div class="card" style="padding:clamp(24px, 4vw, 40px);line-height:1.75;color:var(--ink-2);font-size:15px;">
          <h2 style="color:var(--ink);margin-bottom:12px;font-size:22px;">1. Engineering Scope &amp; Milestones</h2>
          <p style="margin-bottom:18px;">All software development, AI automation pipelines, and digital services are executed pursuant to a mutually executed Statement of Work (SOW) detailing technical specifications, delivery milestones, and sign-off criteria.</p>

          <h2 style="color:var(--ink);margin-bottom:12px;font-size:22px;">2. Intellectual Property (IP) Ownership</h2>
          <p style="margin-bottom:18px;">Upon final milestone settlement, 100% of custom developed source code, design systems, Figma files, and proprietary database architectures become the sole and exclusive intellectual property of the Client.</p>

          <h2 style="color:var(--ink);margin-bottom:12px;font-size:22px;">3. 30-Day Post-Launch SLA Warranty</h2>
          <p style="margin-bottom:18px;">Every custom software, mobile app, and web project delivered by TOCO Technologies includes 30 consecutive calendar days of complimentary engineering warranty covering bug remediation, security patching, and server tuning.</p>

          <h2 style="color:var(--ink);margin-bottom:12px;font-size:22px;">4. Confidentiality &amp; Non-Disclosure</h2>
          <p style="margin-bottom:18px;">Both parties agree to treat all business information, architectural plans, customer records, and trade secrets as strictly confidential under UAE law.</p>

          <h2 style="color:var(--ink);margin-bottom:12px;font-size:22px;">5. Governing Law &amp; Jurisdiction</h2>
          <p>This Agreement shall be governed by and construed in accordance with the laws of the Emirate of Dubai and the applicable Federal Laws of the United Arab Emirates. Any dispute shall be subject to the exclusive jurisdiction of the Dubai Courts.</p>
        </div>
      </div>
    </section>
  </main>
{render_footer()}
</body>
</html>'''

    t_dir = os.path.join(ROOT_DIR, "terms-of-service")
    os.makedirs(t_dir, exist_ok=True)
    with open(os.path.join(t_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(t_content)
    print("Generated Terms of Service: /terms-of-service")

    # 404 Error Page
    err_url = "/404.html"
    err_canonical = f"{SITE_BASE}/404"
    err_title = "Page Not Found (404) | TOCO Technologies Dubai"
    err_desc = "The requested page could not be located. Browse TOCO Technologies' AI automation, software engineering, and digital services in Dubai."
    err_schema = {"@context": "https://schema.org", "@type": "WebPage", "name": err_title, "url": err_canonical}

    err_content = f'''{render_head_tags(err_title, err_desc, err_canonical, err_schema)}
{render_header()}
  <main id="main-content">
    <section class="page-hero" style="text-align:center;padding:clamp(80px, 12vw, 140px) 0;">
      <div class="wrap" style="max-width:680px;margin:0 auto;">
        <div class="eyebrow" style="color:var(--cyan);">Error 404 • Resource Not Found</div>
        <h1 style="font-size:clamp(44px, 7vw, 92px);margin-bottom:14px;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">404</h1>
        <p class="lede" style="margin:0 auto 28px;">
          The page or system resource you requested could not be located on our Dubai server. It may have been relocated or updated.
        </p>
        <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
          <a href="/" class="btn btn-primary">
            <span>Return to Homepage</span>
            <svg class="arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="/services" class="btn btn-ghost">
            <span>Explore Services</span>
          </a>
          <a href="/contact" class="btn btn-ghost">
            <span>Contact Dubai HQ</span>
          </a>
        </div>
      </div>
    </section>
  </main>
{render_footer()}
</body>
</html>'''

    with open(os.path.join(ROOT_DIR, "404.html"), "w", encoding="utf-8") as f:
        f.write(err_content)
    print("Generated 404 Page: /404.html")


print("Auxiliary pages builder configured.")
# -----------------------------------------------------------------------------
# 8. Generate Homepage (/index.html)
# -----------------------------------------------------------------------------
def build_homepage():
    url = "/"
    canonical = f"{SITE_BASE}/"
    title = "TOCO Technologies | AI Automation & Software in Dubai, UAE"
    desc = "TOCO Technologies engineers AI business automation, custom website & mobile application software, ERP platforms, and digital solutions in Dubai, UAE."

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["Organization", "LocalBusiness"],
                "@id": f"{SITE_BASE}/#organization",
                "name": "TOCO Technologies",
                "url": f"{SITE_BASE}/",
                "logo": f"{SITE_BASE}/assets/images/logo-square.webp",
                "image": f"{SITE_BASE}/assets/images/og-cover.jpg",
                "description": desc,
                "telephone": "+971-4-577-0725",
                "email": "info@tocoplus.com",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "Port Saeed, Deira",
                    "addressLocality": "Dubai",
                    "addressRegion": "Dubai",
                    "addressCountry": "AE"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 25.249344,
                    "longitude": 55.331351
                },
                "areaServed": [
                    {"@type": "City", "name": "Dubai"},
                    {"@type": "City", "name": "Abu Dhabi"},
                    {"@type": "City", "name": "Sharjah"},
                    {"@type": "Country", "name": "United Arab Emirates"}
                ]
            },
            {
                "@type": "WebSite",
                "@id": f"{SITE_BASE}/#website",
                "url": f"{SITE_BASE}/",
                "name": "TOCO Technologies",
                "publisher": {"@id": f"{SITE_BASE}/#organization"}
            },
            make_faq_schema([
                {"q": "What services does TOCO Technologies offer in Dubai?", "a": "We provide end-to-end technology engineering including AI workflow automation, AI business conversions, mobile application software (iOS & Android), custom web development, bespoke ERP platforms, performance digital marketing, and technical SEO."},
                {"q": "Where is TOCO Technologies located in the UAE?", "a": "Our corporate headquarters is located in Port Saeed, Deira, Dubai, UAE. We serve commercial clients across Dubai, Abu Dhabi, Sharjah, and the wider Arabian Gulf region."},
                {"q": "What proprietary software products has TOCO Technologies built?", "a": "We have engineered software products including an e-learning & LMS platform, interior design quote & sales automation, an AI-powered ERP, and UAE WPS payroll automation, alongside upcoming Analytics and Real Estate CRM suites."},
                {"q": "Do you provide a warranty on custom software and web applications?", "a": "Yes. Every custom build includes our 30-day post-launch engineering SLA warranty covering bug remediation, security patches, and cloud optimization at zero extra charge."},
                {"q": "How does TOCO Technologies ensure UAE data privacy compliance?", "a": "We build in strict compliance with UAE Federal Decree-Law No. 45 of 2021 regarding Personal Data Protection, offering private AWS UAE cloud hosting and on-premise deployments."}
            ])
        ]
    }

    # Testimonials Data
    testimonials = [
        {"quote": "Our logistics and delivery dispatch workflow has never been smoother. TOCO delivered a stable, custom ERP solution that handles 15,000+ monthly shipments with zero downtime.", "name": "Faisal Al-Mansoori", "role": "Operations Director, iKart Express", "logo": "/assets/images/clients/ikart.webp"},
        {"quote": "The custom e-commerce engine developed by TOCO Technologies elevated our luxury brand's digital storefront, driving a direct 42% lift in mobile conversions.", "name": "Mariam Al-Sayegh", "role": "Creative Lead, MŌJ Perfume", "logo": "/assets/images/clients/moj.webp"},
        {"quote": "TOCO Technologies built a highly scalable international platform that transformed our backend efficiency. Their architecture is clean, fast, and engineered to last.", "name": "Alexander Mercer", "role": "CTO, GlobalEdge International", "logo": "/assets/images/clients/global.webp"}
    ]

    testi_cards_html = ""
    for t in testimonials:
        testi_cards_html += f'''          <div class="card testi-card">
            <p class="testi-quote">"{t["quote"]}"</p>
            <div class="testi-author">
              <div>
                <div class="testi-name">{t["name"]}</div>
                <div class="testi-role">{t["role"]}</div>
              </div>
              <img src="{t["logo"]}" alt="{t["name"]} Company" class="testi-logo" loading="lazy">
            </div>
          </div>\n'''

    # FAQs Data
    faqs = [
        {"q": "What services does TOCO Technologies offer in Dubai?", "a": "We provide end-to-end technology engineering including AI workflow automation, AI business conversions, mobile application software (iOS & Android), custom web development, bespoke ERP platforms, performance digital marketing, and technical SEO."},
        {"q": "Where is TOCO Technologies located in the UAE?", "a": "Our corporate headquarters is located in Port Saeed, Deira, Dubai, UAE. We serve commercial clients across Dubai, Abu Dhabi, Sharjah, and the wider Arabian Gulf region."},
        {"q": "What proprietary software products has TOCO Technologies built?", "a": "We have engineered software products including an e-learning & LMS platform, interior design quote & sales automation, an AI-powered ERP, and UAE WPS payroll automation, alongside upcoming Analytics and Real Estate CRM suites."},
        {"q": "Do you provide a warranty on custom software and web applications?", "a": "Yes. Every custom build includes our 30-day post-launch engineering SLA warranty covering bug remediation, security patches, and cloud optimization at zero extra charge."},
        {"q": "How does TOCO Technologies ensure UAE data privacy compliance?", "a": "We build in strict compliance with UAE Federal Decree-Law No. 45 of 2021 regarding Personal Data Protection, offering private AWS UAE cloud hosting and on-premise deployments."},
        {"q": "Can TOCO Technologies integrate AI into our existing business software?", "a": "Yes. We engineer resilient API bridges and webhook middleware connecting modern AI models directly to your legacy ERP, CRM, or accounting software without disrupting ongoing operations."}
    ]

    faq_items_html = ""
    for i, f in enumerate(faqs):
        is_first = (i == 0)
        faq_items_html += f'''        <div class="faq-item{' open' if is_first else ''}">
          <button class="faq-q" type="button" aria-expanded="{'true' if is_first else 'false'}">
            <span>{f["q"]}</span>
            <i></i>
          </button>
          <div class="faq-a" style="{'max-height:220px;' if is_first else ''}">
            <div class="faq-a-inner">
              <p>{f["a"]}</p>
            </div>
          </div>
        </div>\n'''

    html_content = f'''{render_head_tags(title, desc, canonical, schema)}
{render_header("home")}

  <main id="main-content">
    <!-- SECTION 1: HERO (Modern Clean Centered Stage) -->
    <section class="hero" id="home">
      <!-- Ambient Concentric Rings (Deflexai inspired, elegant, no icons) -->
      <div class="hero-bg-rings" aria-hidden="true">
        <svg viewBox="0 0 1200 800" fill="none" xmlns="http://www.w3.org/2000/svg" class="hero-rings-svg">
          <circle cx="600" cy="380" r="160" stroke="rgba(59, 130, 246, 0.22)" stroke-width="1" stroke-dasharray="4 6"/>
          <circle cx="600" cy="380" r="300" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1"/>
          <circle cx="600" cy="380" r="460" stroke="rgba(59, 130, 246, 0.14)" stroke-width="1" stroke-dasharray="6 8"/>
          <circle cx="600" cy="380" r="620" stroke="rgba(255, 255, 255, 0.04)" stroke-width="1"/>
        </svg>
        <div class="hero-ambient-glow"></div>
      </div>

      <!-- Main Content -->
      <div class="wrap hero-content-wrap">
        <div class="hero-badge-pill">
          <span class="badge-dot"></span>
          <span>Dubai &amp; UAE Enterprise Technology Partner</span>
        </div>

        <h1>Engineering <span class="grad-text">AI Systems</span> &amp; High-Impact Software in Dubai</h1>

        <p class="lede">
          We engineer intelligent AI automation, custom ERP systems, and high-performance digital platforms that help UAE enterprises scale, automate workflows, and drive measurable revenue.
        </p>

        <div class="hero-cta">
          <a href="/contact" class="btn btn-primary">
            <span>Book Strategic Consultation</span>
            <svg class="arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="/services" class="btn btn-ghost">
            <span>Explore Solutions</span>
          </a>
        </div>

        <!-- Trust Badges Bar -->
        <div class="hero-trust-bar">
          <div class="trust-item">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--blue-bright)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Port Saeed, Dubai HQ</span>
          </div>
          <div class="trust-sep"></div>
          <div class="trust-item">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--blue-bright)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>30-Day Launch Warranty</span>
          </div>
          <div class="trust-sep"></div>
          <div class="trust-item">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--blue-bright)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>100% Code Ownership</span>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: INFINITE LOGO MARQUEE (Crisp Clean White Background, No Boxes) -->
    <section class="sec" style="padding:28px 0;background:#FFFFFF;border-top:1px solid rgba(10,10,10,0.08);border-bottom:1px solid rgba(10,10,10,0.08);">
      <div class="wrap" style="text-align:center;margin-bottom:16px;">
        <span style="font-size:11.5px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#64748B;">
          Trusted by Innovative UAE Enterprises &amp; Regional Brands
        </span>
      </div>
      <div class="marquee">
        <div class="marquee-track">
          <div class="marquee-item"><img src="/assets/images/clients/ikart.webp" alt="iKart Express" width="110" height="32"></div>
          <div class="marquee-item"><img src="/assets/images/clients/moj.webp" alt="MŌJ Perfume" width="100" height="30"></div>
          <div class="marquee-item"><img src="/assets/images/clients/global.webp" alt="GlobalEdge" width="110" height="32"></div>
          <div class="marquee-item"><img src="/assets/images/clients/indoroot.webp" alt="Indoroot" width="105" height="30"></div>
          <div class="marquee-item"><img src="/assets/images/clients/space.webp" alt="Spaceown" width="100" height="30"></div>
          <div class="marquee-item"><img src="/assets/images/clients/tekora.webp" alt="Tekora" width="105" height="30"></div>
          <div class="marquee-item"><img src="/assets/images/clients/kai.webp" alt="KAI Digital" width="95" height="28"></div>
          <div class="marquee-item"><img src="/assets/images/clients/celestial.webp" alt="Celestial" width="105" height="30"></div>
          <div class="marquee-item"><img src="/assets/images/clients/confident.webp" alt="Confident" width="110" height="32"></div>
          <div class="marquee-item"><img src="/assets/images/clients/shoppy.webp" alt="Shoppy" width="100" height="30"></div>

          <!-- Duplicate Set for Seamless Loop -->
          <div class="marquee-item"><img src="/assets/images/clients/ikart.webp" alt="iKart Express" width="110" height="32"></div>
          <div class="marquee-item"><img src="/assets/images/clients/moj.webp" alt="MŌJ Perfume" width="100" height="30"></div>
          <div class="marquee-item"><img src="/assets/images/clients/global.webp" alt="GlobalEdge" width="110" height="32"></div>
          <div class="marquee-item"><img src="/assets/images/clients/indoroot.webp" alt="Indoroot" width="105" height="30"></div>
          <div class="marquee-item"><img src="/assets/images/clients/space.webp" alt="Spaceown" width="100" height="30"></div>
          <div class="marquee-item"><img src="/assets/images/clients/tekora.webp" alt="Tekora" width="105" height="30"></div>
          <div class="marquee-item"><img src="/assets/images/clients/kai.webp" alt="KAI Digital" width="95" height="28"></div>
          <div class="marquee-item"><img src="/assets/images/clients/celestial.webp" alt="Celestial" width="105" height="30"></div>
          <div class="marquee-item"><img src="/assets/images/clients/confident.webp" alt="Confident" width="110" height="32"></div>
          <div class="marquee-item"><img src="/assets/images/clients/shoppy.webp" alt="Shoppy" width="100" height="30"></div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: WHAT WE BUILD (2-Column Editorial Row Architecture) -->
    <section class="sec" id="what-we-build">
      <div class="wrap">
        <div class="sec-head" style="margin-bottom:36px;">
          <div class="eyebrow">
            <span class="badge-dot"></span>
            Enterprise Capabilities
          </div>
          <h2>What We Build for UAE Businesses</h2>
          <p style="max-width:680px;">
            Production-grade technology platforms engineered for commercial scale, operational autonomy, and long-term maintainability.
          </p>
        </div>

        <!-- 2-Column Row Layout (No Heavy Boxes) -->
        <div class="cap-two-col rv">
          
          <!-- Column 1: AI & Autonomous Systems -->
          <div class="cap-col">
            <div class="cap-col-header">
              <span class="cap-col-num">01 / CAPABILITY DIVISION</span>
              <h3 class="cap-col-title">AI &amp; Autonomous Systems</h3>
              <p class="cap-col-desc">Multi-agent pipelines, automated conversions, and deterministic reasoning engines.</p>
            </div>

            <!-- Item 1.1 -->
            <a href="/services/ai-automation" class="cap-row-item">
              <div class="cap-row-head">
                <span class="cap-row-title">Autonomous Multi-Agent Pipelines</span>
                <span class="cap-row-arr">↗</span>
              </div>
              <p class="cap-row-desc">
                Deterministic LLM pipelines and multi-agent workflows that automate document extraction, complex decision trees, and multi-system data routing without manual entry.
              </p>
              <div class="cap-row-tags">
                <span class="cap-tag">Multi-Agent LangGraph</span>
                <span class="cap-tag">Doc Intelligence</span>
                <span class="cap-tag">FastAPI</span>
                <span class="cap-metric">&lt; 420ms Latency</span>
              </div>
            </a>

            <!-- Item 1.2 -->
            <a href="/services/ai-business-automation" class="cap-row-item">
              <div class="cap-row-head">
                <span class="cap-row-title">AI Business Conversions &amp; WhatsApp</span>
                <span class="cap-row-arr">↗</span>
              </div>
              <p class="cap-row-desc">
                Sub-minute lead capture across WhatsApp Cloud and website chat with autonomous qualification, real-time CRM syncing, and meeting scheduling.
              </p>
              <div class="cap-row-tags">
                <span class="cap-tag">WhatsApp Cloud API</span>
                <span class="cap-tag">Instant Lead Qual</span>
                <span class="cap-tag">Calendar Sync</span>
                <span class="cap-metric">+42% Lead Lift</span>
              </div>
            </a>

            <!-- Item 1.3 -->
            <a href="/services/ai-automation" class="cap-row-item">
              <div class="cap-row-head">
                <span class="cap-row-title">Enterprise AI &amp; Data Intelligence</span>
                <span class="cap-row-arr">↗</span>
              </div>
              <p class="cap-row-desc">
                Internal knowledge retrieval (RAG), private LLM fine-tuning, and deterministic data extraction engineered for strict UAE Data Residency compliance.
              </p>
              <div class="cap-row-tags">
                <span class="cap-tag">Private RAG</span>
                <span class="cap-tag">UAE Decree-Law 45</span>
                <span class="cap-tag">OCR Telemetry</span>
                <span class="cap-metric">100% On-Premise / UAE Cloud</span>
              </div>
            </a>
          </div>

          <!-- Column 2: Enterprise Software & Platforms -->
          <div class="cap-col">
            <div class="cap-col-header">
              <span class="cap-col-num">02 / CAPABILITY DIVISION</span>
              <h3 class="cap-col-title">Enterprise Software &amp; Platforms</h3>
              <p class="cap-col-desc">Custom ERPs, 60fps mobile applications, and sub-second digital systems.</p>
            </div>

            <!-- Item 2.1 -->
            <a href="/services/erp-and-custom-software" class="cap-row-item">
              <div class="cap-row-head">
                <span class="cap-row-title">Custom ERP &amp; Operating Systems</span>
                <span class="cap-row-arr">↗</span>
              </div>
              <p class="cap-row-desc">
                Bespoke enterprise suites, logistics dispatch consoles, warehouse inventory, and automated MOHRE WPS payroll compliance with zero recurring SaaS tax.
              </p>
              <div class="cap-row-tags">
                <span class="cap-tag">Logistics Dispatch</span>
                <span class="cap-tag">MOHRE WPS Invoicing</span>
                <span class="cap-tag">RBAC Security</span>
                <span class="cap-metric">100% Code Ownership</span>
              </div>
            </a>

            <!-- Item 2.2 -->
            <a href="/services/mobile-app-development" class="cap-row-item">
              <div class="cap-row-head">
                <span class="cap-row-title">Mobile Application Software</span>
                <span class="cap-row-arr">↗</span>
              </div>
              <p class="cap-row-desc">
                Native and Flutter iOS &amp; Android applications built for silky 60fps performance, Apple Pay checkouts, biometric login, and live GPS telemetry.
              </p>
              <div class="cap-row-tags">
                <span class="cap-tag">Flutter &amp; Swift</span>
                <span class="cap-tag">Apple Pay 1-Tap</span>
                <span class="cap-tag">GPS Telemetry</span>
                <span class="cap-metric">60 FPS Native</span>
              </div>
            </a>

            <!-- Item 2.3 -->
            <a href="/services/website-and-software-development" class="cap-row-item">
              <div class="cap-row-head">
                <span class="cap-row-title">Sub-Second Web &amp; E-Commerce</span>
                <span class="cap-row-arr">↗</span>
              </div>
              <p class="cap-row-desc">
                Sub-second corporate web platforms and high-converting storefronts on Shopify Plus or custom headless stacks with Tabby/Tamara 4-split installments.
              </p>
              <div class="cap-row-tags">
                <span class="cap-tag">Static Edge Architecture</span>
                <span class="cap-tag">Tabby / Tamara</span>
                <span class="cap-tag">Arabic RTL</span>
                <span class="cap-metric">99/100 Core Web Vitals</span>
              </div>
            </a>
          </div>

        </div>
      </div>
    </section>

    <!-- SECTION 4: AI WORKING INSIDE YOUR BUSINESS (3 Alternating Deep-Dives with Live Mockups) -->
    <section class="sec" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Enterprise Intelligence</div>
          <h2>AI Working Inside Your Business</h2>
          <p>See how intelligent automation transforms day-to-day operations from manual lag to autonomous precision.</p>
        </div>

        <!-- 01 AI Automation -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;margin-bottom:80px;">
          <div>
            <div class="eyebrow" style="color:var(--cyan);">01 • WORKFLOW AUTOMATION</div>
            <h3 style="font-size:clamp(24px, 3vw, 36px);margin-bottom:16px;">Autonomous Multi-Step Agent Execution</h3>
            <p style="color:var(--ink-2);font-size:15px;line-height:1.65;margin-bottom:20px;">
              Eliminate repetitive manual handoffs. Our custom AI agent orchestrator reads incoming vendor invoices, validates line items against procurement purchase orders, and updates your financial database in seconds.
            </p>
            <div style="display:flex;flex-direction:column;gap:10px;margin-bottom:24px;">
              <div style="font-size:14px;color:var(--ink);">✓ 99.4% document OCR extraction accuracy</div>
              <div style="font-size:14px;color:var(--ink);">✓ Direct webhook dispatch to enterprise accounting suites</div>
              <div style="font-size:14px;color:var(--ink);">✓ Human approval fallback for unexpected discrepancies</div>
            </div>
            <a href="/services/ai-automation" class="btn btn-primary btn-sm">
              <span>Explore AI Automation</span>
              <svg class="arr" width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
          </div>

          <!-- Pure CSS Agent Workflow Checklist Mockup -->
          <div>
            <div class="card flow-box rv">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
                <span style="font-size:13px;font-weight:700;color:var(--ink);">ORCHESTRATOR PIPELINE #812</span>
                <span class="tag-badge live">Executing</span>
              </div>
              <div class="flow-step">
                <span class="badge">01</span>
                <div style="flex:1;">
                  <div style="font-size:13.5px;font-weight:600;color:var(--ink);">Ingest Vendor Invoice PDF</div>
                  <div style="font-size:12px;color:var(--ink-3);">Extracted from accounts@supplier.ae</div>
                </div>
                <span class="status complete">✓ 0.4s</span>
              </div>
              <div class="flow-step">
                <span class="badge">02</span>
                <div style="flex:1;">
                  <div style="font-size:13.5px;font-weight:600;color:var(--ink);">OCR Parsing &amp; VAT Extraction</div>
                  <div style="font-size:12px;color:var(--ink-3);">5% UAE VAT verified against TRN</div>
                </div>
                <span class="status complete">✓ 0.8s</span>
              </div>
              <div class="flow-step active">
                <span class="badge" style="background:var(--blue);color:#FFF;">03</span>
                <div style="flex:1;">
                  <div style="font-size:13.5px;font-weight:600;color:var(--cyan);">PO Reconciliation &amp; Ledger Check</div>
                  <div style="font-size:12px;color:var(--ink-2);">Matching SKU 4882 against ERP PO-991...</div>
                </div>
                <span class="status" style="color:var(--cyan);font-weight:700;">Processing</span>
              </div>
              <div class="flow-step">
                <span class="badge">04</span>
                <div style="flex:1;">
                  <div style="font-size:13.5px;font-weight:600;color:var(--ink-2);">Manager WhatsApp Instant Signoff</div>
                  <div style="font-size:12px;color:var(--ink-3);">Awaiting trigger...</div>
                </div>
                <span class="status" style="color:var(--ink-dim);">Pending</span>
              </div>
            </div>
          </div>
        </div>

        <!-- 02 Business AI Conversions -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;margin-bottom:80px;">
          <!-- Pure CSS Live Chat Assistant Bubble UI Mockup -->
          <div style="order:2;">
            <div class="eyebrow" style="color:var(--cyan);">02 • COMMERCIAL CONVERSIONS</div>
            <h3 style="font-size:clamp(24px, 3vw, 36px);margin-bottom:16px;">Turn Enquiries into Qualified Bookings</h3>
            <p style="color:var(--ink-2);font-size:15px;line-height:1.65;margin-bottom:20px;">
              Responding in 5 minutes vs 30 minutes increases conversion rates by 391%. Our conversational AI engages website visitors and WhatsApp leads in under 45 seconds, answers technical queries, qualifies budget, and schedules a meeting on your sales calendar.
            </p>
            <div style="display:flex;flex-direction:column;gap:10px;margin-bottom:24px;">
              <div style="font-size:14px;color:var(--ink);">✓ Sub-45-second average response speed</div>
              <div style="font-size:14px;color:var(--ink);">✓ Direct Google Calendar &amp; Outlook booking integration</div>
              <div style="font-size:14px;color:var(--ink);">✓ Native Arabic and English conversational fluency</div>
            </div>
            <a href="/services/ai-business-automation" class="btn btn-primary btn-sm">
              <span>Explore AI Conversions</span>
              <svg class="arr" width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
          </div>

          <div style="order:1;">
            <div class="card chat-box rv">
              <div style="display:flex;align-items:center;gap:10px;padding-bottom:12px;border-bottom:1px solid var(--line);margin-bottom:14px;">
                <div style="width:10px;height:10px;border-radius:50%;background:var(--emerald);"></div>
                <div style="font-size:13px;font-weight:700;color:var(--ink);">TOCO Conversational AI Assistant</div>
                <div style="margin-left:auto;font-size:11px;color:var(--ink-3);">WhatsApp Cloud API</div>
              </div>
              <div class="chat-bubble user">
                Hi, do you build custom ERP systems for food distribution companies in Dubai?
              </div>
              <div class="chat-bubble assistant">
                Hello! Yes, we engineer custom logistics and distribution ERPs across the UAE. We recently completed a dispatch platform for iKart Express handling over 15,000 monthly orders. What is your current fleet size and warehouse setup?
              </div>
              <div class="chat-bubble user">
                We have 18 vans and 2 warehouses in Al Quoz. Can we see a demo?
              </div>
              <div class="chat-bubble assistant" style="border-left:3px solid var(--cyan);">
                🎯 <strong>Qualified High-Intent Lead.</strong> I can connect you with our senior systems architect tomorrow. Would 11:00 AM or 3:00 PM GST work best for an interactive screen share?
              </div>
            </div>
          </div>
        </div>

        <!-- 03 AI Apps & Custom Software -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;">
          <div>
            <div class="eyebrow" style="color:var(--cyan);">03 • MISSION-CRITICAL PLATFORMS</div>
            <h3 style="font-size:clamp(24px, 3vw, 36px);margin-bottom:16px;">High-Concurrency Web &amp; Mobile Software</h3>
            <p style="color:var(--ink-2);font-size:15px;line-height:1.65;margin-bottom:20px;">
              Beyond automation, we engineer the high-performance digital engines that power modern enterprises. From consumer mobile apps with Apple Pay to complex client portals, our clean architectures guarantee high velocity.
            </p>
            <div style="display:flex;flex-direction:column;gap:10px;margin-bottom:24px;">
              <div style="font-size:14px;color:var(--ink);">✓ Sub-second API response latency (&lt; 85ms)</div>
              <div style="font-size:14px;color:var(--ink);">✓ Zero framework bloat; lightweight maintainable code</div>
              <div style="font-size:14px;color:var(--ink);">✓ Complete intellectual property transfer with source repositories</div>
            </div>
            <a href="/services/website-and-software-development" class="btn btn-primary btn-sm">
              <span>Explore Custom Software</span>
              <svg class="arr" width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
          </div>

          <div>
            <div class="card rv" style="padding:24px;">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
                <span style="font-size:13px;font-weight:700;color:var(--ink);">API ENDPOINT LATENCY TELEMETRY</span>
                <span style="font-size:11px;color:var(--emerald);font-weight:600;">99.98% HEALTH</span>
              </div>
              <div style="display:flex;flex-direction:column;gap:10px;">
                <div style="background:rgba(255,255,255,0.03);border:1px solid var(--line);border-radius:8px;padding:10px 14px;display:flex;justify-content:space-between;align-items:center;">
                  <span style="font-size:13px;font-family:monospace;color:var(--ink);">GET /api/v1/dispatch/orders</span>
                  <span style="font-size:12px;color:var(--emerald);font-weight:600;">42ms</span>
                </div>
                <div style="background:rgba(255,255,255,0.03);border:1px solid var(--line);border-radius:8px;padding:10px 14px;display:flex;justify-content:space-between;align-items:center;">
                  <span style="font-size:13px;font-family:monospace;color:var(--ink);">POST /api/v1/ai/inquiry-eval</span>
                  <span style="font-size:12px;color:var(--cyan);font-weight:600;">88ms</span>
                </div>
                <div style="background:rgba(255,255,255,0.03);border:1px solid var(--line);border-radius:8px;padding:10px 14px;display:flex;justify-content:space-between;align-items:center;">
                  <span style="font-size:13px;font-family:monospace;color:var(--ink);">GET /api/v1/wps/sif-export</span>
                  <span style="font-size:12px;color:var(--emerald);font-weight:600;">55ms</span>
                </div>
              </div>
              <div style="margin-top:16px;padding-top:12px;border-top:1px solid var(--line);display:flex;justify-content:space-between;font-size:12px;color:var(--ink-3);">
                <span>Infrastructure: AWS UAE (me-central-1)</span>
                <span>Encrypted AES-256</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: PRODUCTS — FEATURED EDITORIAL ROW -->
    <section class="sec" id="products">
      <div class="wrap">
        <div class="pf-layout">
          <!-- Left: Section label + featured large product -->
          <div class="pf-left">
            <div class="eyebrow" style="margin-bottom:12px;">Proprietary Platforms</div>
            <h2 style="margin-bottom:10px;">Built In-House.<br>Deployed Across UAE.</h2>
            <p style="font-size:15px;color:var(--ink-2);max-width:360px;line-height:1.65;margin-bottom:32px;">Purpose-built SaaS platforms engineered by TOCO Technologies for GCC commercial verticals — owned, maintained, and licensed directly.</p>
            <!-- Featured card -->
            <a href="/products/elearning-platform" class="pf-featured rv">
              <div class="pf-feat-eyebrow">
                <span class="prod-status-pill is-live"><span class="pulse-dot"></span> Live v2.4</span>
                <span class="pf-feat-category">Education &amp; Academies</span>
              </div>
              <h3 class="pf-feat-title">E-Learning &amp; LMS Platform</h3>
              <p class="pf-feat-desc">Enterprise distance-learning LMS with adaptive video streaming, automated grading, and learner verification for GCC institutions.</p>
              <div class="pf-feat-metric">
                <span class="pf-feat-num">10,000+</span>
                <span class="pf-feat-label">Concurrent Active Learners</span>
              </div>
              <div class="pf-feat-tech">
                <span>Next.js 14</span><span>PostgreSQL</span><span>HLS Video</span>
              </div>
              <div class="pf-feat-arrow">
                <span>Explore Platform</span>
                <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </div>
            </a>
          </div>

          <!-- Right: 4 compact product rows -->
          <div class="pf-right">
            <a href="/products/interior-quote-automation" class="pf-row rv">
              <div class="pf-row-top">
                <div>
                  <span class="pf-row-cat">Architecture &amp; Fit-Out</span>
                  <h4 class="pf-row-title">Interior Quote &amp; Sales Automation</h4>
                </div>
                <span class="prod-status-pill is-live"><span class="pulse-dot"></span> Live</span>
              </div>
              <p class="pf-row-desc">Instant luxury BOQ proposals with automated e-signatures and UAE VAT invoicing for fit-out studios in Dubai.</p>
              <div class="pf-row-stat">&lt; 3 mins — BOQ Generation</div>
            </a>

            <a href="/products/ai-erp-platform" class="pf-row rv">
              <div class="pf-row-top">
                <div>
                  <span class="pf-row-cat">Operations &amp; Commerce</span>
                  <h4 class="pf-row-title">AI-Powered ERP</h4>
                </div>
                <span class="prod-status-pill is-live"><span class="pulse-dot"></span> Live</span>
              </div>
              <p class="pf-row-desc">Customer inquiry to dispatch automation — predictive inventory, RBAC, and courier API sync across all branches.</p>
              <div class="pf-row-stat">99.8% — Dispatch Accuracy</div>
            </a>

            <a href="/products/payroll-automation" class="pf-row rv">
              <div class="pf-row-top">
                <div>
                  <span class="pf-row-cat">HR &amp; Compliance</span>
                  <h4 class="pf-row-title">Payroll Automation &amp; WPS</h4>
                </div>
                <span class="prod-status-pill is-live"><span class="pulse-dot"></span> Live</span>
              </div>
              <p class="pf-row-desc">One-click .SIF export, automated gratuity calculation, and UAE Labor Law end-of-service compliance.</p>
              <div class="pf-row-stat">100% — MOHRE &amp; SIF Compliant</div>
            </a>

            <a href="/products/real-estate-crm" class="pf-row rv">
              <div class="pf-row-top">
                <div>
                  <span class="pf-row-cat">PropTech &amp; Brokerage</span>
                  <h4 class="pf-row-title">Real Estate CRM Suite</h4>
                </div>
                <span class="prod-status-pill is-dev"><span class="dev-dot"></span> Beta</span>
              </div>
              <p class="pf-row-desc">WhatsApp lead parsing, broker round-robin, Bayut &amp; Property Finder portal sync, and DLD escrow tracking.</p>
              <div class="pf-row-stat">Instant — Portal Webhooks</div>
            </a>

            <div style="padding-top:20px;border-top:1px solid var(--line);">
              <a href="/products" class="btn btn-ghost" style="font-size:13px;padding:9px 20px;">
                <span>All 6 Products</span>
                <svg class="arr" width="13" height="13" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 6: WHERE TO BEGIN    <!-- SECTION 6: WHERE TO BEGIN (AI-Readiness Graphic / 4-Tier Visual Process) -->
    <section class="sec" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Implementation Framework</div>
          <h2>Where to Begin: Your AI-Readiness Journey</h2>
          <p>A structured 4-tier roadmap guiding UAE organizations from operational audit to autonomous scaling.</p>
        </div>
        <div class="grid-4">
          <div class="card step-card rv">
            <div class="step-num">01</div>
            <h3 style="font-size:19px;margin-bottom:8px;font-family:var(--font-display);">Opportunity Audit</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              We analyze your recurring manual bottlenecks, calculate ROI savings, and identify high-leverage automation candidates.
            </p>
          </div>
          <div class="card step-card rv">
            <div class="step-num">02</div>
            <h3 style="font-size:19px;margin-bottom:8px;font-family:var(--font-display);">Architecture &amp; PoC</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Within 14 days, we build a working Proof-of-Concept testing data extraction, API latency, and model accuracy.
            </p>
          </div>
          <div class="card step-card rv">
            <div class="step-num">03</div>
            <h3 style="font-size:19px;margin-bottom:8px;font-family:var(--font-display);">Enterprise Rollout</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Hardened engineering integration with your ERP and CRM databases, role permissions, and full staff onboarding.
            </p>
          </div>
          <div class="card step-card rv">
            <div class="step-num">04</div>
            <h3 style="font-size:19px;margin-bottom:8px;font-family:var(--font-display);">Autonomous Scale</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Continuous telemetry monitoring, model retraining, and dedicated 30-day post-launch engineering SLA warranty.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 7: STATS COUNTERS -->
    <section class="sec">
      <div class="wrap">
        <div class="grid-4">
          <div class="card stat-card rv">
            <div class="stat-num" data-target="99.8">99.8</div>
            <div class="stat-lbl" style="font-size:16px;font-weight:700;color:var(--ink);margin-bottom:4px;">% Uptime SLA</div>
            <p style="font-size:13.5px;color:var(--ink-3);">Guaranteed cloud platform reliability backed by local Dubai support.</p>
          </div>
          <div class="card stat-card rv">
            <div class="stat-num" data-target="30">30</div>
            <div class="stat-lbl" style="font-size:16px;font-weight:700;color:var(--ink);margin-bottom:4px;">-Day Launch Warranty</div>
            <p style="font-size:13.5px;color:var(--ink-3);">Dedicated engineering monitoring and zero-cost post-launch patches.</p>
          </div>
          <div class="card stat-card rv">
            <div class="stat-num" data-target="45">45</div>
            <div class="stat-lbl" style="font-size:16px;font-weight:700;color:var(--ink);margin-bottom:4px;">% Conversion Lift</div>
            <p style="font-size:13.5px;color:var(--ink-3);">Average mobile checkout and enquiry conversion improvement.</p>
          </div>
          <div class="card stat-card rv">
            <div class="stat-num" data-target="24">24</div>
            <div class="stat-lbl" style="font-size:16px;font-weight:700;color:var(--ink);margin-bottom:4px;">/7 AI Execution</div>
            <p style="font-size:13.5px;color:var(--ink-3);">Autonomous workflows processing orders during and outside work hours.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 8: INDUSTRIES — NUMBERED ROW LAYOUT -->
    <section class="sec" id="industries">
      <div class="wrap">
        <div class="ind-row-layout">
          <div class="ind-row-left">
            <div class="eyebrow">UAE Market Verticals</div>
            <h2>Industry Expertise,<br>Built Into Every Line of Code.</h2>
            <p>We build technology shaped around UAE regulatory frameworks, local payment infrastructure, and GCC business logic — not generic offshore templates.</p>
            <a href="/industries" class="btn btn-primary" style="font-size:14px;padding:11px 24px;">
              <span>Explore All Industries</span>
              <svg class="arr" width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
          </div>

          <div class="ind-row-right">
            <a href="/industries" class="ind-nr rv">
              <span class="ind-nr-num">01</span>
              <div class="ind-nr-body">
                <span class="ind-nr-title">Logistics &amp; Distribution</span>
                <span class="ind-nr-sub">Fleet Dispatch · Dubai Trade &amp; Customs · Live GPS</span>
              </div>
              <svg class="ind-nr-arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M4 12L12 4M12 4H6M12 4V10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
            <a href="/industries" class="ind-nr rv">
              <span class="ind-nr-num">02</span>
              <div class="ind-nr-body">
                <span class="ind-nr-title">Luxury Retail &amp; Perfumes</span>
                <span class="ind-nr-sub">Tabby · Tamara · Arabic RTL · Sub-700ms Loads</span>
              </div>
              <svg class="ind-nr-arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M4 12L12 4M12 4H6M12 4V10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
            <a href="/industries" class="ind-nr rv">
              <span class="ind-nr-num">03</span>
              <div class="ind-nr-body">
                <span class="ind-nr-title">Real Estate &amp; Off-Plan</span>
                <span class="ind-nr-sub">RERA Compliant · DLD Escrow · Portal Integrations</span>
              </div>
              <svg class="ind-nr-arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M4 12L12 4M12 4H6M12 4V10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
            <a href="/industries" class="ind-nr rv">
              <span class="ind-nr-num">04</span>
              <div class="ind-nr-body">
                <span class="ind-nr-title">Healthcare &amp; Polyclinics</span>
                <span class="ind-nr-sub">DOH Licensed · Patient Portals · EMR Integration</span>
              </div>
              <svg class="ind-nr-arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M4 12L12 4M12 4H6M12 4V10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
            <a href="/industries" class="ind-nr rv">
              <span class="ind-nr-num">05</span>
              <div class="ind-nr-body">
                <span class="ind-nr-title">Higher Education &amp; LMS</span>
                <span class="ind-nr-sub">SCORM · Apple Pay · Bilingual RTL · 10K+ Learners</span>
              </div>
              <svg class="ind-nr-arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M4 12L12 4M12 4H6M12 4V10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
            <a href="/industries" class="ind-nr rv">
              <span class="ind-nr-num">06</span>
              <div class="ind-nr-body">
                <span class="ind-nr-title">Professional &amp; Legal Advisory</span>
                <span class="ind-nr-sub">Document AI · Case Portals · Secure Client Vaults</span>
              </div>
              <svg class="ind-nr-arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M4 12L12 4M12 4H6M12 4V10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 9: PORTFOLIO / CASE STUDIES    <!-- SECTION 9: PORTFOLIO — EDITORIAL CASE STUDY ROWS -->
    <section class="sec" id="portfolio">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Client Engineering Impact</div>
          <h2>Real Projects.<br>Measurable Results.</h2>
          <p>Selected case studies from TOCO Technologies engagements across Dubai and the GCC.</p>
        </div>

        <div class="cs-row-list">
          <!-- iKart -->
          <a href="/portfolio" class="cs-row rv">
            <div class="cs-row-index">01</div>
            <div class="cs-row-body">
              <div class="cs-row-meta">
                <span class="cs-row-cat">Logistics ERP &amp; Dispatch</span>
                <span class="cs-row-metric">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                  15,000+ orders automated
                </span>
              </div>
              <h3 class="cs-row-title">iKart Express — Multi-Courier ERP</h3>
              <p class="cs-row-desc">Sub-minute automated routing and live GPS driver tracking across all 7 Emirates, eliminating 100% of manual dispatch.</p>
              <div class="cs-row-tags"><span>Fleet Engine</span><span>Next.js 14</span><span>PostgreSQL</span><span>Real-Time GPS</span></div>
            </div>
            <div class="cs-row-img">
              <img src="/assets/images/portfolio/ikart-erp.webp" alt="iKart Express Logistics ERP" width="420" height="240" loading="lazy">
            </div>
          </a>

          <!-- MŌJ -->
          <a href="/portfolio" class="cs-row rv">
            <div class="cs-row-index">02</div>
            <div class="cs-row-body">
              <div class="cs-row-meta">
                <span class="cs-row-cat">Luxury Commerce &amp; D2C</span>
                <span class="cs-row-metric">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                  +42% mobile checkout lift
                </span>
              </div>
              <h3 class="cs-row-title">MŌJ Luxury Fragrance Storefront</h3>
              <p class="cs-row-desc">High-converting perfume boutique with sub-700ms page loads, Tabby installment checkout, and seamless Arabic RTL support.</p>
              <div class="cs-row-tags"><span>Headless Shopify</span><span>Tabby 4-Pay</span><span>Arabic RTL</span><span>Cloudflare Edge</span></div>
            </div>
            <div class="cs-row-img">
              <img src="/assets/images/portfolio/moj-ecommerce.webp" alt="MŌJ Perfume E-Commerce" width="420" height="240" loading="lazy">
            </div>
          </a>

          <!-- GlobalEdge -->
          <a href="/portfolio" class="cs-row rv">
            <div class="cs-row-index">03</div>
            <div class="cs-row-body">
              <div class="cs-row-meta">
                <span class="cs-row-cat">Enterprise Corporate Web</span>
                <span class="cs-row-metric">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                  98/100 Core Web Vitals
                </span>
              </div>
              <h3 class="cs-row-title">GlobalEdge International Suite</h3>
              <p class="cs-row-desc">Scalable corporate web platform engineered for high-concurrency enterprise traffic, multi-language localization, and sub-second global edge performance.</p>
              <div class="cs-row-tags"><span>Static Edge</span><span>Enterprise SEO</span><span>Zero Bloat</span><span>WCAG A11y</span></div>
            </div>
            <div class="cs-row-img">
              <img src="/assets/images/portfolio/globaledge-platform.webp" alt="GlobalEdge Platform" width="420" height="240" loading="lazy">
            </div>
          </a>
        </div>

        <div style="text-align:center;margin-top:40px;">
          <a href="/portfolio" class="btn btn-ghost">
            <span>View All Case Studies</span>
            <svg class="arr" width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 10: PROCESS TIMELINE    <!-- SECTION 10: PROCESS TIMELINE (MINIMAL EDITORIAL) -->
    <section class="sec process-split-sec" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:56px 0;" id="methodology">
      <div class="wrap">
        <div class="sec-head" style="margin-bottom:28px;">
          <div class="eyebrow">Delivery Process</div>
          <h2 style="font-size:clamp(24px, 2.6vw, 32px);letter-spacing:-0.02em;margin-bottom:0;">How We Build &amp; Ship</h2>
        </div>

        <div class="editorial-framework rv">
          <!-- Top Border & Column Headers -->
          <div class="framework-header">
            <div class="f-head-col left">
              <span class="f-col-title">Design &amp; Architecture</span>
              <span class="f-col-meta">04</span>
            </div>
            <div class="f-head-col right">
              <span class="f-col-meta">04</span>
              <span class="f-col-title">Engineering &amp; Launch</span>
            </div>
          </div>

          <!-- Split Body with Hairline Center Divider -->
          <div class="framework-body">
            <!-- Left Column: Design / Pre-Build -->
            <div class="f-col left">
              <div class="f-item">
                <span class="f-idx">01</span>
                <span class="f-name">Scoping &amp; Architecture</span>
              </div>
              <div class="f-item">
                <span class="f-idx">02</span>
                <span class="f-name">UI/UX Prototyping</span>
              </div>
              <div class="f-item">
                <span class="f-idx">03</span>
                <span class="f-name">Design Systems</span>
              </div>
              <div class="f-item">
                <span class="f-idx">04</span>
                <span class="f-name">API &amp; Integration Specs</span>
              </div>
            </div>

            <!-- Right Column: Production / Engineering -->
            <div class="f-col right">
              <div class="f-item is-right">
                <span class="f-name">Clean-Code Sprints</span>
                <span class="f-idx">05</span>
              </div>
              <div class="f-item is-right">
                <span class="f-name">ERP &amp; Database Sync</span>
                <span class="f-idx">06</span>
              </div>
              <div class="f-item is-right">
                <span class="f-name">Automated QA Audits</span>
                <span class="f-idx">07</span>
              </div>
              <div class="f-item is-right">
                <span class="f-name">Production &amp; 30-Day SLA</span>
                <span class="f-idx">08</span>
              </div>
            </div>
          </div>

          <!-- Bottom Footer Bar -->
          <div class="framework-footer">
            <a href="/contact" class="f-foot-link">
              <span>Get project roadmap</span>
              <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
            <span class="f-foot-meta">3 to 6 weeks delivery SLA</span>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 11: TESTIMONIALS SLIDER -->
    <section class="sec" id="testimonials">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Client Feedback</div>
          <h2>Trusted by Operations, Product &amp; Brand Leaders</h2>
          <p>Feedback from organizations partnering with TOCO Technologies across custom ERP, e-commerce, and enterprise web engineering.</p>
        </div>

        <div class="testi-slider">
          <div class="testi-track">
{testi_cards_html}          </div>
          <div class="slider-controls">
            <button class="slider-btn prev" type="button" aria-label="Previous testimonial slide">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M10 12L6 8L10 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </button>
            <div class="slider-dots"></div>
            <button class="slider-btn next" type="button" aria-label="Next testimonial slide">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M6 12L10 8L6 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 12: FAQ ACCORDION -->
    <section class="sec" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line);" id="faq">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Clear Answers</div>
          <h2>Frequently Asked Questions in Dubai &amp; the UAE</h2>
          <p>Transparent information regarding engagement timelines, code ownership, and technical support.</p>
        </div>
        <div class="faq-wrap">
{faq_items_html}        </div>
      </div>
    </section>

    <!-- SECTION 13: BIG CTA BANNER -->
    {render_cta_band("Ready to Build Your Next Digital Advantage in Dubai?", "Partner with TOCO Technologies in Port Saeed, Dubai. Schedule a strategy session with our senior engineers and receive a detailed project roadmap within 24 hours.")}
  </main>

{render_footer()}
</body>
</html>'''

    with open(os.path.join(ROOT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Generated Homepage: /index.html")


# -----------------------------------------------------------------------------
# 9. Generate Sitemap & Robots.txt
# -----------------------------------------------------------------------------
def build_sitemap_and_robots():
    all_urls = [
        ("/", "1.0", "weekly"),
        ("/about", "0.9", "monthly"),
        ("/services", "0.9", "weekly"),
        ("/products", "0.9", "weekly"),
        ("/industries", "0.8", "monthly"),
        ("/portfolio", "0.8", "monthly"),
        ("/contact", "0.9", "monthly"),
        ("/privacy-policy", "0.3", "yearly"),
        ("/terms-of-service", "0.3", "yearly"),
    ]

    for s in SERVICES_DATA:
        all_urls.append((f"/services/{s['slug']}", "0.85", "monthly"))

    for p in PRODUCTS_DATA:
        all_urls.append((f"/products/{p['slug']}", "0.85", "monthly"))

    sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>',
                   '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, prio, freq in all_urls:
        url_str = f"{SITE_BASE}{path}" if path != "/" else f"{SITE_BASE}/"
        sitemap_xml.append(f'  <url>\n    <loc>{url_str}</loc>\n    <lastmod>2026-11-12</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>')
    sitemap_xml.append('</urlset>')

    with open(os.path.join(ROOT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_xml))
    print(f"Generated sitemap.xml with {len(all_urls)} URLs.")

    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {SITE_BASE}/sitemap.xml
"""
    with open(os.path.join(ROOT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_txt)
    print("Generated robots.txt.")


# -----------------------------------------------------------------------------
# Main Execution Runner
# -----------------------------------------------------------------------------
def main():
    print("Beginning generation of all 26 static pages for TOCO Technologies...")

    # Services
    for svc in SERVICES_DATA:
        generate_service_page(svc)

    # Products
    for prod in PRODUCTS_DATA:
        generate_product_page(prod)

    # Hubs & Auxiliary Pages
    build_services_hub()
    build_products_hub()
    build_about_page()
    build_industries_page()
    build_portfolio_page()
    build_contact_page()
    build_legal_and_404()
    build_homepage()
    build_sitemap_and_robots()

    # Premium v2 layout for selected service pages (preview: ai-automation)
    from service_v2 import main as build_service_v2
    build_service_v2()

    # Assign white / black / blue palettes to every section
    from apply_theme import main as apply_theme
    apply_theme()

    print("ALL 26 STATIC PAGES GENERATED SUCCESSFULLY!")

if __name__ == "__main__":
    main()

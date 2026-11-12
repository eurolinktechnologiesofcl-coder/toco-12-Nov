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
            "icon": "🚚",
            "title": "Logistics, Supply Chain & Dispatch",
            "desc": "Real-time fleet tracking, automated manifests, warehouse inventory sync, and multi-courier dispatch consoles tailored for UAE distribution.",
            "points": ["iKart Express custom ERP case study", "Sub-minute courier route optimization", "Automated UAE proof of delivery (POD)"]
        },
        {
            "icon": "💎",
            "title": "Luxury Perfumes, Fashion & Retail E-Commerce",
            "desc": "High-converting digital storefronts with Apple Pay, Tabby/Tamara installment integrations, and multi-currency GCC checkout experiences.",
            "points": ["MŌJ luxury fragrance platform", "Sub-second mobile checkout UX", "Automated 5% UAE VAT invoicing"]
        },
        {
            "icon": "🏙️",
            "title": "Real Estate Brokerages & Property Developers",
            "desc": "Off-plan inventory management, automated Bayut and Property Finder WhatsApp lead intake, and interactive client presentation portals.",
            "points": ["Real Estate CRM platform", "Automated broker lead assignment", "Interactive floor plans & payment plans"]
        },
        {
            "icon": "🏥",
            "title": "Healthcare, Medical Centers & Polyclinics",
            "desc": "HIPAA-grade patient appointment portals, automated SMS and WhatsApp reminder sequences, and secure EMR database sync.",
            "points": ["Patient appointment self-booking", "Reduced clinic no-show rates by 48%", "Full data privacy compliance"]
        },
        {
            "icon": "🎓",
            "title": "Higher Education, Academies & Corporate LMS",
            "desc": "Bilingual distance learning portals, DRM protected video streaming, automated grading, and cryptographic completion certificates.",
            "points": ["Custom e-learning & LMS platforms", "10,000+ concurrent exam sessions", "Integrated UAE payment gateways"]
        },
        {
            "icon": "💼",
            "title": "Professional Services, Legal & Financial Advisory",
            "desc": "Executive corporate portals, encrypted document exchange rooms, automated billing, and compliance workflow trackers.",
            "points": ["Role-based access security", "Client onboarding automation", "Zero data retention API configurations"]
        }
    ]

    cards_html = ""
    for ind in industries_list:
        points_html = "".join([f'<li style="font-size:13.5px;color:var(--ink-2);margin-bottom:6px;">✓ {p}</li>' for p in ind["points"]])
        cards_html += f'''        <div class="card rv" style="padding:28px;">
          <div style="font-size:32px;margin-bottom:12px;">{ind["icon"]}</div>
          <h3 style="font-size:20px;margin-bottom:8px;font-family:var(--font-display);color:var(--ink);">{ind["title"]}</h3>
          <p style="font-size:14.5px;color:var(--ink-2);line-height:1.6;margin-bottom:16px;">{ind["desc"]}</p>
          <ul style="list-style:none;padding:0;border-top:1px solid var(--line);padding-top:14px;">
            {points_html}
          </ul>
        </div>\n'''

    content = f'''{render_head_tags(title, desc, canonical, schema)}
{render_header("industries")}
  <main id="main-content">
    <section class="page-hero">
      <div class="wrap">
        {render_breadcrumbs(crumbs)}
        <div style="max-width:820px;">
          <div class="eyebrow">Sector Capabilities • Dubai &amp; Across UAE</div>
          <h1>Tailored Technology Solutions for UAE Enterprise Sectors</h1>
          <p class="lede">
            Every industry operates under distinct regulatory mandates, operational constraints, and customer expectations. We engineer domain-specific software platforms across core UAE commercial verticals.
          </p>
        </div>
      </div>
    </section>

    <section class="sec">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Industry Verticals</div>
          <h2>Proven Domain Expertise in the Arabian Gulf</h2>
          <p>Explore how we solve specialized operational and commercial challenges for regional leaders.</p>
        </div>
        <div class="grid-3">
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
    <!-- SECTION 1: HERO (Highest Design Priority) -->
    <section class="hero" id="home">
      <div class="wrap">
        <div class="hero-grid">
          <!-- Hero Copy -->
          <div>
            <div class="eyebrow" style="margin-bottom:18px;">
              <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--cyan);margin-right:6px;box-shadow:0 0 8px var(--cyan);"></span>
              DUBAI &amp; UAE ENTERPRISE TECHNOLOGY PARTNER
            </div>
            <h1>Engineering <span class="grad-text">AI Business Automation</span> &amp; High-Impact Software in Dubai</h1>
            <p class="lede">
              We build powerful websites, intelligent AI applications, custom ERPs, and conversion-engineered digital experiences that help UAE businesses connect, automate, and grow.
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
            <div style="display:flex;align-items:center;gap:20px;margin-top:28px;font-size:13px;color:var(--ink-3);">
              <span>✓ Port Saeed, Dubai Office</span>
              <span>✓ 30-Day Launch Warranty</span>
              <span>✓ 100% Code Ownership</span>
            </div>
          </div>

          <!-- Hero Pure CSS / HTML Visual Mockup -->
          <div class="hero-visual">
            <div class="mock-card">
              <div class="mock-header">
                <div class="mock-dots">
                  <span></span><span></span><span></span>
                </div>
                <div class="mock-title">tocotechnologies.ae / system-telemetry</div>
                <div style="font-size:11px;color:var(--cyan);font-weight:600;">ACTIVE</div>
              </div>

              <!-- Metrics Summary Row -->
              <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-bottom:16px;">
                <div style="background:rgba(255,255,255,0.025);border:1px solid var(--line);border-radius:10px;padding:12px;">
                  <div style="font-size:11px;color:var(--ink-3);text-transform:uppercase;margin-bottom:4px;">Core Web Vitals</div>
                  <div style="font-size:20px;font-weight:700;color:var(--ink);font-family:var(--font-display);">98 / 100</div>
                  <div style="font-size:11px;color:var(--emerald);">Fast Mobile UX</div>
                </div>
                <div style="background:rgba(255,255,255,0.025);border:1px solid var(--line);border-radius:10px;padding:12px;">
                  <div style="font-size:11px;color:var(--ink-3);text-transform:uppercase;margin-bottom:4px;">AI Automation</div>
                  <div style="font-size:20px;font-weight:700;color:var(--ink);font-family:var(--font-display);">24/7 Live</div>
                  <div style="font-size:11px;color:var(--cyan);">&lt; 45s Response</div>
                </div>
                <div style="background:rgba(255,255,255,0.025);border:1px solid var(--line);border-radius:10px;padding:12px;">
                  <div style="font-size:11px;color:var(--ink-3);text-transform:uppercase;margin-bottom:4px;">Platform Uptime</div>
                  <div style="font-size:20px;font-weight:700;color:var(--ink);font-family:var(--font-display);">99.8%</div>
                  <div style="font-size:11px;color:var(--blue-bright);">Cloud SLA</div>
                </div>
              </div>

              <!-- Real-Time Telemetry Graph -->
              <div style="background:rgba(10,16,28,0.7);border:1px solid var(--line);border-radius:12px;padding:16px;margin-bottom:14px;">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
                  <span style="font-size:13px;font-weight:600;color:var(--ink);">Inquiry &amp; Conversion Telemetry</span>
                  <span style="font-size:11px;padding:2px 8px;border-radius:999px;background:rgba(6,182,212,0.15);color:var(--cyan);border:1px solid rgba(6,182,212,0.3);">Real-Time Sync</span>
                </div>
                <!-- Pure SVG Sparkline -->
                <svg viewBox="0 0 360 80" style="width:100%;height:80px;overflow:visible;">
                  <defs>
                    <linearGradient id="chartGrad" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0.35"/>
                      <stop offset="100%" stop-color="#3B82F6" stop-opacity="0.0"/>
                    </linearGradient>
                  </defs>
                  <path d="M0,65 Q45,55 90,48 T180,32 T270,22 T360,10 L360,80 L0,80 Z" fill="url(#chartGrad)"/>
                  <path d="M0,65 Q45,55 90,48 T180,32 T270,22 T360,10" fill="none" stroke="#3B82F6" stroke-width="2.5"/>
                  <circle cx="180" cy="32" r="4.5" fill="#06B6D4" stroke="#0E1626" stroke-width="2"/>
                  <circle cx="360" cy="10" r="5" fill="#3B82F6" stroke="#FFFFFF" stroke-width="2"/>
                </svg>
              </div>

              <!-- Location & Status Pills -->
              <div style="display:flex;justify-content:space-between;align-items:center;font-size:12px;color:var(--ink-2);padding-top:4px;">
                <span style="display:flex;align-items:center;gap:6px;">
                  <span style="width:6px;height:6px;border-radius:50%;background:var(--emerald);"></span>
                  Port Saeed, Dubai HQ
                </span>
                <span>Full-Stack Engineering &amp; AI</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: INFINITE LOGO MARQUEE -->
    <section class="sec" style="padding:20px 0;background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
      <div class="wrap" style="text-align:center;margin-bottom:12px;">
        <span style="font-size:12px;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;color:var(--ink-3);">
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

    <!-- SECTION 3: WHAT WE BUILD (Card Grid with ↗ links and tags) -->
    <section class="sec" id="what-we-build">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Enterprise Capabilities</div>
          <h2>What We Build for UAE Businesses</h2>
          <p>Production-grade technology platforms engineered for commercial growth, high concurrency, and long-term maintainability.</p>
        </div>
        <div class="grid-3">
          <!-- Card 1 -->
          <a href="/services/ai-automation" class="card rv" style="text-decoration:none;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
              <span style="font-size:28px;">🤖</span>
              <span style="color:var(--cyan);font-size:20px;font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">AI Automation &amp; Autonomous Agents</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:16px;">
              Intelligent multi-agent systems and LLM pipelines that execute complex operational workflows without manual data entry.
            </p>
            <div class="tags">
              <span>LLM Pipelines</span>
              <span>Doc Intelligence</span>
              <span>FastAPI</span>
            </div>
          </a>

          <!-- Card 2 -->
          <a href="/services/ai-business-automation" class="card rv" style="text-decoration:none;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
              <span style="font-size:28px;">⚡</span>
              <span style="color:var(--cyan);font-size:20px;font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">AI Business Conversions</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:16px;">
              Instant sub-minute lead capture across WhatsApp and website chat, autonomous qualification, and immediate CRM synchronization.
            </p>
            <div class="tags">
              <span>WhatsApp Cloud</span>
              <span>Instant Lead Qual</span>
              <span>Calendar Sync</span>
            </div>
          </a>

          <!-- Card 3 -->
          <a href="/services/mobile-app-development" class="card rv" style="text-decoration:none;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
              <span style="font-size:28px;">📱</span>
              <span style="color:var(--cyan);font-size:20px;font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">Mobile Application Software</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:16px;">
              Native and Flutter iOS &amp; Android applications built for silky 60fps performance, Apple Pay checkouts, and live GPS dispatch.
            </p>
            <div class="tags">
              <span>Flutter</span>
              <span>Apple Pay</span>
              <span>GPS Telemetry</span>
            </div>
          </a>

          <!-- Card 4 -->
          <a href="/services/website-and-software-development" class="card rv" style="text-decoration:none;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
              <span style="font-size:28px;">💻</span>
              <span style="color:var(--cyan);font-size:20px;font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">Website &amp; Custom Software</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:16px;">
              Sub-second corporate web platforms, client portals, and cloud microservices engineered for Core Web Vitals dominance.
            </p>
            <div class="tags">
              <span>Sub-Second Speeds</span>
              <span>Semantic HTML5</span>
              <span>REST APIs</span>
            </div>
          </a>

          <!-- Card 5 -->
          <a href="/services/ecommerce-development" class="card rv" style="text-decoration:none;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
              <span style="font-size:28px;">🛍️</span>
              <span style="color:var(--cyan);font-size:20px;font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">E-Commerce Development</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:16px;">
              High-converting digital storefronts on Shopify Plus or custom headless stacks with Tabby/Tamara installments and UAE VAT invoicing.
            </p>
            <div class="tags">
              <span>Shopify Plus</span>
              <span>Tabby / Tamara</span>
              <span>Live POS Sync</span>
            </div>
          </a>

          <!-- Card 6 -->
          <a href="/services/erp-and-custom-software" class="card rv" style="text-decoration:none;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
              <span style="font-size:28px;">🏢</span>
              <span style="color:var(--cyan);font-size:20px;font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">Custom ERP &amp; Business Systems</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:16px;">
              Bespoke enterprise resource planning suites, logistics dispatch consoles, and warehouse inventory systems tailored to your exact rules.
            </p>
            <div class="tags">
              <span>Logistics Dispatch</span>
              <span>RBAC Security</span>
              <span>Zero License Fees</span>
            </div>
          </a>
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

    <!-- SECTION 5: OUR PRODUCTS SHOWCASE -->
    <section class="sec" id="products">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Proprietary Software</div>
          <h2>Our Products Showcase</h2>
          <p>Purpose-built software platforms engineered by TOCO Technologies for regional UAE commercial verticals.</p>
        </div>
        <div class="grid-3">
          <!-- E-Learning Platform -->
          <a href="/products/elearning-platform" class="card prod-card rv" style="text-decoration:none;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
              <span class="tag-badge live">Live Platform</span>
              <span style="color:var(--cyan);font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">E-Learning &amp; LMS Platform</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:14px;">
              An enterprise distance-learning LMS with adaptive video streaming, automated grading, and learner verification.
            </p>
            <div class="tags">
              <span>10K+ Concurrent</span>
              <span>Bilingual RTL</span>
              <span>Apple Pay</span>
            </div>
          </a>

          <!-- Interior Quote Automation -->
          <a href="/products/interior-quote-automation" class="card prod-card rv" style="text-decoration:none;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
              <span class="tag-badge live">Live Platform</span>
              <span style="color:var(--cyan);font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">Interior Quote &amp; Sales Automation</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:14px;">
              Interior design quote generation and sales automation platform delivering instant luxury BOQ proposals for fit-out studios in Dubai.
            </p>
            <div class="tags">
              <span>85% Faster Quotes</span>
              <span>E-Signatures</span>
              <span>UAE VAT Invoices</span>
            </div>
          </a>

          <!-- AI-Powered ERP -->
          <a href="/products/ai-erp-platform" class="card prod-card rv" style="text-decoration:none;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
              <span class="tag-badge live">Live Platform</span>
              <span style="color:var(--cyan);font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">AI-Powered ERP</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:14px;">
              AI-assisted enterprise operations platform that bridges customer inquiries directly to procurement, dispatch, and automated invoicing.
            </p>
            <div class="tags">
              <span>Predictive Stock</span>
              <span>Auto Dispatch</span>
              <span>Role RBAC</span>
            </div>
          </a>

          <!-- Payroll Automation -->
          <a href="/products/payroll-automation" class="card prod-card rv" style="text-decoration:none;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
              <span class="tag-badge live">Live Platform</span>
              <span style="color:var(--cyan);font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">Payroll Automation &amp; WPS</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:14px;">
              Automated payroll and WPS compliance software for UAE businesses. One-click .SIF file generation and automated gratuity calculation.
            </p>
            <div class="tags">
              <span>100% SIF Valid</span>
              <span>MOHRE Labor Law</span>
              <span>Encrypted</span>
            </div>
          </a>

          <!-- Analytics Suite -->
          <a href="/products/analytics-tracking" class="card prod-card rv" style="text-decoration:none;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
              <span class="tag-badge dev">In Development</span>
              <span style="color:var(--cyan);font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">Analytics Tracking Suite</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:14px;">
              Privacy-first customer journey attribution and real-time business telemetry designed for GCC commerce.
            </p>
            <div class="tags">
              <span>Cookie-Less</span>
              <span>&lt; 5KB Tag</span>
            </div>
          </a>

          <!-- Real Estate CRM -->
          <a href="/products/real-estate-crm" class="card prod-card rv" style="text-decoration:none;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
              <span class="tag-badge dev">In Development</span>
              <span style="color:var(--cyan);font-weight:700;">↗</span>
            </div>
            <h3 style="font-size:20px;margin-bottom:8px;color:var(--ink);">Real Estate CRM Suite</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;margin-bottom:14px;">
              Purpose-built CRM for Dubai property brokerages with automated portal lead capture, WhatsApp parsing, and unit inventory sync.
            </p>
            <div class="tags">
              <span>Bayut &amp; PF Sync</span>
              <span>Broker WhatsApp</span>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 6: WHERE TO BEGIN (AI-Readiness Graphic / 4-Tier Visual Process) -->
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

    <!-- SECTION 8: INDUSTRIES CHIPS -->
    <section class="sec" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Specialized Verticals</div>
          <h2>Industries We Accelerate in the UAE</h2>
          <p>Domain-specific architectures engineered around local business models and regulatory requirements.</p>
        </div>
        <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;max-width:960px;margin:0 auto 30px;">
          <a href="/industries" class="t-chip" style="font-size:14.5px;padding:10px 18px;text-decoration:none;">🚚 Logistics &amp; Distribution</a>
          <a href="/industries" class="t-chip" style="font-size:14.5px;padding:10px 18px;text-decoration:none;">💎 Luxury Retail &amp; Perfumes</a>
          <a href="/industries" class="t-chip" style="font-size:14.5px;padding:10px 18px;text-decoration:none;">🏙️ Real Estate &amp; Off-Plan</a>
          <a href="/industries" class="t-chip" style="font-size:14.5px;padding:10px 18px;text-decoration:none;">🏥 Healthcare &amp; Polyclinics</a>
          <a href="/industries" class="t-chip" style="font-size:14.5px;padding:10px 18px;text-decoration:none;">🎓 Higher Education &amp; LMS</a>
          <a href="/industries" class="t-chip" style="font-size:14.5px;padding:10px 18px;text-decoration:none;">💼 Professional &amp; Legal Advisory</a>
        </div>
        <div style="text-align:center;">
          <a href="/industries" class="btn btn-ghost">
            <span>Explore Industry Case Studies</span>
            <svg class="arr" width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 9: PORTFOLIO / CASE STUDIES -->
    <section class="sec" id="portfolio">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Proven Engineering</div>
          <h2>Verified Client Case Studies</h2>
          <p>Real platforms delivering verified commercial results across Dubai and the UAE.</p>
        </div>
        <div class="grid-3">
          <div class="card rv" style="padding:0;overflow:hidden;">
            <img src="/assets/images/portfolio/ikart-erp.webp" alt="iKart Express ERP" width="600" height="340" style="width:100%;height:200px;object-fit:cover;border-bottom:1px solid var(--line);">
            <div style="padding:22px;">
              <span class="tag-badge live" style="margin-bottom:8px;">Logistics &amp; ERP</span>
              <h3 style="font-size:18px;margin-bottom:8px;font-family:var(--font-display);color:var(--ink);">iKart Express Logistics ERP</h3>
              <p style="font-size:13.5px;color:var(--ink-2);line-height:1.55;margin-bottom:12px;">
                Custom dispatch console handling 15,000+ monthly deliveries with sub-minute route calculation and live GPS tracking.
              </p>
              <div style="font-size:12.5px;color:var(--cyan);font-weight:600;">✓ 65% faster dispatch velocity</div>
            </div>
          </div>

          <div class="card rv" style="padding:0;overflow:hidden;">
            <img src="/assets/images/portfolio/moj-ecommerce.webp" alt="MŌJ Perfume E-Commerce" width="600" height="340" style="width:100%;height:200px;object-fit:cover;border-bottom:1px solid var(--line);">
            <div style="padding:22px;">
              <span class="tag-badge live" style="margin-bottom:8px;">Luxury E-Commerce</span>
              <h3 style="font-size:18px;margin-bottom:8px;font-family:var(--font-display);color:var(--ink);">MŌJ Luxury Fragrance Storefront</h3>
              <p style="font-size:13.5px;color:var(--ink-2);line-height:1.55;margin-bottom:12px;">
                High-converting digital perfume boutique with Tabby installment checkout, 0.7s load times, and automated VAT invoices.
              </p>
              <div style="font-size:12.5px;color:var(--cyan);font-weight:600;">✓ +42% mobile conversion lift</div>
            </div>
          </div>

          <div class="card rv" style="padding:0;overflow:hidden;">
            <img src="/assets/images/portfolio/globaledge-platform.webp" alt="GlobalEdge Platform" width="600" height="340" style="width:100%;height:200px;object-fit:cover;border-bottom:1px solid var(--line);">
            <div style="padding:22px;">
              <span class="tag-badge live" style="margin-bottom:8px;">Enterprise Web</span>
              <h3 style="font-size:18px;margin-bottom:8px;font-family:var(--font-display);color:var(--ink);">GlobalEdge International Suite</h3>
              <p style="font-size:13.5px;color:var(--ink-2);line-height:1.55;margin-bottom:12px;">
                Scalable corporate web platform engineered for high concurrency, multi-language localization, and sub-second global speeds.
              </p>
              <div style="font-size:12.5px;color:var(--cyan);font-weight:600;">✓ Core Web Vitals score of 98</div>
            </div>
          </div>
        </div>
        <div style="text-align:center;margin-top:32px;">
          <a href="/portfolio" class="btn btn-ghost">
            <span>View All Client Case Studies</span>
            <svg class="arr" width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 10: PROCESS TIMELINE (Discover, Design, Develop, Launch) -->
    <section class="sec" style="background:var(--bg-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
      <div class="wrap">
        <div class="sec-head">
          <div class="eyebrow">Proven Methodology</div>
          <h2>Our 4-Phase Delivery Framework</h2>
          <p>Transparent milestones, weekly sprint updates, and rigorous quality assurance at every stage.</p>
        </div>
        <div class="grid-4">
          <div class="card step-card rv">
            <div class="step-num">Phase 01</div>
            <h3 style="font-size:19px;margin-bottom:8px;font-family:var(--font-display);">Strategic Discovery</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Deep operational scoping, database modeling, and technical specification signed off in Port Saeed, Dubai.
            </p>
          </div>
          <div class="card step-card rv">
            <div class="step-num">Phase 02</div>
            <h3 style="font-size:19px;margin-bottom:8px;font-family:var(--font-display);">UI/UX Prototyping</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Figma design tokens, interactive clickable wireframes, and WCAG AA accessibility verification.
            </p>
          </div>
          <div class="card step-card rv">
            <div class="step-num">Phase 03</div>
            <h3 style="font-size:19px;margin-bottom:8px;font-family:var(--font-display);">Sprint Engineering</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Agile development using clean code principles, automated unit testing, and continuous deployment builds.
            </p>
          </div>
          <div class="card step-card rv">
            <div class="step-num">Phase 04</div>
            <h3 style="font-size:19px;margin-bottom:8px;font-family:var(--font-display);">Production &amp; SLA</h3>
            <p style="font-size:14px;color:var(--ink-2);line-height:1.6;">
              Zero-downtime deployment, staff onboarding, and 30 consecutive calendar days of engineering warranty.
            </p>
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

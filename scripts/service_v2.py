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

V2_SLUGS = ["ai-automation"]

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
    }
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
    bento_html = f'''        <div class="sv-bento-grid">
          <!-- Bento 1: Large Featured Multi-Agent (Spans 2 cols) -->
          <article class="bento-card bento-wide is-featured rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("bot")}MULTI-AGENT ARCHITECTURE</span>
              <h3>Autonomous Multi-Agent Orchestration</h3>
              <p>We deploy specialized deterministic agents coordinated by an intelligent supervisor. Each agent handles a single task under strict validation rules, with zero hallucinatory drift and full cryptographic audit logging.</p>
            </div>
            <div class="bento-agent-telemetry">
              <div class="agent-bar-row">
                <div class="agent-info"><b>Intake Agent</b><small>Ingests email PDFs &amp; WhatsApp</small></div>
                <div class="agent-track"><span style="width: 94%;"></span></div>
                <span class="agent-pct">94% active</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Validation Agent</b><small>Enforces UAE TRN &amp; 5% VAT rules</small></div>
                <div class="agent-track"><span style="width: 78%;"></span></div>
                <span class="agent-pct">78% active</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Posting Agent</b><small>Direct REST API sync to ERP</small></div>
                <div class="agent-track"><span style="width: 62%;"></span></div>
                <span class="agent-pct">62% active</span>
              </div>
            </div>
          </article>

          <!-- Bento 2: Vision OCR (Spans 1 col) -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("file-text")}DOCUMENT INTELLIGENCE</span>
              <h3>Document Vision &amp; Arabic OCR</h3>
              <p>Extract line items, tax numbers, and vendor details from Arabic &amp; English PDFs with 99.4% precision.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="ocr-preview">
                <div class="ocr-tag">TRN: 100234891000003</div>
                <div class="ocr-val">VAT 5%: AED 1,450.00</div>
                <div class="ocr-status ok">{svg("check")} Validated FTA Registry</div>
              </div>
            </div>
          </article>

          <!-- Bento 3: Human Safeguards (Spans 1 col) -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("message")}ZERO FRICTION</span>
              <h3>Human-in-the-Loop Sign-offs</h3>
              <p>Never let AI make blind decisions. When an order or invoice exceeds thresholds, managers receive a 1-tap WhatsApp approval.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="wa-preview">
                <div class="wa-msg">Invoice #AE-894 exceeds AED 20,000 threshold. Approve payment?</div>
                <div class="wa-actions">
                  <span class="wa-btn ok">Approve</span>
                  <span class="wa-btn flag">Inspect</span>
                </div>
              </div>
            </div>
          </article>

          <!-- Bento 4: Security & UAE Data Sovereignty (Spans 2 cols) -->
          <article class="bento-card bento-wide is-security rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("shield")}UAE ENTERPRISE COMPLIANCE</span>
              <h3>UAE Data Sovereignty &amp; Private VPC Deployment</h3>
              <p>Host models within UAE borders (AWS Middle East UAE or Azure UAE Central), fully compliant with UAE Federal Decree-Law No. 45 on Personal Data Protection. Zero training on your proprietary corporate records.</p>
            </div>
            <div class="security-cluster">
              <div class="sec-pill">{svg("lock")}<span>AES-256 Cloud Encryption</span></div>
              <div class="sec-pill">{svg("map-pin")}<span>AWS / Azure UAE Data Residency</span></div>
              <div class="sec-pill">{svg("shield")}<span>Zero-Retention Corporate APIs</span></div>
              <div class="sec-pill">{svg("users")}<span>Granular Role-Based Access (RBAC)</span></div>
            </div>
          </article>
        </div>'''

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

    # High-Variety Related Cards (Replaces 3 uniform boxes from Screenshot 2)
    related_html = f'''        <div class="sv-rel-grid">
          <!-- Card 1: AI Business Conversions (Featured Royal Navy Glow) -->
          <a href="/services/ai-business-automation" class="sv-rel-card is-featured rv">
            <div>
              <span class="rel-tag">{svg("zap")} SERVICE &bull; SALES ACCELERATION</span>
              <h3>AI Business Conversions</h3>
              <p>Turn web visitors and WhatsApp inquiries into verified business opportunities with autonomous qualification agents.</p>
              <div class="rel-mockup">
                <div style="display:flex;align-items:center;justify-content:space-between;font-size:11.5px;margin-bottom:4px;">
                  <span>Inbound Lead</span>
                  <span style="color:#60A5FA;">18s WhatsApp AI</span>
                  <span style="color:#34D399;">✓ Qualified Deal</span>
                </div>
                <div style="height:3px;background:rgba(255,255,255,0.1);border-radius:2px;overflow:hidden;">
                  <div style="width:75%;height:100%;background:linear-gradient(90deg, #3B82F6, #10B981);"></div>
                </div>
              </div>
            </div>
            <span class="rel-action"><span>Explore Sales Automation</span>{svg("arrow-up-right")}</span>
          </a>

          <!-- Card 2: Custom ERP & Business Software (Technical Blueprint) -->
          <a href="/services/erp-and-custom-software" class="sv-rel-card is-tech rv">
            <div>
              <span class="rel-tag">{svg("building")} SERVICE &bull; ENTERPRISE CORE</span>
              <h3>Custom ERP &amp; Software</h3>
              <p>Unify your business operations with bespoke ERP suites, dispatch platforms, and custom REST API integrations.</p>
              <div class="rel-mockup">
                <div style="display:flex;align-items:center;gap:8px;font-family:ui-monospace,monospace;font-size:11px;color:#334155;">
                  <span style="width:7px;height:7px;border-radius:50%;background:#10B981;display:inline-block;"></span>
                  <span>PostgreSQL &harr; ERP &harr; Dispatch Live Sync (12ms)</span>
                </div>
              </div>
            </div>
            <span class="rel-action"><span>Explore Custom ERP</span>{svg("arrow-up-right")}</span>
          </a>

          <!-- Card 3: Payroll Automation Platform (High-Trust Compliance) -->
          <a href="/products/payroll-automation" class="sv-rel-card is-compliance rv">
            <div>
              <span class="rel-tag">{svg("shield")} PRODUCT &bull; UAE WPS COMPLIANT</span>
              <h3>Payroll Automation Platform</h3>
              <p>Engineered specifically for UAE labor law, Ministry of Human Resources (MOHRE) compliance, and 1-click SIF file generation.</p>
              <div class="rel-mockup">
                <div style="display:flex;align-items:center;gap:6px;font-size:11.5px;font-weight:600;color:#047857;">
                  {svg("badge-check")}
                  <span>1-Click SIF File Generated &bull; 100% Validated</span>
                </div>
              </div>
            </div>
            <span class="rel-action"><span>View Payroll Software</span>{svg("arrow-up-right")}</span>
          </a>
        </div>'''

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
              <a href="/contact" class="btn btn-primary"><span>Book a Free Automation Audit</span>{arrow}</a>
              <a href="https://wa.me/97145770725" target="_blank" rel="noopener" class="btn btn-ghost"><span>Chat on WhatsApp</span></a>
            </div>
            <div class="sv-points">{points}</div>
          </div>

          <div class="sv-visual" aria-hidden="true">
            <div class="sv-console">
              <div class="sv-console-bar"><i></i><i></i><i></i><span>agent / invoice-pipeline.py</span><span class="live">Live</span></div>
              <div class="sv-flow">
{nodes}              </div>
              <div class="sv-progress"><span></span></div>
            </div>
            <div class="sv-float f1">{svg("shield")}<div>Human approval<small>for exceptions only</small></div></div>
            <div class="sv-float f2">{svg("clock")}<div>Runs 24/7<small>incl. weekends</small></div></div>
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
            <h2>Automation that executes the work, not just reports on it</h2>
          </div>
          <p>Production-grade agent architecture engineered around how UAE enterprises actually operate in Dubai and across the GCC.</p>
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
            <div class="eyebrow">Use Cases by Department</div>
            <h2>Where UAE Teams Start Automating</h2>
          </div>
          <p>Select a department below to explore how custom autonomous agents transform day-to-day operations.</p>
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
          <p>The commercial metrics we engineer and guarantee every automation against.</p>
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
            <h3>Have a custom workflow in mind?</h3>
            <p>Talk directly with an automation engineer in Port Saeed, Dubai. We reply within one business day.</p>
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
          <p>Connect your automated workflows across our unified digital and software ecosystem.</p>
        </div>
{related_html}
      </div>
    </section>

    {render_cta_band("Ready to Hand Repetitive Work to AI?", "Book a free automation audit with our Port Saeed team. We'll map your workflows and show you where AI pays back fastest.")}
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

#!/usr/bin/env python3
"""
TOCO Technologies — Service page template v2 (premium layout).

Currently applied ONLY to /services/ai-automation as a design preview.
To roll it out to every service, add the slug to V2_SLUGS and give it an
entry in EXTRA (before/after, use cases, timeline durations, hero points).
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
        "pill": "AI Automation",
        "pill_note": "Agents that work inside your systems",
        "h1_html": 'AI Automation &amp; <span class="grad-text">Autonomous Agents</span> for Dubai Businesses',
        "hero_points": ["Human-in-the-loop approvals", "UAE data residency options", "30-day post-launch warranty"],
        "integrations": ["OpenAI", "WhatsApp Business", "Zoho", "HubSpot", "Microsoft 365", "Google Workspace", "PostgreSQL", "AWS UAE"],
        "console": [
            ("file-text", "Invoice received", "accounts@supplier.ae · PDF", "done", "Done"),
            ("search", "Data extracted", "Vendor, TRN, line items, 5% VAT", "done", "Done"),
            ("layers", "Matched against ERP", "Checking PO and goods received", "run", "Running"),
            ("message", "Manager approval", "One-tap sign-off on WhatsApp", "wait", "Queued"),
        ],
        "big_title": "One orchestrator, many specialised agents",
        "big_desc": "We design a team of focused AI agents — each with one job, clear rules and a full audit log — coordinated by a single orchestrator that hands work between them and escalates to a person when something looks off.",
        "agents": [("Intake agent", "Reads emails & files", 92), ("Validation agent", "Applies your rules", 74), ("Posting agent", "Updates your ERP", 58)],
        "before": [
            "Staff re-type invoices, orders and forms into the ERP by hand",
            "Approvals are chased by email and phone calls",
            "Mistakes surface at month-end, when they are expensive to fix",
            "Work stops after office hours and over the weekend",
            "No clear record of who changed what, and when",
        ],
        "after": [
            "Documents are read, checked and posted automatically",
            "Approvals arrive on WhatsApp with one-tap sign-off",
            "Validation rules stop mismatches before anything is posted",
            "Agents keep working evenings, weekends and holidays",
            "Every action is logged for audit and compliance",
        ],
        "durations": ["Days 1–5", "Days 6–14", "Weeks 3–4", "Launch + 30 days"],
        "use_cases": [
            ("wallet", "Finance & accounts", ["Invoice capture & PO matching", "VAT and TRN checks", "Bank reconciliation", "Payment reminders"]),
            ("truck", "Logistics & operations", ["Delivery notes & POD capture", "Dispatch status updates", "Customs document checks", "Stock alerts"]),
            ("message", "Sales & customer service", ["Inbox triage & routing", "Quotation drafting", "CRM updates", "Follow-up sequences"]),
            ("users", "HR & administration", ["Visa & Emirates ID checks", "Onboarding packs", "Leave requests", "Policy Q&A assistant"]),
        ],
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
                    "address": {"@type": "PostalAddress", "streetAddress": "Port Saeed", "addressLocality": "Dubai", "addressCountry": "AE"},
                },
                "areaServed": [{"@type": "City", "name": "Dubai"}, {"@type": "City", "name": "Abu Dhabi"}, {"@type": "Country", "name": "United Arab Emirates"}],
            },
            make_breadcrumb_schema(crumbs),
            make_faq_schema(svc["faqs"]),
        ],
    }

    check = svg("check")
    arrow = '<svg class="arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

    points = "".join(f"<span>{check}{p}</span>" for p in x["hero_points"])

    nodes = ""
    for ico, title, sub, st, label in x["console"]:
        nodes += f'''                <div class="sv-node{' is-run' if st == 'run' else ''}">
                  <div class="sv-node-ico">{svg(ico)}</div>
                  <div><b>{title}</b><small>{sub}</small></div>
                  <span class="st {st}">{label}</span>
                </div>\n'''

    integrations = "".join(f"<span>{i}</span>" for i in x["integrations"])

    feats = svc["features"]
    agents = "".join(
        f'<div class="sv-agent"><b>{n}</b><small>{d}</small><div class="bar"><span style="width:{w}%"></span></div></div>'
        for n, d, w in x["agents"]
    )
    bento = f'''          <article class="sv-b big rv">
            <span class="ico-tile">{_ico(feats[0]["icon"])}</span>
            <h3>{x["big_title"]}</h3>
            <p>{x["big_desc"]}</p>
            <div class="sv-agents">{agents}</div>
          </article>\n'''
    for f in feats[1:]:
        bento += f'''          <article class="sv-b rv">
            <span class="ico-tile">{_ico(f["icon"])}</span>
            <h3>{f["title"]}</h3>
            <p>{f["desc"]}</p>
          </article>\n'''

    x_ico = svg("x")
    before = "".join(f'<li><span class="mk">{x_ico}</span>{t}</li>' for t in x["before"])
    after = "".join(f'<li><span class="mk">{check}</span>{t}</li>' for t in x["after"])

    steps = ""
    for i, s in enumerate(svc["steps"]):
        steps += f'''          <div class="sv-step rv">
            <div class="dot">{s["num"]}</div>
            <span class="when">{x["durations"][i]}</span>
            <h3>{s["title"]}</h3>
            <p>{s["desc"]}</p>
          </div>\n'''

    results = "".join(
        f'<div class="sv-res rv"><b>{b["metric"]}</b><h3>{b["title"]}</h3><p>{b["desc"]}</p></div>'
        for b in svc["benefits"]
    )

    small_check = svg("check")
    cases = ""
    for ico, title, items in x["use_cases"]:
        lis = "".join(f"<li>{small_check}{it}</li>" for it in items)
        cases += f'''          <article class="sv-case rv">
            <span class="ico-tile">{svg(ico)}</span>
            <h3>{title}</h3>
            <ul>{lis}</ul>
          </article>\n'''

    faqs = ""
    for i, q in enumerate(svc["faqs"]):
        first = i == 0
        faqs += f'''            <div class="faq-item{' open' if first else ''}">
              <button class="faq-q" type="button" aria-expanded="{'true' if first else 'false'}"><span>{q["q"]}</span><i></i></button>
              <div class="faq-a" style="{'max-height:260px;' if first else ''}"><div class="faq-a-inner"><p>{q["a"]}</p></div></div>
            </div>\n'''

    go = svg("arrow-up-right")
    related = ""
    for r in svc["related"]:
        kind = "Product" if r["url"].startswith("/products") else ("Case studies" if r["url"] == "/portfolio" else "Service")
        related += f'''          <a href="{r["url"]}" class="sv-rel rv">
            <div><small>{kind}</small><h3>{r["title"]}</h3><p>{r["desc"]}</p></div>
            <span class="go2">{go}</span>
          </a>\n'''

    html = f'''{render_head_tags(svc["title"], svc["meta_desc"], canonical, schema)}
{render_header("services")}

  <main id="main-content">
    <!-- HERO -->
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
              <div class="sv-console-bar"><i></i><i></i><i></i><span>agent / invoice-pipeline</span><span class="live">Live</span></div>
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

    <!-- INTEGRATIONS STRIP -->
    <section class="sv-strip theme-light">
      <div class="wrap">
        <span class="sv-strip-label">Connects with your stack</span>
        <div class="sv-strip-list">{integrations}</div>
      </div>
    </section>

    <!-- CAPABILITIES (BENTO) -->
    <section class="sv-sec theme-light">
      <div class="wrap">
        <div class="sv-head">
          <div>
            <div class="eyebrow">What we build</div>
            <h2>Automation that does the work, not just the reporting</h2>
          </div>
          <p>Production-grade agents and pipelines, designed around how your team already works in Dubai and across the UAE.</p>
        </div>
        <div class="sv-bento">
{bento}        </div>
      </div>
    </section>

    <!-- BEFORE / AFTER -->
    <section class="sv-sec theme-alt">
      <div class="wrap">
        <div class="sv-head center">
          <div>
            <div class="eyebrow">The difference</div>
            <h2>From manual hand-offs to hands-free operations</h2>
          </div>
          <p>What changes for your team on day one of going live.</p>
        </div>
        <div class="sv-compare">
          <div class="sv-col before rv">
            <h3><span class="sv-tag">Today</span>Manual process</h3>
            <ul>{before}</ul>
          </div>
          <div class="sv-col after rv">
            <h3><span class="sv-tag">With TOCO</span>AI-automated</h3>
            <ul>{after}</ul>
          </div>
        </div>
      </div>
    </section>

    <!-- PROCESS TIMELINE -->
    <section class="sv-sec theme-dark">
      <div class="wrap">
        <div class="sv-head">
          <div>
            <div class="eyebrow">How it works</div>
            <h2>Live in weeks, not quarters</h2>
          </div>
          <p>A phased rollout with a working pilot first, so you see real results before committing to the full build.</p>
        </div>
        <div class="sv-timeline">
{steps}        </div>
      </div>
    </section>

    <!-- RESULTS -->
    <section class="sv-sec theme-blue">
      <div class="wrap">
        <div class="sv-head">
          <div>
            <div class="eyebrow">Results</div>
            <h2>What automation changes in the numbers</h2>
          </div>
          <p>The outcomes we design and measure every automation against.</p>
        </div>
        <div class="sv-results">{results}</div>
      </div>
    </section>

    <!-- USE CASES -->
    <section class="sv-sec theme-light">
      <div class="wrap">
        <div class="sv-head">
          <div>
            <div class="eyebrow">Use cases</div>
            <h2>Where UAE teams start automating</h2>
          </div>
          <p>Common first projects, by department. Most clients begin with one workflow and expand from there.</p>
        </div>
        <div class="sv-cases">
{cases}        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="sv-sec theme-alt">
      <div class="wrap sv-faq">
        <div>
          <div class="eyebrow">FAQ</div>
          <h2 style="font-size:clamp(30px,3.6vw,46px);margin-top:14px;letter-spacing:-.03em;">Questions we hear from Dubai teams</h2>
          <div class="sv-help">
            <h3>Still have a question?</h3>
            <p>Talk to an engineer, not a salesperson. We reply within one business day.</p>
            <a href="https://wa.me/97145770725" target="_blank" rel="noopener" class="btn btn-primary btn-sm"><span>Message us on WhatsApp</span>{arrow}</a>
          </div>
        </div>
        <div class="faq-wrap">
{faqs}        </div>
      </div>
    </section>

    <!-- RELATED -->
    <section class="sv-sec theme-light">
      <div class="wrap">
        <div class="sv-head">
          <div>
            <div class="eyebrow">Keep exploring</div>
            <h2>Related services &amp; products</h2>
          </div>
        </div>
        <div class="sv-related">
{related}        </div>
      </div>
    </section>

    {render_cta_band("Ready to hand repetitive work to AI?", "Book a free automation audit with our Port Saeed team. We'll map your workflows and show you where AI pays back fastest.")}
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

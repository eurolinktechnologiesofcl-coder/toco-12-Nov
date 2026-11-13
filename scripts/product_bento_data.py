import sys
import os

from icons import ICONS

def get_svg(name):
    path = ICONS.get(name, "")
    return f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'

PRODUCT_BENTO = {
    "elearning-platform": {
        "pill": "PLATFORM CAPABILITIES",
        "h2": "Engineered for <em>High-Velocity</em><br>Business Execution",
        "sub": "Every feature designed to reduce friction, eliminate operational error, and accelerate commercial workflow.",
        "cards": [
            {
                "num": "01",
                "icon": "users",
                "title": "Student & Instructor Portals",
                "desc": "Course navigation, progress tracking, downloadable materials, and live Q&A — bilingual."
            },
            {
                "num": "02",
                "icon": "video",
                "title": "Adaptive Bitrate Video",
                "desc": "Buffer-free HLS streaming for Gulf connections — anti-piracy DRM and auto-captions included."
            },
            {
                "num": "03",
                "icon": "file-text",
                "title": "Quizzes & Timed Assessments",
                "desc": "MCQs, coding challenges, automated grading, and anti-cheating tab detection."
            },
            {
                "num": "04",
                "icon": "award",
                "title": "Digital Certificates & QR",
                "desc": "Auto-generated PDF certificates with cryptographic QR authentication for employers."
            },
            {
                "num": "05",
                "icon": "credit-card",
                "title": "UAE Payment Gateways",
                "desc": "Apple Pay, Stripe, Tabby — course subscriptions and team seats with UAE VAT billing."
            },
            {
                "num": "06",
                "icon": "globe",
                "title": "Bilingual Arabic & English",
                "desc": "Full RTL Arabic mirroring, localized content, and dual-language assessment across the GCC."
            }
        ]
    },
    "interior-quote-automation": {
        "pill": "ESTIMATION CAPABILITIES",
        "h2": "Engineered for <em>High-Velocity</em><br>Fit-Out Proposals",
        "sub": "Every feature designed to eliminate quoting errors, accelerate client sign-offs, and protect profit margins.",
        "cards": [
            {
                "num": "01",
                "icon": "ruler",
                "title": "Room & Dimension Calculator",
                "desc": "Input room specs, wall finishes, and ceiling heights to compute exact material volumes instantly."
            },
            {
                "num": "02",
                "icon": "wallet",
                "title": "Dynamic Costing Engine",
                "desc": "Real-time pricing for UAE marbles, custom joinery, MEP fixtures, and subcontractor rates."
            },
            {
                "num": "03",
                "icon": "file-text",
                "title": "Instant Luxury Proposals",
                "desc": "One-click branded client quotation decks with 3D moodboards, itemized bills, and scopes."
            },
            {
                "num": "04",
                "icon": "pen",
                "title": "E-Sign & Milestone Checkout",
                "desc": "Clients configure finishes, sign digital contracts, and settle deposit milestones securely."
            },
            {
                "num": "05",
                "icon": "bar-chart",
                "title": "Estimator & Pipeline Analytics",
                "desc": "Track conversion rates, quote velocity, pending bids, and average fit-out contract values."
            },
            {
                "num": "06",
                "icon": "refresh",
                "title": "Direct ERP & Procurement Sync",
                "desc": "Approved proposals trigger automated purchase orders, supplier requisitions, and dispatch."
            }
        ]
    },
    "ai-erp-platform": {
        "pill": "ENTERPRISE CAPABILITIES",
        "h2": "Engineered for <em>Autonomous</em><br>Enterprise Operations",
        "sub": "Every feature designed to streamline procurement, automate dispatch, and maintain airtight compliance.",
        "cards": [
            {
                "num": "01",
                "icon": "bot",
                "title": "Inquiry-to-Order AI Parser",
                "desc": "AI automatically ingests client RFQs, validates warehouse stock, and creates sales orders."
            },
            {
                "num": "02",
                "icon": "bar-chart",
                "title": "Predictive Stock Telemetry",
                "desc": "Machine learning forecasts GCC seasonal demand, alerting procurement before stockouts."
            },
            {
                "num": "03",
                "icon": "truck",
                "title": "Autonomous Fleet Routing",
                "desc": "Dynamically bundle shipments and optimize multi-stop delivery routes across all 7 Emirates."
            },
            {
                "num": "04",
                "icon": "file-text",
                "title": "Automated UAE VAT Invoicing",
                "desc": "Instant FTA-compliant electronic VAT invoices matched against live bank reconciliations."
            },
            {
                "num": "05",
                "icon": "users",
                "title": "Role-Based Unified Portals",
                "desc": "Dedicated low-latency interfaces for executive suites, warehouse pick-pack, and field drivers."
            },
            {
                "num": "06",
                "icon": "lock",
                "title": "Immutable Audit Ledger",
                "desc": "Cryptographic audit trail tracking every price change, inventory adjustment, and sign-off."
            }
        ]
    },
    "payroll-automation": {
        "pill": "COMPLIANCE CAPABILITIES",
        "h2": "Engineered for <em>Zero-Error</em><br>UAE WPS Payroll",
        "sub": "Every feature designed to ensure MOHRE compliance, automate SIF generation, and safeguard salary disbursals.",
        "cards": [
            {
                "num": "01",
                "icon": "briefcase",
                "title": "1-Click UAE WPS SIF Export",
                "desc": "Generate and validate Ministry-compliant .SIF files for all UAE banks and exchange houses."
            },
            {
                "num": "02",
                "icon": "scale",
                "title": "MOHRE Gratuity Engine",
                "desc": "Automated end-of-service gratuity calculations compliant with UAE Federal Decree-Law No. 33."
            },
            {
                "num": "03",
                "icon": "calendar",
                "title": "Leave & Attendance Sync",
                "desc": "Track annual leaves, sick leaves, public holidays, and automated salary deductions."
            },
            {
                "num": "04",
                "icon": "file-text",
                "title": "Encrypted Digital Payslips",
                "desc": "Automated PDF payslip delivery to employee inboxes or private self-service mobile portals."
            },
            {
                "num": "05",
                "icon": "flag",
                "title": "Emiratisation GPSSA Pension",
                "desc": "Automated pension calculations and monthly filings for UAE national employees."
            },
            {
                "num": "06",
                "icon": "lock",
                "title": "Bank-Grade Security & Audit",
                "desc": "Role-based HR permissions, AES-256 encrypted salary ledgers, and tamper-proof logs."
            }
        ]
    },
    "analytics-tracking": {
        "pill": "TELEMETRY CAPABILITIES",
        "h2": "Engineered for <em>Sub-Second</em><br>Business Telemetry",
        "sub": "Every feature designed to unify multi-touch attribution, protect data privacy, and deliver real-time clarity.",
        "cards": [
            {
                "num": "01",
                "icon": "trending-up",
                "title": "Omnichannel Attribution",
                "desc": "Track touchpoints from Instagram ad to WhatsApp inquiry and closed enterprise contract."
            },
            {
                "num": "02",
                "icon": "lock",
                "title": "Cookieless Privacy Stack",
                "desc": "First-party server-side telemetry designed for strict GCC data privacy regulations."
            },
            {
                "num": "03",
                "icon": "zap",
                "title": "Sub-Second Live Telemetry",
                "desc": "Real-time active visitor stream, checkout velocity, and conversion drop-off counters."
            },
            {
                "num": "04",
                "icon": "flag",
                "title": "GCC Regional Insights",
                "desc": "Granular market telemetry across Dubai, Abu Dhabi, Riyadh, and GCC capitals."
            },
            {
                "num": "05",
                "icon": "plug",
                "title": "Lightweight <5KB Tracker",
                "desc": "Zero performance penalty with asynchronous single-line script preserving Core Web Vitals."
            },
            {
                "num": "06",
                "icon": "bar-chart",
                "title": "Executive KPI Dashboards",
                "desc": "Jargon-free business metrics focused purely on CAC, pipeline value, and net revenue."
            }
        ]
    },
    "real-estate-crm": {
        "pill": "BROKERAGE CAPABILITIES",
        "h2": "Engineered for <em>High-Velocity</em><br>Property Conversions",
        "sub": "Every feature designed to capture portal leads instantly, sync WhatsApp interactions, and close deals faster.",
        "cards": [
            {
                "num": "01",
                "icon": "home",
                "title": "Portal Lead Ingestion",
                "desc": "Direct webhook ingestion from Bayut and Property Finder with instant 30-second lead routing."
            },
            {
                "num": "02",
                "icon": "message",
                "title": "WhatsApp Conversation Log",
                "desc": "Synchronize buyer WhatsApp conversations directly to property deals without screenshots."
            },
            {
                "num": "03",
                "icon": "map",
                "title": "Off-Plan Inventory Matrix",
                "desc": "Interactive floor plans, payment schedules, developer brochures, and live unit availability."
            },
            {
                "num": "04",
                "icon": "target",
                "title": "AI Buyer-to-Unit Matchmaker",
                "desc": "Match registered buyer budgets and target communities against available inventory."
            },
            {
                "num": "05",
                "icon": "briefcase",
                "title": "Commission & Pipeline Split",
                "desc": "Manage Form A/B workflows, trustee appointments, and broker commission splits."
            },
            {
                "num": "06",
                "icon": "smartphone",
                "title": "Mobile Broker Companion",
                "desc": "Field-ready iOS & Android app for agents to log showings and send brochures instantly."
            }
        ]
    }
}

def render_bento_capabilities(slug):
    data = PRODUCT_BENTO.get(slug)
    if not data:
        return ""

    cards_html = ""
    for card in data["cards"]:
        svg_code = get_svg(card["icon"])
        cards_html += f'''          <!-- Card {card["num"]} -->
          <div class="cap-card">
            <div class="cap-icon">
              {svg_code}
            </div>
            <span class="cap-num">{card["num"]}</span>
            <h3>{card["title"]}</h3>
            <p>{card["desc"]}</p>
          </div>\n'''

    return f'''    <!-- Platform Capabilities: Modern 2-Column Bento Grid -->
    <section class="sec-capability-thread" id="capabilities">
      <div class="wrap">
        <div class="cap-header">
          <div class="cap-pill">
            <span class="cap-pill-dot"></span>
            {data["pill"]}
          </div>
          <h2>{data["h2"]}</h2>
          <p>{data["sub"]}</p>
        </div>

        <div class="cap-bento">
{cards_html}        </div>
      </div>
    </section>'''

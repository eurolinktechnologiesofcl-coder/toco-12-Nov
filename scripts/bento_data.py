#!/usr/bin/env python3
"""
Bespoke Asymmetric Bento Grid & Page Metadata for All 10 Services
TOCO Technologies — Dubai, UAE
"""

from icons import svg

SERVICE_META = {
    "ai-automation": {
        "console_file": "agent / invoice-pipeline.py",
        "hero_cta": "Book a Free Automation Audit",
        "float1": ("shield", "Human approval", "for exceptions only"),
        "float2": ("clock", "Runs 24/7", "incl. weekends"),
        "cap_heading": "Automation that executes the work, not just reports on it",
        "cap_sub": "Production-grade agent architecture engineered around how UAE enterprises actually operate in Dubai and across the GCC.",
        "studio_heading": "Where UAE Teams Start Automating",
        "studio_sub": "Select a department below to explore how custom autonomous agents transform day-to-day operations.",
        "cta_title": "Ready to Hand Repetitive Work to AI?",
        "cta_sub": "Book a free automation audit with our Port Saeed team. We'll map your workflows and show you where AI pays back fastest.",
        "faq_help_title": "Have a custom workflow in mind?",
        "faq_help_desc": "Talk directly with an automation engineer in Port Saeed, Dubai. We reply within one business day.",
    },
    "ai-business-automation": {
        "console_file": "agent / lead-conversion.py",
        "hero_cta": "Book a Sales Conversion Audit",
        "float1": ("zap", "18s Response", "Average WhatsApp speed"),
        "float2": ("trending-up", "3.2x Booking Rate", "Verified conversion lift"),
        "cap_heading": "Conversion systems that turn high-intent leads into closed business",
        "cap_sub": "Autonomous lead capture, qualification models, and instant scheduling engineered for Dubai sales velocity.",
        "studio_heading": "Where UAE Teams Accelerate Conversions",
        "studio_sub": "Select a channel below to explore how autonomous conversion agents qualify and book deals around the clock.",
        "cta_title": "Ready to Convert High-Value UAE Inquiries Faster?",
        "cta_sub": "Schedule a 20-minute discovery consultation with our Dubai growth team. We'll show you where deals are dropping off.",
        "faq_help_title": "Want to automate your lead pipeline?",
        "faq_help_desc": "Talk with an AI conversion specialist in Port Saeed, Dubai. We reply within one business day.",
    },
    "mobile-app-development": {
        "console_file": "build / flutter-pipeline.dart",
        "hero_cta": "Schedule App Architecture Call",
        "float1": ("smartphone", "120Hz Flutter", "Native ARM64 code"),
        "float2": ("shield", "100% Code Ownership", "Zero vendor lock-in"),
        "cap_heading": "Engineering responsive, high-performance mobile software",
        "cap_sub": "Cross-platform Flutter and native mobile architecture built for high concurrency and sub-second responsiveness in Dubai.",
        "studio_heading": "Mobile Engineering Disciplines & Use Cases",
        "studio_sub": "Select an application category below to explore how purpose-built mobile software accelerates operational performance.",
        "cta_title": "Ready to Build Your iOS & Android Mobile Platform?",
        "cta_sub": "Talk directly with our Dubai senior mobile architects. We'll review your feature scope and deliver a phased sprint roadmap.",
        "faq_help_title": "Planning a mobile app in Dubai?",
        "faq_help_desc": "Connect directly with our mobile engineering leads in Port Saeed. We reply within one business day.",
    },
    "website-and-software-development": {
        "console_file": "deploy / edge-worker.ts",
        "hero_cta": "Request Web Architecture Review",
        "float1": ("zap", "< 380ms TTFB", "Cloudflare UAE edge"),
        "float2": ("badge-check", "99/100 Lighthouse", "Full Core Web Vitals pass"),
        "cap_heading": "Sub-second web platforms engineered for maximum conversions",
        "cap_sub": "Static edge architecture, zero-dependency engineering, and headless portals built for UAE enterprise stability.",
        "studio_heading": "Web Platform Disciplines & Architecture",
        "studio_sub": "Select a platform discipline below to explore how sub-second engineering eliminates technical debt and drives results.",
        "cta_title": "Ready for a Sub-Second Enterprise Web Platform?",
        "cta_sub": "Book an architecture review with our Port Saeed team. We'll audit your current performance and map a modern static-edge stack.",
        "faq_help_title": "Need a high-performance web platform?",
        "faq_help_desc": "Talk with our senior web engineering architects in Port Saeed, Dubai. We reply within one business day.",
    },
    "digital-marketing": {
        "console_file": "campaigns / google-ads-roas.py",
        "hero_cta": "Request Free PPC Performance Audit",
        "float1": ("target", "Google Partner", "Certified PPC team"),
        "float2": ("trending-up", "4.8x ROAS", "Attributed revenue"),
        "cap_heading": "Precision paid media engineered for high-intent UAE customer acquisition",
        "cap_sub": "Data-driven Google Search, Meta ads, and server-side GA4 attribution that eliminates wasted ad spend across Dubai and GCC.",
        "studio_heading": "Paid Acquisition Channels by Strategy",
        "studio_sub": "Select a paid media discipline below to explore how algorithmic targeting and closed-loop attribution scale revenue.",
        "cta_title": "Ready to Stop Wasting Ad Spend on Low-Intent Clicks?",
        "cta_sub": "Request a complimentary Google Ads and paid media audit from our Dubai team. We'll uncover high-converting keyword opportunities.",
        "faq_help_title": "Want higher ROAS on UAE paid ads?",
        "faq_help_desc": "Consult with a Google-certified paid acquisition director in Port Saeed, Dubai. We reply within one business day.",
    },
    "seo": {
        "console_file": "crawler / search-console-audit.ts",
        "hero_cta": "Request Technical SEO Audit",
        "float1": ("search", "Page 1 Google", "Dubai high-intent terms"),
        "float2": ("map-pin", "Maps 3-Pack", "Local search dominance"),
        "cap_heading": "Dominating high-intent search queries across Dubai and the GCC",
        "cap_sub": "Forensic crawl architecture, Core Web Vitals engineering, and semantic entity SEO that Google ranks on page one.",
        "studio_heading": "Search Optimization Disciplines & Results",
        "studio_sub": "Select an SEO discipline below to explore how technical precision and local authority generate permanent organic growth.",
        "cta_title": "Ready to Dominate Google Search Across Dubai & UAE?",
        "cta_sub": "Request a comprehensive technical and local SEO audit from our Port Saeed team. We'll map your path to page-one organic rankings.",
        "faq_help_title": "Want page 1 Google rankings in Dubai?",
        "faq_help_desc": "Speak with our technical SEO director in Port Saeed, Dubai. We reply within one business day.",
    },
    "ecommerce-development": {
        "console_file": "store / checkout-pipeline.ts",
        "hero_cta": "Schedule E-Commerce Architecture Call",
        "float1": ("credit-card", "Tabby & Tamara", "4-Pay installment ready"),
        "float2": ("truck", "Direct Courier API", "Aramex & Fetchr auto labels"),
        "cap_heading": "High-converting storefronts built for GCC shopping behaviors",
        "cap_sub": "Shopify Plus and headless storefronts with Tabby BNPL, UAE payment gateways, bilingual Arabic RTL, and courier automation.",
        "studio_heading": "E-Commerce Capabilities & Architecture",
        "studio_sub": "Select an e-commerce model below to explore how specialized checkout architecture and courier integrations maximize revenue.",
        "cta_title": "Ready to Launch a High-Converting UAE Storefront?",
        "cta_sub": "Consult with our Dubai e-commerce architects. We'll map your payment gateways, BNPL integration, and shipping automation.",
        "faq_help_title": "Building an online store in Dubai?",
        "faq_help_desc": "Talk with our e-commerce solutions architects in Port Saeed, Dubai. We reply within one business day.",
    },
    "erp-and-custom-software": {
        "console_file": "erp / core-dispatch.py",
        "hero_cta": "Book ERP Architecture Consultation",
        "float1": ("building", "Zero SaaS Tax", "100% full IP ownership"),
        "float2": ("shield", "UAE VAT & WPS", "FTA compliant invoicing"),
        "cap_heading": "Enterprise software architecture engineered for operational mastery",
        "cap_sub": "Bespoke dispatch suites, automated 3-way matching, live inventory, and UAE statutory compliance without monthly SaaS tax.",
        "studio_heading": "Enterprise ERP Modules & Workflows",
        "studio_sub": "Select an operational module below to explore how custom software architecture unifies your business operations.",
        "cta_title": "Ready to Own Your Business Software Without Monthly SaaS Tax?",
        "cta_sub": "Book a systems architecture consultation in Port Saeed, Dubai. We'll map your operational workflows and build a prototype.",
        "faq_help_title": "Need custom business software in Dubai?",
        "faq_help_desc": "Consult directly with a senior ERP architect in Port Saeed, Dubai. We reply within one business day.",
    },
    "social-media-management": {
        "console_file": "social / content-scheduler.py",
        "hero_cta": "Request Social Strategy Proposal",
        "float1": ("video", "Studio Video Reels", "4K filmed in Dubai"),
        "float2": ("users", "B2B LinkedIn", "+340 executive network/mo"),
        "cap_heading": "Strategic social positioning that commands B2B trust across the UAE",
        "cap_sub": "Executive LinkedIn leadership, high-production video reels, and native bilingual Arabic copywriting that drives commercial authority.",
        "studio_heading": "Social Media Channels & Creative Formats",
        "studio_sub": "Select a content channel below to explore how executive positioning and cinematic production establish regional prestige.",
        "cta_title": "Ready to Command B2B Authority Across the UAE?",
        "cta_sub": "Schedule a social media strategy consultation with our Dubai creative team. We'll design your 90-day executive growth calendar.",
        "faq_help_title": "Want to elevate your UAE brand presence?",
        "faq_help_desc": "Speak with a social media director in Port Saeed, Dubai. We reply within one business day.",
    },
    "branding-and-ui-ux-design": {
        "console_file": "design / tokens-and-system.figma",
        "hero_cta": "Book Design Discovery Session",
        "float1": ("pen-tool", "Figma Design System", "420+ tokenized components"),
        "float2": ("globe", "Bilingual RTL", "Native Arabic type pairing"),
        "cap_heading": "Design systems and corporate identities that command market leadership",
        "cap_sub": "Figma component systems, usability-tested UX flows, bilingual Arabic RTL typography, and comprehensive corporate guidelines.",
        "studio_heading": "Design Disciplines & Brand Deliverables",
        "studio_sub": "Select a design discipline below to explore how structured design systems and usability testing transform digital products.",
        "cta_title": "Ready to Elevate Your Brand Above the UAE Competition?",
        "cta_sub": "Discuss your brand identity and product UI/UX with our Dubai design team. We'll map a full Figma design system for your business.",
        "faq_help_title": "Starting a brand or product redesign?",
        "faq_help_desc": "Consult with our design director in Port Saeed, Dubai. We reply within one business day.",
    },
}


def get_bento_html(slug):
    """Generate bespoke 4-card asymmetric bento grid for any service slug."""
    check = svg("check")
    
    if slug == "ai-automation":
        return f'''        <div class="sv-bento-grid">
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
                <div class="ocr-status ok">{check} Validated FTA Registry</div>
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

    elif slug == "ai-business-automation":
        return f'''        <div class="sv-bento-grid">
          <!-- Bento 1: Featured Inbound Lead Speed -->
          <article class="bento-card bento-wide is-featured rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("zap")}REAL-TIME CONVERSIONS</span>
              <h3>Sub-60s Inbound Lead Qualification</h3>
              <p>Autonomous sales concierge agents intercept incoming WhatsApp and web leads instantly. Evaluates buying intent, budget, and project scope before routing qualified prospects to senior engineers.</p>
            </div>
            <div class="bento-agent-telemetry">
              <div class="agent-bar-row">
                <div class="agent-info"><b>Lead Intake Speed</b><small>18s median response time across WhatsApp</small></div>
                <div class="agent-track"><span style="width: 98%;"></span></div>
                <span class="agent-pct">98% active</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Intent Qualification</b><small>Budget &amp; timeline scored automatically</small></div>
                <div class="agent-track"><span style="width: 86%;"></span></div>
                <span class="agent-pct">86% active</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Calendar Booking</b><small>WhatsApp calendar slots confirmed</small></div>
                <div class="agent-track"><span style="width: 74%;"></span></div>
                <span class="agent-pct">74% active</span>
              </div>
            </div>
          </article>

          <!-- Bento 2: WhatsApp Cloud API -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("message")}WHATSAPP CONVERSIONS</span>
              <h3>Official WhatsApp Cloud API</h3>
              <p>Bilingual Arabic &amp; English conversational flows with verified green-tick sender profile.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="ocr-preview">
                <div class="ocr-tag">WHATSAPP LIVE &bull; +971 4 577 0725</div>
                <div class="ocr-val">Intent: Custom ERP &bull; Tier: Enterprise</div>
                <div class="ocr-status ok">{check} 18s Response Delivered</div>
              </div>
            </div>
          </article>

          <!-- Bento 3: Instant Booking -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("calendar")}INSTANT BOOKING</span>
              <h3>Zero-Friction Scheduling</h3>
              <p>Prospects choose open calendar slots directly inside WhatsApp without email back-and-forth.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="wa-preview">
                <div class="wa-msg">Slot confirmed: Senior Engineer Intro &bull; Thursday 2:00 PM GST</div>
                <div class="wa-actions">
                  <span class="wa-btn ok">Calendar Synced</span>
                  <span class="wa-btn flag">Details</span>
                </div>
              </div>
            </div>
          </article>

          <!-- Bento 4: CRM Sync -->
          <article class="bento-card bento-wide is-security rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("shield")}ENTERPRISE CRM COMPLIANCE</span>
              <h3>Bi-Directional CRM &amp; Pipeline Synchronization</h3>
              <p>Every conversation, lead score, and booked consultation is instantly synchronized to HubSpot, Zoho, Salesforce, or your custom ERP with zero human re-keying and full audit logging.</p>
            </div>
            <div class="security-cluster">
              <div class="sec-pill">{svg("zap")}<span>HubSpot &amp; Zoho REST Sync</span></div>
              <div class="sec-pill">{svg("lock")}<span>GDPR &amp; UAE PDP Compliant</span></div>
              <div class="sec-pill">{svg("shield")}<span>Zero Human Re-keying</span></div>
              <div class="sec-pill">{svg("users")}<span>Instant WhatsApp Handoff</span></div>
            </div>
          </article>
        </div>'''

    elif slug == "mobile-app-development":
        return f'''        <div class="sv-bento-grid">
          <!-- Bento 1: Cross-Platform Performance -->
          <article class="bento-card bento-wide is-featured rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("smartphone")}CROSS-PLATFORM PERFORMANCE</span>
              <h3>Flutter &amp; Native iOS/Android Core</h3>
              <p>We build single-codebase Flutter applications compiled directly to native ARM64 machine code, achieving buttery 120Hz refresh rates and identical UI precision across iPhone and Android devices.</p>
            </div>
            <div class="bento-agent-telemetry">
              <div class="agent-bar-row">
                <div class="agent-info"><b>iOS Engine</b><small>Swift &amp; Metal acceleration</small></div>
                <div class="agent-track"><span style="width: 99%;"></span></div>
                <span class="agent-pct">120Hz smooth</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Android Engine</b><small>Kotlin &amp; Vulkan runtime</small></div>
                <div class="agent-track"><span style="width: 96%;"></span></div>
                <span class="agent-pct">60fps native</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>REST / GraphQL Sync</b><small>Sub-80ms payload delivery to ERP</small></div>
                <div class="agent-track"><span style="width: 88%;"></span></div>
                <span class="agent-pct">80ms latency</span>
              </div>
            </div>
          </article>

          <!-- Bento 2: Biometric Auth -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("lock")}BIOMETRIC SECURITY</span>
              <h3>Face ID &amp; Biometric Auth</h3>
              <p>Hardware-backed security enclave integration for instantaneous, friction-free customer authentication.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="ocr-preview">
                <div class="ocr-tag">SECURE ENCLAVE &bull; iOS 17+</div>
                <div class="ocr-val">Auth: Face ID Authenticated</div>
                <div class="ocr-status ok">{check} AES-256 Token Validated</div>
              </div>
            </div>
          </article>

          <!-- Bento 3: Apple Pay & Tabby -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("credit-card")}GCC PAYMENTS</span>
              <h3>Apple Pay &amp; Tabby BNPL</h3>
              <p>Seamless UAE checkout integration with 1-tap Apple Pay and interest-free split payments.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="wa-preview">
                <div class="wa-msg">Order Total: AED 1,450.00 &bull; 4x AED 362.50 via Tabby</div>
                <div class="wa-actions">
                  <span class="wa-btn ok">Apple Pay 1-Tap</span>
                  <span class="wa-btn flag">Tabby 4-Pay</span>
                </div>
              </div>
            </div>
          </article>

          <!-- Bento 4: Offline Caching -->
          <article class="bento-card bento-wide is-security rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("shield")}OFFLINE-FIRST ARCHITECTURE</span>
              <h3>Enterprise Offline Caching &amp; Background Sync</h3>
              <p>Built-in SQLite database caching allows your field technicians and delivery drivers to continue full operations inside basements, warehouses, and remote UAE locations with zero signal.</p>
            </div>
            <div class="security-cluster">
              <div class="sec-pill">{svg("database")}<span>SQLite Offline Delta Sync</span></div>
              <div class="sec-pill">{svg("lock")}<span>Encrypted Local Keychain</span></div>
              <div class="sec-pill">{svg("badge-check")}<span>App Store Approval Guarantee</span></div>
              <div class="sec-pill">{svg("users")}<span>100% Full Code Ownership</span></div>
            </div>
          </article>
        </div>'''

    elif slug == "website-and-software-development":
        return f'''        <div class="sv-bento-grid">
          <!-- Bento 1: Static Edge Architecture -->
          <article class="bento-card bento-wide is-featured rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("globe")}SUB-SECOND EDGE INFRASTRUCTURE</span>
              <h3>Static-First Edge Architecture</h3>
              <p>Sub-380ms Time-To-First-Byte (TTFB) delivered from Cloudflare Middle East edge nodes in Dubai and Abu Dhabi. Semantic HTML5, strict zero-dependency builds, and instant page transitions.</p>
            </div>
            <div class="bento-agent-telemetry">
              <div class="agent-bar-row">
                <div class="agent-info"><b>Edge Delivery</b><small>UAE CDN Edge Cache in Dubai</small></div>
                <div class="agent-track"><span style="width: 99%;"></span></div>
                <span class="agent-pct">318ms TTFB</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Core Web Vitals</b><small>LCP 1.1s &bull; CLS 0.00 &bull; INP 42ms</small></div>
                <div class="agent-track"><span style="width: 100%;"></span></div>
                <span class="agent-pct">100% green</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Security Gateway</b><small>Cloudflare Enterprise WAF &bull; Zero bloat</small></div>
                <div class="agent-track"><span style="width: 100%;"></span></div>
                <span class="agent-pct">0 vuln</span>
              </div>
            </div>
          </article>

          <!-- Bento 2: 99/100 Lighthouse -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("zap")}PERFORMANCE AUDIT</span>
              <h3>99/100 Google Lighthouse</h3>
              <p>Every template passes Google's Core Web Vitals with flawless accessibility and semantic SEO scores.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="ocr-preview">
                <div class="ocr-tag">PERFORMANCE: 99 / 100</div>
                <div class="ocr-val">LCP: 1.1s &bull; CLS: 0.00 &bull; INP: 42ms</div>
                <div class="ocr-status ok">{check} 100% Passing Google Audit</div>
              </div>
            </div>
          </article>

          <!-- Bento 3: Headless API -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("code")}ENTERPRISE STACK</span>
              <h3>Modern Headless Stacks</h3>
              <p>Clean TypeScript, Next.js, or static architecture paired with robust PostgreSQL and headless APIs.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="wa-preview">
                <div class="wa-msg">API Latency: 42ms &bull; Payload: 14KB &bull; 0 Dependencies</div>
                <div class="wa-actions">
                  <span class="wa-btn ok">REST API Live</span>
                  <span class="wa-btn flag">Zero Bloat</span>
                </div>
              </div>
            </div>
          </article>

          <!-- Bento 4: Zero Dependency Security -->
          <article class="bento-card bento-wide is-security rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("shield")}ZERO-DEPENDENCY SECURITY</span>
              <h3>Enterprise Security &amp; Zero Maintenance Overhead</h3>
              <p>Say goodbye to WordPress plugin vulnerabilities, database crashes, and slow shared hosting. Static edge architecture cannot be hacked, requires zero security patches, and handles unlimited traffic surges.</p>
            </div>
            <div class="security-cluster">
              <div class="sec-pill">{svg("shield")}<span>Zero WordPress Bloat</span></div>
              <div class="sec-pill">{svg("lock")}<span>Automated SSL &amp; DDoS Shield</span></div>
              <div class="sec-pill">{svg("globe")}<span>Arabic RTL Native Mirroring</span></div>
              <div class="sec-pill">{svg("badge-check")}<span>30-Day Launch Warranty</span></div>
            </div>
          </article>
        </div>'''

    elif slug == "digital-marketing":
        return f'''        <div class="sv-bento-grid">
          <!-- Bento 1: Google PPC Precision -->
          <article class="bento-card bento-wide is-featured rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("trending-up")}ALGORITHMIC PAID ACQUISITION</span>
              <h3>Intent-Driven Google Search &amp; Display PPC</h3>
              <p>We eliminate wasted ad spend by bidding exclusively on commercial-intent UAE search queries. Rigorous negative keyword hygiene, automated bid adjustments, and hyper-localized Dubai ad targeting.</p>
            </div>
            <div class="bento-agent-telemetry">
              <div class="agent-bar-row">
                <div class="agent-info"><b>Exact Match Share</b><small>Targeting high-intent UAE search queries</small></div>
                <div class="agent-track"><span style="width: 88%;"></span></div>
                <span class="agent-pct">88% share</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Ad Quality Score</b><small>10/10 Google rating on primary keywords</small></div>
                <div class="agent-track"><span style="width: 94%;"></span></div>
                <span class="agent-pct">10/10 score</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Wasted Click Waste</b><small>0% budget wasted on low-intent tourists</small></div>
                <div class="agent-track"><span style="width: 100%;"></span></div>
                <span class="agent-pct">0% waste</span>
              </div>
            </div>
          </article>

          <!-- Bento 2: Meta Funnels -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("target")}AUDIENCE RETARGETING</span>
              <h3>Meta &amp; Instagram Funnels</h3>
              <p>Multi-stage paid social campaigns engineered to capture attention and convert cold UAE audiences.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="ocr-preview">
                <div class="ocr-tag">ROAS ATTRIBUTED: 4.8X</div>
                <div class="ocr-val">CPL: AED 94.20 &bull; Verified Leads</div>
                <div class="ocr-status ok">{check} 3.5% CTR UAE Performance</div>
              </div>
            </div>
          </article>

          <!-- Bento 3: B2B LinkedIn -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("users")}B2B DEMAND GEN</span>
              <h3>LinkedIn Enterprise Outreach</h3>
              <p>Laser-focused B2B campaigns targeting CXOs, Directors, and procurement heads across the GCC.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="wa-preview">
                <div class="wa-msg">Target: UAE C-Suite / Owners &bull; 14 Enterprise Inquiries</div>
                <div class="wa-actions">
                  <span class="wa-btn ok">Verified Leads</span>
                  <span class="wa-btn flag">Scale Budget</span>
                </div>
              </div>
            </div>
          </article>

          <!-- Bento 4: Attribution -->
          <article class="bento-card bento-wide is-security rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("shield")}DATA ATTRIBUTION ACCURACY</span>
              <h3>Server-Side Tracking &amp; Full-Funnel Attribution</h3>
              <p>Server-side Google Tag Manager and GA4 pipelines bypass iOS 17 ad blockers and cookie expiration, passing offline CRM revenue back to ad algorithms for true closed-loop ROAS calculation.</p>
            </div>
            <div class="security-cluster">
              <div class="sec-pill">{svg("bar-chart")}<span>Server-Side GTM Setup</span></div>
              <div class="sec-pill">{svg("zap")}<span>Closed-Loop Offline CRM Sync</span></div>
              <div class="sec-pill">{svg("trending-up")}<span>Transparent AED Live Dashboard</span></div>
              <div class="sec-pill">{svg("badge-check")}<span>Google Partner Certified Team</span></div>
            </div>
          </article>
        </div>'''

    elif slug == "seo":
        return f'''        <div class="sv-bento-grid">
          <!-- Bento 1: Technical SEO -->
          <article class="bento-card bento-wide is-featured rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("search")}TECHNICAL SEO ARCHITECTURE</span>
              <h3>Forensic Crawl Architecture &amp; Core Web Vitals</h3>
              <p>We resolve technical crawl debt, indexation blocks, and canonical conflicts before building semantic topical authority across Google UAE. Fast, search-compliant HTML that Google ranks on page one.</p>
            </div>
            <div class="bento-agent-telemetry">
              <div class="agent-bar-row">
                <div class="agent-info"><b>Indexation Rate</b><small>Clean crawl budget &bull; 0 server errors</small></div>
                <div class="agent-track"><span style="width: 100%;"></span></div>
                <span class="agent-pct">100% indexed</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Core Web Vitals</b><small>LCP 1.1s &bull; CLS 0.00 &bull; INP 40ms</small></div>
                <div class="agent-track"><span style="width: 100%;"></span></div>
                <span class="agent-pct">100% green</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Search Visibility</b><small>Topical cluster organic growth</small></div>
                <div class="agent-track"><span style="width: 92%;"></span></div>
                <span class="agent-pct">+218% growth</span>
              </div>
            </div>
          </article>

          <!-- Bento 2: Local Search -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("map-pin")}LOCAL SEARCH DOMINANCE</span>
              <h3>Google Maps 3-Pack Supremacy</h3>
              <p>Geo-targeted Google Business Profile optimization and UAE citation building that puts you on top.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="ocr-preview">
                <div class="ocr-tag">DUBAI LOCAL SEARCH #1</div>
                <div class="ocr-val">Maps 3-Pack: Position #2</div>
                <div class="ocr-status ok">{check} LocalBusiness Schema Live</div>
              </div>
            </div>
          </article>

          <!-- Bento 3: Rich Snippets -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("file-text")}RICH SERP SNIPPETS</span>
              <h3>Structured Data &amp; Schema.org</h3>
              <p>Full JSON-LD implementation delivering expandable FAQ accordions and breadcrumb paths in SERPs.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="wa-preview">
                <div class="wa-msg">Rich Snippet: FAQ Accordion Active &bull; 0 Validation Errors</div>
                <div class="wa-actions">
                  <span class="wa-btn ok">3 Snippets Live</span>
                  <span class="wa-btn flag">Verified</span>
                </div>
              </div>
            </div>
          </article>

          <!-- Bento 4: Backlinks -->
          <article class="bento-card bento-wide is-security rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("shield")}ETHICAL WHITE-HAT COMPLIANCE</span>
              <h3>High-Authority GCC Editorial Backlinks</h3>
              <p>We secure contextual, high-DA backlinks from established UAE media, business directories, and regional industry publications — building permanent domain authority that algorithm updates cannot wipe out.</p>
            </div>
            <div class="security-cluster">
              <div class="sec-pill">{svg("badge-check")}<span>100% White-Hat Editorial Links</span></div>
              <div class="sec-pill">{svg("globe")}<span>Semantic UAE Entity Graph</span></div>
              <div class="sec-pill">{svg("search")}<span>Bilingual Arabic &amp; English SEO</span></div>
              <div class="sec-pill">{svg("trending-up")}<span>Weekly Keyword Rank Tracking</span></div>
            </div>
          </article>
        </div>'''

    elif slug == "ecommerce-development":
        return f'''        <div class="sv-bento-grid">
          <!-- Bento 1: High-Volume Catalog -->
          <article class="bento-card bento-wide is-featured rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("shopping-bag")}HIGH-CONVERSION STOREFRONT</span>
              <h3>Sub-Second Catalog &amp; High-Volume Checkout</h3>
              <p>High-converting digital storefronts built on Shopify Plus or custom headless stacks with sub-second product page loads, instant inventory lookup, and conversion-optimized 1-page checkout flows.</p>
            </div>
            <div class="bento-agent-telemetry">
              <div class="agent-bar-row">
                <div class="agent-info"><b>Storefront Speed</b><small>Sub-1.2s LCP on mobile network</small></div>
                <div class="agent-track"><span style="width: 98%;"></span></div>
                <span class="agent-pct">1.2s LCP</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Checkout Conversion</b><small>Above average UAE e-commerce CVR</small></div>
                <div class="agent-track"><span style="width: 94%;"></span></div>
                <span class="agent-pct">4.8% CVR</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Cart Abandonment</b><small>Reduced via Tabby &amp; Tamara split payments</small></div>
                <div class="agent-track"><span style="width: 86%;"></span></div>
                <span class="agent-pct">-35% drop</span>
              </div>
            </div>
          </article>

          <!-- Bento 2: Tabby & Tamara -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("credit-card")}LOCALIZED PAYMENT</span>
              <h3>Tabby &amp; Tamara 4-Pay BNPL</h3>
              <p>Interest-free installment checkouts that boost average order values across Dubai and the GCC.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="ocr-preview">
                <div class="ocr-tag">CART TOTAL: AED 1,200.00</div>
                <div class="ocr-val">4x Payments of AED 300 / mo</div>
                <div class="ocr-status ok">{check} Tabby BNPL Pre-Approved</div>
              </div>
            </div>
          </article>

          <!-- Bento 3: Courier APIs -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("truck")}LOGISTICS INTEGRATION</span>
              <h3>Live Courier Shipping APIs</h3>
              <p>Real-time rates and automated shipping label generation with Aramex, Fetchr, and SMSA.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="wa-preview">
                <div class="wa-msg">Shipping: Aramex Express &bull; Tracking #ARX-9941 Generated</div>
                <div class="wa-actions">
                  <span class="wa-btn ok">Auto Label</span>
                  <span class="wa-btn flag">Tracked</span>
                </div>
              </div>
            </div>
          </article>

          <!-- Bento 4: PCI-DSS Compliance -->
          <article class="bento-card bento-wide is-security rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("shield")}FINANCIAL COMPLIANCE</span>
              <h3>UAE Central Bank &amp; PCI-DSS Compliant Payments</h3>
              <p>Native integration with PayTabs, Network International, Stripe UAE, and Apple Pay — with automated 5% UAE VAT invoice generation and WPS/corporate tax compliance built-in.</p>
            </div>
            <div class="security-cluster">
              <div class="sec-pill">{svg("lock")}<span>PCI-DSS Level 1 Gateway</span></div>
              <div class="sec-pill">{svg("file-text")}<span>Automated 5% VAT Invoicing</span></div>
              <div class="sec-pill">{svg("globe")}<span>Arabic RTL Native Storefront</span></div>
              <div class="sec-pill">{svg("refresh")}<span>Real-Time ERP &amp; POS Sync</span></div>
            </div>
          </article>
        </div>'''

    elif slug == "erp-and-custom-software":
        return f'''        <div class="sv-bento-grid">
          <!-- Bento 1: Enterprise Core -->
          <article class="bento-card bento-wide is-featured rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("building")}ENTERPRISE CORE ARCHITECTURE</span>
              <h3>Bespoke Clean-Code ERP Architecture</h3>
              <p>Tailored business management software engineered around your specific operational workflows. Eliminate repetitive SaaS subscription fees and gain 100% full source code ownership of your intellectual property.</p>
            </div>
            <div class="bento-agent-telemetry">
              <div class="agent-bar-row">
                <div class="agent-info"><b>Core Database</b><small>PostgreSQL high-concurrency connection pool</small></div>
                <div class="agent-track"><span style="width: 99%;"></span></div>
                <span class="agent-pct">12ms p50</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>REST API Pipeline</b><small>Sub-60ms execution across all endpoints</small></div>
                <div class="agent-track"><span style="width: 98%;"></span></div>
                <span class="agent-pct">60ms latency</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Automated Sync</b><small>Real-time fleet &amp; inventory telemetry</small></div>
                <div class="agent-track"><span style="width: 92%;"></span></div>
                <span class="agent-pct">92% auto</span>
              </div>
            </div>
          </article>

          <!-- Bento 2: 3-Way Match -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("file-text")}3-WAY AUTOMATED MATCH</span>
              <h3>Automated PO-GRN-Invoice Reconciliation</h3>
              <p>Instantly match incoming invoices against purchase orders and warehouse receipts with zero manual data entry.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="ocr-preview">
                <div class="ocr-tag">PO #9481 &bull; AL FUTTAIM</div>
                <div class="ocr-val">Reconciliation: 100% Item Match</div>
                <div class="ocr-status ok">{check} Approved for Ledger Posting</div>
              </div>
            </div>
          </article>

          <!-- Bento 3: Dispatch Console -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("truck")}DISPATCH CONSOLE</span>
              <h3>Live Fleet &amp; Delivery Dispatch</h3>
              <p>Interactive dispatch console with real-time GPS tracking, automated manifest generation, and digital POD.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="wa-preview">
                <div class="wa-msg">28 Vehicles Live in Dubai &bull; 91 Deliveries Completed Today</div>
                <div class="wa-actions">
                  <span class="wa-btn ok">Assign Driver</span>
                  <span class="wa-btn flag">Capture POD</span>
                </div>
              </div>
            </div>
          </article>

          <!-- Bento 4: Statutory Compliance -->
          <article class="bento-card bento-wide is-security rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("shield")}UAE STATUTORY COMPLIANCE</span>
              <h3>UAE VAT Invoicing &amp; WPS Payroll Compliance</h3>
              <p>Purpose-built for UAE Federal Tax Authority (FTA) rules with automated TRN validation, 5% VAT calculations, and one-click SIF file generation for Ministry of Human Resources WPS salary transfers.</p>
            </div>
            <div class="security-cluster">
              <div class="sec-pill">{svg("badge-check")}<span>FTA TRN Real-Time Validation</span></div>
              <div class="sec-pill">{svg("wallet")}<span>One-Click WPS SIF Generation</span></div>
              <div class="sec-pill">{svg("lock")}<span>Granular Role-Based Access (RBAC)</span></div>
              <div class="sec-pill">{svg("shield")}<span>100% Source Code Ownership</span></div>
            </div>
          </article>
        </div>'''

    elif slug == "social-media-management":
        return f'''        <div class="sv-bento-grid">
          <!-- Bento 1: B2B Thought Leadership -->
          <article class="bento-card bento-wide is-featured rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("megaphone")}EXECUTIVE B2B POSITIONING</span>
              <h3>Strategic Thought Leadership &amp; LinkedIn Dominance</h3>
              <p>We position your enterprise executives as industry authorities on LinkedIn across Dubai, Abu Dhabi, and the GCC through high-substance articles, data carousels, and strategic commentary.</p>
            </div>
            <div class="bento-agent-telemetry">
              <div class="agent-bar-row">
                <div class="agent-info"><b>LinkedIn Reach</b><small>14,800+ impressions per month</small></div>
                <div class="agent-track"><span style="width: 96%;"></span></div>
                <span class="agent-pct">14.8k reach</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Executive Network Growth</b><small>+340 CXO &amp; Director connections / month</small></div>
                <div class="agent-track"><span style="width: 92%;"></span></div>
                <span class="agent-pct">+340 execs</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>B2B Inquiries</b><small>High-intent inbound consultations generated</small></div>
                <div class="agent-track"><span style="width: 84%;"></span></div>
                <span class="agent-pct">14 leads/mo</span>
              </div>
            </div>
          </article>

          <!-- Bento 2: Video Reels -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("video")}SHORT-FORM REELS</span>
              <h3>High-Production Video Reels</h3>
              <p>Cinematic 30-second studio and on-site video reels edited specifically for Instagram and TikTok algorithm reach.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="ocr-preview">
                <div class="ocr-tag">REEL ENGAGEMENT: 7.2%</div>
                <div class="ocr-val">28,420 Views &bull; 342 Saves</div>
                <div class="ocr-status ok">{check} Above UAE Average (2.8%)</div>
              </div>
            </div>
          </article>

          <!-- Bento 3: Content Calendar -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("calendar")}SCHEDULED AUTOMATION</span>
              <h3>90-Day Content Calendars</h3>
              <p>Structured monthly publishing calendars approved in advance with optimal posting times for the UAE audience.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="wa-preview">
                <div class="wa-msg">Queue: 36 Posts / Month &bull; Mon/Wed/Fri Cadence</div>
                <div class="wa-actions">
                  <span class="wa-btn ok">Client Approved</span>
                  <span class="wa-btn flag">Scheduled</span>
                </div>
              </div>
            </div>
          </article>

          <!-- Bento 4: Bilingual Localization -->
          <article class="bento-card bento-wide is-security rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("shield")}BILINGUAL LOCALIZATION</span>
              <h3>Culturally Nuanced Arabic &amp; English Content</h3>
              <p>Every post, caption, and video overlay is written by native bilingual copywriters who understand Gulf business etiquette, eliminating awkward translations and preserving your executive prestige.</p>
            </div>
            <div class="security-cluster">
              <div class="sec-pill">{svg("globe")}<span>Native Arabic &amp; English Copy</span></div>
              <div class="sec-pill">{svg("camera")}<span>On-Site Dubai Studio Shoots</span></div>
              <div class="sec-pill">{svg("bar-chart")}<span>Monthly Executive ROI Reports</span></div>
              <div class="sec-pill">{svg("users")}<span>Dedicated Account Director</span></div>
            </div>
          </article>
        </div>'''

    elif slug == "branding-and-ui-ux-design":
        return f'''        <div class="sv-bento-grid">
          <!-- Bento 1: Figma Design System -->
          <article class="bento-card bento-wide is-featured rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("pen-tool")}DESIGN SYSTEM ARCHITECTURE</span>
              <h3>Comprehensive Figma Design Systems &amp; Tokens</h3>
              <p>Scalable design systems built with auto-layout, responsive component variants, and semantic design tokens that bridge design and code, accelerating frontend development velocity by 3x.</p>
            </div>
            <div class="bento-agent-telemetry">
              <div class="agent-bar-row">
                <div class="agent-info"><b>Design Tokens</b><small>Color, typography, elevation &amp; spacing tokens</small></div>
                <div class="agent-track"><span style="width: 100%;"></span></div>
                <span class="agent-pct">142 tokens</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Figma Master Library</b><small>420+ components &bull; 100% auto-layout</small></div>
                <div class="agent-track"><span style="width: 100%;"></span></div>
                <span class="agent-pct">420+ items</span>
              </div>
              <div class="agent-bar-row">
                <div class="agent-info"><b>Developer Handoff</b><small>Zero spec ambiguity &bull; tokenized exports</small></div>
                <div class="agent-track"><span style="width: 100%;"></span></div>
                <span class="agent-pct">0 ambiguity</span>
              </div>
            </div>
          </article>

          <!-- Bento 2: Usability Testing -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("layout")}PROTOTYPE TESTING</span>
              <h3>Usability-Validated UI/UX</h3>
              <p>Interactive prototypes stress-tested with real UAE users to ensure 90%+ task completion before code.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="ocr-preview">
                <div class="ocr-tag">USABILITY SCORE: 82 / 100</div>
                <div class="ocr-val">92% Task Completion Rate</div>
                <div class="ocr-status ok">{check} Zero Navigation Ambiguity</div>
              </div>
            </div>
          </article>

          <!-- Bento 3: Arabic RTL Typography -->
          <article class="bento-card is-tech rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("globe")}BILINGUAL TYPOGRAPHY</span>
              <h3>Arabic RTL &amp; Bilingual Typography</h3>
              <p>Carefully paired English and Arabic typefaces engineered for seamless bidirectional screen layouts.</p>
            </div>
            <div class="bento-mini-mockup">
              <div class="wa-preview">
                <div class="wa-msg">Space Grotesk + Noto Kufi &bull; Full RTL Mirrored &bull; Pixel-Perfect</div>
                <div class="wa-actions">
                  <span class="wa-btn ok">RTL Mirrored</span>
                  <span class="wa-btn flag">Inspect</span>
                </div>
              </div>
            </div>
          </article>

          <!-- Bento 4: Brand Standards -->
          <article class="bento-card bento-wide is-security rv">
            <div class="bento-top">
              <span class="bento-badge">{svg("shield")}BRAND ASSET GOVERNANCE</span>
              <h3>60+ Page Corporate Brand Standards</h3>
              <p>Complete visual governance manuals defining primary and secondary logo usage, clear space, colour formulas (HEX, RGB, CMYK, Pantone), and print/digital collateral specifications.</p>
            </div>
            <div class="security-cluster">
              <div class="sec-pill">{svg("pen-tool")}<span>Vector SVG &amp; Print Assets</span></div>
              <div class="sec-pill">{svg("layout")}<span>Figma Master Library Access</span></div>
              <div class="sec-pill">{svg("globe")}<span>Bilingual Corporate Collateral</span></div>
              <div class="sec-pill">{svg("badge-check")}<span>100% Full IP Ownership</span></div>
            </div>
          </article>
        </div>'''
    
    return ""


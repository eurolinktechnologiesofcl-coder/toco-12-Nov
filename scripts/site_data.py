"""
TOCO Technologies UAE — Site Data and Rich Content Store
Contains exhaustive content, SEO metadata, features, FAQs, and schemas
for all 26 pages. Target commercial intent: Dubai and across the UAE.
"""

SERVICES_DATA = [
    {
        "slug": "ai-automation",
        "title": "AI Automation Company in Dubai | Autonomous Agents & Workflows",
        "meta_desc": "Premier AI automation company in Dubai. TOCO Technologies builds autonomous agents, custom LLM pipelines, and enterprise workflow automations across UAE.",
        "h1": "AI Automation & Autonomous Workflow Agents in Dubai, UAE",
        "lede": "Eliminate operational bottlenecks with intelligent AI agents. We engineer custom workflow automation pipelines, enterprise LLM integrations, and document intelligence systems tailored for UAE corporations.",
        "features": [
            {
                "icon": "🤖",
                "title": "Autonomous AI Agent Orchestration",
                "desc": "Multi-agent systems designed to execute complex, multi-step business tasks without manual intervention, from data extraction to operational decisions."
            },
            {
                "icon": "📄",
                "title": "Document Intelligence & OCR",
                "desc": "Automated ingestion, parsing, and classification of UAE trade licenses, invoices, customs declarations, and legal contracts with 99.4% accuracy."
            },
            {
                "icon": "⚡",
                "title": "Legacy System & ERP Integration",
                "desc": "Bridge older databases and on-premise software with modern AI layers via resilient REST APIs, webhook listeners, and background task queues."
            },
            {
                "icon": "🔒",
                "title": "On-Premise & Private Cloud LLM Deployment",
                "desc": "Host proprietary language models within UAE borders or private AWS/Azure VPCs, fully complying with UAE Federal Decree-Law No. 45 on Data Protection."
            },
            {
                "icon": "📊",
                "title": "Automated Workflow Monitoring & Alerts",
                "desc": "Real-time telemetry dashboards tracking throughput, error thresholds, token usage, and automated fallback triggers for zero downtime."
            },
            {
                "icon": "🔄",
                "title": "Human-in-the-Loop Approval Portals",
                "desc": "Configure custom threshold rules that seamlessly route edge cases to human managers for instant WhatsApp or email verification before execution."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Workflow Audit & Opportunity Discovery",
                "desc": "We analyze your recurring daily operational tasks, calculate potential time and cost savings, and map out the high-ROI automation candidates."
            },
            {
                "num": "02",
                "title": "Architecture & Pilot PoC Build",
                "desc": "We develop a rapid Proof of Concept (PoC) within 14 days, verifying data extraction accuracy, latency constraints, and system integration points."
            },
            {
                "num": "03",
                "title": "Enterprise Pipeline Engineering",
                "desc": "Our Dubai engineering team builds the production-grade pipeline with complete error resilience, cryptographic security, and automated logging."
            },
            {
                "num": "04",
                "title": "Deployment, Training & 30-Day SLA Warranty",
                "desc": "We launch the live system, train your internal staff, and provide 30 days of complimentary engineering monitoring and operational support."
            }
        ],
        "benefits": [
            {"metric": "70%", "title": "Reduction in Manual Processing", "desc": "Free your teams from repetitive data entry and administrative overhead."},
            {"metric": "10x", "title": "Faster Operational Turnaround", "desc": "Invoices, approvals, and dispatch documents processed in seconds instead of hours."},
            {"metric": "99.4%", "title": "Extraction Precision", "desc": "Deterministic validation rules prevent erroneous data from contaminating ERPs."},
            {"metric": "24/7", "title": "Continuous Execution", "desc": "Autonomous agents handle night shifts, weekend queues, and holiday backlogs."}
        ],
        "tech_stack": ["Python", "FastAPI", "OpenAI GPT-4o", "LangChain", "LlamaIndex", "Celery", "PostgreSQL", "Docker", "AWS UAE"],
        "faqs": [
            {
                "q": "How does TOCO Technologies integrate AI automation into existing Dubai enterprise systems?",
                "a": "We connect modern AI models to your existing ERP, CRM, database, or accounting software using secure REST APIs, webhooks, and headless middleware. Your existing system remains the source of truth while AI operates as an accelerated execution engine."
            },
            {
                "q": "Is our corporate data safe and compliant with UAE data protection laws?",
                "a": "Yes. We strictly adhere to UAE Federal Decree-Law No. 45 of 2021 regarding Personal Data Protection. We offer zero-retention enterprise API configurations and on-premise private VPC deployments where sensitive data never leaves your infrastructure."
            },
            {
                "q": "What is the typical timeline for an AI automation deployment?",
                "a": "A focused single-process automation (such as invoice processing or customer intake) is typically prototyped in 7–10 days and rolled out to production within 3–4 weeks. Complex enterprise-wide workflows take 6–8 weeks."
            },
            {
                "q": "Do you offer post-launch support and maintenance in Dubai?",
                "a": "Every TOCO deployment includes our 30-day comprehensive post-launch warranty with dedicated engineering support. Following that, we provide monthly SLA maintenance agreements with guaranteed response times."
            }
        ],
        "related": [
            {"title": "AI Business Automation", "url": "/services/ai-business-automation", "desc": "Turn traffic and inquiries into verified business deals."},
            {"title": "Custom ERP & Software", "url": "/services/erp-and-custom-software", "desc": "Connect your automated workflows to a tailored ERP suite."},
            {"title": "Comfity Payroll Automation", "url": "/products/comfity-payroll-automation", "desc": "Explore our automated payroll product for UAE WPS."}
        ]
    },
    {
        "slug": "ai-business-automation",
        "title": "AI Business Automation & Conversions Dubai | TOCO Technologies",
        "meta_desc": "Convert inquiries into closed deals with AI business automation in Dubai. Instant multi-channel response, lead qualification, and CRM sync.",
        "h1": "AI Business Automation for High-Impact Conversions in Dubai",
        "lede": "Stop losing high-value UAE customer inquiries to delayed follow-ups. We engineer AI business automation that captures leads across WhatsApp, website chat, and social channels, qualifies intent in real-time, and drives immediate conversions.",
        "features": [
            {
                "icon": "⚡",
                "title": "Sub-60-Second Lead Response",
                "desc": "Engage website visitors and social media leads immediately with intelligent bilingual conversational AI, dramatically lifting conversion rates."
            },
            {
                "icon": "💬",
                "title": "WhatsApp Business Cloud AI Integration",
                "desc": "Autonomous conversational agents on official WhatsApp Business APIs that answer technical queries, share brochures, and book meetings."
            },
            {
                "icon": "🎯",
                "title": "Dynamic Lead Scoring & Qualification",
                "desc": "Intelligent qualification models evaluate budget, timeline, and authority before instantly routing high-intent deals to your senior sales team."
            },
            {
                "icon": "📅",
                "title": "Automated Calendar Scheduling",
                "desc": "Direct Google Calendar and Outlook integrations allowing prospects to book discovery calls and showroom visits inside the chat window."
            },
            {
                "icon": "🔄",
                "title": "Real-Time CRM & ERP Synchronization",
                "desc": "Every conversation, contact field, and qualified intent score is synced in real-time to HubSpot, Salesforce, Zoho, or your custom ERP."
            },
            {
                "icon": "🌐",
                "title": "Bilingual Arabic & English Conversational Engine",
                "desc": "Natural, culturally nuanced Arabic and English understanding that speaks the commercial language of Dubai, Abu Dhabi, and the GCC."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Conversion Funnel Mapping",
                "desc": "We analyze your current inbound lead channels, drop-off rates, customer FAQs, and sales qualification criteria."
            },
            {
                "num": "02",
                "title": "Conversational Knowledge Engineering",
                "desc": "We train domain-specific AI models on your product specifications, pricing policies, service catalogues, and brand tone of voice."
            },
            {
                "num": "03",
                "title": "Multi-Channel Omni-Channel Integration",
                "desc": "We deploy the AI conversational system across your website, WhatsApp Business API, Meta Lead Ads, and internal CRM."
            },
            {
                "num": "04",
                "title": "A/B Conversion Tuning & Live Handoff",
                "desc": "Continuous analysis of conversation transcripts to refine response scripts, optimize booking conversion, and ensure seamless human handoffs."
            }
        ],
        "benefits": [
            {"metric": "3.8x", "title": "Increase in Qualified Bookings", "desc": "Prospects schedule meetings while their purchase intent is at its peak."},
            {"metric": "< 45s", "title": "Average Response Speed", "desc": "Never leave a WhatsApp or web inquiry unanswered during or outside business hours."},
            {"metric": "+42%", "title": "Conversion Rate Lift", "desc": "Higher appointment show-up rates and structured CRM data for sales reps."},
            {"metric": "100%", "title": "CRM Data Accuracy", "desc": "Clean lead contact details and conversation summaries populated automatically."}
        ],
        "tech_stack": ["WhatsApp Business API", "Node.js", "OpenAI", "Anthropic Claude", "HubSpot API", "Zoho CRM", "FastAPI", "Webhooks"],
        "faqs": [
            {
                "q": "How does AI business automation increase sales for Dubai companies?",
                "a": "Studies consistently prove that responding to an inbound lead within 5 minutes results in a 391% increase in conversions. Our AI engines respond in under 45 seconds, answer specific catalog questions, qualify project budget, and secure a calendar appointment before competitors even open the email."
            },
            {
                "q": "Can the AI handle technical inquiries about our Dubai real estate or services?",
                "a": "Yes. We use Retrieval-Augmented Generation (RAG) mapped directly to your brochures, floor plans, pricing sheets, and policies. The AI answers with factual, verified details and never hallucinates unapproved prices."
            },
            {
                "q": "What happens when a customer requests to speak with a human executive?",
                "a": "The system immediately alerts your designated sales consultant via WhatsApp and CRM notification, pausing the AI and passing full conversation context to your human team for a seamless continuation."
            },
            {
                "q": "Does this work with official Meta WhatsApp Business accounts?",
                "a": "Yes. We set up and configure your official Meta WhatsApp Business Cloud API with your verified green tick branding, ensuring zero risk of account ban or delivery failure."
            }
        ],
        "related": [
            {"title": "AI Automation & Agents", "url": "/services/ai-automation", "desc": "Automate backend operational tasks after closing the deal."},
            {"title": "Digital Marketing & PPC", "url": "/services/digital-marketing", "desc": "Drive high-intent UAE traffic to your AI conversion funnel."},
            {"title": "Real Estate CRM Product", "url": "/products/real-estate-crm", "desc": "Explore our specialized CRM for UAE property brokerages."}
        ]
    },
    {
        "slug": "mobile-app-development",
        "title": "Mobile App Development Company Dubai | iOS & Android Software",
        "meta_desc": "Top mobile app development company in Dubai. TOCO Technologies builds high-performance iOS and Android applications with Flutter and cloud APIs.",
        "h1": "Mobile Application Software Engineering in Dubai, UAE",
        "lede": "From consumer mobile commerce to high-security enterprise field operations, we engineer responsive, intuitive iOS and Android applications built on modern Flutter and native frameworks with resilient cloud backends.",
        "features": [
            {
                "icon": "📱",
                "title": "Cross-Platform Flutter & Native Architecture",
                "desc": "Single-codebase efficiency with 60fps native performance across both iOS App Store and Google Play platforms."
            },
            {
                "icon": "💳",
                "title": "GCC Payment Gateways & Apple Pay",
                "desc": "Seamless checkout integrations with Apple Pay, Google Pay, Network International, Telr, Stripe, Tabby, and Tamara."
            },
            {
                "icon": "📍",
                "title": "Real-Time Geolocation & Dispatch Telemetry",
                "desc": "GPS live driver tracking, route optimization, geofenced alerts, and map routing built for UAE logistics and delivery operations."
            },
            {
                "icon": "🔔",
                "title": "Segmented Push Notifications & Marketing",
                "desc": "Engage users with behavioral push campaigns, order milestone alerts, and re-engagement messaging via Firebase Cloud Messaging."
            },
            {
                "icon": "🔒",
                "title": "Enterprise Biometrics & Security",
                "desc": "Face ID, Touch ID, end-to-end encrypted storage, JWT auth tokens, and OWASP mobile security compliance."
            },
            {
                "icon": "☁️",
                "title": "Microservices Cloud Backend & Auto-Scaling",
                "desc": "Sub-100ms API endpoints built with Node.js or Go, backed by Redis caching and resilient cloud databases."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Product UX Strategy & Interactive Prototyping",
                "desc": "We transform your app concept into interactive Figma wireframes, validating user journeys against UAE user expectations."
            },
            {
                "num": "02",
                "title": "Agile Sprint Development",
                "desc": "Two-week agile engineering sprints with test builds delivered to your devices via TestFlight and Google Internal Testing."
            },
            {
                "num": "03",
                "title": "Rigorous QA & Device Compatibility Testing",
                "desc": "End-to-end automated and manual testing across 30+ physical screen sizes, network conditions, and operating system versions."
            },
            {
                "num": "04",
                "title": "App Store Submission & Production Launch",
                "desc": "Full handling of Apple Developer and Google Play Console compliance, review approval, screenshots, and launch monitoring."
            }
        ],
        "benefits": [
            {"metric": "60 FPS", "title": "Fluid UI Performance", "desc": "Silky-smooth animations and instant tap interactions that retain mobile users."},
            {"metric": "99.9%", "title": "Crash-Free Sessions", "desc": "Hardened architecture with comprehensive automated error boundary trapping."},
            {"metric": "35%", "title": "Lower Development Cost", "desc": "Cross-platform Flutter framework cuts dual iOS/Android costs significantly."},
            {"metric": "30-Day", "title": "Post-Launch Warranty", "desc": "Complete store maintenance and priority bug patching included with every build."}
        ],
        "tech_stack": ["Flutter", "Dart", "Swift", "Kotlin", "Firebase", "Node.js", "PostgreSQL", "Apple Pay", "REST APIs"],
        "faqs": [
            {
                "q": "Should we build cross-platform with Flutter or pure native for our Dubai app?",
                "a": "For 90% of business and consumer applications in the UAE, Flutter offers native-identical 60fps performance while reducing initial development budget and ongoing maintenance by approximately 35–40%. For specialized hardware integrations or low-level graphics, we provide native Swift and Kotlin."
            },
            {
                "q": "How long does it take to develop a custom mobile application in Dubai?",
                "a": "An MVP (Minimum Viable Product) application typically takes 8–10 weeks from UX wireframes to App Store submission. Complex enterprise applications with live GPS tracking and multi-tier ERP sync take 12–16 weeks."
            },
            {
                "q": "Do you handle App Store and Google Play submissions?",
                "a": "Yes. We manage the entire store submission process, ensuring full compliance with Apple App Store Review Guidelines and Google Play policies, including privacy disclosures and metadata optimization."
            },
            {
                "q": "Can the mobile app sync in real-time with our web software and database?",
                "a": "Absolutely. We build unified RESTful and WebSocket API layers so your mobile app, web dashboard, and ERP database remain in continuous real-time synchronization."
            }
        ],
        "related": [
            {"title": "Website & Custom Software", "url": "/services/website-and-software-development", "desc": "Complement your mobile app with a high-performance web dashboard."},
            {"title": "UI/UX Product Design", "url": "/services/branding-and-ui-ux-design", "desc": "Explore our interactive Figma product prototyping services."},
            {"title": "E-Commerce Development", "url": "/services/ecommerce-development", "desc": "Launch mobile m-commerce storefronts with fast Apple Pay checkout."}
        ]
    },
    {
        "slug": "website-and-software-development",
        "title": "Website & Custom Software Development Dubai | TOCO Technologies",
        "meta_desc": "High-performance website and custom software development company in Dubai, UAE. We build fast, secure web platforms and bespoke enterprise software.",
        "h1": "Website & Custom Software Engineering in Dubai, UAE",
        "lede": "Corporate websites, SaaS portals, and mission-critical web applications engineered for lightning load speeds, ironclad security, and high commercial conversions across Dubai and the Arabian Gulf.",
        "features": [
            {
                "icon": "⚡",
                "title": "Sub-Second Page Speeds & 95+ Core Web Vitals",
                "desc": "Engineered with clean, semantic markup, zero bloated frameworks, modern CSS, and edge caching for top Google rankings."
            },
            {
                "icon": "🛡️",
                "title": "Hardened Enterprise Security Architecture",
                "desc": "OWASP Top 10 protection, strict Content Security Policies (CSP), SSL enforcement, and SQL injection prevention."
            },
            {
                "icon": "📱",
                "title": "Mobile-First Fluid Responsive Engineering",
                "desc": "Flawless UI presentation tested on 360px mobile viewports up to 4K ultra-wide commercial desktop displays."
            },
            {
                "icon": "🔌",
                "title": "Custom API Middleware & Microservices",
                "desc": "Scalable REST and GraphQL backend services designed to connect frontend portals to payment processors and third-party CRMs."
            },
            {
                "icon": "📈",
                "title": "Technical SEO & Conversion Architecture",
                "desc": "Built-in structured JSON-LD schemas, breadcrumb graphs, Open Graph metadata, and high-converting CTA funnels."
            },
            {
                "icon": "🌐",
                "title": "Bilingual Arabic & English Localization",
                "desc": "Native RTL (Right-to-Left) typography support, fluid font switching, and culturally resonant UX design."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Technical Scoping & Information Architecture",
                "desc": "We map out page hierarchies, conversion pathways, database models, and API integrations around your business goals."
            },
            {
                "num": "02",
                "title": "Figma Wireframing & Design System",
                "desc": "Creation of an executive-grade design system with custom typography scales, UI components, and desktop/mobile prototypes."
            },
            {
                "num": "03",
                "title": "Production Engineering & Testing",
                "desc": "High-velocity development using clean code principles, accessibility audits (WCAG AA), and rigorous cross-browser testing."
            },
            {
                "num": "04",
                "title": "Zero-Downtime Deployment & Handover",
                "desc": "Deployment to enterprise cloud hosting or Vercel, DNS configuration, Google Search Console indexing, and training."
            }
        ],
        "benefits": [
            {"metric": "< 0.8s", "title": "Average Load Time", "desc": "Lightning-fast page delivery drives higher engagement and lower bounce rates."},
            {"metric": "100%", "title": "Ownership of Source Code", "desc": "No recurring vendor lock-in; you retain complete ownership of all repository assets."},
            {"metric": "30-Day", "title": "SLA Launch Warranty", "desc": "Dedicated engineering support ensuring your web application operates flawlessly."},
            {"metric": "95+", "title": "Core Web Vitals Score", "desc": "Compliant with Google's mobile ranking criteria for organic search advantage."}
        ],
        "tech_stack": ["HTML5", "CSS3", "JavaScript", "Python", "Node.js", "PostgreSQL", "Docker", "Vercel", "AWS"],
        "faqs": [
            {
                "q": "Why does TOCO Technologies emphasize lightweight, vanilla web architectures?",
                "a": "Heavy JavaScript frameworks often add megabytes of render-blocking script, resulting in slow mobile load times, high bounce rates, and poor Core Web Vitals scores. By utilizing clean semantic HTML5, modern CSS3, and vanilla JS, we achieve sub-second load times and superior SEO rankings."
            },
            {
                "q": "Will our website be fully bilingual in Arabic and English?",
                "a": "Yes. We engineer complete bidirectional support with proper RTL stylesheets, correct hreflang metadata tags, and localized typography that renders Arabic script beautifully."
            },
            {
                "q": "Can you build custom client portals and secure internal software?",
                "a": "Yes. In addition to corporate public storefronts, we build secure client dashboards, role-based internal portals, document management systems, and automated billing software."
            },
            {
                "q": "Do you provide hosting and domain management in Dubai?",
                "a": "We assist with local `.ae` domain registrations through tdra accredited registrars and configure enterprise-grade hosting with global CDN caching and local UAE edge points of presence."
            }
        ],
        "related": [
            {"title": "Technical SEO & Search", "url": "/services/seo", "desc": "Maximize organic Dubai search visibility for your new website."},
            {"title": "Mobile App Development", "url": "/services/mobile-app-development", "desc": "Extend your platform with companion iOS and Android applications."},
            {"title": "Edutechy E-Learning", "url": "/products/edutechy-elearning-platform", "desc": "See how we engineered our proprietary learning software."}
        ]
    },
    {
        "slug": "digital-marketing",
        "title": "Digital Marketing Agency Dubai | Performance Marketing & PPC",
        "meta_desc": "ROI-focused digital marketing agency in Dubai. High-converting Google Ads (PPC), Meta social campaigns, and data-driven lead generation across UAE.",
        "h1": "Performance Digital Marketing & Paid Acquisition in Dubai",
        "lede": "Generate qualified B2B enquiries and high-value consumer sales with precision-targeted campaigns. We manage Google Ads, Meta performance funnels, and GA4 analytics to deliver predictable commercial returns for UAE businesses.",
        "features": [
            {
                "icon": "🎯",
                "title": "Google Ads (PPC) & Search Acquisition",
                "desc": "Dominate high-intent commercial keywords across Dubai and the UAE with laser-focused search, shopping, and display campaigns."
            },
            {
                "icon": "📱",
                "title": "Meta Ads (Instagram & Facebook Funnels)",
                "desc": "High-converting visual ad creatives, retargeting sequences, and instant lead forms targeting Gulf demographics and decision-makers."
            },
            {
                "icon": "💼",
                "title": "B2B LinkedIn Marketing & Account-Based Ads",
                "desc": "Reach C-suite executives, procurement heads, and enterprise buyers in DIFC, Business Bay, and Abu Dhabi."
            },
            {
                "icon": "📊",
                "title": "GA4 Advanced Conversion Attribution",
                "desc": "Server-side tagging, custom conversion events, and transparent revenue dashboards eliminating marketing guesswork."
            },
            {
                "icon": "🚀",
                "title": "High-Converting Landing Page Optimization",
                "desc": "Dedicated landing page designs with split-testing (A/B testing) to maximize lead conversion from paid ad traffic."
            },
            {
                "icon": "📈",
                "title": "Transparent Weekly Commercial Reporting",
                "desc": "Clear breakdown of spend, cost-per-lead (CPL), customer acquisition cost (CAC), and return on ad spend (ROAS)."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Market Research & Competitor Audit",
                "desc": "We evaluate competitor ad copies, bidding strategies, and high-value search volumes in the UAE marketplace."
            },
            {
                "num": "02",
                "title": "Tracking Setup & Campaign Architecture",
                "desc": "We install server-side Google Tag Manager and Meta Pixel, ensuring every phone call, form submission, and purchase is tracked."
            },
            {
                "num": "03",
                "title": "Creative Production & Launch",
                "desc": "Our team drafts high-converting ad copy, designs visual assets, and launches targeted campaigns with strict negative keyword lists."
            },
            {
                "num": "04",
                "title": "Continuous Bidding Optimization & Scaling",
                "desc": "Daily budget reallocation toward the top-performing keywords and ad creatives to lower your acquisition costs while scaling volume."
            }
        ],
        "benefits": [
            {"metric": "4.2x", "title": "Average ROAS", "desc": "Generating demonstrable commercial revenue far exceeding your monthly ad investment."},
            {"metric": "-32%", "title": "Lower Cost-Per-Acquisition", "desc": "Negative keywords and audience exclusions stop wasted ad spend immediately."},
            {"metric": "100%", "title": "Attributed Telemetry", "desc": "Know exactly which keyword, ad creative, and campaign produced every closed client."},
            {"metric": "Weekly", "title": "Executive Performance Briefs", "desc": "No vanity impressions; only actionable metrics that matter to your business."}
        ],
        "tech_stack": ["Google Ads", "Meta Ads Manager", "LinkedIn Campaign Manager", "Google Analytics 4", "Google Tag Manager", "Looker Studio"],
        "faqs": [
            {
                "q": "What is the recommended monthly ad budget for advertising in Dubai?",
                "a": "While campaigns can begin with AED 3,500 – 5,000 per month for focused local targeting, enterprise B2B and competitive sectors (such as Real Estate, Legal, and Healthcare) typically see optimal results with monthly spends between AED 10,000 and AED 25,000+."
            },
            {
                "q": "How quickly do we start seeing leads from paid digital marketing?",
                "a": "Google Search Ads and Meta Lead funnels begin generating inquiries within 48 to 72 hours of campaign launch. Full algorithmic learning and cost-per-lead optimization occur over the first 2 to 3 weeks."
            },
            {
                "q": "Do you handle ad creatives and copywriting in both English and Arabic?",
                "a": "Yes. Our in-house marketing strategists write native English and Arabic ad copy tailored specifically to Gulf consumer psychology and corporate sensibilities."
            },
            {
                "q": "Do you tie your campaigns into our CRM?",
                "a": "Yes. We configure direct webhooks that deliver incoming leads straight into your CRM or WhatsApp, notifying your sales reps within seconds."
            }
        ],
        "related": [
            {"title": "AI Business Conversions", "url": "/services/ai-business-automation", "desc": "Automate lead qualification for all incoming ad traffic."},
            {"title": "Technical SEO Services", "url": "/services/seo", "desc": "Build long-term organic traffic to complement paid acquisition."},
            {"title": "Analytics Tracking Suite", "url": "/products/analytics-tracking", "desc": "Track multi-touch customer attribution across all channels."}
        ]
    },
    {
        "slug": "seo",
        "title": "SEO Company Dubai | Technical SEO & UAE Search Optimization",
        "meta_desc": "Top technical SEO company in Dubai, UAE. We drive high-intent organic rankings, Core Web Vitals optimization, and enterprise local search growth.",
        "h1": "Technical SEO & Search Optimization in Dubai, UAE",
        "lede": "Secure commanding positions on Google for the high-intent keywords that drive real revenue in Dubai and across the UAE. We engineer technical SEO architectures, schema graphs, and content strategies that outrank competitors permanently.",
        "features": [
            {
                "icon": "🔍",
                "title": "Technical SEO Audits & Core Web Vitals",
                "desc": "Deep resolution of crawl errors, render blocking, canonical duplicates, slow TTFB, and mobile usability flags."
            },
            {
                "icon": "📍",
                "title": "Dubai & UAE Local Search Domination",
                "desc": "Google Business Profile optimization, local citations, NAP consistency, and targeted geolocational landing pages."
            },
            {
                "icon": "🏗️",
                "title": "Structured Data & Schema Graph Engineering",
                "desc": "Comprehensive JSON-LD schema implementation (Organization, LocalBusiness, Service, Product, FAQ) for rich snippets."
            },
            {
                "icon": "✍️",
                "title": "Commercial Intent Keyword & Content Strategy",
                "desc": "Targeting commercial search queries that indicate immediate buyer intent rather than useless vanity traffic."
            },
            {
                "icon": "🌐",
                "title": "Bilingual Arabic & English SEO Architecture",
                "desc": "Complete hreflang tag configuration and native Arabic search optimization for regional GCC markets."
            },
            {
                "icon": "🔗",
                "title": "Ethical Authority & Digital PR Outreach",
                "desc": "High-quality regional Gulf editorial placements and contextual backlinks that build permanent domain rating authority."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Comprehensive Technical & Competitor Audit",
                "desc": "We inspect your website with Screaming Frog and Google Search Console, benchmarking against top 3 Dubai search competitors."
            },
            {
                "num": "02",
                "title": "Codebase Optimization & Schema Injection",
                "desc": "Our front-end engineers resolve code bottlenecks, inject JSON-LD structured schemas, and optimize mobile Core Web Vitals."
            },
            {
                "num": "03",
                "title": "Commercial Content & On-Page Execution",
                "desc": "We optimize headings, metadata, internal link equity, and draft high-authority service pages tailored to UAE commercial intent."
            },
            {
                "num": "04",
                "title": "Authority Expansion & Monthly Search Tracking",
                "desc": "Ongoing link acquisition, indexation management, and monthly rank tracking reports showing verified Google keyword movement."
            }
        ],
        "benefits": [
            {"metric": "1st Page", "title": "High-Intent Commercial Rankings", "desc": "Capture buyers who are actively searching for your services in Dubai."},
            {"metric": "+185%", "title": "Organic Inbound Growth", "desc": "Sustainable compounding traffic that doesn't stop when you pause ad spend."},
            {"metric": "Zero", "title": "Black-Hat Tactics", "desc": "Strictly 100% white-hat Google guideline compliance protecting your brand domain."},
            {"metric": "Top 3", "title": "Google Map Pack Visibility", "desc": "Attract local phone calls and direct visits to your Port Saeed or Dubai office."}
        ],
        "tech_stack": ["Google Search Console", "Screaming Frog", "Ahrefs", "Semrush", "Schema.org", "PageSpeed Insights", "Looker Studio"],
        "faqs": [
            {
                "q": "How long does it take to rank on the first page of Google in Dubai?",
                "a": "For local UAE business terms, initial keyword movement typically appears within 6 to 8 weeks following technical code remediation and schema injection. Major competitive keywords achieve first-page rankings within 3 to 6 months of continuous optimization."
            },
            {
                "q": "Do you guarantee number-one rankings on Google?",
                "a": "No ethical SEO agency can guarantee a #1 ranking because Google's algorithm contains hundreds of evolving factors. However, we guarantee strict adherence to Google Search Essentials, proven technical optimization, and measurable month-over-month growth in rankings and organic leads."
            },
            {
                "q": "Why is technical SEO more important than blog writing?",
                "a": "If search engine bots encounter slow server response times, unoptimized JavaScript rendering, or broken crawl directives, great content will never be properly indexed. Technical SEO ensures your site architecture provides Google with the fastest, clearest signals possible."
            },
            {
                "q": "Can you optimize our existing website without redesigning it?",
                "a": "Yes. We can conduct a standalone Technical SEO Remediation on your current website, correcting on-page code, metadata, schemas, and Core Web Vitals."
            }
        ],
        "related": [
            {"title": "Website Development", "url": "/services/website-and-software-development", "desc": "Pair technical SEO with a sub-second, cleanly coded web architecture."},
            {"title": "Digital Marketing", "url": "/services/digital-marketing", "desc": "Run paid PPC campaigns while your organic search authority builds."},
            {"title": "Portfolio & Case Studies", "url": "/portfolio", "desc": "Review verified client SEO outcomes across Dubai sectors."}
        ]
    },
    {
        "slug": "ecommerce-development",
        "title": "E-Commerce Website Development Dubai | Shopify & Custom Stores",
        "meta_desc": "High-converting e-commerce development company in Dubai, UAE. We build custom online stores, Shopify platforms, and seamless UAE payment gateways.",
        "h1": "E-Commerce Development & Storefront Architecture in Dubai",
        "lede": "Turn online visitors into repeat buyers. We engineer fast, visually arresting e-commerce platforms built on Shopify, WooCommerce, or bespoke headless architectures with native UAE payment gateways and live ERP sync.",
        "features": [
            {
                "icon": "🛍️",
                "title": "Shopify Plus & Bespoke Storefronts",
                "desc": "Customized themes, fluid mobile checkouts, and custom apps built specifically for your retail, luxury, or wholesale business model."
            },
            {
                "icon": "💳",
                "title": "UAE Payment Gateways & Buy-Now-Pay-Later",
                "desc": "Seamless checkout integrations with Tabby, Tamara, Apple Pay, Telr, Network International, Checkout.com, and Stripe."
            },
            {
                "icon": "📦",
                "title": "Warehouse & Logistics Dispatch Sync",
                "desc": "Automated order routing to local UAE couriers and 3PL providers including Aramex, DHL, Emirates Post, and iKart Express."
            },
            {
                "icon": "🌐",
                "title": "Multi-Currency & GCC Tax Compliance",
                "desc": "Full support for AED, SAR, KWD, BHD, and OMR currencies with automated 5% UAE VAT invoice generation."
            },
            {
                "icon": "⚡",
                "title": "Sub-Second Mobile Checkout UX",
                "desc": "Frictionless one-page checkouts designed to minimize cart abandonment on smartphones across the Emirates."
            },
            {
                "icon": "🔄",
                "title": "Live Inventory & ERP Integration",
                "desc": "Two-way synchronization between your physical retail POS systems, warehouses, and digital storefront."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "E-Commerce Architecture & Catalog Strategy",
                "desc": "We analyze your SKU count, product variations, payment gateway requirements, and courier fulfillment models."
            },
            {
                "num": "02",
                "title": "High-Conversion UI/UX Design",
                "desc": "We craft luxury product pages, intuitive category filters, sticky 'Add to Cart' mobile bars, and streamlined checkout screens."
            },
            {
                "num": "03",
                "title": "Payment, VAT & Logistics Integration",
                "desc": "Our engineers connect your UAE merchant accounts, configure multi-currency conversions, and test end-to-end checkout flows."
            },
            {
                "num": "04",
                "title": "Launch, Staff Training & Live Support",
                "desc": "We conduct complete order test runs, train your operational team on order processing, and provide 30-day launch support."
            }
        ],
        "benefits": [
            {"metric": "+38%", "title": "Mobile Conversion Uplift", "desc": "Friction-free checkout experiences designed specifically for smartphone shoppers."},
            {"metric": "100%", "title": "UAE VAT Compliance", "desc": "Automated tax calculations and compliant electronic tax invoice generation."},
            {"metric": "< 1s", "title": "Product Catalog Load", "desc": "Lightning-fast catalog browsing that prevents shoppers from abandoning your store."},
            {"metric": "30-Day", "title": "Launch Engineering SLA", "desc": "Immediate bug resolution and checkout monitoring during peak trading hours."}
        ],
        "tech_stack": ["Shopify Plus", "WooCommerce", "Liquid", "Node.js", "Stripe", "Tabby", "Tamara", "Aramex API", "PostgreSQL"],
        "faqs": [
            {
                "q": "Which e-commerce platform is best for my Dubai business: Shopify or custom?",
                "a": "For most retail and D2C brands selling up to 5,000 SKUs, Shopify offers unparalleled stability, top-tier security, and fast deployment. For enterprise operations with complex multi-warehouse inventory rules, B2B wholesale pricing, or custom ERP logic, we build tailored headless architectures."
            },
            {
                "q": "How do we integrate Tabby and Tamara Buy-Now-Pay-Later in the UAE?",
                "a": "We handle the complete API integration with Tabby and Tamara, embedding on-site installment widgets on product pages and cart screens to lift average order value by up to 28%."
            },
            {
                "q": "Can the online store synchronize inventory with our physical store in Dubai?",
                "a": "Yes. We build bi-directional API bridges between your digital store and physical retail POS or ERP systems, ensuring stock counts update instantly to avoid overselling."
            },
            {
                "q": "Does your team handle Arabic localization for UAE e-commerce?",
                "a": "Yes. We configure comprehensive bilingual Arabic and English storefronts with mirrored RTL layouts, localized currency formatting, and separate search indexing."
            }
        ],
        "related": [
            {"title": "Custom ERP & Software", "url": "/services/erp-and-custom-software", "desc": "Connect your online store to custom dispatch and inventory software."},
            {"title": "Digital Marketing", "url": "/services/digital-marketing", "desc": "Run profitable Meta and Google Shopping campaigns for your store."},
            {"title": "MŌJ Luxury Perfume Case Study", "url": "/portfolio", "desc": "See how we built a luxury UAE e-commerce fragrance storefront."}
        ]
    },
    {
        "slug": "erp-and-custom-software",
        "title": "Custom ERP Software Dubai | Enterprise Software Development",
        "meta_desc": "Bespoke custom ERP and enterprise software development in Dubai, UAE. We build logistics suites, inventory systems, and operational software.",
        "h1": "Custom ERP & Enterprise Software Platforms in Dubai",
        "lede": "Off-the-shelf software often forces you to compromise your unique operations. We engineer bespoke ERP platforms, operational dispatch suites, and role-based client portals tailored exactly to your Dubai enterprise workflows.",
        "features": [
            {
                "icon": "🏢",
                "title": "Tailored Business Process Engineering",
                "desc": "Built around your precise organizational workflows, eliminating redundant software subscriptions and disconnected spreadsheets."
            },
            {
                "icon": "📦",
                "title": "Inventory, Procurement & Warehouse Management",
                "desc": "Real-time stock tracking across multiple Dubai and GCC warehouses, automated reorder thresholds, and barcode scanner support."
            },
            {
                "icon": "🚚",
                "title": "Logistics Dispatch & Fleet Telemetry",
                "desc": "Real-time driver dispatch consoles, delivery manifest generation, digital proof of delivery (POD), and route tracking."
            },
            {
                "icon": "👥",
                "title": "Granular Role-Based Access Control (RBAC)",
                "desc": "Custom permission hierarchies protecting sensitive financial records while empowering managers, accountants, and staff."
            },
            {
                "icon": "📑",
                "title": "UAE VAT Invoicing & Financial Accounting",
                "desc": "Integrated accounts receivable, accounts payable, automated VAT calculation, and exportable audit reports."
            },
            {
                "icon": "🔒",
                "title": "Cloud or On-Premise UAE Hosting",
                "desc": "Deployed on your preferred infrastructure with automated daily cryptographic backups and failover redundancy."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Operational Systems Audit",
                "desc": "We shadow your department heads in Dubai, mapping every manual handoff, calculation rule, and reporting requirement."
            },
            {
                "num": "02",
                "title": "Database Schema & Architecture Modeling",
                "desc": "We design normalized relational database architectures engineered for sub-second query latency even with millions of records."
            },
            {
                "num": "03",
                "title": "Modular Sprint Development",
                "desc": "We build and roll out individual modules (Procurement, Inventory, Dispatch, Invoicing) in prioritized phases to avoid operational disruption."
            },
            {
                "num": "04",
                "title": "User Acceptance Testing & Legacy Migration",
                "desc": "We migrate your historical data, conduct intensive team training, and support your transition until the system runs autonomously."
            }
        ],
        "benefits": [
            {"metric": "100%", "title": "Bespoke Process Alignment", "desc": "Software that adapts to your business rules, never forcing your business to adapt."},
            {"metric": "-65%", "title": "Reduction in Operational Errors", "desc": "Automated validation halts dispatch mistakes and duplicate billing entries."},
            {"metric": "Zero", "title": "Per-User Monthly License Fees", "desc": "Scale from 10 to 1,000 employees without paying escalating SaaS license fees."},
            {"metric": "99.8%", "title": "High-Availability Uptime SLA", "desc": "Mission-critical reliability backed by local Dubai engineering support."}
        ],
        "tech_stack": ["Python", "FastAPI", "PostgreSQL", "Node.js", "Docker", "Redis", "AWS UAE", "REST APIs"],
        "faqs": [
            {
                "q": "Why choose custom ERP software over SAP, Odoo, or Zoho?",
                "a": "Generic ERPs come with expensive recurring user licenses, steep learning curves, and rigid modules that require costly custom development anyway. A custom TOCO ERP is engineered exclusively for your specific operational flow, provides full code ownership, and eliminates ongoing per-user license fees."
            },
            {
                "q": "Can you migrate our historical data from Excel and older accounting software?",
                "a": "Yes. Our data engineers extract, clean, validate, and migrate your historical customer databases, purchase records, and inventory ledgers into your new relational database with zero data loss."
            },
            {
                "q": "How secure is our company financial data?",
                "a": "We implement bank-grade AES-256 data encryption at rest and TLS 1.3 in transit, strict role-based access control, comprehensive audit logging of all user actions, and automated encrypted off-site backups."
            },
            {
                "q": "What ongoing maintenance and engineering support do you provide?",
                "a": "Every system launch includes a 30-day comprehensive warranty. Following launch, we provide ongoing SLA agreements covering regular security patches, performance monitoring, and continuous feature expansion."
            }
        ],
        "related": [
            {"title": "AI Conversions ERP Product", "url": "/products/ai-conversions-erp", "desc": "Explore our proprietary AI-assisted enterprise operational platform."},
            {"title": "iKart Express Case Study", "url": "/portfolio", "desc": "Discover how we built custom logistics and dispatch software."},
            {"title": "Comfity Payroll Automation", "url": "/products/comfity-payroll-automation", "desc": "Integrate UAE WPS compliant payroll into your business suite."}
        ]
    },
    {
        "slug": "social-media-management",
        "title": "Social Media Management Agency Dubai | B2B & Brand Growth",
        "meta_desc": "Results-driven social media management agency in Dubai. B2B LinkedIn growth, high-production video reels, and targeted GCC brand engagement.",
        "h1": "Strategic Social Media Management & Brand Growth in Dubai",
        "lede": "Establish undeniable brand authority across the UAE and GCC. We craft strategic social media architectures, executive thought leadership on LinkedIn, high-impact video reels, and conversion-focused social funnels.",
        "features": [
            {
                "icon": "💼",
                "title": "B2B LinkedIn Executive Authority",
                "desc": "Position your founders and corporate brand as regional leaders through data-backed industry analysis and case studies."
            },
            {
                "icon": "🎬",
                "title": "High-Production Short-Form Video & Reels",
                "desc": "Concept, scripting, editing, and publishing of dynamic Instagram Reels and TikTok videos that capture attention."
            },
            {
                "icon": "📅",
                "title": "Monthly Strategic Editorial Calendars",
                "desc": "Structured content matrices balancing brand education, social proof, product features, and commercial calls to action."
            },
            {
                "icon": "💬",
                "title": "Active Community & Direct Message Management",
                "desc": "Timely engagement with comments, prospect questions, and inbound direct message routing into your sales pipeline."
            },
            {
                "icon": "🌐",
                "title": "Culturally Resonant English & Arabic Copywriting",
                "desc": "Flawless bilingual messaging tailored to UAE cultural nuances, commercial etiquette, and modern slang."
            },
            {
                "icon": "📊",
                "title": "Monthly Commercial Impact & Growth Analytics",
                "desc": "Transparent reporting tracking follower quality, engagement rates, profile clicks, and attributed customer inquiries."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Brand Voice & Competitor Persona Audit",
                "desc": "We establish your visual aesthetic, tone of voice, content pillars, and study leading competitors in your UAE niche."
            },
            {
                "num": "02",
                "title": "Content Production & Approval Workflow",
                "desc": "Our designers and copywriters produce your complete monthly content calendar in advance for single-click review."
            },
            {
                "num": "03",
                "title": "Scheduled Publishing & Active Community Nurturing",
                "desc": "Optimized posting during peak Gulf commercial hours, paired with active community engagement and comment moderation."
            },
            {
                "num": "04",
                "title": "Performance Review & Strategy Iteration",
                "desc": "Monthly executive review of top-performing content themes, audience demographics, and conversion pathways."
            }
        ],
        "benefits": [
            {"metric": "3.5x", "title": "Average Engagement Rate Lift", "desc": "Move beyond dead vanity metrics to active community discussions."},
            {"metric": "100%", "title": "Bilingual Gulf Fluency", "desc": "Culturally native English and Arabic content crafted for UAE audiences."},
            {"metric": "+120%", "title": "Inbound Direct Message Inquiries", "desc": "Convert profile views into direct business conversations on WhatsApp & DM."},
            {"metric": "Consistent", "title": "Daily Digital Brand Presence", "desc": "Never leave your social media channels dormant or outdated."}
        ],
        "tech_stack": ["Figma", "Adobe Premiere Pro", "After Effects", "LinkedIn", "Instagram", "TikTok", "Meta Business Suite", "Buffer"],
        "faqs": [
            {
                "q": "Which social media platforms are most effective for businesses in Dubai?",
                "a": "For B2B companies, professional services, and tech enterprises in Dubai, LinkedIn is undeniably the most lucrative platform for executive lead generation. For retail, luxury, hospitality, and real estate, Instagram Reels and TikTok deliver massive brand recall and direct inquiries."
            },
            {
                "q": "Do we get to review and approve posts before they go live?",
                "a": "Yes. We prepare full monthly content calendars containing visuals, video drafts, and captions two weeks in advance. Nothing is published without your written sign-off."
            },
            {
                "q": "Can social media management generate real B2B sales in the UAE?",
                "a": "Yes. When executive leadership profiles post insightful industry breakdowns and client case studies on LinkedIn, decision-makers in Dubai and Abu Dhabi reach out directly via messaging to request proposals."
            },
            {
                "q": "Do you provide video production services in Dubai?",
                "a": "Yes. We script, edit, animate, and subtitle video reels from your provided footage or arrange on-site content capture sessions across Dubai."
            }
        ],
        "related": [
            {"title": "Branding & UI/UX Design", "url": "/services/branding-and-ui-ux-design", "desc": "Establish a world-class visual brand identity before scaling social."},
            {"title": "Performance Digital Marketing", "url": "/services/digital-marketing", "desc": "Boost high-performing social posts with paid Meta and LinkedIn ads."},
            {"title": "AI Business Conversions", "url": "/services/ai-business-automation", "desc": "Automate responses to all incoming social media direct messages."}
        ]
    },
    {
        "slug": "branding-and-ui-ux-design",
        "title": "UI UX Design & Branding Agency Dubai | TOCO Technologies",
        "meta_desc": "Award-winning UI/UX design and corporate branding agency in Dubai, UAE. We build Figma design systems, corporate identities, and high-conversion prototypes.",
        "h1": "Corporate Branding & UI/UX Product Design in Dubai",
        "lede": "Stand out with an authoritative, modern digital brand. We design comprehensive brand identity guidelines, scalable Figma UI component systems, and intuitive user experiences engineered for high conversions and user delight.",
        "features": [
            {
                "icon": "🎨",
                "title": "Complete Corporate Brand Identity Books",
                "desc": "Logotypes, icon marks, responsive lockups, primary and secondary color palettes, and typographic hierarchies."
            },
            {
                "icon": "📐",
                "title": "Scalable Figma Design Systems & Tokens",
                "desc": "Atomic design components, auto-layout variants, interactive button states, and CSS design token export readiness."
            },
            {
                "icon": "📱",
                "title": "Interactive High-Fidelity Prototypes",
                "desc": "Clickable, animated prototypes demonstrating realistic application flow for investor pitch decks and stakeholder reviews."
            },
            {
                "icon": "🧪",
                "title": "User Research & Usability Testing",
                "desc": "Heuristic evaluation, persona mapping, task completion testing, and UX friction removal for GCC user profiles."
            },
            {
                "icon": "♿",
                "title": "WCAG AA Accessibility Compliance",
                "desc": "High-contrast color auditing, keyboard navigation states, screen-reader semantic hierarchies, and touch targets."
            },
            {
                "icon": "📄",
                "title": "Marketing Collateral & Pitch Deck Design",
                "desc": "Stationery suites, company profile brochures, proposal templates, and executive investor presentations."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Discovery & Brand Essence Alignment",
                "desc": "We unpack your company vision, target customer psychology, market positioning, and aesthetic preferences."
            },
            {
                "num": "02",
                "title": "Creative Concept Exploration",
                "desc": "Our senior art directors present 3 distinct visual identity directions complete with typography, color palettes, and mockups."
            },
            {
                "num": "03",
                "title": "Wireframing & High-Fidelity UI Prototyping",
                "desc": "We build pixel-perfect user interface layouts in Figma, connecting them into fully clickable, responsive prototypes."
            },
            {
                "num": "04",
                "title": "Design System Handover & Developer Specs",
                "desc": "Complete delivery of vector assets, font licenses, interactive component libraries, and CSS guidelines for engineers."
            }
        ],
        "benefits": [
            {"metric": "100%", "title": "Vector Design Ownership", "desc": "Complete master Figma files, SVG exports, and brand guidelines transferred to you."},
            {"metric": "3x", "title": "Faster Engineering Velocity", "desc": "Clean design tokens and component specs drastically reduce frontend dev time."},
            {"metric": "+40%", "title": "Usability Score Lift", "desc": "Intuitive navigation flows that eliminate cognitive load and user confusion."},
            {"metric": "Bespoke", "title": "Zero Stock Template Design", "desc": "Every visual element custom crafted specifically for your Dubai enterprise."}
        ],
        "tech_stack": ["Figma", "Adobe Illustrator", "Photoshop", "Principle", "Zeroheight", "Design Tokens", "SVG"],
        "faqs": [
            {
                "q": "What deliverables are included in a complete TOCO branding project?",
                "a": "You receive the master vector logo suite (SVG, PNG, EPS), complete Brand Identity Guidelines PDF (covering logo clearance, color codes in HEX/RGB/CMYK, typography usage), social media profile assets, stationery templates (business cards, letterheads), and master Figma design files."
            },
            {
                "q": "Why is a Figma design system critical before software development?",
                "a": "A comprehensive design system establishes shared component standards (buttons, form inputs, modal dialogs, typography sizes). This prevents design inconsistencies, reduces developer rework by up to 50%, and makes future feature updates fast and economical."
            },
            {
                "q": "Do you design for both mobile app and web platforms?",
                "a": "Yes. We design unified cross-platform interfaces that provide consistent branding and interaction standards across iOS, Android, and responsive desktop web applications."
            },
            {
                "q": "Can we hire TOCO only for UI/UX design without development?",
                "a": "Yes. We frequently provide standalone UI/UX product design, handing off complete, developer-ready Figma files with auto-layout and design tokens to your internal engineering team."
            }
        ],
        "related": [
            {"title": "Website Development", "url": "/services/website-and-software-development", "desc": "Turn your Figma designs into clean, sub-second web code."},
            {"title": "Mobile App Development", "url": "/services/mobile-app-development", "desc": "Engineer iOS and Android applications from your design system."},
            {"title": "Portfolio Showcase", "url": "/portfolio", "desc": "Inspect our visual design craftsmanship across real UAE client projects."}
        ]
    }
]

PRODUCTS_DATA = [
    {
        "slug": "edutechy-elearning-platform",
        "title": "Edutechy E-Learning LMS Platform | Built by TOCO Technologies",
        "meta_desc": "Edutechy – we built it. An enterprise e-learning and LMS platform with video streaming, automated grading, student portals, and corporate compliance in UAE.",
        "h1": "Edutechy — Modern E-Learning Platform Built by TOCO",
        "status_badge": "Live Platform / Built by TOCO",
        "lede": "Edutechy is our flagship proprietary learning management system (LMS) engineered by TOCO Technologies. Designed for higher education academies, corporate training institutes, and GCC enterprises requiring scalable, bilingual digital learning.",
        "features": [
            {
                "icon": "🎓",
                "title": "Adaptive Student & Instructor Portals",
                "desc": "Intuitive course navigation, lesson progress bars, downloadable study materials, and interactive Q&A discussion boards."
            },
            {
                "icon": "🎥",
                "title": "Adaptive Bitrate Video Streaming",
                "desc": "Buffer-free HLS video playback optimized for Gulf internet connections, with anti-piracy DRM protection and auto-captions."
            },
            {
                "icon": "📝",
                "title": "Automated Quizzes & Timed Assessments",
                "desc": "Support for multiple-choice, coding challenges, essay submissions, automated grading algorithms, and anti-cheating tab detection."
            },
            {
                "icon": "🏆",
                "title": "Verifiable Digital Certificates & QR Verification",
                "desc": "Automated PDF certificate generation upon course completion with instant cryptographic QR code authentication for employers."
            },
            {
                "icon": "💳",
                "title": "Integrated UAE Payment Gateways",
                "desc": "Sell one-off courses, recurring subscription tiers, or corporate team seats using Apple Pay, Stripe, and local credit cards."
            },
            {
                "icon": "🌐",
                "title": "Full Bilingual Arabic & English LMS Engine",
                "desc": "Right-to-Left (RTL) Arabic interface mirroring, localized course content, and dual-language assessment support."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Platform Provisioning & White-Label Theming",
                "desc": "We deploy an isolated Edutechy tenant branded with your institution's logo, colors, custom domain, and corporate email SMTP."
            },
            {
                "num": "02",
                "title": "Curriculum & Course Structure Ingestion",
                "desc": "Bulk upload of video lectures, quizzes, PDF reading materials, and instructor profiles organized into modular learning paths."
            },
            {
                "num": "03",
                "title": "Payment & Compliance Integration",
                "desc": "Connecting your UAE merchant accounts, configuring corporate group billing, and integrating internal HR single sign-on (SSO)."
            },
            {
                "num": "04",
                "title": "Launch, Training & Dedicated SLA Support",
                "desc": "Comprehensive onboarding for instructors and administrators, backed by 24/7 cloud uptime monitoring and SLA guarantees."
            }
        ],
        "benefits": [
            {"metric": "10,000+", "title": "Concurrent Students Supported", "desc": "High-concurrency microservices cloud architecture that never crashes during live exams."},
            {"metric": "100%", "title": "White-Label Brand Freedom", "desc": "Your own institution name, custom domain, and zero third-party platform branding."},
            {"metric": "99.8%", "title": "Cloud Platform Uptime", "desc": "AWS UAE hosting ensuring constant availability for distance learning programs."},
            {"metric": "30-Day", "title": "Onboarding & Launch Warranty", "desc": "Direct engineering support from the team that architected the platform from scratch."}
        ],
        "tech_stack": ["Node.js", "Python", "PostgreSQL", "AWS S3 / CloudFront", "Docker", "Stripe", "HLS Video", "REST APIs"],
        "faqs": [
            {
                "q": "What makes Edutechy different from open-source systems like Moodle?",
                "a": "Edutechy was engineered from the ground up for modern speed, intuitive smartphone user experience, and native bilingual Arabic/English execution. Unlike bloated legacy platforms, Edutechy loads in under 0.9 seconds, eliminates plugin vulnerability risks, and requires zero technical maintenance from your academic staff."
            },
            {
                "q": "Can Edutechy be hosted on our private cloud within the UAE?",
                "a": "Yes. We offer both managed cloud hosting on AWS UAE regions (satisfying local data residency mandates) or dedicated on-premise installation inside your corporate data center."
            },
            {
                "q": "Can we sell courses with recurring monthly subscriptions in the UAE?",
                "a": "Yes. Edutechy includes a complete monetization engine supporting one-time course fees, monthly/annual student memberships, corporate seat licensing, and discount voucher codes."
            },
            {
                "q": "Does Edutechy support live virtual classrooms?",
                "a": "Yes. Edutechy integrates seamlessly with Zoom API, Microsoft Teams, and WebRTC live streaming for interactive real-time lectures."
            }
        ],
        "related": [
            {"title": "Custom Software Development", "url": "/services/website-and-software-development", "desc": "Learn how we build bespoke enterprise web applications."},
            {"title": "AI Automation Services", "url": "/services/ai-automation", "desc": "Add AI auto-grading and student tutoring chatbots to your LMS."},
            {"title": "Contact for Demo", "url": "/contact", "desc": "Request a guided live walkthrough of the Edutechy LMS platform."}
        ]
    },
    {
        "slug": "adam-designs",
        "title": "Adam Designs | Interior Design Quote & Sales Automation Platform",
        "meta_desc": "Adam Designs: proprietary interior design quote generation and sales automation platform engineered by TOCO Technologies for UAE fit-out firms.",
        "h1": "Adam Designs — Interior Quote & Sales Automation Platform",
        "status_badge": "Live Platform / Built by TOCO",
        "lede": "Architected specifically for interior design studios, fit-out contractors, and architectural firms in Dubai and Abu Dhabi. Adam Designs automates complex bill-of-quantities (BOQ), material estimation, and client proposal generation in minutes.",
        "features": [
            {
                "icon": "📐",
                "title": "Automated Room & Space Dimension Calculator",
                "desc": "Input space dimensions, wall treatments, flooring specs, and ceiling heights to automatically compute exact material volumes."
            },
            {
                "icon": "💰",
                "title": "Dynamic Material & Labor Pricing Engine",
                "desc": "Real-time cost indexing for UAE marbles, joinery, lighting, plumbing, and contractor labor rates with custom profit margins."
            },
            {
                "icon": "📑",
                "title": "Instant Luxury Client Proposals in PDF",
                "desc": "Generate breathtaking, branded client quotation decks with 3D moodboard attachments, itemized pricing, and terms in one click."
            },
            {
                "icon": "✍️",
                "title": "Digital E-Signature & Milestone Payments",
                "desc": "Clients review, configure finish options, sign contracts electronically, and pay initial mobilization deposits via secure online checkout."
            },
            {
                "icon": "📊",
                "title": "Sales Pipeline & Estimator Performance Tracking",
                "desc": "Comprehensive management dashboard tracking win rates, pending quotes, estimator velocity, and average project deal size."
            },
            {
                "icon": "🔄",
                "title": "Direct ERP & Procurement Sync",
                "desc": "Approved quotes automatically generate purchase orders, supplier material requests, and project dispatch schedules."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Catalog & Price Book Setup",
                "desc": "We import your suppliers, material price matrices, labor day-rates, and profit markup tiers into your private Adam Designs tenant."
            },
            {
                "num": "02",
                "title": "Proposal Template Brand Customization",
                "desc": "We customize the client-facing PDF quote templates to reflect your interior studio's luxury branding, typography, and legal terms."
            },
            {
                "num": "03",
                "title": "Workflow Integration & Team Training",
                "desc": "We train your senior estimators, designers, and project managers to generate quotes and track client revisions."
            },
            {
                "num": "04",
                "title": "Go-Live with Full Dedicated Support",
                "desc": "Your estimators start generating instant quotes, shortening deal cycles from 7 days down to 20 minutes."
            }
        ],
        "benefits": [
            {"metric": "85%", "title": "Faster Quote Turnaround", "desc": "Deliver detailed luxury proposals while competing studios are still crunching spreadsheets."},
            {"metric": "+34%", "title": "Proposal Win Rate Lift", "desc": "Impeccably formatted, transparent proposals establish immediate client trust and authority."},
            {"metric": "Zero", "title": "Estimator Calculation Errors", "desc": "Standardized mathematical formulas eliminate underbidding and unexpected project losses."},
            {"metric": "100%", "title": "UAE VAT & Payment Ready", "desc": "Automated 5% VAT calculations and integrated UAE merchant checkout for fast deposits."}
        ],
        "tech_stack": ["Python", "FastAPI", "PostgreSQL", "React/Vanilla JS", "PDF Engine", "Stripe", "Docker", "AWS"],
        "faqs": [
            {
                "q": "Why is Adam Designs superior to generic estimating software?",
                "a": "Generic software is built for general construction. Adam Designs is purpose-built for UAE luxury interior design and commercial fit-out companies, featuring specialized modules for joinery finishes, Italian marble square-meter rates, sanitaryware packages, and Dubai Municipality permitting fees."
            },
            {
                "q": "Can our clients customize finish options directly inside the quote?",
                "a": "Yes. Interactive web proposals allow clients to toggle between standard and premium finish options, watching the total price update dynamically before signing electronically."
            },
            {
                "q": "Does Adam Designs integrate with our existing accounting software?",
                "a": "Yes. Approved quotes push directly into QuickBooks, Xero, Zoho Books, or your custom ERP, creating corresponding invoices and purchase orders automatically."
            },
            {
                "q": "Can we license Adam Designs for our Dubai interior studio?",
                "a": "Yes. We offer both private SaaS tenant subscriptions and fully dedicated, customized enterprise deployments for established fit-out contractors."
            }
        ],
        "related": [
            {"title": "Custom ERP Development", "url": "/services/erp-and-custom-software", "desc": "Build an end-to-end operational system around your estimating engine."},
            {"title": "AI Business Conversions", "url": "/services/ai-business-automation", "desc": "Capture inbound interior design inquiries automatically on WhatsApp."},
            {"title": "Book Adam Designs Demo", "url": "/contact", "desc": "Schedule an interactive demo tailored to your interior design studio."}
        ]
    },
    {
        "slug": "ai-conversions-erp",
        "title": "AI Conversions: ERP | Intelligent Enterprise Software in Dubai",
        "meta_desc": "AI Conversions ERP by TOCO Technologies. Next-generation enterprise software bridging customer inquiries directly to procurement, dispatch, and billing.",
        "h1": "AI Conversions: ERP — Intelligent Enterprise Workflow Platform",
        "status_badge": "Live Platform / Built by TOCO",
        "lede": "Where enterprise resource planning meets autonomous AI decision engines. AI Conversions ERP eliminates the manual gap between incoming customer orders, inventory checks, supplier procurement, and delivery dispatch.",
        "features": [
            {
                "icon": "🤖",
                "title": "Autonomous Inquiry-to-Order Conversion",
                "desc": "AI parses incoming client purchase orders, RFQs, and emails, validating product availability and generating sales orders automatically."
            },
            {
                "icon": "📊",
                "title": "Predictive Stock & Inventory Telemetry",
                "desc": "Machine learning algorithms forecast regional GCC demand patterns, alerting procurement before fast-moving SKUs stock out."
            },
            {
                "icon": "🚚",
                "title": "Autonomous Fleet Dispatch Optimization",
                "desc": "Dynamically bundle orders and assign delivery routes to optimize driver mileage, fuel consumption, and customer delivery windows."
            },
            {
                "icon": "📑",
                "title": "Automated UAE VAT Invoicing & Reconciliation",
                "desc": "Instant electronic VAT tax invoices generated upon order dispatch, matched against bank reconciliation statements."
            },
            {
                "icon": "👥",
                "title": "Role-Based Executive & Warehouse Dashboards",
                "desc": "Separate high-speed interfaces tailored for executive oversight, warehouse pick-and-pack crews, and field delivery drivers."
            },
            {
                "icon": "🔒",
                "title": "Cryptographic Audit Trail & Compliance",
                "desc": "Immutable ledger tracking every price override, inventory adjustment, and approval action for financial audit readiness."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Enterprise Workflow Telemetry Mapping",
                "desc": "We analyze your order lifecycle from initial prospect inquiry through fulfillment, invoicing, and payment collection."
            },
            {
                "num": "02",
                "title": "Module Deployment & Rule Configuration",
                "desc": "We configure your custom pricing tiers, warehouse locations, automated approval thresholds, and AI parsing rules."
            },
            {
                "num": "03",
                "title": "Legacy System Data Ingestion",
                "desc": "Seamless historical migration of customer databases, vendor ledgers, and historical sales data into the new platform."
            },
            {
                "num": "04",
                "title": "Enterprise Rollout & Continuous SLA Warranty",
                "desc": "Phased departmental launch with on-site staff training, dedicated technical support, and guaranteed uptime SLAs."
            }
        ],
        "benefits": [
            {"metric": "60%", "title": "Faster Order-to-Fulfillment", "desc": "Eliminate hours of manual data entry between sales teams and warehouse dispatchers."},
            {"metric": "Zero", "title": "Stockout Surprises", "desc": "Predictive AI alerting ensures high-demand inventory is reordered proactively."},
            {"metric": "100%", "title": "Audit-Ready Financials", "desc": "Clean, automated UAE VAT records that comply with Federal Tax Authority standards."},
            {"metric": "99.8%", "title": "Platform Availability SLA", "desc": "Enterprise cloud reliability built to support continuous multi-shift operations."}
        ],
        "tech_stack": ["Python", "FastAPI", "PostgreSQL", "Redis", "Celery", "OpenAI Embeddings", "Docker", "AWS UAE"],
        "faqs": [
            {
                "q": "How does AI Conversions: ERP differ from standard ERP systems?",
                "a": "Standard ERPs are passive databases that require humans to manually type in every quote, order, and invoice. AI Conversions: ERP acts as an active assistant that reads emails, extracts line items from PDF purchase orders, checks warehouse stock, and presents pre-verified orders for one-click manager signoff."
            },
            {
                "q": "Can AI Conversions: ERP connect with our existing e-commerce storefront?",
                "a": "Yes. It comes with built-in RESTful connectors for Shopify, WooCommerce, and custom web portals, synchronizing orders and inventory in real time."
            },
            {
                "q": "Is this software suitable for logistics and distribution companies in Dubai?",
                "a": "Yes. It was specifically engineered for trading, distribution, and logistics enterprises operating across Dubai, Sharjah, Abu Dhabi, and the wider GCC region."
            },
            {
                "q": "What hosting options are supported?",
                "a": "We deploy on private AWS UAE cloud VPCs or on-premise physical servers inside your Dubai facility, ensuring compliance with local corporate data security standards."
            }
        ],
        "related": [
            {"title": "Custom ERP Development", "url": "/services/erp-and-custom-software", "desc": "Explore bespoke engineering options for your enterprise."},
            {"title": "AI Automation & Agents", "url": "/services/ai-automation", "desc": "Learn about autonomous workflow execution pipelines."},
            {"title": "Contact Our Enterprise Team", "url": "/contact", "desc": "Schedule a private consultation for your executive team."}
        ]
    },
    {
        "slug": "comfity-payroll-automation",
        "title": "Comfity Payroll Automation | UAE WPS & HR Compliance Platform",
        "meta_desc": "Comfity: automated payroll and WPS compliance software for UAE businesses. One-click SIF file generation, automated gratuity, and labor law compliance.",
        "h1": "Comfity — Automated UAE Payroll & WPS Compliance",
        "status_badge": "Live Platform / Built by TOCO",
        "lede": "Say goodbye to payroll calculation errors and late WPS filing penalties. Comfity is our proprietary payroll automation platform engineered specifically for UAE labor law, Ministry of Human Resources and Emiratisation (MOHRE) compliance, and one-click SIF file generation.",
        "features": [
            {
                "icon": "💼",
                "title": "One-Click UAE WPS SIF File Generation",
                "desc": "Automatically format and validate Wages Protection System (WPS) .SIF files for instant processing across all UAE banks and exchange houses."
            },
            {
                "icon": "⚖️",
                "title": "UAE Labor Law & MOHRE Gratuity Engine",
                "desc": "Automated end-of-service gratuity calculations compliant with the latest UAE Federal Decree-Law No. 33 on Labor Relations."
            },
            {
                "icon": "📅",
                "title": "Automated Leave & Attendance Tracking",
                "desc": "Track annual leaves, sick leaves, public UAE holidays, and unpaid leave with automatic monthly salary deductions and accruals."
            },
            {
                "icon": "📑",
                "title": "Confidential Digital Payslip Generation",
                "desc": "Automated PDF payslip distribution directly to employee emails or private self-service employee mobile portals."
            },
            {
                "icon": "🇦🇪",
                "title": "Emiratisation (GPSSA) Pension Support",
                "desc": "Built-in calculations for UAE national employee contributions to the General Pension and Social Security Authority (GPSSA)."
            },
            {
                "icon": "🔒",
                "title": "Bank-Grade Encryption & Audit Trails",
                "desc": "Encrypted employee salary records, role-based HR access control, and complete historical audit logs."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Employee & Salary Data Onboarding",
                "desc": "Bulk upload of employee records, passport details, labor card numbers, routing bank IBANs, and salary contracts."
            },
            {
                "num": "02",
                "title": "Bank & MOHRE Routing Verification",
                "desc": "Configuration of your corporate bank details, employer MOHRE labor code, and chosen WPS exchange house credentials."
            },
            {
                "num": "03",
                "title": "Monthly Automated Payroll Execution",
                "desc": "Every month-end, review pre-calculated hours, allowances, deductions, and click one button to generate validated SIF files."
            },
            {
                "num": "04",
                "title": "Instant Payslip Distribution & Archiving",
                "desc": "One-click digital payslip dispatch to employee emails with complete records archived for government inspection."
            }
        ],
        "benefits": [
            {"metric": "100%", "title": "UAE WPS SIF Compliance", "desc": "Zero rejected bank files or delayed salary penalties from the Ministry of Human Resources."},
            {"metric": "10 Mins", "title": "Monthly Payroll Processing", "desc": "Reduce hours of manual Excel formula auditing down to a 10-minute automated review."},
            {"metric": "Zero", "title": "End-of-Service Calculation Errors", "desc": "Automated gratuity calculations precisely aligned with current UAE labor laws."},
            {"metric": "Bank-Grade", "title": "Confidential Data Security", "desc": "Restricted role-based access ensuring executive and staff salaries remain strictly confidential."}
        ],
        "tech_stack": ["Python", "FastAPI", "PostgreSQL", "WPS SIF Engine", "PDF Generator", "Docker", "AWS UAE"],
        "faqs": [
            {
                "q": "Does Comfity generate official .SIF files for UAE banks?",
                "a": "Yes. Comfity generates valid Wages Protection System (WPS) .SIF files formatted to the precise technical specifications mandated by the Central Bank of the UAE and accepted by all commercial banks including Emirates NBD, FAB, Mashreq, and ADCB."
            },
            {
                "q": "How does Comfity handle UAE end-of-service gratuity calculations?",
                "a": "Comfity automatically applies the statutory formulas dictated by UAE Federal Decree-Law No. 33 of 2021, distinguishing between basic salary and allowances, partial years of service, and contract termination types."
            },
            {
                "q": "Can Comfity manage payroll for companies with multiple UAE trade licenses?",
                "a": "Yes. Comfity supports multi-entity corporate structures, allowing HR managers to run separate WPS payrolls for multiple sister companies from a single dashboard."
            },
            {
                "q": "How can my company deploy Comfity in Dubai?",
                "a": "We offer Comfity as a turnkey cloud subscription or as an integrated payroll module connected directly into your custom TOCO ERP platform."
            }
        ],
        "related": [
            {"title": "Custom ERP Development", "url": "/services/erp-and-custom-software", "desc": "Integrate payroll directly into your broader business operations."},
            {"title": "AI Automation Services", "url": "/services/ai-automation", "desc": "Automate document processing for trade licenses and visas."},
            {"title": "Contact for Comfity Setup", "url": "/contact", "desc": "Get your UAE business onboarded with automated payroll."}
        ]
    },
    {
        "slug": "analytics-tracking",
        "title": "Analytics Tracking Suite | Real-Time Business Intelligence Dubai",
        "meta_desc": "Analytics Tracking Suite by TOCO Technologies. Multi-touch customer journey telemetry and privacy-first analytics for GCC digital businesses. Join waitlist.",
        "h1": "Analytics Tracking Suite — Real-Time Business Telemetry",
        "status_badge": "In Development / VIP Waitlist",
        "is_waitlist": True,
        "lede": "Next-generation customer journey attribution, multi-touch event telemetry, and privacy-first analytics tailored for regional GCC digital commerce. Currently in private beta development by TOCO Technologies.",
        "features": [
            {
                "icon": "📈",
                "title": "Multi-Touch Journey Attribution",
                "desc": "Track user touchpoints from initial ad click on Instagram to WhatsApp inquiry and final closed deal without losing tracking continuity."
            },
            {
                "icon": "🔒",
                "title": "Cookie-Less & Privacy-First Architecture",
                "desc": "Engineered for a cookieless web with first-party server-side event collection that complies with UAE PDP and GDPR regulations."
            },
            {
                "icon": "⚡",
                "title": "Sub-Second Real-Time Telemetry Stream",
                "desc": "Live visitor counters, active cart sessions, and conversion funnel velocities updated instantaneously via WebSockets."
            },
            {
                "icon": "🇦🇪",
                "title": "GCC Localized Regional Insights",
                "desc": "Specialized geographic breakdown across Dubai, Abu Dhabi, Sharjah, Riyadh, and GCC capitals with local currency reporting."
            },
            {
                "icon": "🔌",
                "title": "Drop-In Single-Line JavaScript Tag",
                "desc": "Ultra-lightweight (< 5KB) tracker script that does not impact your Core Web Vitals or mobile page load speeds."
            },
            {
                "icon": "📊",
                "title": "Custom Executive KPI Dashboards",
                "desc": "No confusing analytics jargon; only actionable dashboards tracking revenue, lead volume, and customer acquisition cost."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Private Beta Validation",
                "desc": "Currently being battle-tested on select enterprise client platforms in Dubai to calibrate high-concurrency ingestion."
            },
            {
                "num": "02",
                "title": "VIP Early Access Invitation",
                "desc": "Waitlist members receive priority invitation codes, complimentary onboarding, and discounted founding member pricing."
            },
            {
                "num": "03",
                "title": "Single-Click Website Integration",
                "desc": "Add one lightweight script tag to your website or mobile app to immediately begin capturing rich attribution data."
            },
            {
                "num": "04",
                "title": "Autonomous Weekly Business Insights",
                "desc": "Receive automated weekly executive email summaries highlighting conversion bottlenecks and growth opportunities."
            }
        ],
        "benefits": [
            {"metric": "< 5 KB", "title": "Ultra-Lightweight Footprint", "desc": "Zero impact on your Google Core Web Vitals or mobile rendering speeds."},
            {"metric": "100%", "title": "First-Party Data Ownership", "desc": "Your user data remains yours, never shared or resold to ad networks."},
            {"metric": "Zero", "title": "Data Sampling", "desc": "Every single visit and conversion recorded accurately, unlike free analytics tools."},
            {"metric": "VIP", "title": "Early Access Perks", "desc": "Founding members receive direct feature input and dedicated technical support."}
        ],
        "tech_stack": ["ClickHouse", "Go", "FastAPI", "WebSockets", "TimescaleDB", "Docker", "AWS UAE"],
        "faqs": [
            {
                "q": "When will the Analytics Tracking Suite launch publicly in Dubai?",
                "a": "The platform is currently operating in private beta with select enterprise partners. Public beta access is scheduled to open to waitlist members in early Q3 2026."
            },
            {
                "q": "Why is this better than standard Google Analytics 4 (GA4)?",
                "a": "GA4 has become overly complex, relies on data thresholding and sampling, and suffers from ad-blocker loss. Our Analytics Suite operates server-side, captures 100% of real customer journeys, connects directly to WhatsApp leads, and provides straightforward revenue attribution."
            },
            {
                "q": "Does joining the VIP waitlist obligate us to purchase?",
                "a": "No. Joining the waitlist gives you early preview access, priority onboarding, and exclusive founding tier pricing with zero purchase obligation."
            }
        ],
        "related": [
            {"title": "Performance Digital Marketing", "url": "/services/digital-marketing", "desc": "Scale campaigns with accurate attribution data."},
            {"title": "Technical SEO Services", "url": "/services/seo", "desc": "Track organic search user journeys across your website."},
            {"title": "Real Estate CRM Product", "url": "/products/real-estate-crm", "desc": "Explore our companion CRM product currently in development."}
        ]
    },
    {
        "slug": "real-estate-crm",
        "title": "Real Estate CRM Software Dubai | Gulf Brokerage Acceleration",
        "meta_desc": "Real Estate CRM: purpose-built for Dubai property brokerages and off-plan developers. WhatsApp lead parsing, inventory matching, and agent pipelines. Join waitlist.",
        "h1": "Real Estate CRM — Gulf Brokerage & Lead Acceleration",
        "status_badge": "In Development / VIP Waitlist",
        "is_waitlist": True,
        "lede": "Purpose-built for Dubai real estate brokerages, off-plan developers, and leasing agencies. Features automated WhatsApp lead intake, Property Finder & Bayut integration, unit inventory matching, and agent commission tracking.",
        "features": [
            {
                "icon": "🏙️",
                "title": "Dubai Portal Lead Ingestion (Bayut & Property Finder)",
                "desc": "Automated webhook capture of incoming portal inquiries with instant agent assignment within 30 seconds."
            },
            {
                "icon": "💬",
                "title": "WhatsApp Lead Parsing & Conversation Log",
                "desc": "Log every client WhatsApp interaction directly against property listings without relying on agents' personal phone screenshots."
            },
            {
                "icon": "🗺️",
                "title": "Off-Plan Project & Unit Inventory Matrix",
                "desc": "Interactive floor plans, payment plan schedules, developer brochure attachments, and live unit availability status."
            },
            {
                "icon": "🎯",
                "title": "Smart Buyer-to-Property Matchmaking",
                "desc": "AI algorithms match registered buyer budgets and preferred Dubai communities against your active secondary and off-plan inventory."
            },
            {
                "icon": "💼",
                "title": "Agent Commission & Deal Pipeline Split",
                "desc": "Track deal stages from Form A / Form B signing through trustee office transfer, with automated agent commission calculations."
            },
            {
                "icon": "📱",
                "title": "Mobile-First Broker Companion App",
                "desc": "Enable your agents on the road in Downtown, Marina, and Dubai Hills to log viewings and send brochures in seconds."
            }
        ],
        "steps": [
            {
                "num": "01",
                "title": "Private Beta with Leading Dubai Brokerages",
                "desc": "Currently deployed with select boutique and mid-market Dubai real estate firms to fine-tune Gulf transaction workflows."
            },
            {
                "num": "02",
                "title": "Portal & WhatsApp Gateway Calibration",
                "desc": "Optimizing instant lead assignment rules and WhatsApp Business API routing to ensure sub-minute response times."
            },
            {
                "num": "03",
                "title": "VIP Early Access Waitlist Rollout",
                "desc": "Inviting registered brokerages to experience the platform with customized onboarding and historical lead imports."
            },
            {
                "num": "04",
                "title": "Enterprise Customization & Team Training",
                "desc": "Full configuration of your brokerage's specific commission splits, branding, and team hierarchies."
            }
        ],
        "benefits": [
            {"metric": "< 30s", "title": "Portal Lead Assignment", "desc": "Connect portal inquiries to active brokers while the client is still viewing the listing."},
            {"metric": "+45%", "title": "Viewing Show-Up Rate", "desc": "Automated WhatsApp viewing reminders with location pins sent to buyers."},
            {"metric": "100%", "title": "Brokerage Lead Protection", "desc": "All client records and chat histories securely owned by the brokerage, not private agent phones."},
            {"metric": "VIP", "title": "Early Access Advantage", "desc": "Gain early access before your competing Dubai brokerages can acquire it."}
        ],
        "tech_stack": ["Node.js", "Python", "PostgreSQL", "WhatsApp API", "WebSockets", "Docker", "AWS UAE"],
        "faqs": [
            {
                "q": "How does this CRM capture leads from Property Finder and Bayut in Dubai?",
                "a": "The platform integrates with portal webhooks and email parsing listeners. When a prospect submits an inquiry, the CRM captures lead details, parses the listing reference code, and immediately notifies the assigned broker via WhatsApp."
            },
            {
                "q": "Can the brokerage protect its client database from departing agents?",
                "a": "Yes. Granular security permissions ensure agents only see their assigned deals while masking full contact numbers or preventing bulk exports, protecting your brokerage's valuable client rolodex."
            },
            {
                "q": "When will public access open for Dubai real estate agencies?",
                "a": "Private beta testing is concluding. Waitlist members will receive priority onboarding invitations starting Q3 2026."
            }
        ],
        "related": [
            {"title": "AI Business Conversions", "url": "/services/ai-business-automation", "desc": "Automate real estate lead qualification via conversational AI."},
            {"title": "Website Development", "url": "/services/website-and-software-development", "desc": "Build an ultra-fast Dubai real estate portal for your brokerage."},
            {"title": "Performance Digital Marketing", "url": "/services/digital-marketing", "desc": "Generate high-intent off-plan buyers with targeted Meta & Google Ads."}
        ]
    }
]

print("Site data dictionary verified successfully.")


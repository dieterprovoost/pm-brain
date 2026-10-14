"""
CMS Platform Selection Scorecard — Q8Oils / LOUNGE Website
───────────────────────────────────────────────────────────
Run from the project root:
  source /tmp/xlsx_env/bin/activate
  python3 skills/cms-platform-selection/scripts/generate_scorecard_q8oils.py
"""

import shutil
import datetime
from copy import copy
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter

CLIENT_NAME = "Q8Oils"

PLATFORMS = [
    "Storyblok",
    "Contentful",
    "Drupal",
]

# Each requirement: (label, weight, p1_score, p1_comment, p2_score, p2_comment, p3_score, p3_comment)
# Scores: 3 = Strong native | 2 = Partial / config needed | 1 = Weak / plugin-dependent | 0 = Hard blocker

CATEGORIES = [
    ("1. Architecture & Core Fit", [
        (
            "Headless / API-first architecture",
            5,
            3, "API-first with REST and GraphQL; strong SDKs for Next.js/Nuxt.",
            3, "Pioneer of headless CMS; mature REST and GraphQL APIs with excellent DX.",
            3, "Full JSON:API and GraphQL support in core; proven in large headless setups.",
        ),
        (
            "Azure hosting & self-hosting compatibility",
            5,
            2, "SaaS hosted by Storyblok; frontend can run on Azure but CMS infra is vendor-controlled.",
            2, "SaaS hosted by Contentful; frontend deployable on Azure; no IaC for the CMS layer.",
            3, "Fully self-hosted on Azure; IaC-ready; Q8Oils retains full infrastructure control.",
        ),
        (
            "SSO with Azure AD / Entra ID",
            5,
            3, "SAML-based SSO available on Enterprise plan; Azure AD configured as IdP.",
            3, "SAML SSO on Enterprise plan; Azure AD integration well-documented.",
            3, "simplesamlphp / OpenID Connect modules are mature; Azure AD integration battle-tested.",
        ),
        (
            "Multi-locale & multi-site content structure",
            5,
            3, "Field-level translation and dedicated locale spaces; story-level locale switching.",
            3, "Locale-aware content model; multi-environment and multi-locale natively supported.",
            3, "Best-in-class core multilingual; entity-level translation; multi-site via Domain Access.",
        ),
        (
            "Pimcore real-time API integration",
            5,
            3, "REST webhooks allow Pimcore to push updates; Management API creates/updates stories.",
            3, "CMA programmatic entry creation; Pimcore-to-Contentful push is a proven pattern.",
            3, "Custom Migrate or Feeds module; more implementation effort but full pipeline control.",
        ),
        (
            "GDPR compliance & data sovereignty",
            4,
            3, "ISO 27001 certified SaaS; EU data residency option; GDPR DPA available.",
            3, "SOC 2 Type II, ISO 27001; EU data residency; GDPR DPA available.",
            3, "Self-hosted on Azure; full data control; no third-party SaaS data sharing.",
        ),
        (
            "CI/CD pipeline & IaC support",
            4,
            2, "CMS config not versionable via IaC; frontend CI/CD works normally.",
            2, "CMA for content migrations; no native IaC; environment branching partially covers this.",
            3, "Config Management exports all config as YAML; Drush deploy; full IaC on Azure.",
        ),
    ]),

    ("2. Editor Experience", [
        (
            "Visual editor with in-context live preview",
            5,
            3, "Industry-leading Visual Editor; WYSIWYG block-by-block editing with live preview.",
            2, "Content Preview API available but no native WYSIWYG; Contentful Studio is improving.",
            2, "Layout Builder offers visual editing; less polished than headless SaaS alternatives.",
        ),
        (
            "Content scheduling by date and locale",
            5,
            3, "Story-level scheduling per locale natively supported.",
            3, "Launch feature enables scheduled publishing; locale-aware scheduling.",
            3, "Scheduler module supports date-based publishing per content item and locale.",
        ),
        (
            "Arabic RTL language support",
            5,
            2, "RTL text direction in content fields works; admin UI RTL support requires configuration.",
            1, "No native RTL admin UI; Arabic text fields work but editing UX is not RTL-optimised.",
            3, "Core RTL support for both admin UI and front-end; Arabic direction natively handled.",
        ),
        (
            "Version history & content revert",
            4,
            3, "Full version history on all stories; one-click revert to any previous version.",
            3, "Versions stored per entry; restore to any earlier version available.",
            3, "Native revisions on all content entities; revision comparison and revert built in.",
        ),
        (
            "AI-assisted translation workflow",
            4,
            2, "Phrase, DeepL, and AI translation integrations in Marketplace; not fully native.",
            2, "Phrase / Lokalise integrations available; AI translation via third-party apps.",
            2, "TMGMT module with DeepL / Google Translate providers; mature but requires configuration.",
        ),
        (
            "Multi-role editorial workflow (draft → review → approve → publish)",
            5,
            3, "Approval workflow with custom roles on Enterprise; locale-aware publishing control.",
            2, "Content workflow via Tasks; less granular than Storyblok or Drupal without add-ons.",
            3, "Content Moderation module provides configurable workflow states per locale.",
        ),
    ]),

    ("3. Editorial Autonomy (No Developer)", [
        (
            "Redirect manager with chain detection",
            4,
            1, "No native redirect manager; third-party tool or custom middleware required.",
            1, "No native redirect manager; external tooling or CDN-level redirects required.",
            3, "Redirect module with chain detection and audit log; fully editor-managed.",
        ),
        (
            "SEO metadata management per page",
            5,
            3, "SEO plugin provides editable meta title, description, og tags per story.",
            3, "SEO content type pattern is well-established; fully editor-managed.",
            3, "Metatag module covers all SEO fields; Pathauto for URL patterns; editor-friendly.",
        ),
        (
            "Form builder for lead capture & gated downloads",
            4,
            1, "No native form builder; forms require HubSpot, Marketo, or custom front-end.",
            1, "No native forms; integration with HubSpot or custom frontend required.",
            3, "Webform module is best-in-class; gated downloads with conditional logic built in.",
        ),
        (
            "Cookie consent management (CMP integration)",
            4,
            2, "Third-party CMP (OneTrust, CookieFirst) injected via GTM; no native consent tool.",
            2, "CMP injected via GTM or script injection; not native to the CMS.",
            3, "EU Cookie Compliance module or custom CMP; consent logic manageable without dev.",
        ),
        (
            "Enhanced mega menu management",
            4,
            2, "Navigation modelled as a content type; no native visual mega menu builder.",
            2, "Navigation as structured content; editors manage via content model.",
            3, "Mega Menu module with drag-and-drop; configurable showcase column per menu item.",
        ),
        (
            "Reusable component / block library",
            5,
            3, "Blok library is the core strength; all components reusable and composable.",
            3, "Modular content model with References; strong component reuse pattern.",
            3, "Paragraphs + Layout Builder; all components reusable across content types.",
        ),
    ]),

    ("4. Content Architecture & Governance", [
        (
            "Structured page builder with configurable blocks",
            5,
            3, "Block-based page composition is Storyblok's flagship use case.",
            3, "Rich content modelling with References enables block-based composition.",
            3, "Layout Builder + Paragraphs support all required block types natively.",
        ),
        (
            "Article / blog content type with taxonomy",
            4,
            3, "Custom content types and taxonomy stories; related articles via references.",
            3, "Fully customisable content types; taxonomy via entries and references.",
            3, "Article content type with Taxonomy module; Views for related content.",
        ),
        (
            "Brandfolder DAM sync (bi-directional, metadata)",
            4,
            2, "Brandfolder connector in Marketplace; metadata sync requires configuration.",
            2, "Brandfolder integration via API or DAM app; metadata sync feasible with dev effort.",
            2, "Custom media integration module required; no off-the-shelf Brandfolder connector.",
        ),
        (
            "Country / locale-specific compliance pages",
            3,
            3, "Per-locale story visibility manageable via folder structure and access rules.",
            3, "Locale-scoped content and environment rules support market-specific pages.",
            3, "Domain Access + Language module controls locale visibility at entity level.",
        ),
        (
            "Structured data / schema.org markup",
            4,
            2, "JSON-LD must be implemented in frontend; no native schema.org CMS tooling.",
            2, "Schema.org fields modelled manually; JSON-LD rendered in frontend.",
            3, "Schema.org Blueprints module generates structured data from content types natively.",
        ),
        (
            "Gated downloads with lead-capture form (PDS / SDS)",
            4,
            1, "No native gated download flow; requires HubSpot form + custom frontend logic.",
            1, "No native gated content; external form tool and conditional rendering required.",
            3, "Webform with file conditional access; sector-based routing natively achievable.",
        ),
    ]),

    ("5. Product Catalogue & Data Integrations", [
        (
            "Pimcore PIM sync for auto-generated product pages",
            5,
            3, "Webhook-driven import from Pimcore; Management API creates/updates stories.",
            3, "CMA programmatic entry creation; Pimcore-to-Contentful push is a proven pattern.",
            2, "Custom Migrate or Feeds module required; more effort but full pipeline control.",
        ),
        (
            "Dynamic product filtering with zero-result hiding",
            5,
            2, "Filtering in frontend + search engine (Algolia/Typesense); CMS provides data.",
            2, "Same architecture; filtering in frontend/search layer; Contentful serves product data.",
            3, "Search API + Facets module handles dynamic filtering with zero-result hiding natively.",
        ),
        (
            "On-site search engine integration",
            4,
            2, "Integrates with Algolia, Typesense, or MeiliSearch; no native CMS search.",
            2, "Integrates with Algolia or Coveo; no native CMS search engine.",
            3, "Search API + Solr / Elasticsearch / Typesense; rich faceting with native indexing.",
        ),
        (
            "Product cross-reference / equivalence tool",
            4,
            2, "Data model supports it; tool logic implemented in frontend using Pimcore data.",
            2, "Same; Pimcore data surfaced via API; tool logic in frontend.",
            3, "Views + Search API can power cross-reference tool without custom frontend work.",
        ),
        (
            "Dealer locator with Google Maps integration",
            4,
            2, "CMS stores dealer data; Google Maps integration in frontend; no native map component.",
            2, "Dealer content type in Contentful; map logic in frontend.",
            3, "Geofield + Geolocation modules provide native dealer locator with map integration.",
        ),
        (
            "CRM integration for lead forms (HubSpot / Salesforce)",
            3,
            2, "HubSpot forms embedded directly or via GTM; form data routed to CRM.",
            2, "Same approach; CRM integration via frontend form handling or GTM.",
            2, "Webform HubSpot / Salesforce handlers; solid integration but requires module setup.",
        ),
    ]),

    ("6. SEO, Compliance & Optimisation", [
        (
            "SEO metadata, canonical tags, hreflang management",
            5,
            3, "SEO plugin provides full meta control; hreflang per locale; canonical configurable.",
            3, "SEO fields in content model; hreflang managed in frontend; canonical configurable.",
            3, "Metatag + Pathauto + Redirect modules; hreflang auto-generated; canonical native.",
        ),
        (
            "WCAG 2.1 AA accessibility support",
            5,
            2, "WCAG compliance depends on frontend implementation; CMS output is clean.",
            2, "Same; accessible front-end depends on implementation team.",
            3, "Drupal core has strong WCAG commitment; accessibility checking built into admin UI.",
        ),
        (
            "Native A/B testing capability",
            5,
            2, "A/B testing on Enterprise plan; story-level variant testing supported.",
            1, "No native A/B; Contentful Personalize (Ninetailed) is a separate paid add-on.",
            2, "Smart Content module enables rule-based personalisation and A/B testing; less polished.",
        ),
        (
            "Geo-based content personalisation",
            3,
            1, "Not native; requires CDN-level (Cloudflare Workers) or middleware personalisation.",
            1, "Ninetailed (separate product) required; not included in base Contentful.",
            2, "Smart Content + Geofield modules support geo-based display rules natively.",
        ),
        (
            "Analytics integration (PiwikPro + event tracking)",
            4,
            3, "GTM injection straightforward; PiwikPro tag manager works natively.",
            3, "GTM / PiwikPro injected in frontend; no CMS-level restriction.",
            3, "PiwikPro module available; GTM integration via module or theme hook.",
        ),
        (
            "Automated XML sitemap & robots.txt management",
            3,
            3, "Sitemap via frontend (Next Sitemap); robots.txt configurable in deployment.",
            3, "Same frontend-driven approach; no CMS-native sitemap generation.",
            3, "Simple XML Sitemap module auto-generates on publish; Robots.txt module is editor-friendly.",
        ),
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# Generator — no edits needed below this line.
# ══════════════════════════════════════════════════════════════════════════════

TEMPLATE = Path("templates/cms-platform-selection/CMS-selection-scorecard-template.xlsx")
OUTPUT   = Path(f"deliverables/{CLIENT_NAME}-CMS-Platform-Selection-Scorecard.xlsx")


def _freeze(cell):
    return {
        "font":   copy(cell.font),
        "fill":   copy(cell.fill),
        "border": copy(cell.border),
        "align":  copy(cell.alignment),
        "numfmt": cell.number_format,
    }


def _apply(cell, style: dict):
    cell.font          = copy(style["font"])
    cell.fill          = copy(style["fill"])
    cell.border        = copy(style["border"])
    cell.alignment     = copy(style["align"])
    cell.number_format = style["numfmt"]


def generate():
    assert TEMPLATE.exists(), f"Template not found: {TEMPLATE}"
    assert len(PLATFORMS) == 3, "Exactly 3 platform names required."
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(TEMPLATE, OUTPUT)

    wb = openpyxl.load_workbook(OUTPUT)
    ws = wb["CMS Scorecard"]

    S = {
        "cat_hdr":   _freeze(ws["A10"]),
        "cat_hdr_c": _freeze(ws["C10"]),
        "cat_hdr_d": _freeze(ws["D10"]),
        "req_b":     _freeze(ws["B11"]),
        "req_c":     _freeze(ws["C11"]),
        "req_d":     _freeze(ws["D11"]),
        "req_e":     _freeze(ws["E11"]),
        "req_f":     _freeze(ws["F11"]),
        "total_b":   _freeze(ws["B15"]),
        "total_d":   _freeze(ws["D15"]),
        "total_e":   _freeze(ws["E15"]),
        "grand_b":   _freeze(ws["B65"]),
        "grand_d":   _freeze(ws["D65"]),
        "grand_e":   _freeze(ws["E65"]),
        "max_b":     _freeze(ws["B66"]),
        "max_d":     _freeze(ws["D66"]),
        "pct_b":     _freeze(ws["B67"]),
        "pct_d":     _freeze(ws["D67"]),
        "pct_e":     _freeze(ws["E67"]),
    }

    for merge in list(ws.merged_cells.ranges):
        if merge.min_row >= 10:
            ws.unmerge_cells(str(merge))
    for r in range(10, ws.max_row + 1):
        for c in range(1, 13):
            ws.cell(r, c).value = None

    try:
        ws["B3"] = datetime.date.today()
    except Exception:
        pass

    for idx, (name, col) in enumerate(zip(PLATFORMS, [4, 7, 10])):
        ws.cell(9, col).value = name

    row = 10
    total_rows: list[int] = []

    for cat_name, reqs in CATEGORIES:
        _apply(ws.cell(row, 1, cat_name), S["cat_hdr"])
        _apply(ws.cell(row, 2, None),     S["cat_hdr"])
        _apply(ws.cell(row, 3, "Weight (1-5)"), S["cat_hdr_c"])
        for col in [4, 7, 10]:
            _apply(ws.cell(row, col,   "Score (0-3)"),              S["cat_hdr_d"])
            _apply(ws.cell(row, col+1, "Weighted score"),           S["cat_hdr_d"])
            _apply(ws.cell(row, col+2, "Comments / justification"), S["cat_hdr_d"])
        row += 1
        req_start = row

        for label, weight, s1, c1, s2, c2, s3, c3 in reqs:
            ws.cell(row, 1).value = None
            _apply(ws.cell(row, 2, label),  S["req_b"])
            _apply(ws.cell(row, 3, weight), S["req_c"])

            for score, comment, sc_col, ws_col, cm_col in [
                (s1, c1,  4,  5,  6),
                (s2, c2,  7,  8,  9),
                (s3, c3, 10, 11, 12),
            ]:
                _apply(ws.cell(row, sc_col, score), S["req_d"])
                _apply(ws.cell(row, ws_col,
                               f"=C{row}*{get_column_letter(sc_col)}{row}"), S["req_e"])
                _apply(ws.cell(row, cm_col, comment), S["req_f"])
            row += 1

        req_end = row - 1

        total_rows.append(row)
        ws.cell(row, 1).value = None
        _apply(ws.cell(row, 2, "TOTAL"), S["total_b"])
        ws.cell(row, 3).value = None
        for sc_col, ws_col in [(4, 5), (7, 8), (10, 11)]:
            cl = get_column_letter
            _apply(ws.cell(row, sc_col,
                           f"=SUM({cl(sc_col)}{req_start}:{cl(sc_col)}{req_end})"),
                   S["total_d"])
            _apply(ws.cell(row, ws_col,
                           f"=SUM({cl(ws_col)}{req_start}:{cl(ws_col)}{req_end})"),
                   S["total_e"])
        row += 2

    for col, hdr in [(4, "Score"), (5, "Weighted score"),
                     (7, "Score"), (8, "Weighted score"),
                     (10, "Score"), (11, "Weighted score")]:
        c = ws.cell(row, col, hdr)
        c.font = Font(bold=True)
        c.alignment = Alignment(horizontal="center", wrap_text=True)
    row += 1

    grand_row = row
    _apply(ws.cell(row, 2, "GRAND TOTAL SCORE"), S["grand_b"])
    ws.cell(row, 3).value = None
    for sc_col, ws_col in [(4, 5), (7, 8), (10, 11)]:
        cl = get_column_letter
        _apply(ws.cell(row, sc_col,
                       "=" + "+".join(f"{cl(sc_col)}{r}" for r in total_rows)),
               S["grand_d"])
        _apply(ws.cell(row, ws_col,
                       "=" + "+".join(f"{cl(ws_col)}{r}" for r in total_rows)),
               S["grand_e"])
    row += 1

    max_row = row
    total_reqs = sum(len(r) for _, r in CATEGORIES)
    _apply(ws.cell(row, 2, "Max total score"), S["max_b"])
    ws.cell(row, 3).value = None
    for sc_col, ws_col in [(4, 5), (7, 8), (10, 11)]:
        cl = get_column_letter
        _apply(ws.cell(row, sc_col, f"={total_reqs}*3"),      S["max_d"])
        _apply(ws.cell(row, ws_col, f"=5*{cl(sc_col)}{row}"), S["max_d"])
    row += 1

    _apply(ws.cell(row, 2, "%"), S["pct_b"])
    ws.cell(row, 3).value = None
    for sc_col, ws_col in [(4, 5), (7, 8), (10, 11)]:
        cl = get_column_letter
        pct_sc = ws.cell(row, sc_col,
                         f"={cl(sc_col)}{grand_row}/{cl(sc_col)}{max_row}")
        _apply(pct_sc, S["pct_d"]); pct_sc.number_format = "0%"
        pct_ws = ws.cell(row, ws_col,
                         f"={cl(ws_col)}{grand_row}/{cl(ws_col)}{max_row}")
        _apply(pct_ws, S["pct_e"]); pct_ws.number_format = "0%"

    wrap_top_left = Alignment(wrap_text=True, vertical="top", horizontal="left")
    for r in range(10, row + 1):
        ws.row_dimensions[r].height = 55
        for c in range(1, 13):
            ws.cell(r, c).alignment = copy(wrap_top_left)

    wb.save(OUTPUT)
    print(f"✓  {OUTPUT}")
    print(f"   {total_reqs} requirements · {len(CATEGORIES)} categories · {len(PLATFORMS)} platforms")
    print(f"   TOTAL rows : {total_rows}")
    print(f"   Grand total: row {grand_row} · Max score: row {max_row}")


if __name__ == "__main__":
    generate()

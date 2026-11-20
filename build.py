#!/usr/bin/env python3
"""Builds the Mola website into static HTML (GitHub Pages serves the repository root).

    python3 build.py

Pages: landing (tr at /, en at /en/), privacy (gizlilik, en/privacy), terms (kosullar, en/terms), KVKK, deleting your
data (hesap-silme, en/delete-account), support (destek, en/support), 404, sitemap.xml. Legal and help pages are
Markdown in src/*.md (the legal texts are copies of the app repository's docs/legal, tools/import_legal.py); this
script renders them and wraps them in the shared header and footer. Every link is relative, so the site works both at
https://mhmtmutlu.github.io/mola-app/ and at https://mola.mm-apps.com/. No cookies, no analytics, no third-party
requests: the font is self-hosted.
"""
import html, json, pathlib, re

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"
SITE_URL = "https://mola.mm-apps.com/"
CONTACT = "destek@mm-apps.com"

# The single switch for launch day: True turns the App Store badge into a real link and drops "coming soon".
APP_STORE_LIVE = False
APP_ID = ""
APP_STORE_URL = f"https://apps.apple.com/app/id{APP_ID}"
PUBLISHER = {"@type": "Organization", "@id": "https://mm-apps.com/#org", "name": "mm-apps",
             "url": "https://mm-apps.com/", "email": CONTACT}
# Site languages in menu order: code → (its own name, Open Graph locale). A language is built once
# src/landing.<code>.json exists; the app speaks the same fifteen.
LANGUAGES = {
    "tr": ("Türkçe", "tr_TR"), "en": ("English", "en_US"), "de": ("Deutsch", "de_DE"), "fr": ("Français", "fr_FR"),
    "es": ("Español", "es_ES"), "pt-BR": ("Português (Brasil)", "pt_BR"), "it": ("Italiano", "it_IT"),
    "nl": ("Nederlands", "nl_NL"), "pl": ("Polski", "pl_PL"), "ja": ("日本語", "ja_JP"), "ko": ("한국어", "ko_KR"),
    "zh-Hant": ("繁體中文", "zh_TW"), "zh-Hans": ("简体中文", "zh_CN"), "id": ("Bahasa Indonesia", "id_ID"),
    "ar": ("العربية", "ar_SA"),
}
RTL = {"ar"}
# Search and answer-engine crawlers are named so that a later "Disallow" for one of them is a decision, not a default.
CRAWLERS = ["Googlebot", "Bingbot", "Applebot", "Applebot-Extended", "DuckDuckBot", "YandexBot", "GPTBot",
            "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot",
            "Perplexity-User", "Google-Extended", "CCBot"]


def esc(text):
    return html.escape(str(text), quote=True)


# ----------------------------------------------------------------------------------------------- markdown
URL = re.compile(r"(https?://[^\s<)]+[^\s<).,;:])")
EMAIL = re.compile(r"(?<![\w/>.])([\w.+-]+@[\w-]+\.[\w.-]+\w)")
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def inline(text):
    """Escapes, then **bold**, [text](href), bare URLs and e-mail addresses."""
    placeholders = []

    def hold(markup):
        placeholders.append(markup)
        return f"\x00{len(placeholders) - 1}\x00"

    text = LINK.sub(lambda m: hold(f'<a href="{esc(m.group(2))}">{esc(m.group(1))}</a>'), text)
    text = URL.sub(lambda m: hold(f'<a href="{esc(m.group(1))}">{esc(m.group(1))}</a>'), text)
    text = EMAIL.sub(lambda m: hold(f'<a href="mailto:{esc(m.group(1))}">{esc(m.group(1))}</a>'), text)
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: placeholders[int(m.group(1))], text)


def slug(text):
    text = re.sub(r"[^\w\s-]", "", text.lower(), flags=re.UNICODE)
    return re.sub(r"\s+", "-", text.strip())


def table(rows):
    cells = [[c.strip() for c in row.strip().strip("|").split("|")] for row in rows]
    head, body = cells[0], cells[2:]
    out = ['<div class="table"><table>']
    if any(head):
        out.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>")
    out.append("<tbody>")
    for row in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def bullets(lines):
    """A list with one level of nesting ('  - '); wrapped lines continue their item."""
    items = []
    for line in lines:
        nested = re.match(r"^\s{2,}[-*] (.*)", line)
        top = re.match(r"^[-*] (.*)", line)
        ordered = re.match(r"^\d+\. (.*)", line)
        if top or ordered:
            items.append({"text": (top or ordered).group(1), "sub": []})
        elif nested and items:
            items[-1]["sub"].append(nested.group(1))
        elif items and items[-1]["sub"]:
            items[-1]["sub"][-1] += " " + line.strip()
        elif items:
            items[-1]["text"] += " " + line.strip()
    tag = "ol" if re.match(r"^\d+\. ", lines[0]) else "ul"
    parts = []
    for item in items:
        sub = "<ul>" + "".join(f"<li>{inline(s)}</li>" for s in item["sub"]) + "</ul>" if item["sub"] else ""
        parts.append(f"<li>{inline(item['text'])}{sub}</li>")
    return f"<{tag}>" + "".join(parts) + f"</{tag}>"


def markdown(text):
    """(title, html). The first heading is the page title; the subset the documents use, no dependency."""
    lines = text.replace("\r\n", "\n").split("\n")
    title, out, i = None, [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            content = line[level:].strip()
            if level == 1 and title is None:
                title = content
            else:
                out.append(f'<h{level} id="{esc(slug(content))}">{inline(content)}</h{level}>')
            i += 1
        elif line.strip() == "---":
            out.append("<hr>")
            i += 1
        elif line.lstrip().startswith("|"):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            out.append(table(lines[i:j]))
            i = j
        elif re.match(r"^([-*]|\d+\.) ", line):
            j = i
            while j < len(lines) and lines[j].strip() and not lines[j].startswith("#") and not lines[j].lstrip().startswith("|"):
                if j > i and not re.match(r"^(\s*[-*]|\d+\.) |^\s+\S", lines[j]):
                    break
                j += 1
            out.append(bullets(lines[i:j]))
            i = j
        else:
            j = i
            while j < len(lines) and lines[j].strip() and not re.match(r"^(#|\||[-*] |\d+\. )", lines[j]) and lines[j].strip() != "---":
                j += 1
            out.append("<p>" + inline(" ".join(part.strip() for part in lines[i:j])) + "</p>")
            i = j
    if title is None:
        raise SystemExit("a document must start with a '# ' title")
    return title, "\n".join(out)


# ----------------------------------------------------------------------------------------------- pages
# path of each page per language, relative to the site root ("" = the root itself)
PAGES = {
    "home": {"tr": "", "en": "en/"},
    "privacy": {"tr": "gizlilik/", "en": "en/privacy/"},
    "terms": {"tr": "kosullar/", "en": "en/terms/"},
    "kvkk": {"tr": "kvkk/"},
    "delete": {"tr": "hesap-silme/", "en": "en/delete-account/"},
    "support": {"tr": "destek/", "en": "en/support/"},
    "guide-block": {"tr": "rehber/uygulama-engelleme/", "en": "en/guides/block-apps/"},
    "guide-limit": {"tr": "rehber/gunluk-sure-siniri/", "en": "en/guides/daily-time-limit/"},
    "guide-pomodoro": {"tr": "rehber/pomodoro-teknigi/", "en": "en/guides/pomodoro-technique/"},
}
GUIDES = [key for key in PAGES if key.startswith("guide-")]
# The landing copy lives in src/landing.<lang>.json, so it can be reviewed and translated as text.
S = {lang: json.loads((SRC / f"landing.{lang}.json").read_text(encoding="utf-8"))
     for lang in LANGUAGES if (SRC / f"landing.{lang}.json").exists()}
# Every other language lives under /<code>/ with the English path names. A page exists in a language when its text
# does: the legal texts are binding in Turkish and English only, so other languages link to the English ones.
for _key, _paths in PAGES.items():
    for _lang in S:
        if _lang not in _paths and (_key == "home" or (SRC / f"{_key}.{_lang}.md").exists()):
            _paths[_lang] = f"{_lang.lower()}/" + _paths["en"][len("en/"):]


def page_path(key, lang):
    """The page in this language, or in English where it is not translated (Turkish for the KVKK notice)."""
    return PAGES[key].get(lang) or PAGES[key].get("en") or PAGES[key]["tr"]

DOCS = ["privacy", "terms", "kvkk", "delete", "support", *GUIDES]
# The day the guides were last checked against iOS and the app; shown on the page and in its structured data.
GUIDES_UPDATED = "2026-11-17"

# Screenshots a landing page needs (assets/shots/<name>-<lang>.png, made with tools/shots.sh in the app repository).
SHOT_WIDTH, SHOT_HEIGHT = 603, 1311


def rel(from_path, to_path):
    """A relative link between two site paths ('en/privacy/' → '../../assets/site.css')."""
    return "../" * from_path.count("/") + to_path


def alternates(key):
    """hreflang links of a page that exists in more than one language; English is the default for other languages."""
    paths = PAGES[key]
    if len(paths) < 2:
        return ""
    links = [f'<link rel="alternate" hreflang="{lang}" href="{SITE_URL}{path}">' for lang, path in paths.items()]
    links.append(f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}{paths.get("en", paths["tr"])}">')
    return "\n".join(links) + "\n"


def graph(lang, path, title, description, extra=()):
    """The page's JSON-LD: who publishes the site, the site, this page, and whatever the page adds."""
    site = {"@type": "WebSite", "@id": f"{SITE_URL}#website", "url": SITE_URL, "name": "Mola",
            "publisher": {"@id": PUBLISHER["@id"]}, "inLanguage": list(S)}
    page = {"@type": "WebPage", "@id": f"{SITE_URL}{path}#webpage", "url": f"{SITE_URL}{path}", "name": title,
            "description": description, "inLanguage": lang, "isPartOf": {"@id": site["@id"]}}
    data = {"@context": "https://schema.org", "@graph": [PUBLISHER, site, page, *extra]}
    return ('<script type="application/ld+json">'
            + json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>\n")


def shell(lang, path, title, description, body, key, extra=(), index=True):
    t = S[lang]
    home = rel(path, PAGES["home"][lang])
    # every language this page (or, failing that, the home page) exists in
    choices = "".join(
        f'<li><a href="{rel(path, PAGES[key].get(code, PAGES["home"][code]))}" lang="{code}" hreflang="{code}"'
        f'{" aria-current=\"true\"" if code == lang else ""}>{esc(LANGUAGES[code][0])}</a></li>' for code in S)
    top = "".join(f'<a href="{home}#{anchor}">{esc(label)}</a>' for anchor, label in t["nav"].items())
    foot = "".join(f'<a href="{rel(path, page_path(k, lang))}">{esc(label)}</a>' for k, label in t["foot_nav"].items()
                   if k != "kvkk" or lang == "tr")
    return f"""<!doctype html>
<html lang="{lang}"{' dir="rtl"' if lang in RTL else ''}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
{f'<link rel="canonical" href="{SITE_URL}{path}">' if index else '<meta name="robots" content="noindex">'}
{alternates(key) if index else ''}{f'<meta name="apple-itunes-app" content="app-id={APP_ID}">' if APP_STORE_LIVE else ''}
<link rel="icon" href="{rel(path, 'assets/icon-64.png')}">
<link rel="apple-touch-icon" href="{rel(path, 'assets/icon-180.png')}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Mola">
<meta property="og:locale" content="{LANGUAGES[lang][1]}">
<meta property="og:url" content="{SITE_URL}{path}">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{SITE_URL}assets/{'og.jpg' if lang == 'tr' else 'og-en.jpg'}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="theme-color" content="#F3EEE6" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#15130F" media="(prefers-color-scheme: dark)">
<link rel="stylesheet" href="{rel(path, 'assets/site.css')}">
{graph(lang, path, title, description, extra) if index else ''}</head>
<body>
<a class="skip" href="#main">{esc(t['skip'])}</a>
<header class="top">
<a class="brand" href="{home}"><img src="{rel(path, 'assets/icon-180.png')}" alt="" width="36" height="36"><span>Mola</span></a>
<nav class="menu" aria-label="{esc(t['menu_label'])}">{top}</nav>
<details class="langs"><summary aria-label="{esc(t['language_label'])}">{esc(LANGUAGES[lang][0])}</summary><ul>{choices}</ul></details>
</header>
<main id="main">
{body}
</main>
<footer>
<div class="foot">
<a class="brand" href="{home}"><img src="{rel(path, 'assets/icon-180.png')}" alt="" width="32" height="32"><span>Mola</span></a>
<nav aria-label="{esc(t['foot_label'])}">{foot}</nav>
</div>
<p>{esc(t['footer'])} <a href="mailto:{CONTACT}">{CONTACT}</a> · <a href="https://mm-apps.com/{'en/' if lang == 'en' else ''}">{esc(t['more_apps'])}</a></p>
</footer>
</body>
</html>
"""


def badge(lang):
    t = S[lang]["hero"]
    if APP_STORE_LIVE:
        return f'<a class="button" href="{APP_STORE_URL}">{esc(t["store"])}</a>'
    return f'<span class="button soon">{esc(t["soon"])}</span>'


def phone(path, name, lang, alt, eager=False, night=False):
    """A screenshot in a plain device frame."""
    # a language without its own screenshots shows the English ones
    shot_lang = lang if (ROOT / f"assets/shots/{name}-{lang}.png").exists() else "en"
    source = rel(path, f"assets/shots/{name}-{shot_lang}.png")
    loading = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<div class="phone{" night" if night else ""}"><img src="{source}" alt="{esc(alt)}" '
            f'width="{SHOT_WIDTH}" height="{SHOT_HEIGHT}" {loading}></div>')


def landing(lang):
    t, path = S[lang], PAGES["home"][lang]
    hero, family, privacy = t["hero"], t["family"], t["privacy"]
    steps = "".join(f'<li><span class="num" aria-hidden="true">{n}</span><h3>{esc(title)}</h3><p>{esc(text)}</p></li>'
                    for n, (title, text) in enumerate(t["steps"], 1))
    features = ""
    for index, feature in enumerate(t["features"]):
        points = "".join(f"<li>{esc(point)}</li>" for point in feature["points"])
        night = feature["shot"] in ("focus", "wall")
        features += f"""<article class="feature{' flip' if index % 2 else ''}">
<div class="copy">
<p class="tag tint{index % 4}">{esc(feature['tag'])}</p>
<h3>{esc(feature['title'])}</h3>
<p>{esc(feature['text'])}</p>
<ul class="ticks">{points}</ul>
</div>
{phone(path, feature['shot'], lang, feature['alt'], night=night)}
</article>
"""
    extras = "".join(f'<article class="card"><h3>{esc(title)}</h3><p>{esc(text)}</p></article>'
                     for title, text in t["extras"])
    family_points = "".join(f"<li><h3>{esc(title)}</h3><p>{esc(text)}</p></li>" for title, text in family["points"])
    privacy_points = "".join(f"<li>{esc(point)}</li>" for point in privacy["points"])
    faq = "".join(f"<details><summary>{esc(question)}</summary><p>{esc(answer)}</p></details>"
                  for question, answer in t["faq"])
    guides = "".join(f'<article class="card"><h3><a href="{rel(path, page_path(key, lang))}">{esc(title)}</a></h3>'
                     f"<p>{esc(text)}</p></article>" for key, title, text in t["guides"])
    body = f"""<section class="hero">
<div class="copy">
<p class="eyebrow">{esc(hero['eyebrow'])}</p>
<h1>{esc(hero['headline'])}</h1>
<p class="lead">{esc(hero['lead'])}</p>
<p class="actions">{badge(lang)}</p>
<p class="fine">{esc(hero['note'])}</p>
</div>
<div class="stage">{phone(path, 'today', lang, hero['alt'], eager=True)}</div>
</section>

<section class="steps" aria-labelledby="steps-title">
<h2 id="steps-title">{esc(t['steps_title'])}</h2>
<ol>{steps}</ol>
</section>

<section id="features" aria-labelledby="features-title">
<h2 id="features-title" class="center">{esc(t['features_title'])}</h2>
{features}
<div class="grid">{extras}</div>
</section>

<section id="family" class="band" aria-labelledby="family-title">
<div class="copy">
<p class="tag tint2">{esc(family['tag'])}</p>
<h2 id="family-title">{esc(family['title'])}</h2>
<p>{esc(family['text'])}</p>
<ul class="pairs">{family_points}</ul>
<p class="fine">{esc(family['note'])}</p>
</div>
<div class="duo">
{phone(path, 'parent', lang, family['alt_parent'])}
{phone(path, 'child', lang, family['alt_child'])}
</div>
</section>

<section id="privacy" class="split" aria-labelledby="privacy-title">
<div>
<p class="tag tint0">{esc(privacy['tag'])}</p>
<h2 id="privacy-title">{esc(privacy['title'])}</h2>
<p>{esc(privacy['text'])}</p>
<p><a href="{rel(path, page_path('privacy', lang))}">{esc(privacy['more'])}</a></p>
</div>
<ul class="ticks card">{privacy_points}</ul>
</section>

<section id="faq" class="faq" aria-labelledby="faq-title">
<h2 id="faq-title">{esc(t['faq_title'])}</h2>
{faq}
</section>

<section id="guides" class="guides" aria-labelledby="guides-title">
<h2 id="guides-title">{esc(t['guides_title'])}</h2>
<div class="grid">{guides}</div>
</section>

<section class="cta">
<img src="{rel(path, 'assets/icon-512.png')}" alt="" width="88" height="88" loading="lazy">
<h2>{esc(t['cta']['title'])}</h2>
<p>{esc(t['cta']['text'])}</p>
{badge(lang) if APP_STORE_LIVE else ''}
</section>"""
    app = {"@type": ["MobileApplication", "SoftwareApplication"], "@id": f"{SITE_URL}#app", "name": "Mola",
           "description": t["description"], "url": f"{SITE_URL}{path}", "operatingSystem": "iOS 18, iPadOS 18, watchOS 11",
           "applicationCategory": "ProductivityApplication", "inLanguage": lang, "publisher": {"@id": PUBLISHER["@id"]},
           "image": f"{SITE_URL}assets/icon-512.png",
           "screenshot": [f"{SITE_URL}assets/shots/{name}-{lang if (ROOT / f'assets/shots/{name}-{lang}.png').exists() else 'en'}.png"
                          for name in ("today", "plan", "focus", "wall")]}
    if APP_STORE_LIVE:
        app["downloadUrl"] = APP_STORE_URL
    # The questions and answers are the ones on the page, word for word.
    questions = {"@type": "FAQPage", "@id": f"{SITE_URL}{path}#faq", "mainEntity": [
        {"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}}
        for question, answer in t["faq"]]}
    write(path, shell(lang, path, t["title"], t["description"], body, "home", extra=(app, questions)))


def document(key, lang):
    path = PAGES[key][lang]
    title, body = markdown((SRC / f"{key}.{lang}.md").read_text(encoding="utf-8"))
    t = S[lang]
    description, extra, stamp = title, (), ""
    if key in GUIDES:
        # A guide answers its question in its first paragraph; that paragraph is also its description.
        description = html.unescape(re.sub(r"<[^>]+>", "", re.search(r"<p>(.*?)</p>", body, re.S).group(1)))
        extra = ({"@type": "Article", "@id": f"{SITE_URL}{path}#article", "headline": title, "description": description,
                  "inLanguage": lang, "dateModified": GUIDES_UPDATED, "mainEntityOfPage": f"{SITE_URL}{path}",
                  "author": {"@id": PUBLISHER["@id"]}, "publisher": {"@id": PUBLISHER["@id"]},
                  "about": {"@id": f"{SITE_URL}#app"}},)
        stamp = f'<p class="fine">{esc(t["updated"])}: <time datetime="{GUIDES_UPDATED}">{GUIDES_UPDATED}</time></p>'
    page = f'<article class="doc"><p class="crumb"><a href="{rel(path, PAGES["home"][lang])}">{esc(t["back"])}</a></p><h1>{esc(title)}</h1>\n{body}\n{stamp}</article>'
    write(path, shell(lang, path, f"{title} · Mola", description, page, key, extra=extra))


def llms():
    """A plain summary for answer engines, made from the same copy as the pages so the two cannot disagree."""
    t = S["en"]
    facts = [("Platforms", "iPhone (iOS 18 or later) and iPad (iPadOS 18 or later); a focus timer on Apple Watch (watchOS 11 or later)"),
             ("Sign-up", "none (no email, no password); the family feature pairs devices with a QR code and asks only for a display name"),
             ("Price", "free for your own use; the family feature is a monthly or yearly subscription bought through Apple"),
             ("Ads, tracking, analytics", "none"),
             ("Where data lives", t["privacy"]["points"][1]),
             ("Languages", t["extras"][3][1]),
             ("App Store", APP_STORE_URL if APP_STORE_LIVE else "not released yet"),
             ("Publisher", f"{PUBLISHER['name']} ({PUBLISHER['url']}), {CONTACT}")]
    names = {"home": "Overview", "privacy": "Privacy policy", "terms": "Terms of use", "delete": "Deleting your data",
             "support": "Support"}
    out = ["# Mola", "", f"> {t['description']}", "", "## Facts", ""]
    out += [f"- {label}: {value}" for label, value in facts]
    out += ["", "## What it does", ""] + [f"- {f['title']}: {f['text']}" for f in t["features"]]
    out += ["", "## Questions", ""] + [f"- {q} {a}" for q, a in t["faq"]]
    out += ["", "## Pages", ""] + [f"- [{names[k]}]({SITE_URL}{PAGES[k]['en']})" for k in names]
    out += ["", "## Guides", ""] + [f"- [{title}]({SITE_URL}{PAGES[k]['en']}): {text}" for k, title, text in t["guides"]]
    out += ["", "## Türkçe", ""] + [f"- [{S['tr']['foot_nav'].get(k, 'Mola')}]({SITE_URL}{PAGES[k]['tr']})"
                                     for k in PAGES if k not in GUIDES]
    out += [f"- [{title}]({SITE_URL}{PAGES[k]['tr']})" for k, title, _ in S["tr"]["guides"]]
    return "\n".join(out) + "\n"


written = []


def write(path, content):
    target = ROOT / path / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    written.append(path)


def check_links():
    """Every relative link and asset of every written page must exist."""
    missing = []
    for path in written:
        page = (ROOT / path / "index.html").read_text(encoding="utf-8")
        for target in re.findall(r'(?:href|src)="([^"#]+)"', page):
            if re.match(r"^(https?:|mailto:)", target):
                continue
            resolved = (ROOT / path / target).resolve()
            if not (resolved.is_file() or (resolved / "index.html").is_file()):
                missing.append(f"{path or '/'} → {target}")
    if missing:
        raise SystemExit("broken links:\n  " + "\n  ".join(missing))


def main():
    for lang in S:
        landing(lang)
        for key in DOCS:
            if lang in PAGES[key]:
                document(key, lang)
    t = S["tr"]
    notfound = shell("tr", "", t["notfound_title"] + " · Mola", t["notfound_body"],
                     f'<article class="doc"><h1>{esc(t["notfound_title"])}</h1><p>{esc(t["notfound_body"])} '
                     f'<a href="{SITE_URL}">{esc(t["back"])}</a></p></article>', "home", index=False)
    # The 404 page is served for any path: its links must be absolute.
    notfound = re.sub(r'(href|src)="(?!https?:|mailto:)([^"]*)"', lambda m: f'{m.group(1)}="/{m.group(2).lstrip("./")}"', notfound)
    (ROOT / "404.html").write_text(notfound, encoding="utf-8")
    urls = ""
    for paths in PAGES.values():
        links = "".join(f'<xhtml:link rel="alternate" hreflang="{lang}" href="{SITE_URL}{path}"/>'
                        for lang, path in paths.items()) if len(paths) > 1 else ""
        urls += "".join(f"<url><loc>{SITE_URL}{path}</loc>{links}</url>" for path in paths.values())
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        f'xmlns:xhtml="http://www.w3.org/1999/xhtml">{urls}</urlset>\n', encoding="utf-8")
    robots = "".join(f"User-agent: {name}\n" for name in ["*", *CRAWLERS])
    (ROOT / "robots.txt").write_text(f"{robots}Allow: /\n\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")
    (ROOT / "llms.txt").write_text(llms(), encoding="utf-8")
    check_links()
    print(f"{len(written)} pages")


if __name__ == "__main__":
    main()

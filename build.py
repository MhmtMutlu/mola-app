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
}
DOCS = ["privacy", "terms", "kvkk", "delete", "support"]

# The landing copy lives in src/landing.<lang>.json, so it can be reviewed and translated as text.
S = {lang: json.loads((SRC / f"landing.{lang}.json").read_text(encoding="utf-8")) for lang in ("tr", "en")}
# Screenshots a landing page needs (assets/shots/<name>-<lang>.png, made with tools/shots.sh in the app repository).
SHOT_WIDTH, SHOT_HEIGHT = 603, 1311


def rel(from_path, to_path):
    """A relative link between two site paths ('en/privacy/' → '../../assets/site.css')."""
    return "../" * from_path.count("/") + to_path


def shell(lang, path, title, description, body, key):
    t = S[lang]
    other_name, other_lang = t["other"]
    other_path = PAGES[key].get(other_lang, PAGES["home"][other_lang])
    home = rel(path, PAGES["home"][lang])
    top = "".join(f'<a href="{home}#{anchor}">{esc(label)}</a>' for anchor, label in t["nav"].items())
    foot = "".join(f'<a href="{rel(path, PAGES[k][lang])}">{esc(label)}</a>' for k, label in t["foot_nav"].items())
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{SITE_URL}{path}">
<link rel="icon" href="{rel(path, 'assets/icon-64.png')}">
<link rel="apple-touch-icon" href="{rel(path, 'assets/icon-180.png')}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{SITE_URL}assets/icon-512.png">
<meta name="theme-color" content="#F3EEE6" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#15130F" media="(prefers-color-scheme: dark)">
<link rel="stylesheet" href="{rel(path, 'assets/site.css')}">
</head>
<body>
<a class="skip" href="#main">{esc(t['skip'])}</a>
<header class="top">
<a class="brand" href="{home}"><img src="{rel(path, 'assets/icon-180.png')}" alt="" width="36" height="36"><span>Mola</span></a>
<nav class="menu" aria-label="{esc(t['menu_label'])}">{top}</nav>
<a class="lang" href="{rel(path, other_path)}" lang="{other_lang}" hreflang="{other_lang}">{esc(other_name)}</a>
</header>
<main id="main">
{body}
</main>
<footer>
<div class="foot">
<a class="brand" href="{home}"><img src="{rel(path, 'assets/icon-180.png')}" alt="" width="32" height="32"><span>Mola</span></a>
<nav aria-label="{esc(t['foot_label'])}">{foot}</nav>
</div>
<p>{esc(t['footer'])} <a href="mailto:{CONTACT}">{CONTACT}</a></p>
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
    source = rel(path, f"assets/shots/{name}-{lang}.png")
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
<p><a href="{rel(path, PAGES['privacy'][lang])}">{esc(privacy['more'])}</a></p>
</div>
<ul class="ticks card">{privacy_points}</ul>
</section>

<section id="faq" class="faq" aria-labelledby="faq-title">
<h2 id="faq-title">{esc(t['faq_title'])}</h2>
{faq}
</section>

<section class="cta">
<img src="{rel(path, 'assets/icon-512.png')}" alt="" width="88" height="88" loading="lazy">
<h2>{esc(t['cta']['title'])}</h2>
<p>{esc(t['cta']['text'])}</p>
{badge(lang) if APP_STORE_LIVE else ''}
</section>"""
    write(path, shell(lang, path, t["title"], t["description"], body, "home"))


def document(key, lang):
    path = PAGES[key][lang]
    title, body = markdown((SRC / f"{key}.{lang}.md").read_text(encoding="utf-8"))
    t = S[lang]
    page = f'<article class="doc"><p class="crumb"><a href="{rel(path, PAGES["home"][lang])}">{esc(t["back"])}</a></p><h1>{esc(title)}</h1>\n{body}</article>'
    write(path, shell(lang, path, f"{title} · Mola", title, page, key))


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
                     f'<a href="{SITE_URL}">{esc(t["back"])}</a></p></article>', "home")
    # The 404 page is served for any path: its links must be absolute.
    notfound = re.sub(r'(href|src)="(?!https?:|mailto:)([^"]*)"', lambda m: f'{m.group(1)}="/{m.group(2).lstrip("./")}"', notfound)
    (ROOT / "404.html").write_text(notfound, encoding="utf-8")
    urls = "".join(f"<url><loc>{SITE_URL}{path}</loc></url>" for path in written)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n',
        encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")
    check_links()
    print(f"{len(written)} pages")


if __name__ == "__main__":
    main()

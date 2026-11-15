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
import html, pathlib, re

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

S = {
    "tr": {
        "name": "Mola", "tagline": "Ekran süresini kavgaya değil, anlaşmaya çevirin.",
        "description": "Mola, ailelerin ekran süresi kurallarını birlikte koyduğu, çocukların süre isteyebildiği ve odaklandıkça çini boyanan bir iPhone uygulaması.",
        "lead": "Mola, ebeveynle çocuğun kuralları birlikte koyduğu bir aile ekran süresi uygulaması. Yasak yok, mola var: neyin neden ve ne zamana kadar kapalı olduğu her zaman görünür.",
        "soon": "Çok yakında App Store'da", "store": "App Store'dan indir",
        "features_title": "Anlaşma, gözetim değil",
        "features": [
            ("Birlikte konan kurallar", "Günlük sınır, okul ve uyku modu. Çocuk kendi ekranında bütün kuralları görür; gizli hiçbir şey yoktur."),
            ("“15 dakika daha?”", "Çocuk kısa bir nedenle süre ister, ebeveyn tek dokunuşla yanıtlar. İnat yerine konuşma."),
            ("Odaklan, çinini boya", "Her odak oturumu bir çiniyi boyar: önce kontur, sonra renk, sonunda sır. Yarım kalan çini kaybolmaz, sonra tamamlanır."),
            ("Bilekten pomodoro", "Apple Watch'ta program seç, tur ve mola geçişlerini bileğinde hisset."),
        ],
        "privacy_title": "Gizlilik sözümüz",
        "privacy_points": [
            "Ad, e-posta, telefon ya da konum istemeyiz. Hesap açmazsın.",
            "Kullanım verin telefonundan çıkmaz; biz de ebeveyn de göremez.",
            "Mesajlarını okumayız. Mola'nın buna ne izni ne de bir yolu vardır.",
            "Ailenizin cihazları arasındaki her şey uçtan uca şifrelidir; sunucumuz okuyamaz.",
            "Reklam, izleme ve analiz aracı yoktur.",
        ],
        "privacy_more": "Gizlilik politikasının tamamı",
        "alt_today": "Çocuğun Bugün ekranı: kalan süre, yarım kalan çini ve aile anlaşması",
        "alt_wall": "Çini duvarı: tamamlanan çiniler ve sıradaki desen",
        "alt_tiles": "Bir çininin dört aşaması: ham, kontur, renk, sır",
        "nav": {"privacy": "Gizlilik", "terms": "Koşullar", "kvkk": "KVKK", "delete": "Verileri silme", "support": "Destek"},
        "footer": "Bireysel geliştirici Mehmet Mutlu tarafından yapıldı.",
        "other": ("English", "en"), "back": "Ana sayfa",
        "notfound_title": "Sayfa bulunamadı", "notfound_body": "Aradığın sayfa burada değil.",
    },
    "en": {
        "name": "Mola", "tagline": "Turn screen time from a fight into an agreement.",
        "description": "Mola is an iPhone app where families set screen-time rules together, children can ask for time, and every focus session paints a tile.",
        "lead": "Mola is a family screen-time app where parent and child set the rules together. Nothing is forbidden, things take a break: what is closed, why and until when is always visible.",
        "soon": "Coming soon to the App Store", "store": "Download on the App Store",
        "features_title": "An agreement, not surveillance",
        "features": [
            ("Rules made together", "A daily limit, school and sleep modes. The child sees every rule on their own screen; nothing is hidden."),
            ("“15 more minutes?”", "A child asks for time with a short reason, a parent answers with one tap. A conversation instead of a standoff."),
            ("Focus and paint your tile", "Every focus session paints a tile: outline first, then colour, finally the glaze. A half-painted tile is never lost; you finish it later."),
            ("Pomodoro on your wrist", "Pick a program on Apple Watch and feel rounds and breaks change on your wrist."),
        ],
        "privacy_title": "Our privacy promise",
        "privacy_points": [
            "We do not ask for a name, e-mail, phone number or location. There is no account.",
            "Usage data never leaves the phone; neither we nor a parent can see it.",
            "We do not read messages. Mola has neither the permission nor any way to do so.",
            "Everything between your family's devices is end-to-end encrypted; our server cannot read it.",
            "No ads, no tracking, no analytics.",
        ],
        "privacy_more": "Read the full privacy policy",
        "alt_today": "The child's Today screen: time left, a half-painted tile and the family agreement",
        "alt_wall": "The tile wall: finished tiles and the next pattern",
        "alt_tiles": "Four stages of a tile: raw, outline, colour, glaze",
        "nav": {"privacy": "Privacy", "terms": "Terms", "delete": "Deleting your data", "support": "Support"},
        "footer": "Made by Mehmet Mutlu, an individual developer.",
        "other": ("Türkçe", "tr"), "back": "Home",
        "notfound_title": "Page not found", "notfound_body": "The page you are looking for is not here.",
    },
}


def rel(from_path, to_path):
    """A relative link between two site paths ('en/privacy/' → '../../assets/site.css')."""
    return "../" * from_path.count("/") + to_path


def shell(lang, path, title, description, body, key):
    t = S[lang]
    other_name, other_lang = t["other"]
    other_path = PAGES[key].get(other_lang, PAGES["home"][other_lang])
    nav = "".join(f'<a href="{rel(path, PAGES[k][lang])}">{esc(label)}</a>' for k, label in t["nav"].items())
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
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{SITE_URL}assets/icon-512.png">
<link rel="stylesheet" href="{rel(path, 'assets/site.css')}">
</head>
<body>
<header class="top">
<a class="brand" href="{rel(path, PAGES['home'][lang])}"><img src="{rel(path, 'assets/icon-180.png')}" alt="" width="40" height="40"><span>Mola</span></a>
<a class="lang" href="{rel(path, other_path)}" lang="{other_lang}">{esc(other_name)}</a>
</header>
<main>
{body}
</main>
<footer>
<nav aria-label="{esc(t['name'])}">{nav}</nav>
<p>{esc(t['footer'])} <a href="mailto:{CONTACT}">{CONTACT}</a></p>
</footer>
</body>
</html>
"""


def badge(lang):
    t = S[lang]
    if APP_STORE_LIVE:
        return f'<a class="button" href="{APP_STORE_URL}">{esc(t["store"])}</a>'
    return f'<span class="chip">{esc(t["soon"])}</span>'


def landing(lang):
    t, path = S[lang], PAGES["home"][lang]
    asset = lambda name: rel(path, "assets/" + name)
    features = "".join(f'<article class="card tint{i % 4}"><h3>{esc(title)}</h3><p>{esc(text)}</p></article>'
                       for i, (title, text) in enumerate(t["features"]))
    points = "".join(f"<li>{esc(point)}</li>" for point in t["privacy_points"])
    shot = "focus-en.png" if lang == "en" else "today-tr.png"
    body = f"""<section class="hero">
<div>
<img class="icon" src="{asset('icon-512.png')}" alt="" width="112" height="112">
<h1>{esc(t['name'])}</h1>
<p class="tagline">{esc(t['tagline'])}</p>
<p class="lead">{esc(t['lead'])}</p>
{badge(lang)}
</div>
<div class="shots">
<img src="{asset('shots/' + shot)}" alt="{esc(t['alt_today'])}" width="300" loading="lazy">
<img src="{asset('shots/wall.png')}" alt="{esc(t['alt_wall'])}" width="300" loading="lazy">
</div>
</section>
<section>
<h2>{esc(t['features_title'])}</h2>
<div class="grid">{features}</div>
</section>
<section class="night">
<img src="{asset('tiles.png')}" alt="{esc(t['alt_tiles'])}" loading="lazy">
</section>
<section class="card">
<h2>{esc(t['privacy_title'])}</h2>
<ul class="checks">{points}</ul>
<p><a href="{rel(path, PAGES['privacy'][lang])}">{esc(t['privacy_more'])}</a></p>
</section>"""
    write(path, shell(lang, path, f"{t['name']}: {t['tagline']}", t["description"], body, "home"))


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

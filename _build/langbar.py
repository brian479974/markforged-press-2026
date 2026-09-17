# -*- coding: utf-8 -*-
"""news.markforged.tw 語言切換列 —— 站上單一標準來源（2026-09-17 Brian 定版）。

版位＝header 之下、hero 之上的黑底橫條，左側語言標籤，膠囊狀連結。
不是右上角浮動膠囊（2026-09-17 廣東模具刀具那頁曾長成那樣，已收斂）。

為什麼要有這支：同一段 CSS 與 markup 曾被逐字複製到 5 支 build 腳本裡，
第 5 個案子就長出第二種設計。複製貼上維持的不是標準，是巧合。

用法（新案子的 build 腳本）：
    import sys; sys.path.insert(0, str(Path.home() / "markforged-press/_build"))
    from langbar import css_rules, render, inject
    html = inject(html, slug="my-slug", lang="tw")

accent 參數：官方 Manufacturing Yellow 是 #FFFF00（mf-brand 唯一強調色）。
站上舊頁型長期用 #FFC500 琥珀黃，那是偏差不是第二選擇；新頁一律用預設值。
"""
import re

OFFICIAL_YELLOW = "#FFFF00"
LEGACY_YELLOW = "#FFC500"

LANGS = ("tw", "cn", "en")
LABEL = {"tw": "繁體中文", "cn": "简体中文", "en": "English"}
SWITCH_LABEL = {"tw": "語言", "cn": "语言", "en": "Language"}
LANG_ATTR = {"tw": "zh-TW", "cn": "zh-CN", "en": "en"}
OG_LOCALE = {"tw": "zh_TW", "cn": "zh_CN", "en": "en_US"}

# hero 之前的錨點。找不到就該大聲失敗，不要靜默貼到 <body> 後面變回浮動列。
ANCHOR = '  <div class="hero">'


def files(slug):
    return {"tw": f"{slug}.html", "cn": f"{slug}-sc.html", "en": f"{slug}-en.html"}


def css_rules(accent=OFFICIAL_YELLOW, indent="  "):
    """5 條標準規則。手機 padding 另在各站 article.css 的 @media 裡。"""
    return "\n".join(indent + r for r in [
        ".langbar{background:#111;padding:8px 40px;display:flex;gap:6px;"
        "align-items:center;border-top:1px solid #222}",
        ".langbar span{color:#666;font-size:10px;letter-spacing:.12em;"
        "text-transform:uppercase;margin-right:4px}",
        ".langbar a{font-size:11.5px;font-weight:700;color:#888;text-decoration:none;"
        "padding:3px 10px;border-radius:20px;border:1px solid #333}",
        f".langbar a:hover{{color:{accent};border-color:{accent}}}",
        f".langbar a.on{{background:{accent};color:#000;border-color:{accent}}}",
    ])


def render(slug, cur):
    """回傳 (head 用的 hreflang 串, body 用的語言列 div)。"""
    F = files(slug)
    links = "".join(
        f'<a href="{F[L]}"{" class=\"on\"" if L == cur else ""}>{LABEL[L]}</a>'
        for L in LANGS)
    hreflang = "".join(
        f'<link rel="alternate" hreflang="{LANG_ATTR[L]}" href="{F[L]}">'
        for L in LANGS)
    bar = f'  <div class="langbar"><span>{SWITCH_LABEL[cur]}</span>{links}</div>'
    return hreflang, bar


def inject(html, slug, lang):
    """把語言列放進成品。重跑不重複注入；錨點不見就丟 RuntimeError。"""
    if 'class="langbar"' in html:
        html = re.sub(r"<style>\s*\.langbar.*?</style>", "", html, flags=re.S)
        html = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">', "", html)
        html = re.sub(r'\s*<div class="langbar">.*?</div>\n?', "", html, flags=re.S)
    hreflang, bar = render(slug, lang)
    html = html.replace("</head>", hreflang + "\n</head>", 1)
    if ANCHOR not in html:
        raise RuntimeError(f"語言列注入失敗：找不到 hero 錨點，版位無法確認（{slug} / {lang}）")
    html = html.replace(ANCHOR, bar + "\n\n" + ANCHOR, 1)
    html = re.sub(r'<html lang="[^"]*"', f'<html lang="{LANG_ATTR[lang]}"', html, count=1)
    if "og:locale" in html:
        html = re.sub(r'(<meta property="og:locale" content=")[^"]*(")',
                      rf'\g<1>{OG_LOCALE[lang]}\g<2>', html, count=1)
    return html


def check(html, slug, lang):
    """回傳違規清單（空 list ＝ 合標準）。給佈署閘用。"""
    F, bad = files(slug), []
    if 'class="langbar"' not in html:
        return [f"{F[lang]}：沒有語言列"]
    if not re.search(r'</div>\s*<div class="langbar">.*?</div>\s*<div class="hero">',
                     html, flags=re.S):
        bad.append(f"{F[lang]}：語言列不在 header 與 hero 之間（版位非標準）")
    if f"<span>{SWITCH_LABEL[lang]}</span>" not in html:
        bad.append(f"{F[lang]}：缺語言標籤「{SWITCH_LABEL[lang]}」")
    for L in LANGS:
        if f'href="{F[L]}"' not in html:
            bad.append(f"{F[lang]}：沒有指向 {F[L]} 的切換連結")
        if f'hreflang="{LANG_ATTR[L]}"' not in html:
            bad.append(f"{F[lang]}：缺 hreflang {LANG_ATTR[L]}")
    if f'<html lang="{LANG_ATTR[lang]}"' not in html:
        bad.append(f"{F[lang]}：html lang 不是 {LANG_ATTR[lang]}")
    if re.search(r'<a href="[^"]*"( class="on")?>[^<]*</a>\s*</div>', html) and \
            html.count('class="on"') != 1:
        bad.append(f"{F[lang]}：當前語言標記數不等於 1")
    return bad

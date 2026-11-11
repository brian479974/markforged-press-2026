#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""本週專題・產業觀點（汽車）產生器 —— content_auto_perspective.py → 繁中／簡中／英文三頁＋出廠閘。

沿用 build_fx10_landing.py 的樣式元件與文字轉換（T／text_of／CSS／JS），版面改成專題感：
開場左文右圖、三段價值鏈、七類應用、章節大字標題帶＋案例卡、編輯部觀點、行動區、延伸閱讀。
網站共用件同 FX10 頁：globalbar 第一行、analytics.js、標準版位語言列（header → langbar → <div class="hero">）、hreflang、www 頁尾。

閘：L1 覆蓋率 · L2 英文純度 · L3 簡中（t2s 零差異、台灣用語零）· L4 引號 · L5 禁用字（含 SDHQ 對調數字 93%／99%）·
    L6 機型標籤（每張卡都有；FX10 只能標在 GRP）· L7 資源存在與不重複 · L8 網站共用件
"""
import html as _html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_fx10_landing as B  # noqa: E402  共用 T／text_of／CSS／JS
import content_auto_perspective as C  # noqa: E402

T, text_of = B.T, B.text_of
OUT = os.path.dirname(HERE)

CSS_EXTRA = r"""
.hero{display:grid;grid-template-columns:1.05fr 1fr;align-items:stretch;min-height:max(520px,calc(100vh - 170px))}
.hero:after{display:none}
.hero .txt{display:flex;flex-direction:column;justify-content:flex-end;padding:56px 48px 56px max(32px,calc((100vw - 1200px)/2 + 32px));background:#000}
.hero .pic{background:#111 center/cover no-repeat;min-height:320px}
.hero h1{font-size:clamp(36px,4.8vw,72px);line-height:1.08}
.hero .meta{color:#8f8f8f;font-size:13px;margin-top:22px;letter-spacing:.04em}
.chain{background:#0b0b0b;color:#fff;padding:76px 0}
.chain h2{font-size:clamp(24px,2.8vw,36px);font-weight:900}
.c3{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:#222;margin-top:30px}
.c3 > a{display:block;background:#0b0b0b;padding:28px 26px 30px;text-decoration:none;color:#fff;border-top:3px solid var(--y);transition:background .15s}
.c3 > a:hover{background:#151515}
.c3 .no{color:var(--y);font-weight:900;font-size:13px;letter-spacing:.2em}
.c3 .eb{font-size:clamp(24px,2.6vw,34px);font-weight:900;line-height:1.05;margin:8px 0 6px}
.c3 b{display:block;font-size:18px;margin-bottom:8px}
.c3 span{color:#bdbdbd;font-size:14.5px;line-height:1.7}
.apps{background:var(--g1);padding:72px 0}
.apps h2{font-size:clamp(24px,2.8vw,36px);font-weight:900}
.apps .src{color:#888;font-size:12.5px;margin-top:6px}
.a5{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:26px}
.a5 div{background:#fff;padding:22px 18px 24px;border-top:4px solid #000}
.a5 i{display:block;font-style:normal;color:#aaa;font-size:12px;font-weight:900;margin-bottom:6px}
.a5 b{display:block;font-size:18px;font-weight:900;margin-bottom:10px}
.a5 span{font-size:14px;color:#444;line-height:1.85}
.chh{background:#000;color:#fff;padding:72px 0 56px}
.chh .no{font-size:14px;font-weight:900;color:var(--y);letter-spacing:.2em}
.chh .big{font-size:clamp(44px,8vw,120px);font-weight:900;line-height:.95;letter-spacing:-.03em;margin:8px 0 16px}
.chh h2{font-size:clamp(22px,2.6vw,32px);font-weight:900}
.chh p{font-size:clamp(15px,1.5vw,18px);color:#cfcfcf;max-width:46em;margin-top:10px;line-height:1.75}
.view{padding:76px 0;background:#fff}
.vbox{border-left:6px solid var(--y);background:var(--g1);padding:34px 36px}
.vbox .k{font-size:12px;font-weight:900;letter-spacing:.18em;color:#000}
.vbox h2{font-size:clamp(24px,2.8vw,36px);font-weight:900;margin-top:6px}
.vbox ol{margin:20px 0 0 1.2em}
.vbox li{font-size:18px;font-weight:700;line-height:1.6;margin-bottom:10px}
.adopt{font-size:14.5px;color:#555;margin-top:22px}
.adopt a{color:#000;font-weight:800}
@media (max-width:900px){
 .hero{grid-template-columns:1fr}
 .hero .pic{order:-1;min-height:46vw}
 .hero .txt{padding:36px 20px 40px}
 .c3,.a5{grid-template-columns:1fr 1fr}
}
@media (max-width:560px){.c3,.a5{grid-template-columns:1fr}}
"""


def keep(item, lang):
    return not (lang == "cn" and (item.get("defense") or item.get("no_cn")))


def render(lang):
    E = _html.escape
    P = []
    A = P.append
    A(f'<!DOCTYPE html>\n<html lang="{C.LANG_ATTR[lang]}">\n<head>\n<meta charset="UTF-8">')
    A('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    A(f"<title>{T(C.META['title'], lang)}</title>")
    A(f'<meta name="description" content="{E(_html.unescape(T(C.META["desc"], lang)))}">')
    A(f'<meta property="og:title" content="{E(_html.unescape(T(C.META["og_title"], lang)))}">')
    A(f'<meta property="og:description" content="{E(T(C.META["og_desc"], lang))}">')
    A(f'<meta property="og:image" content="https://news.markforged.tw/images/{C.S}-og.jpg">')
    A('<meta property="og:type" content="article">')
    for L in C.LANGS:
        A(f'<link rel="alternate" hreflang="{C.LANG_ATTR[L]}" href="https://news.markforged.tw/{C.FILES[L]}">')
    A(f"<style>{B.CSS}{CSS_EXTRA}</style>")
    A('<script src="analytics.js" defer></script>')
    A("</head>\n<body>\n<script src=\"/globalbar.js\"></script>")
    A(f"<script>{B.JS.split(chr(10))[1]}</script>")

    on = ' class="on"'
    links = "".join(f'<a href="{C.FILES[L]}"{on if L == lang else ""}>{C.LANG_NAMES[L]}</a>' for L in C.LANGS)
    A('<div class="top"><a href="index.html" class="logo"><img src="images/markforged-logo-white.png" alt="Markforged"></a>'
      f'<div class="ev">{T(C.UI["hdr_ev"], lang)}</div></div>')
    A(f'<div class="langbar"><span>{T(C.UI["switch_label"], lang)}</span>{links}</div>')

    H = C.HERO
    A('<div class="hero">'
      f'<div class="txt"><div class="kicker">{T(H["kicker"], lang)}</div><h1>{T(H["h1"], lang)}</h1>'
      f'<p class="sub">{T(H["sub"], lang)}</p><div class="meta">{T(H["meta"], lang)}</div></div>'
      f'<div class="pic" role="img" aria-label="{E(T(C.UI["hero_alt"], lang))}" style="background-image:url(\'images/{C.S}-hero.jpg\')"></div>'
      '</div>')

    CH = C.CHAIN
    items = "".join(f'<a class="rv" href="#{C.CHAPTERS[k]["id"]}"><div class="no">{i["no"]}</div><div class="eb">{i["en_big"]}</div>'
                    f'<b>{T(i["b"], lang)}</b><span>{T(i["s"], lang)}</span></a>' for k, i in enumerate(CH["items"]))
    A(f'<section class="chain"><div class="wrapx"><h2>{T(CH["h"], lang)}</h2><div class="c3">{items}</div></div></section>')

    AP = C.APPS
    a5 = "".join(f'<div class="rv"><i>0{n + 1}</i><b>{T(g["h"], lang)}</b><span>{T(g["items"], lang)}</span></div>' for n, g in enumerate(AP["groups"]))
    A(f'<section class="apps"><div class="wrapx"><h2>{T(AP["h"], lang)}</h2><p class="src">{T(AP["src"], lang)}</p><div class="a5">{a5}</div></div></section>')

    def card(cid):
        c = C.CASES[cid]
        m = c["machine"]
        mb = f'<span class="bdg m{" fx" if m == "fx10" else ""}">{T(C.MACHINE[m], lang)}</span>'
        ex = f'<div class="ex">{T(c["extra"], lang)}</div>' if c.get("extra") and (lang != "cn" or c["extra"].get("cn")) else ""
        if c.get("material"):
            mat = {"tw": f'材料 {c["material"]}（FX10 可列印）', "en": f'Material: {c["material"]} (prints on FX10)'}
            mb += f'<span class="bdg mat">{T(mat, lang)}</span>'
        return (f'<article class="card rv{" ft" if c.get("featured") else ""}" id="case-{cid}">'
                f'<div class="im"><img src="{c["img"]}" alt="{E(T(c["alt"], lang))}" loading="lazy"></div>'
                f'<div class="bd"><div class="badges">{mb}</div><h3>{T(c["title"], lang)}</h3>'
                f'<div class="tg">{T(c["tags"], lang)}</div><p>{T(c["body"], lang)}</p>{ex}'
                f'<div class="mt"><b>{T(c["metric"], lang)}</b><a href="{c["url_lang"][lang] if c.get("url_lang") else c["url"]}">{T(c.get("url_label", C.UI["read_original"]), lang)}</a></div></div></article>')

    for ch in C.CHAPTERS:
        A(f'<section class="chh" id="{ch["id"]}"><div class="wrapx"><div class="no">{ch["no"]}</div><div class="big">{ch["big"]}</div>'
          f'<h2>{T(ch["h"], lang)}</h2><p>{T(ch["intro"], lang)}</p></div></section>')
        A('<div class="chbody"><div class="wrapx">')
        v = ch.get("video")
        if v:
            A(f'<div class="vid rv"><video src="{v["src"][lang]}" poster="{v["poster"]}" controls playsinline preload="metadata"></video></div>'
              f'<div class="vcap">{T(v["cap"], lang)}</div>')
        A('<div class="cards">' + "".join(card(c) for c in ch["cases"] if keep(C.CASES[c], lang)) + "</div>")
        A(f'<div class="chcta"><a href="{E(C.mailto("part", lang))}">{T({"tw": "你的產線也有這種零件？寄圖檔給我們&nbsp;→", "en": "Have a part like this? Send us the file&nbsp;→"}, lang)}</a></div></div></div>')

    V = C.VIEW
    li = "".join(f"<li>{T(q, lang)}</li>" for q in V["items"])
    A(f'<section class="view"><div class="wrapx"><div class="vbox rv"><div class="k">{T(V["kicker"], lang)}</div><h2>{T(V["h"], lang)}</h2><ol>{li}</ol></div>'
      f'<p class="adopt">{T(C.ADOPT, lang)}</p></div></section>')

    CT = C.CTA
    A(f'<section class="cta" id="contact"><div class="wrapx"><div class="cg"><div class="rv">'
      f'<h2>{T(CT["h"], lang)}</h2><p>{T(CT["p"], lang)}</p>'
      f'<div class="btns"><a class="btn k" href="{E(C.mailto("demo", lang))}">{T(CT["btn1"], lang)}</a>'
      f'<a class="btn ok" href="{E(C.mailto("part", lang))}">{T(CT["btn2"], lang)}</a></div>'
      f'<p class="eb">{T(CT["more"], lang)}</p><p class="eb">{T(CT["ebook"], lang)}</p></div>'
      f'<div class="win rv"><img src="brian-chen.jpg" alt="{E(T(B.C.CTA["win_name"], lang))}"><div>'
      f'<small>{T(B.C.CTA["win_label"], lang)}</small><b>{T(B.C.CTA["win_name"], lang)}</b><div class="t">{T(B.C.CTA["win_title"], lang)}</div>'
      f'<div class="d">{T(B.C.CTA["win_desc"], lang)}</div><a href="mailto:{C.MAIL}">{C.MAIL}</a></div></div>'
      f'</div></div></section>')

    RD = C.READ
    rg = "".join(f'<a class="rv" href="{i["href"][lang]}"><b>{T(i["t"], lang)}</b><small>{T(i["s"], lang)}</small></a>'
                 for i in RD["items"] if keep(i, lang))
    A(f'<section class="read"><div class="wrapx"><h2>{T(RD["h"], lang)}</h2><div class="rg">{rg}</div></div></section>')

    A(f'<footer class="ftr"><div class="wrapx">{T(C.FTR["about"], lang)}<br><br>'
      f'<a href="index.html">{T(C.FTR["back"], lang)}</a>　·　<a href="https://www.markforged.tw/">markforged.tw</a></div></footer>')
    A(f"<script>{B.JS}</script>")
    A("</body>\n</html>\n")
    return "\n".join(P)


def gates(out):
    ok = True

    def fail(m):
        nonlocal ok
        ok = False
        print("  ✗ " + m)
    cjk = re.findall(r"[一-鿿　-〿＀-￯]", text_of(out["en"]))
    fail(f"L2 英文純度：殘留 {''.join(sorted(set(cjk)))}") if cjk else print("  ✅ L2 英文純度：英文頁零 CJK／全形")
    cnt = text_of(out["cn"])
    diff = [a for a, b in zip(cnt, B._T2S.convert(cnt)) if a != b]
    fail(f"L3 簡中殘留繁體：{''.join(sorted(set(diff)))}") if diff else print("  ✅ L3 簡中：t2s 回驗零差異")
    tw_terms = [w for w in ["列印", "治具", "航太", "积层", "雷射", "量测", "公厘", "澳洲", "影片", "工安", "控管"] if w in cnt]
    fail(f"L3 簡中台灣用語：{tw_terms}") if tw_terms else print("  ✅ L3 簡中：台灣用語零")
    q_bad = {L: len(re.findall(r"[「」『』“”\"]", text_of(h))) for L, h in out.items()}
    fail(f"L4 引號：{q_bad}") if any(q_bad.values()) else print("  ✅ L4 引號：三版可見文字零引號")
    ban = ["Metal X", "PX100", "Mark Two", "INTERNAL USE", "DMC", "DASAN", "Onyx Pro", "SDHQ", "93%", "99%", "65%", "ULTEM", "seven colors", "七色", "bella", "claude", "MF-GCR"]
    # 只查網址以外的內容：mailto 內的中文經網址編碼會出現 %E9%99%84 這類字串，含「99%」而誤擋（2026-11-11 實測）
    def _no_urls(h):
        return re.sub(r'(?:href|src)="[^"]*"', "", h)
    hits = {L: [b for b in ban if b.lower() in _no_urls(h).lower()] for L, h in out.items()}
    fail(f"L5 禁用字：{hits}") if any(hits.values()) else print("  ✅ L5 禁用字：零")
    fx = sorted(cid for cid, c in C.CASES.items() if c["machine"] == "fx10")
    if fx != ["grp"]:
        fail(f"L6 標成 FX10 的只能是 GRP，現在是 {fx}")
    for L, h in out.items():
        if h.count('<article class="card') != len(re.findall(r'class="bdg m(?: fx)?"', h)):
            fail(f"L6 {L} 版案例卡與機型標籤數對不上")
    print("  ✅ L6 機型標籤：每張卡都有，FX10 只標在 GRP") if ok else None
    for L, h in out.items():
        srcs = re.findall(r'(?:src|poster)="((?:images|video)/[^"]+)"', h) + re.findall(r"url\('((?:images|video)/[^']+)'\)", h)
        miss = [s for s in set(srcs) if not os.path.exists(os.path.join(OUT, s))]
        if miss:
            fail(f"L7 {L} 版缺檔 {miss}")
        imgs = re.findall(r'<img[^>]+src="([^"]+)"', h)
        dup = sorted({s for s in imgs if imgs.count(s) > 1})
        if dup:
            fail(f"L7 {L} 版重複圖 {dup}")
    print("  ✅ L7 資源：都在、不重複")
    for L, h in out.items():
        bf = re.search(r"<body>\s*(<script[^>]*>)", h)
        if not bf or "globalbar.js" not in bf.group(1):
            fail(f"L8 {L} globalbar 不在 <body> 後第一行")
        if 'src="analytics.js"' not in h or 'href="https://www.markforged.tw/"' not in h:
            fail(f"L8 {L} 缺 analytics.js 或 www 頁尾")
        if not re.search(r'</div>\s*<div class="langbar">.*?</div>\s*<div class="hero">', h, flags=re.S):
            fail(f"L8 {L} 語言列不在標準版位")
        if len(re.findall(r'rel="alternate" hreflang=', h)) != 3:
            fail(f"L8 {L} hreflang 不是三條")
    print("  ✅ L8 網站共用件") if ok else None
    return ok


def main():
    out = {L: render(L) for L in C.LANGS}
    for L, h in out.items():
        open(os.path.join(OUT, C.FILES[L]), "w", encoding="utf-8").write(h)
        print(f"✓ 產出 {C.FILES[L]}  {len(h)//1024} KB")
    print("\n── 閘門 ──")
    if not gates(out):
        sys.exit("\n✗ 閘門未全綠")
    print("\n✅ 閘門全綠")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""從單一內容源產出三語 HTML（繁中 / 簡中 / English）+ 內建四道閘。

閘門：
  G1 覆蓋率   每個 key 三語齊全且非空，缺一個就 exit 1
  G2 結構同形 三版的區塊數、圖片數、highlight 數必須一致（GATE-9 的 HTML 版）
  G3 英文純度 英文版文字層不得出現任何 CJK（品牌名例外由白名單控管）
  G4 簡繁殘留 簡中版不得出現繁體專用字（用對照表偵測）
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import (META, UI, LEAD, QUOTE, PROF, TAGS, BLOCKS, CTA, SRC, FTR, LANGS,
                     APPROVED_QUOTES, DOC_TERMS)  # noqa: E402

OUT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# G4 用 OpenCC 實際做 t2s 轉換比對，不手刻字表。
# 2026-09-07 教訓：手刻的「繁體字表」誤收了簡繁同形字（包／硬／臂），
# 對正確的簡中譯文報假紅燈 —— 又是一次「量到的不是我以為的那件事」。
import opencc  # noqa: E402
_T2S = opencc.OpenCC("t2s")

STYLE = """
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:#e8e8e8;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Helvetica Neue',Arial,'Noto Sans TC','Noto Sans SC',sans-serif;color:#1a1a1a}
  .wrap{max-width:700px;margin:0 auto;background:#fff}
  .hdr{background:#000;padding:20px 40px;display:flex;align-items:center;justify-content:space-between}
  .hdr-logo{display:block;line-height:0}
  .hdr-logo img{height:26px;width:auto;display:block}
  .hdr-ev{color:rgba(255,255,255,.6);font-size:12px;text-align:right;line-height:1.6}
  .langbar{background:#111;padding:8px 40px;display:flex;gap:6px;align-items:center;border-top:1px solid #222}
  .langbar span{color:#666;font-size:10px;letter-spacing:.12em;text-transform:uppercase;margin-right:4px}
  .langbar a{font-size:11.5px;font-weight:700;color:#888;text-decoration:none;padding:3px 10px;border-radius:20px;border:1px solid #333}
  .langbar a:hover{color:#FFC500;border-color:#FFC500}
  .langbar a.on{background:#FFC500;color:#000;border-color:#FFC500}
  .hero{position:relative;overflow:hidden}
  .hero img{width:100%;display:block}
  .hero-ov{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.68) 0%,rgba(0,0,0,.15) 50%,rgba(0,0,0,.72) 100%)}
  .hero-top{position:absolute;top:0;left:0;right:0;padding:28px 38px}
  .hero-kicker{color:#FFC500;font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;margin-bottom:9px}
  .hero-title{color:#fff;font-size:26px;font-weight:900;line-height:1.28;max-width:540px;text-shadow:0 2px 12px rgba(0,0,0,.5)}
  .hero-btm{position:absolute;bottom:0;left:0;right:0;padding:16px 38px;background:linear-gradient(transparent,rgba(0,0,0,.75))}
  .hero-meta{color:rgba(255,255,255,.85);font-size:12px;letter-spacing:.04em}
  .ds{background:#FFC500;padding:10px 38px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:6px}
  .ds-l{font-size:12.5px;font-weight:700;color:#000}
  .ds-r{font-size:11.5px;color:#333}
  .body{padding:36px 38px 0}
  .lead{font-size:16px;line-height:1.82;color:#222;margin-bottom:24px;padding-bottom:24px;border-bottom:2px solid #f0f0f0}
  .qb{margin:6px 0 26px;padding:20px 24px;background:#000;border-radius:6px}
  .qb p{color:#FFC500;font-size:18px;font-weight:800;line-height:1.45;margin-bottom:5px}
  .qb small{color:rgba(255,255,255,.45);font-size:10.5px;letter-spacing:.07em}
  .sec{margin-bottom:30px}
  h2{font-size:11px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:#FFC500;margin-bottom:12px;padding-left:11px;border-left:4px solid #FFC500}
  h3{font-size:18px;font-weight:800;color:#111;margin-bottom:12px;line-height:1.32}
  p{font-size:14.5px;line-height:1.82;color:#333;margin-bottom:14px}
  strong{color:#111}
  .tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:24px}
  .tag{background:#111;color:#FFC500;font-size:10px;font-weight:700;letter-spacing:.07em;padding:4px 10px;border-radius:30px}
  .tag.ol{background:#fff;color:#666;border:1.5px solid #ddd}
  .ph-full img{width:100%;display:block}
  .ph-2col{display:grid;grid-template-columns:1fr 1fr;gap:3px}
  .gi{width:100%;display:block;object-fit:cover}
  .gi-43{aspect-ratio:4/3}
  .cap{font-size:11px;color:#aaa;text-align:center;padding:8px 38px 22px;border-bottom:1px solid #eee;margin-bottom:26px;line-height:1.55}
  .hl-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:30px}
  .hl{background:#f7f7f7;border-left:4px solid #FFC500;padding:16px 18px}
  .hl b{display:block;font-size:24px;font-weight:900;color:#111;line-height:1.1;margin-bottom:5px}
  .hl span{font-size:11.5px;color:#777;line-height:1.5;display:block}
  .prof{display:flex;gap:18px;align-items:center;background:#111;padding:22px 24px;border-radius:6px;margin:8px 0 28px}
  .prof img{width:92px;height:92px;object-fit:cover;border-radius:50%;flex-shrink:0;border:3px solid #FFC500}
  .prof-n{color:#fff;font-size:16px;font-weight:800;margin-bottom:4px}
  .prof-t{color:#FFC500;font-size:11.5px;font-weight:700;margin-bottom:7px}
  .prof-d{color:rgba(255,255,255,.6);font-size:11.5px;line-height:1.6}
  .cta{background:#FFC500;padding:28px 32px;margin:6px 0 0}
  .cta h4{font-size:17px;font-weight:900;color:#000;margin-bottom:8px}
  .cta p{font-size:13px;color:#333;line-height:1.7;margin-bottom:16px}
  .btn{display:inline-block;background:#000;color:#FFC500;padding:12px 26px;font-size:13.5px;font-weight:800;text-decoration:none;letter-spacing:.04em}
  .btn:hover{background:#222}
  .srcbox{background:#fafafa;border-top:3px solid #111;padding:22px 38px 26px}
  .srcbox h5{font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:#888;margin-bottom:10px}
  .srcbox li{font-size:11.5px;color:#777;line-height:1.75;margin-left:16px}
  .ftr{background:#000;padding:24px 38px;color:rgba(255,255,255,.5);font-size:11.5px;line-height:1.7}
  .ftr a{color:#FFC500;text-decoration:none}
  @media(max-width:620px){.hero-title{font-size:21px}.body{padding:26px 22px 0}.hl-grid{grid-template-columns:1fr}.prof{flex-direction:column;text-align:center}.langbar{padding:8px 22px}}
"""

LANG_NAMES = {"tw": "繁體中文", "cn": "简体中文", "en": "English"}


def t(node, lang, path):
    """取語言字串，缺值即失敗（G1 覆蓋率閘）。"""
    if lang not in node or not str(node[lang]).strip():
        sys.exit(f"✗ G1 覆蓋率閘：{path} 缺 {lang} 或為空")
    return node[lang]


def langbar(cur):
    links = []
    for L in LANGS:
        cls = ' class="on"' if L == cur else ""
        links.append(f'<a href="{META["file"][L]}"{cls}>{LANG_NAMES[L]}</a>')
    return (f'  <div class="langbar"><span>{t(UI["switch_label"], cur, "switch_label")}</span>'
            + "".join(links) + "</div>\n")


def render(lang):
    P = []
    A = P.append
    A(f'<!DOCTYPE html>\n<html lang="{META["lang_attr"][lang]}">\n<head>\n<meta charset="UTF-8">')
    A('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    A(f'<title>{t(META["title"], lang, "title")}</title>')
    A(f'<meta name="description" content="{t(META["desc"], lang, "desc")}">')
    A(f'<meta property="og:title" content="{t(META["og_title"], lang, "og_title")}">')
    A(f'<meta property="og:description" content="{t(META["og_desc"], lang, "og_desc")}">')
    A('<meta property="og:image" content="https://news.markforged.tw/images/hero-factory-floor.jpg">')
    A('<meta property="og:type" content="article">')
    for L in LANGS:
        A(f'<link rel="alternate" hreflang="{META["lang_attr"][L]}" '
          f'href="https://news.markforged.tw/{META["file"][L]}">')
    A(f"<style>{STYLE}</style>\n</head>\n<body>\n<div class=\"wrap\">\n")

    A('  <div class="hdr">')
    A('    <a href="index.html" class="hdr-logo"><img src="images/markforged-logo-white.png" alt="Markforged"></a>')
    A(f'    <div class="hdr-ev">{t(UI["hdr_ev"], lang, "hdr_ev")}</div>')
    A('  </div>\n')
    A(langbar(lang))

    A('  <div class="hero">')
    A(f'    <img src="images/hero-factory-floor.jpg" alt="{t(UI["hero_alt"], lang, "hero_alt")}">')
    A('    <div class="hero-ov"></div>')
    A('    <div class="hero-top">')
    A(f'      <div class="hero-kicker">{t(UI["hero_kicker"], lang, "hero_kicker")}</div>')
    A(f'      <div class="hero-title">{t(UI["hero_title"], lang, "hero_title")}</div>')
    A('    </div>')
    A(f'    <div class="hero-btm"><div class="hero-meta">{t(UI["hero_meta"], lang, "hero_meta")}</div></div>')
    A('  </div>\n')

    A(f'  <div class="ds"><div class="ds-l">{t(UI["ds_l"], lang, "ds_l")}</div>'
      f'<div class="ds-r">{t(UI["ds_r"], lang, "ds_r")}</div></div>\n')

    A('  <div class="body">\n')
    A(f'    <div class="lead">{t(LEAD["p1"], lang, "lead.p1")}<br><br>{t(LEAD["p2"], lang, "lead.p2")}</div>\n')
    A(f'    <div class="qb"><p>{t(QUOTE["text"], lang, "quote")}</p>'
      f'<small>{t(QUOTE["attr"], lang, "quote.attr")}</small></div>\n')
    A('    <div class="prof">')
    A(f'      <img src="brian-chen.jpg" alt="{t(PROF["alt"], lang, "prof.alt")}">')
    A(f'      <div><div class="prof-n">{t(PROF["name"], lang, "prof.name")}</div>'
      f'<div class="prof-t">{t(PROF["title"], lang, "prof.title")}</div>'
      f'<div class="prof-d">{t(PROF["desc"], lang, "prof.desc")}</div></div>')
    A('    </div>\n')
    A('    <div class="tags">' + "".join(
        f'<span class="tag{"" if g["solid"] else " ol"}">{t(g, lang, "tag")}</span>' for g in TAGS)
      + '</div>\n')

    for i, b in enumerate(BLOCKS):
        if b["kind"] == "sec":
            A('    <div class="sec">')
            A(f'      <h2>{t(b["h2"], lang, f"blk{i}.h2")}</h2>')
            A(f'      <h3>{t(b["h3"], lang, f"blk{i}.h3")}</h3>')
            for j, p in enumerate(b["paras"]):
                A(f'      <p>{t(p, lang, f"blk{i}.p{j}")}</p>')
            if b.get("hl"):
                A('      <div class="hl-grid">')
                for k, h in enumerate(b["hl"]):
                    A(f'        <div class="hl"><b>{t(h["b"], lang, f"blk{i}.hl{k}.b")}</b>'
                      f'<span>{t(h["s"], lang, f"blk{i}.hl{k}.s")}</span></div>')
                A('      </div>')
            for j, p in enumerate(b.get("paras_after", [])):
                A(f'      <p>{t(p, lang, f"blk{i}.pa{j}")}</p>')
            A('    </div>\n')
        elif b["kind"] == "img_full":
            A(f'    <div class="ph-full"><img src="{b["img"]}" alt="{t(b["alt"], lang, f"blk{i}.alt")}"></div>')
            A(f'    <div class="cap">{t(b["cap"], lang, f"blk{i}.cap")}</div>\n')
        elif b["kind"] == "img_2col":
            A('    <div class="ph-2col">')
            for k, src in enumerate(b["imgs"]):
                A(f'      <img class="gi gi-43" src="{src}" alt="{t(b["alts"][k], lang, f"blk{i}.alt{k}")}">')
            A('    </div>')
            A(f'    <div class="cap">{t(b["cap"], lang, f"blk{i}.cap")}</div>\n')

    A('  </div>\n')
    A('  <div class="cta">')
    A(f'    <h4>{t(CTA["h"], lang, "cta.h")}</h4>')
    A(f'    <p>{t(CTA["p"], lang, "cta.p")}</p>')
    A(f'    <a href="https://mfmk.markforged.tw" class="btn">{t(CTA["btn"], lang, "cta.btn")}</a>')
    A('  </div>\n')
    A('  <div class="srcbox">')
    A(f'    <h5>{t(SRC["h"], lang, "src.h")}</h5>')
    A('    <ul>' + "".join(f'<li>{t(it, lang, f"src.item{n}")}</li>'
                           for n, it in enumerate(SRC["items"])) + '</ul>')
    A('  </div>\n')
    A('  <div class="ftr">')
    A(f'    {t(FTR["about"], lang, "ftr.about")}<br><br>')
    A(f'    <a href="index.html">{t(FTR["back"], lang, "ftr.back")}</a>　·　'
      '<a href="https://markforged.tw">markforged.tw</a>')
    A('  </div>\n\n</div>\n</body>\n</html>\n')
    return "\n".join(P)


def text_of(html, drop_langbar=True):
    h = re.sub(r"<style>.*?</style>", " ", html, flags=re.S)
    if drop_langbar:
        # 語言切換列刻意以各語言自身文字書寫（繁體中文／简体中文／English），
        # 屬國際慣例，不納入純度判定；文章本文才是受檢範圍。
        h = re.sub(r'<div class="langbar">.*?</div>', " ", h, flags=re.S)
    h = re.sub(r"<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", h)


def main():
    out = {}
    for L in LANGS:
        html = render(L)
        path = os.path.join(OUT_DIR, META["file"][L])
        open(path, "w", encoding="utf-8").write(html)
        out[L] = html
        print(f"✓ 產出 {META['file'][L]}  {len(html)//1024} KB")

    print("\n── 閘門 ──")
    # G2 結構同形
    shape = {L: (out[L].count('class="sec"'), out[L].count("<img "),
                 out[L].count('class="hl"'), out[L].count("<li>"),
                 out[L].count('class="cap"')) for L in LANGS}
    if len(set(shape.values())) != 1:
        for L in LANGS:
            print(f"   {L}: sec/img/hl/li/cap = {shape[L]}")
        sys.exit("✗ G2 結構同形閘：三版結構不一致")
    print(f"  ✅ G2 結構同形：sec/img/hl/li/cap = {shape['tw']}（三版一致）")

    # G3 英文純度
    cjk = re.findall(r"[一-鿿　-〿＀-￯]", text_of(out["en"]))
    if cjk:
        sys.exit(f"✗ G3 英文純度閘：英文版殘留 {len(cjk)} 個 CJK/全形字元：{''.join(sorted(set(cjk))[:30])}")
    print("  ✅ G3 英文純度：英文版零 CJK／全形字元")

    # G4 簡繁殘留 —— 以 OpenCC t2s 轉換後比對，有差異即代表殘留繁體
    cn_body = text_of(out["cn"])
    converted = _T2S.convert(cn_body)
    if converted != cn_body:
        diff = sorted({a for a, b in zip(cn_body, converted) if a != b})
        sys.exit(f"✗ G4 簡繁閘：簡中版殘留繁體字 {''.join(diff)}")
    print("  ✅ G4 簡繁：簡中版經 OpenCC t2s 回驗零差異")

    # G5 冒名引言閘 —— 2026-09-07 事故：v1 有 10 處掛 Brian 名字的直接引言全是代寫的。
    # 檢查的是「這句話他說過沒有」，不是數幾組引號。
    PAIRS = {"tw": ("\u300c", "\u300d"), "cn": ("\u201c", "\u201d"), "en": ("\u201c", "\u201d")}
    for L in LANGS:
        body = text_of(out[L])
        o, c = PAIRS[L]
        spans = re.findall(re.escape(o) + r"([^" + re.escape(o + c) + r"]{2,})" + re.escape(c), body)
        allowed = [q.strip() for q in APPROVED_QUOTES[L]] + DOC_TERMS
        bad = []
        for s in spans:
            s2 = s.strip().rstrip("\u3002.,")
            if not any(s2 in a or a.strip().rstrip("\u3002.,") in s2 for a in allowed):
                bad.append(s2[:60])
        if bad:
            sys.exit("\u2717 G5 \u5192\u540d\u5f15\u8a00\u9598\uff1a" + L + " \u7248\u6709\u4e0d\u5728\u767d\u540d\u55ae\u7684\u5f15\u8a00\uff1a" + " | ".join(bad))
        print(f"  \u2705 G5 \u5192\u540d\u5f15\u8a00\uff1a{L} \u7248 {len(spans)} \u7d44\u5f15\u865f\u5168\u6578\u6bd4\u5c0d\u767d\u540d\u55ae\u901a\u904e")

    print("\n✅ 五道閘全綠")


if __name__ == "__main__":
    main()

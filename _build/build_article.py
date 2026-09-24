#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""從單一內容源產出三語 HTML（繁中 / 簡中 / English）+ 內建四道閘。

閘門：
  G1 覆蓋率   每個 key 三語齊全且非空，缺一個就 exit 1
  G2 結構同形 三版的區塊數、圖片數、highlight 數必須一致（GATE-9 的 HTML 版）
  G3 英文純度 英文版文字層不得出現任何 CJK（品牌名例外由白名單控管）
  G4 簡繁殘留 簡中版不得出現繁體專用字（用對照表偵測）
  G5 冒名引言 引號內每一段必須在核准白名單裡
  G6 原稿覆蓋 來源 md 的硬 token 必須全數落地，刻意不落地須具名豁免＋理由
  G7 照片重複 感知雜湊比對，同一個畫面的不同版本不得同頁並用
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib  # noqa: E402
# 一支產生器服務多篇文章：ARTICLE_CONTENT 指定內容源，預設 content（既有廣編稿）
_C = importlib.import_module(os.environ.get("ARTICLE_CONTENT", "content"))
META, UI, LEAD, QUOTE, PROF = _C.META, _C.UI, _C.LEAD, _C.QUOTE, _C.PROF
SOURCE_MD = getattr(_C, "SOURCE_MD", None)
COVERAGE_EXEMPT = getattr(_C, "COVERAGE_EXEMPT", {})
TAGS, BLOCKS, CTA, SRC, FTR = _C.TAGS, _C.BLOCKS, _C.CTA, _C.SRC, _C.FTR
LANGS, APPROVED_QUOTES, DOC_TERMS = _C.LANGS, _C.APPROVED_QUOTES, _C.DOC_TERMS

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
  .langbar a:hover{color:#FFFF00;border-color:#FFFF00}
  .langbar a.on{background:#FFFF00;color:#000;border-color:#FFFF00}
  .hero{position:relative;overflow:hidden}
  .hero img{width:100%;display:block}
  .hero-ov{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.68) 0%,rgba(0,0,0,.15) 50%,rgba(0,0,0,.72) 100%)}
  .hero-top{position:absolute;top:0;left:0;right:0;padding:28px 38px}
  .hero-kicker{color:#FFFF00;font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;margin-bottom:9px}
  .hero-title{color:#fff;font-size:26px;font-weight:900;line-height:1.28;max-width:540px;text-shadow:0 2px 12px rgba(0,0,0,.5)}
  .hero-btm{position:absolute;bottom:0;left:0;right:0;padding:16px 38px;background:linear-gradient(transparent,rgba(0,0,0,.75))}
  .hero-meta{color:rgba(255,255,255,.85);font-size:12px;letter-spacing:.04em}
  .ds{background:#FFFF00;padding:10px 38px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:6px}
  .ds-l{font-size:12.5px;font-weight:700;color:#000}
  .ds-r{font-size:11.5px;color:#333}
  .body{padding:36px 38px 0}
  .lead{font-size:16px;line-height:1.82;color:#222;margin-bottom:24px;padding-bottom:24px;border-bottom:2px solid #f0f0f0}
  .qb{margin:6px 0 26px;padding:20px 24px;background:#000;border-radius:6px}
  .qb p{color:#FFFF00;font-size:18px;font-weight:800;line-height:1.45;margin-bottom:5px}
  .qb small{color:rgba(255,255,255,.45);font-size:10.5px;letter-spacing:.07em}
  .sec{margin-bottom:30px}
  h2{font-size:11px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:#111;margin-bottom:12px;padding-left:11px;border-left:4px solid #FFFF00}
  h3{font-size:18px;font-weight:800;color:#111;margin-bottom:12px;line-height:1.32}
  p{font-size:14.5px;line-height:1.82;color:#333;margin-bottom:14px}
  strong{color:#111}
  .tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:24px}
  .tag{background:#111;color:#FFFF00;font-size:10px;font-weight:700;letter-spacing:.07em;padding:4px 10px;border-radius:30px}
  .tag.ol{background:#fff;color:#666;border:1.5px solid #ddd}
  .ph-full img{width:100%;display:block}
  /* 直式照片滿版會把整個視窗撐掉（2026-09-24 FX10 轉正後實測 624→937px 高）→ 收窄置中 */
  .ph-port{background:#f4f4f4;padding:22px 0;display:flex;justify-content:center}
  .ph-port img{width:auto;max-width:62%;max-height:620px;display:block}
  @media(max-width:620px){.ph-port img{max-width:82%}}
  .ph-2col{display:grid;grid-template-columns:1fr 1fr;gap:3px}
  .gi{width:100%;display:block;object-fit:cover}
  .gi-43{aspect-ratio:4/3}
  .gi-34{aspect-ratio:3/4}
  .cap{font-size:11px;color:#aaa;text-align:center;padding:8px 38px 22px;border-bottom:1px solid #eee;margin-bottom:26px;line-height:1.55}
  .hl-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:30px}
  .hl{background:#f7f7f7;border-left:4px solid #FFFF00;padding:16px 18px}
  .hl b{display:block;font-size:24px;font-weight:900;color:#111;line-height:1.1;margin-bottom:5px}
  .hl span{font-size:11.5px;color:#777;line-height:1.5;display:block}
  .prof{display:flex;gap:18px;align-items:center;background:#111;padding:22px 24px;border-radius:6px;margin:8px 0 28px}
  .prof img{width:92px;height:92px;object-fit:cover;border-radius:50%;flex-shrink:0;border:3px solid #FFFF00}
  .prof-n{color:#fff;font-size:16px;font-weight:800;margin-bottom:4px}
  .prof-t{color:#FFFF00;font-size:11.5px;font-weight:700;margin-bottom:7px}
  .prof-d{color:rgba(255,255,255,.6);font-size:11.5px;line-height:1.6}
  .cta{background:#FFFF00;padding:28px 32px;margin:6px 0 0}
  .cta h4{font-size:17px;font-weight:900;color:#000;margin-bottom:8px}
  .cta p{font-size:13px;color:#333;line-height:1.7;margin-bottom:16px}
  .btn{display:inline-block;background:#000;color:#FFFF00;padding:12px 26px;font-size:13.5px;font-weight:800;text-decoration:none;letter-spacing:.04em}
  .btn:hover{background:#222}
  .vid{position:relative;width:100%;padding-top:56.25%;background:#000}
  .vid iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
  .srcbox{background:#fafafa;border-top:3px solid #111;padding:22px 38px 26px}
  .srcbox h5{font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:#888;margin-bottom:10px}
  .srcbox li{font-size:11.5px;color:#777;line-height:1.75;margin-left:16px}
  .ftr{background:#000;padding:24px 38px;color:rgba(255,255,255,.5);font-size:11.5px;line-height:1.7}
  .ftr a{color:#FFFF00;text-decoration:none}
  /* ── 雙方表述：官方引言雙卡 ── */
  .quotes{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:4px 0 30px}
  .qc{background:#111;padding:22px 22px 20px;border-top:4px solid #FFFF00;display:flex;flex-direction:column}
  .qc p{color:#fff;font-size:13.5px;line-height:1.78;margin:0 0 16px;flex:1}
  .qc-who{display:flex;gap:12px;align-items:center}
  .qc-who img{width:54px;height:54px;object-fit:cover;border-radius:50%;flex-shrink:0;border:2px solid #FFFF00}
  .qc-n{color:#FFFF00;font-size:12.5px;font-weight:800;line-height:1.4;margin-bottom:3px}
  .qc-t{color:rgba(255,255,255,.5);font-size:10.5px;line-height:1.55}
  /* ── 活動資料 fact sheet ── */
  .fs{border-top:3px solid #111;margin:4px 0 8px}
  .fs-h{font-size:11px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:#111;padding:14px 0 10px}
  .fs-row{display:flex;gap:18px;padding:10px 0;border-top:1px solid #f0f0f0}
  .fs-k{flex:0 0 92px;font-size:11px;font-weight:700;color:#999;letter-spacing:.05em;line-height:1.75;text-transform:uppercase}
  .fs-v{font-size:13.5px;color:#222;line-height:1.75}
  /* ── 完稿記號（通訊社慣例）── */
  .endmark{text-align:center;letter-spacing:.4em;color:#c4c4c4;font-size:11px;font-weight:700;padding:22px 0 24px}
  /* ── 關於雙方 ── */
  .about{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:0 0 14px}
  .ab{background:#fafafa;border-top:4px solid #111;padding:18px 20px}
  .ab h6{font-size:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#999;margin-bottom:9px}
  .ab p{font-size:11.5px;line-height:1.8;color:#555;margin:0}
  /* ── 媒體聯絡 ── */
  .mc{background:#111;padding:20px 24px;margin:0 0 4px}
  .mc h6{font-size:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#FFFF00;margin-bottom:10px}
  .mc-o{color:#fff;font-size:13px;font-weight:800;margin-bottom:7px}
  .mc p{color:rgba(255,255,255,.6);font-size:11.5px;line-height:1.9;margin:0}
  .mc a{color:#fff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.28)}
  @media(max-width:620px){.hero-title{font-size:21px}.body{padding:26px 22px 0}.hl-grid{grid-template-columns:1fr}.quotes{grid-template-columns:1fr}.about{grid-template-columns:1fr}.prof{flex-direction:column;text-align:center}.langbar{padding:8px 22px}}
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
    A(f'<meta property="og:image" content="{META.get("og_image", "https://news.markforged.tw/images/hero-factory-floor.jpg")}">')
    A('<meta property="og:type" content="article">')
    for L in LANGS:
        A(f'<link rel="alternate" hreflang="{META["lang_attr"][L]}" '
          f'href="https://news.markforged.tw/{META["file"][L]}">')
    A(f"<style>{STYLE}</style>")
    # 瀏覽統計 beacon（供應商可換 · 不放 cookie · 尊重 DNT）
    A('<script src="analytics.js" defer></script>')
    A("</head>\n<body>\n<div class=\"wrap\">\n")

    A('  <div class="hdr">')
    A('    <a href="index.html" class="hdr-logo"><img src="images/markforged-logo-white.png" alt="Markforged"></a>')
    A(f'    <div class="hdr-ev">{t(UI["hdr_ev"], lang, "hdr_ev")}</div>')
    A('  </div>\n')
    A(langbar(lang))

    A('  <div class="hero">')
    A(f'    <img src="{META.get("hero", "images/hero-factory-floor.jpg")}" alt="{t(UI["hero_alt"], lang, "hero_alt")}">')
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
    _lead = [t(LEAD["p1"], lang, "lead.p1")]
    if LEAD.get("p2"):
        _lead.append(t(LEAD["p2"], lang, "lead.p2"))
    A('    <div class="lead">' + "<br><br>".join(_lead) + '</div>\n')
    A(f'    <div class="qb"><p>{t(QUOTE["text"], lang, "quote")}</p>'
      f'<small>{t(QUOTE["attr"], lang, "quote.attr")}</small></div>\n')
    if PROF:   # 具名觀點文才掛作者卡；活動報導裡 Brian 是消息來源，不是作者
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
            # 直式／橫式自動分流：直式走 .ph-port 收窄置中，不讓它撐掉一整屏
            try:
                from PIL import Image as _Im
                with _Im.open(os.path.join(OUT_DIR, b["img"])) as _i:
                    _cls = "ph-full ph-port" if _i.height > _i.width else "ph-full"
            except Exception:
                _cls = "ph-full"
            A(f'    <div class="{_cls}"><img src="{b["img"]}" alt="{t(b["alt"], lang, f"blk{i}.alt")}"></div>')
            A(f'    <div class="cap">{t(b["cap"], lang, f"blk{i}.cap")}</div>\n')
        elif b["kind"] == "video":
            _src = b["src"][lang] if isinstance(b["src"], dict) else b["src"]
            A('    <div class="vid"><iframe src="' + _src + '" '
              f'title="{t(b["alt"], lang, f"blk{i}.alt")}" loading="lazy" '
              'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; '
              'picture-in-picture" allowfullscreen></iframe></div>')
            A(f'    <div class="cap">{t(b["cap"], lang, f"blk{i}.cap")}</div>\n')
        elif b["kind"] == "quotes":
            A('    <div class="quotes">')
            for k, q in enumerate(b["items"]):
                A('      <div class="qc">')
                A(f'        <p>{t(q["text"], lang, f"blk{i}.q{k}.text")}</p>')
                A('        <div class="qc-who">')
                if q.get("img"):
                    A(f'          <img src="{q["img"]}" alt="{t(q["alt"], lang, f"blk{i}.q{k}.alt")}">')
                A(f'          <div><div class="qc-n">{t(q["name"], lang, f"blk{i}.q{k}.name")}</div>'
                  f'<div class="qc-t">{t(q["title"], lang, f"blk{i}.q{k}.title")}</div></div>')
                A('        </div>')
                A('      </div>')
            A('    </div>\n')
        elif b["kind"] == "factsheet":
            A('    <div class="fs">')
            A(f'      <div class="fs-h">{t(b["h"], lang, f"blk{i}.fs.h")}</div>')
            for k, r in enumerate(b["rows"]):
                A('      <div class="fs-row">'
                  f'<div class="fs-k">{t(r["k"], lang, f"blk{i}.fs.k{k}")}</div>'
                  f'<div class="fs-v">{t(r["v"], lang, f"blk{i}.fs.v{k}")}</div></div>')
            A('    </div>\n')
        elif b["kind"] == "endmark":
            A(f'    <div class="endmark">{t(b["text"], lang, f"blk{i}.endmark")}</div>\n')
        elif b["kind"] == "about":
            A('    <div class="about">')
            for k, c in enumerate(b["cols"]):
                A('      <div class="ab">'
                  f'<h6>{t(c["h"], lang, f"blk{i}.ab{k}.h")}</h6>'
                  f'<p>{t(c["p"], lang, f"blk{i}.ab{k}.p")}</p></div>')
            A('    </div>\n')
        elif b["kind"] == "contact":
            A('    <div class="mc">')
            A(f'      <h6>{t(b["h"], lang, f"blk{i}.mc.h")}</h6>')
            A(f'      <div class="mc-o">{t(b["org"], lang, f"blk{i}.mc.org")}</div>')
            A(f'      <p>{t(b["lines"], lang, f"blk{i}.mc.lines")}</p>')
            A('    </div>\n')
        elif b["kind"] == "img_2col":
            A('    <div class="ph-2col">')
            _r = b.get("ratio", "43")   # 43=橫式 · 34=直式（直式硬套 4:3 會把主體切掉）
            for k, src in enumerate(b["imgs"]):
                A(f'      <img class="gi gi-{_r}" src="{src}" alt="{t(b["alts"][k], lang, f"blk{i}.alt{k}")}">')
            A('    </div>')
            A(f'    <div class="cap">{t(b["cap"], lang, f"blk{i}.cap")}</div>\n')

    A('  </div>\n')
    A('  <div class="cta">')
    A(f'    <h4>{t(CTA["h"], lang, "cta.h")}</h4>')
    A(f'    <p>{t(CTA["p"], lang, "cta.p")}</p>')
    A(f'    <a href="{CTA.get("href", "https://mfmk.markforged.tw")}" class="btn">'
      f'{t(CTA["btn"], lang, "cta.btn")}</a>')
    A('  </div>\n')
    # 2026-09-24 Brian：資料來源段不對外顯示。
    # 做成條件式而非刪除 —— sidus / physical-ai 等既有文章仍在用這段，
    # 直接拿掉會讓它們的取材聲明一起消失（病根：same-root-cause 反面，別誤傷旁人）。
    # 關法＝該篇 content_*.py 設 SHOW_SOURCES = False，或 SRC["items"] 留空。
    if getattr(_C, "SHOW_SOURCES", True) and SRC.get("items"):
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
                 out[L].count('class="cap"'), out[L].count('class="qc"'),
                 out[L].count('class="fs-row"'), out[L].count('class="ab"'),
                 out[L].count('class="mc"'), out[L].count('class="endmark"'),
                 out[L].count('class="qc-who"'))
             for L in LANGS}
    if len(set(shape.values())) != 1:
        for L in LANGS:
            print(f"   {L}: sec/img/hl/li/cap/qc/fs/ab/mc/end/who = {shape[L]}")
        sys.exit("✗ G2 結構同形閘：三版結構不一致")
    print(f"  ✅ G2 結構同形：sec/img/hl/li/cap/qc/fs/ab/mc/end/who = {shape['tw']}（三版一致）")

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

    # ── G6 原稿覆蓋率閘 ─────────────────────────────────────────────────────
    # 2026-09-24 事故：網頁版靜默砍掉原稿的 Ivan Siu 引言／活動資料／關於雙方／傳媒查詢／完稿記號，
    # G1-G5 全綠 —— 因為那五道量的都是「三個語版彼此對齊」，沒有一道量「對齊事實來源」。
    # 本閘從來源 md 抽出**改寫後也必須倖存**的硬 token（數值+單位／時間／email／網域／電話／
    # 門牌／英數專名），逐一確認落在繁中版裡。刻意不落地的必須列進 COVERAGE_EXEMPT 並寫理由。
    if SOURCE_MD:
        import pathlib
        src = pathlib.Path(SOURCE_MD)
        if not src.exists():                       # fail-closed：宣告了卻讀不到 = 紅燈，不是跳過
            sys.exit(f"✗ G6 覆蓋率閘：宣告的來源稿讀不到 {SOURCE_MD}")
        mdtxt = src.read_text("utf-8")
        mdtxt = re.sub(r"\A---\n.*?\n---\n", "", mdtxt, flags=re.S)   # 前言＝內部核稿欄位
        mdtxt = re.sub(r"^.*\.jpg\s*\|.*$", "", mdtxt, flags=re.M)      # ::: figure 的 vault 圖路徑
        TOKEN_PAT = (r"[\d][\d,\.]*\s*(?:MPa|磅|公斤|公里|公克|克)"
                     r"|\b\d{1,2}:\d{2}\b"
                     r"|[\w\.\-]+@[\w\.\-]+\.\w+"
                     r"|www\.[\w\.\-]+"
                     r"|\b\d{4}\s\d{4}\b"
                     r"|[\u4e00-\u9fff]{2,4}路\s?\d+\s?號"
                     r"|\b[A-Z][A-Za-z0-9]{2,}(?:\s[A-Z][A-Za-z0-9]+)?\b")
        tokens = sorted(set(re.findall(TOKEN_PAT, mdtxt)))
        tw_body = text_of(out["tw"])
        missing = [x for x in tokens if x not in tw_body and x not in COVERAGE_EXEMPT]
        if missing:
            sys.exit("✗ G6 覆蓋率閘：來源稿有、繁中版沒有的 %d 項 —— %s\n"
                     "   （若為刻意不落地，寫進 content 的 COVERAGE_EXEMPT 並註明理由）"
                     % (len(missing), " | ".join(missing)))
        print(f"  ✅ G6 原稿覆蓋率：來源 {len(tokens)} 項硬 token 全數落在繁中版"
              + (f"（豁免 {len(COVERAGE_EXEMPT)} 項，已具名列出理由）" if COVERAGE_EXEMPT else ""))

    # ── G7 照片重複閘 ───────────────────────────────────────────────────────
    # 2026-09-24 Brian 親糾：「照片你重複用了你知道嗎？」—— 同一場大合照的「專業版」與
    # 「現場版」是兩個檔名、兩個 md5，但肉眼就是同一個畫面。檔名去重擋不住這種重複，
    # 所以用感知雜湊（16x16 平均雜湊 · 256 bit）量「看起來像不像」。
    # 閾值 60：實測同一畫面 1 與 41，最近的不同畫面 91 —— 中間留了 30 bit 的餘裕。
    try:
        from PIL import Image
    except ImportError:
        sys.exit("✗ G7 照片重複閘：缺 Pillow，無法驗證照片是否重複（閘壞掉一律紅燈，不跳過）")

    def _ahash(path, n=16):
        im = Image.open(path).convert("L").resize((n, n), Image.LANCZOS)
        px = list(im.getdata()); avg = sum(px) / len(px)
        return sum(1 << i for i, v in enumerate(px) if v > avg)

    srcs = [m for m in re.findall(r'<img[^>]+src="([^"]+)"', out["tw"])
            if "logo" not in m.lower()]
    dupes = [x for x in set(srcs) if srcs.count(x) > 1]
    if dupes:
        sys.exit(f"✗ G7 照片重複閘：同一個檔在頁面上出現多次 —— {' | '.join(dupes)}")
    hashes = {}
    for rel in srcs:
        f = os.path.join(OUT_DIR, rel)
        if not os.path.exists(f):
            sys.exit(f"✗ G7 照片重複閘：圖檔不存在 {rel}（圖掉了不會有錯誤訊息，所以在這裡擋）")
        hashes[rel] = _ahash(f)
    near = []
    keys = list(hashes)
    for i2 in range(len(keys)):
        for j2 in range(i2 + 1, len(keys)):
            d = bin(hashes[keys[i2]] ^ hashes[keys[j2]]).count("1")
            if d <= 60:
                near.append(f"{keys[i2]} ≈ {keys[j2]}（距離 {d}）")
    if near:
        sys.exit("✗ G7 照片重複閘：以下是同一個畫面的不同版本，不得同頁並用 —— "
                 + " | ".join(near))
    print(f"  ✅ G7 照片重複：{len(srcs)} 張內容照片，互不重複（最近感知距離已驗 > 60）")

    print("\n✅ 七道閘全綠")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FX10 活動頁（活動主視覺版）產生器 —— 一份內容源（content_fx10landing.py）產出繁中／簡中／英文三頁＋出廠閘。

2026-11-11 建立（Brian：「這個頁面要做得更盛大一點、更有吸引力才對」）。
文章版 build_article.py 是 700px 單欄報導版型，裝不下全幅影片開場、章節橫幅、案例卡牆，所以另寫一支；
網站共用的東西照舊：<body> 後第一行 globalbar.js、analytics.js、三語 langbar（langbar_gate 認得的格式）、
hreflang、頁尾 www.markforged.tw。

閘（任何一道失敗 exit 1，不寫檔以外的事）：
  L1 覆蓋率     tw／en 每個字串都要有；cn 沒給就由 tw 自動轉（content_fx10campaign_sc.cn）
  L2 英文純度   英文頁文字層（不含語言切換列）零 CJK／全形字元
  L3 簡中       OpenCC t2s 回驗零差異；國防字眼零；台灣用語零
  L4 引號       可見文字不得出現引號包句（網站冒名引言閘的同一條規則）
  L5 禁用字     Metal X、PX100、65%、ULTEM、FX10 重量、六色（2026-11-13 起 Onyx GF 七色）、Onyx Pro
  L6 機型標籤   每張案例卡都有機型標籤；標成 FX10 的只能是 GRP 與 Plane Support
  L7 資源存在   每個 img／video／poster 檔案都在，且同一頁同一張圖不重複
  L8 網站共用件 globalbar 在 <body> 後第一行、analytics.js、www 頁尾、三語切換恰一個 on、hreflang 三條
"""
import html as _html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import content_fx10landing as C  # noqa: E402
from content_fx10campaign_sc import cn as _to_cn  # noqa: E402
import opencc  # noqa: E402

OUT = os.path.dirname(HERE)
_T2S = opencc.OpenCC("t2s")


def T(node, lang, path="?"):
    if not isinstance(node, dict):
        return node
    if lang == "cn":
        if node.get("cn"):
            return node["cn"]
        if not node.get("tw"):
            sys.exit(f"✗ L1 覆蓋率：{path} 缺 tw（cn 無從轉）")
        return _to_cn(node["tw"])
    v = node.get(lang)
    if not v:
        sys.exit(f"✗ L1 覆蓋率：{path} 缺 {lang}")
    return v


def keep(item, lang):
    if lang == "cn" and (item.get("defense") or item.get("no_cn")):
        return False
    if lang != "cn" and item.get("cn_only"):
        return False
    return True


CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{--y:#FFFF00;--k:#000;--w:#fff;--g1:#f3f3f1;--g2:#e7e7e4;--mut:#8f8f8f;--line:rgba(255,255,255,.14)}
html{scroll-behavior:smooth}
body{background:#fff;color:#111;font-family:-apple-system,BlinkMacSystemFont,'Helvetica Neue',Helvetica,Arial,'PingFang TC','PingFang SC','Noto Sans TC','Noto Sans SC',sans-serif;-webkit-font-smoothing:antialiased;line-height:1.6}
a{color:inherit}
img{display:block;max-width:100%}
.wrapx{max-width:1200px;margin:0 auto;padding:0 32px}
/* 頂部列 */
.top{background:#000;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:14px 32px;gap:16px;flex-wrap:wrap}
.top .logo img{height:24px}
.top .ev{font-size:11px;color:rgba(255,255,255,.55);text-align:right;line-height:1.5}
.langbar{display:flex;gap:6px;align-items:center;background:#111;padding:8px 32px;border-top:1px solid #222}   /* 全站標準版位：header 之下、hero 之上（langbar.py） */
.langbar span{color:#777;font-size:10px;letter-spacing:.12em;text-transform:uppercase;margin-right:4px}
.langbar a{font-size:11.5px;font-weight:700;color:#999;text-decoration:none;padding:3px 10px;border-radius:20px;border:1px solid #333}
.langbar a:hover{color:var(--y);border-color:var(--y)}
.langbar a.on{background:var(--y);color:#000;border-color:var(--y)}
/* 首屏 */
.hero{position:relative;min-height:max(540px,calc(100vh - 170px));min-height:max(540px,calc(100svh - 170px));display:flex;align-items:flex-end;color:#fff;overflow:hidden;background:#000}   /* 170px＝官網導覽列 64＋頁首＋語言列，讓按鈕落在首屏內 */
.hero video,.hero .poster{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,.25) 35%,rgba(0,0,0,.82) 100%)}
.hero-in{position:relative;z-index:2;width:100%;max-width:1200px;margin:0 auto;padding:0 32px 52px}
.kicker{display:inline-block;color:var(--y);font-size:13px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;margin-bottom:18px}
.hero h1{font-size:clamp(40px,7.2vw,104px);line-height:1.04;font-weight:900;letter-spacing:-.01em;max-width:13em}
.hero p.sub{font-size:clamp(16px,1.6vw,20px);line-height:1.7;color:rgba(255,255,255,.9);max-width:46em;margin-top:22px}
.btns{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}
.btn{display:inline-block;font-weight:800;font-size:15px;text-decoration:none;padding:15px 26px;border-radius:2px;letter-spacing:.02em;transition:transform .15s,background .15s}
.btn:hover{transform:translateY(-2px)}
.btn.y{background:var(--y);color:#000}
.btn.o{border:2px solid #fff;color:#fff}
.btn.k{background:#000;color:var(--y)}
.btn.ok{border:2px solid #000;color:#000}
/* 跑馬燈 */
.ticker{background:var(--y);color:#000;overflow:hidden;white-space:nowrap;border-top:1px solid #000;border-bottom:1px solid #000}
.ticker div{display:inline-block;padding:14px 0;font-weight:900;font-size:clamp(18px,2.2vw,28px);letter-spacing:-.01em;animation:tk 38s linear infinite}
.ticker span{margin:0 28px}
.ticker i{font-style:normal;margin:0 6px}
@keyframes tk{from{transform:translateX(0)}to{transform:translateX(-50%)}}
/* 章節導覽 */
.nav{background:#000;position:sticky;top:64px;z-index:20;border-bottom:1px solid #222}   /* 64px＝官網導覽列 globalbar 高度（sticky、z-index 10000），貼它下方 */
[id]{scroll-margin-top:122px}
.nav .wrapx{display:flex;gap:4px;overflow-x:auto}
.nav a{color:#bbb;text-decoration:none;font-size:13px;font-weight:700;padding:13px 14px;white-space:nowrap;border-bottom:3px solid transparent}
.nav a:hover{color:#fff;border-bottom-color:var(--y)}
/* FX10 一句話 */
.line3{background:#0b0b0b;color:#fff;padding:64px 0}
.line3 h2{font-size:clamp(24px,3vw,38px);font-weight:900;line-height:1.25;max-width:22em}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;margin-top:34px;background:#222}
.g3 > div{background:#0b0b0b;padding:26px 24px 28px;border-top:3px solid var(--y)}
.g3 b{display:block;font-size:20px;font-weight:900;margin-bottom:8px}
.g3 span{color:#bdbdbd;font-size:14.5px;line-height:1.7}
/* 數字帶 */
.stats{background:#000;color:#fff;padding:80px 0 72px}
.sec-h{font-size:12px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:var(--y);margin-bottom:10px}
.stats h2{font-size:clamp(28px,3.4vw,44px);font-weight:900}
.stats .note{color:#9a9a9a;font-size:13.5px;margin-top:10px;max-width:60em}
.sg{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:#262626;margin-top:36px;border:1px solid #262626}
.sg > div{background:#000;padding:30px 26px}
.sg .n{font-size:clamp(28px,3.6vw,48px);font-weight:900;color:var(--y);line-height:1.1;letter-spacing:-.01em}
.sg .l{font-size:15px;color:#e6e6e6;margin-top:10px;line-height:1.6}
.sg .src{display:inline-block;margin-top:12px;font-size:11.5px;font-weight:700;color:#000;background:#d9d9d9;padding:2px 8px;border-radius:2px}
.sg .src.fx{background:var(--y)}
/* 零件入口 */
.finder{background:var(--g1);padding:72px 0}
.finder h2{font-size:clamp(26px,3vw,40px);font-weight:900}
.finder p.sub{color:#555;margin-top:6px}
.fg{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:28px}
.fg a{display:flex;justify-content:space-between;align-items:flex-end;gap:12px;background:#fff;text-decoration:none;padding:22px 22px 20px;border:1px solid var(--g2);transition:all .15s;min-height:112px}
.fg a:hover{background:#000;color:#fff;border-color:#000}
.fg a:hover .ar{background:var(--y);color:#000}
.fg b{display:block;font-size:19px;font-weight:900;line-height:1.35}
.fg small{display:block;color:#888;font-size:12.5px;margin-top:6px}
.fg .ar{flex:none;width:36px;height:36px;border-radius:50%;background:#000;color:var(--y);display:flex;align-items:center;justify-content:center;font-weight:900}
/* 章節橫幅 */
.chap{position:relative;min-height:74vh;display:flex;align-items:flex-end;color:#fff;background:#000 center/cover no-repeat;overflow:hidden}
.chap:before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.2) 0%,rgba(0,0,0,.15) 40%,rgba(0,0,0,.88) 100%)}
.chap-in{position:relative;width:100%;max-width:1200px;margin:0 auto;padding:0 32px 64px}
.chap .no{font-size:14px;font-weight:900;color:var(--y);letter-spacing:.2em}
.chap .big{font-size:clamp(48px,10vw,150px);font-weight:900;line-height:.95;letter-spacing:-.03em;margin:10px 0 18px}
.chap h2{font-size:clamp(22px,2.6vw,32px);font-weight:900}
.chap p{font-size:clamp(15px,1.5vw,19px);color:rgba(255,255,255,.88);max-width:44em;margin-top:10px;line-height:1.7}
/* 章節內容 */
.chbody{padding:64px 0 76px;background:#fff}
.vid{position:relative;padding-top:56.25%;background:#000;margin-bottom:12px}
.vid video{position:absolute;inset:0;width:100%;height:100%}
.vcap{font-size:12.5px;color:#888;margin-bottom:46px}
.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}
.card{background:#fff;border:1px solid var(--g2);display:flex;flex-direction:column}
.card .im{aspect-ratio:16/9;overflow:hidden;background:#111}
.card .im img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.card:hover .im img{transform:scale(1.04)}
.card .bd{padding:24px 26px 26px;display:flex;flex-direction:column;flex:1}
.badges{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px}
.bdg{font-size:11.5px;font-weight:800;padding:3px 9px;border-radius:2px;background:#ececea;color:#333}
.bdg.m{background:#111;color:#fff}
.bdg.m.fx{background:var(--y);color:#000}
.bdg.mat{background:#fff;border:1px solid #bbb}
.card h3{font-size:20px;font-weight:900;line-height:1.4}
.card .tg{font-size:12.5px;color:#888;margin-top:6px}
.card p{font-size:15px;color:#333;margin-top:12px;line-height:1.75;flex:1}
.card .mt{margin-top:18px;padding-top:16px;border-top:2px solid #000;display:flex;justify-content:space-between;align-items:flex-end;gap:12px;flex-wrap:wrap}
.card .mt b{font-size:clamp(22px,2.4vw,30px);font-weight:900;line-height:1.1;background:linear-gradient(transparent 62%,var(--y) 62%)}
.card .mt a{font-size:13px;font-weight:800;color:#000;text-decoration:none;border-bottom:2px solid #000;white-space:nowrap}
.card .ex{font-size:13px;margin-top:12px}
.card .ex a{color:#000;font-weight:700}
.card.ft{grid-column:1 / -1;flex-direction:row}
.card.ft .im{flex:0 0 56%;aspect-ratio:auto;min-height:380px}
.card.ft h3{font-size:clamp(22px,2.2vw,28px)}
.chcta{margin-top:30px;text-align:right}
.chcta a{font-weight:900;font-size:16px;color:#000;text-decoration:none;background:var(--y);padding:13px 20px;display:inline-block}
/* Onyx GF */
.onyx{background:var(--g1);padding:84px 0}
.og{display:grid;grid-template-columns:1.1fr 1fr;gap:44px;align-items:center}
.og img{width:100%;background:#000}
.onyx h2{font-size:clamp(30px,3.8vw,52px);font-weight:900;line-height:1.1}
.onyx p.in{font-size:17px;color:#333;margin-top:14px;line-height:1.75}
.onyx .facts{font-size:13px;color:#555;margin-top:16px;padding:12px 14px;background:#fff;border-left:4px solid #000}
.u4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:34px}
.u4 div{background:#fff;padding:22px 20px;border-top:4px solid #000}
.u4 b{display:block;font-size:17px;font-weight:900;margin-bottom:6px}
.u4 span{font-size:14px;color:#555;line-height:1.65}
/* 產品 */
.prod{background:#000;color:#fff;padding:92px 0}
.pg{display:grid;grid-template-columns:1fr 1.15fr;gap:56px;align-items:start}
.pg img{width:100%;background:#111}
.prod h2{font-size:clamp(30px,3.8vw,52px);font-weight:900;line-height:1.12;margin-top:6px}
.prod p.b{font-size:16px;color:#cfcfcf;margin-top:18px;line-height:1.8}
.spec{margin-top:30px;border-top:3px solid var(--y)}
.spec h3{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#9a9a9a;font-weight:800;margin:16px 0 4px}
.spec .r{display:grid;grid-template-columns:9em 1fr;gap:14px;padding:11px 0;border-bottom:1px solid #262626;font-size:14.5px}
.spec .r span:first-child{color:#9a9a9a}
.prod .bundle{margin-top:22px;font-size:14.5px;color:#ddd}
.prod .bundle a{color:var(--y);font-weight:800;text-decoration:none}
/* 下一步 */
.steps{padding:76px 0;background:#fff}
.steps h2{font-size:clamp(26px,3vw,40px);font-weight:900}
.s3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:28px;counter-reset:s}
.s3 div{border-top:3px solid #000;padding-top:18px}
.s3 div:before{counter-increment:s;content:"0" counter(s);display:block;font-size:44px;font-weight:900;line-height:1;margin-bottom:10px;color:#000;-webkit-text-stroke:0}
.s3 b{display:block;font-size:19px;font-weight:900}
.s3 span{color:#555;font-size:14.5px}
/* 行動區 */
.cta{background:var(--y);color:#000;padding:92px 0}
.cg{display:grid;grid-template-columns:1.4fr 1fr;gap:48px;align-items:center}
.cta h2{font-size:clamp(32px,4.6vw,64px);font-weight:900;line-height:1.08;letter-spacing:-.01em}
.cta p{font-size:17px;margin-top:18px;line-height:1.75;max-width:40em}
.cta .eb{font-size:14.5px;margin-top:18px}
.cta .eb a{font-weight:800}
.win{background:#000;color:#fff;padding:28px;display:flex;gap:18px;align-items:center}
.win img{width:84px;height:84px;border-radius:50%;object-fit:cover;border:3px solid var(--y);flex:none}
.win small{display:block;color:var(--y);font-weight:800;font-size:11px;letter-spacing:.16em;text-transform:uppercase}
.win b{display:block;font-size:19px;margin-top:4px}
.win .t{font-size:13px;color:#ccc}
.win .d{font-size:13.5px;color:#eee;margin-top:8px;line-height:1.6}
.win a{color:var(--y);font-size:13.5px;font-weight:700}
/* 延伸閱讀 */
.read{padding:68px 0;background:#fff}
.read h2{font-size:22px;font-weight:900;margin-bottom:18px}
.rg{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.rg a{display:block;text-decoration:none;padding:20px 20px 22px;border:1px solid var(--g2);border-left:4px solid #000;transition:border-color .15s}
.rg a:hover{border-left-color:var(--y);background:var(--g1)}
.rg b{display:block;font-size:16px;line-height:1.45}
.rg small{display:block;color:#888;margin-top:8px;font-size:12.5px}
/* 頁尾 */
.ftr{background:#000;color:#888;font-size:12.5px;line-height:1.8;padding:38px 0 46px}
.ftr a{color:var(--y);text-decoration:none;font-weight:700}
/* 進場動畫（沒有 JS 時內容照常可見） */
.js .rv{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s ease}
.js .rv.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){.ticker div{animation:none}.js .rv{opacity:1;transform:none}html{scroll-behavior:auto}}
@media (max-width:900px){
 .wrapx,.hero-in,.chap-in{padding-left:20px;padding-right:20px}
 .langbar{padding:8px 20px}
 .g3,.sg,.fg,.u4,.s3,.rg{grid-template-columns:1fr 1fr}
 .og,.pg,.cg{grid-template-columns:1fr}
 .cards{grid-template-columns:1fr}
 .card.ft{flex-direction:column}.card.ft .im{flex:none;min-height:0;aspect-ratio:16/9}
 .top{padding:12px 20px}
}
@media (max-width:560px){
 .g3,.sg,.fg,.u4,.s3,.rg{grid-template-columns:1fr}
 .hero-in{padding-bottom:40px}
 .chap{min-height:62vh}
 .spec .r{grid-template-columns:7.5em 1fr}
}
"""

JS = r"""
document.documentElement.classList.add('js');
(function(){
  var els=document.querySelectorAll('.rv');
  if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in')});return;}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}})},{rootMargin:'0px 0px -8% 0px'});
  els.forEach(function(e){io.observe(e)});
  // 保險：捲到接近頁底時，還沒出場的一律顯示（避免頁尾前的元素永遠進不了觀察範圍）
  window.addEventListener('scroll',function(){
    if(window.innerHeight+window.scrollY>=document.body.scrollHeight-400){els.forEach(function(e){e.classList.add('in')});}
  },{passive:true});
})();
"""


def render(lang):
    E = _html.escape
    P = []
    A = P.append
    title = T(C.META["title"], lang, "title")
    A(f'<!DOCTYPE html>\n<html lang="{C.LANG_ATTR[lang]}">\n<head>\n<meta charset="UTF-8">')
    A('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    A(f"<title>{title}</title>")
    A(f'<meta name="description" content="{E(T(C.META["desc"], lang, "desc"))}">')
    A(f'<meta property="og:title" content="{E(T(C.META["og_title"], lang, "og_title"))}">')
    A(f'<meta property="og:description" content="{E(T(C.META["og_desc"], lang, "og_desc"))}">')
    A(f'<meta property="og:image" content="https://news.markforged.tw/images/{C.S}-hero.jpg">')
    A('<meta property="og:type" content="article">')
    for L in C.LANGS:
        A(f'<link rel="alternate" hreflang="{C.LANG_ATTR[L]}" href="https://news.markforged.tw/{C.FILES[L]}">')
    A(f"<style>{CSS}</style>")
    A('<script src="analytics.js" defer></script>')
    A("</head>\n<body>\n<script src=\"/globalbar.js\"></script>")
    A(f"<script>{JS.split(chr(10))[1]}</script>")   # 只先加 .js class；觀察器放頁尾

    # 頂部列＋語言
    ON_ATTR = ' class="on"'
    links = "".join(f'<a href="{C.FILES[L]}"{ON_ATTR if L == lang else ""}>{C.LANG_NAMES[L]}</a>' for L in C.LANGS)
    A('<div class="top"><a href="index.html" class="logo"><img src="images/markforged-logo-white.png" alt="Markforged"></a>'
      f'<div class="ev">{T(C.UI["hdr_ev"], lang)}</div></div>')
    A(f'<div class="langbar"><span>{T(C.UI["switch_label"], lang)}</span>{links}</div>')

    # 首屏
    H = C.HERO
    A('<div class="hero">'
      f'<img class="poster" src="images/{C.S}-hero-poster.jpg" alt="{E(T(C.UI["hero_alt"], lang))}">'
      f'<video autoplay muted loop playsinline preload="auto" poster="images/{C.S}-hero-poster.jpg" aria-hidden="true">'
      f'<source src="video/{C.S}-hero-loop.mp4" type="video/mp4"></video>'
      '<div class="hero-in">'
      f'<div class="kicker">{T(H["kicker"], lang, "hero.kicker")}</div>'
      f'<h1>{T(H["h1"], lang, "hero.h1")}</h1>'
      f'<p class="sub">{T(H["sub"], lang, "hero.sub")}</p>'
      f'<div class="btns"><a class="btn y" href="{E(C.mailto("demo", {"tw": "首屏", "cn": "首屏", "en": "hero"}[lang], lang))}">{T(H["cta1"], lang)}</a>'
      f'<a class="btn o" href="#cases">{T(H["cta2"], lang)}</a></div>'
      '</div></div>')

    # 跑馬燈
    tk = "".join(f"<span>{t}</span><i>／</i>" if lang != "en" else f"<span>{t}</span><i>/</i>" for t in C.TICKER)
    A(f'<div class="ticker" aria-hidden="true"><div>{tk * 4}</div></div>')

    # 章節導覽
    nav = "".join(f'<a href="{h}">{T(t, lang)}</a>' for h, t, d in C.UI["nav"] if not (d and lang == "cn"))
    A(f'<nav class="nav"><div class="wrapx">{nav}</div></nav>')

    # FX10 一句話
    L3 = C.FX10_LINE
    items = "".join(f'<div class="rv"><b>{T(i["b"], lang)}</b><span>{T(i["s"], lang)}</span></div>' for i in L3["items"])
    A(f'<section class="line3"><div class="wrapx"><h2 class="rv">{T(L3["h"], lang)}</h2><div class="g3">{items}</div></div></section>')

    # 數字帶
    St = C.STATS
    sg = ""
    for i in St["items"]:
        if not keep(i, lang):
            continue
        fx = " fx" if i.get("fx10") else ""
        sg += (f'<div class="rv"><div class="n">{T(i["n"], lang)}</div><div class="l">{T(i["l"], lang)}</div>'
               f'<span class="src{fx}">{T(i["src"], lang)}</span></div>')
    A(f'<section class="stats" id="cases"><div class="wrapx"><div class="sec-h">{T(C.UI["machine_note"], lang)}</div>'
      f'<h2>{T(St["h"], lang)}</h2><p class="note">{T(St["note"], lang)}</p><div class="sg">{sg}</div></div></section>')

    # 零件入口
    F = C.FINDER
    fg = "".join(f'<a class="rv" href="{i["href"]}"><span><b>{T(i["t"], lang)}</b><small>{i["c"]}</small></span><span class="ar">→</span></a>'
                 for i in F["items"] if keep(i, lang))
    A(f'<section class="finder"><div class="wrapx"><h2>{T(F["h"], lang)}</h2><p class="sub">{T(F["sub"], lang)}</p><div class="fg">{fg}</div></div></section>')

    def card(cid):
        c = C.CASES[cid]
        m = c["machine"]
        mb = f'<span class="bdg m{" fx" if m == "fx10" else ""}">{T(C.MACHINE[m], lang)}</span>'
        if c.get("material"):
            mat = {"tw": f'材料 {c["material"]}（FX10 可列印）', "en": f'Material: {c["material"]} (prints on FX10)'}
            mb += f'<span class="bdg mat">{T(mat, lang)}</span>'
        ex = f'<div class="ex">{T(c["extra"], lang)}</div>' if c.get("extra") else ""
        return (f'<article class="card rv{" ft" if c.get("featured") else ""}" id="case-{cid}">'
                f'<div class="im"><img src="{c["img"]}" alt="{E(T(c["alt"], lang))}" loading="lazy"></div>'
                f'<div class="bd"><div class="badges">{mb}</div><h3>{T(c["title"], lang)}</h3>'
                f'<div class="tg">{T(c["tags"], lang)}</div><p>{T(c["body"], lang)}</p>{ex}'
                f'<div class="mt"><b>{T(c["metric"], lang)}</b><a href="{c["url"]}">{T(C.UI["read_original"], lang)}</a></div></div></article>')

    def chapter(ch):
        A(f'<section class="chap" id="{ch["id"]}" style="background-image:url(\'{ch["img"]}\')"><div class="chap-in">'
          f'<div class="no">{ch["no"]}</div><div class="big">{ch["big"]}</div>'
          f'<h2>{T(ch["h"], lang)}</h2><p>{T(ch["intro"], lang)}</p></div></section>')
        A('<div class="chbody"><div class="wrapx">')
        v = ch.get("video")
        if v and keep(v, lang):
            A(f'<div class="vid rv"><video src="{v["src"]}" poster="{v["poster"]}" controls playsinline preload="metadata"></video></div>'
              f'<div class="vcap">{T(C.UI[v["cap"]], lang)}</div>')
        A('<div class="cards">' + "".join(card(c) for c in ch["cases"] if keep(C.CASES[c], lang)) + "</div>")
        A(f'<div class="chcta"><a href="{E(C.mailto("part", T(ch["cta_where"], lang), lang))}">{T(C.CH_CTA, lang)}</a></div>')
        A("</div></div>")

    ON = C.ONYX
    for ch in C.CHAPTERS:
        if not keep(ch, lang):
            continue
        chapter(ch)
        if ch["id"] == "ch-auto":
            u4 = "".join(f'<div class="rv"><b>{T(u["b"], lang)}</b><span>{T(u["s"], lang)}</span></div>' for u in ON["uses"])
            A(f'<section class="onyx" id="onyx-gf"><div class="wrapx"><div class="og">'
              f'<img class="rv" src="{ON["img"]}" alt="{E(T(ON["alt"], lang))}" loading="lazy">'
              f'<div class="rv"><div class="sec-h" style="color:#000">{T(ON["kicker"], lang)}</div><h2>{T(ON["h"], lang)}</h2>'
              f'<p class="in">{T(ON["intro"], lang)}</p><div class="facts">{T(ON["facts"], lang)}</div></div></div>'
              f'<div class="u4">{u4}</div></div></section>')

    # 產品
    PR = C.PRODUCT
    rows = "".join(f'<div class="r"><span>{T(k, lang)}</span><span>{T(v, lang)}</span></div>' for k, v in PR["specs"])
    A(f'<section class="prod" id="fx10"><div class="wrapx"><div class="pg">'
      f'<img class="rv" src="{PR["img"]}" alt="{E(T(PR["alt"], lang))}" loading="lazy">'
      f'<div class="rv"><div class="sec-h">{T(PR["kicker"], lang)}</div><h2>{T(PR["h"], lang)}</h2><p class="b">{T(PR["body"], lang)}</p>'
      f'<div class="spec"><h3>{T(PR["specs_h"], lang)}</h3>{rows}</div><p class="bundle">{T(PR["bundle"], lang)}</p></div>'
      f'</div></div></section>')

    # 下一步
    SP = C.STEPS
    s3 = "".join(f'<div class="rv"><b>{T(i["b"], lang)}</b><span>{T(i["s"], lang)}</span></div>' for i in SP["items"])
    A(f'<section class="steps"><div class="wrapx"><h2>{T(SP["h"], lang)}</h2><div class="s3">{s3}</div></div></section>')

    # 行動區
    CT = C.CTA
    A(f'<section class="cta" id="contact"><div class="wrapx"><div class="cg"><div class="rv">'
      f'<h2>{T(CT["h"], lang)}</h2><p>{T(CT["p"], lang)}</p>'
      f'<div class="btns"><a class="btn k" href="{E(C.mailto("demo", {"tw": "行動區", "cn": "行动区", "en": "contact"}[lang], lang))}">{T(CT["btn1"], lang)}</a>'
      f'<a class="btn ok" href="{E(C.mailto("part", {"tw": "行動區", "cn": "行动区", "en": "contact"}[lang], lang))}">{T(CT["btn2"], lang)}</a></div>'
      f'<p class="eb">{T(CT["ebook"], lang)}</p></div>'
      f'<div class="win rv"><img src="brian-chen.jpg" alt="{E(T(CT["win_name"], lang))}"><div>'
      f'<small>{T(CT["win_label"], lang)}</small><b>{T(CT["win_name"], lang)}</b><div class="t">{T(CT["win_title"], lang)}</div>'
      f'<div class="d">{T(CT["win_desc"], lang)}</div><a href="mailto:{C.MAIL}">{C.MAIL}</a></div></div>'
      f'</div></div></section>')

    # 延伸閱讀
    RD = C.READ
    rg = "".join(f'<a class="rv" href="{T(i["href"], lang) if lang != "cn" else i["href"]["cn"]}"><b>{T(i["t"], lang)}</b><small>{T(i["s"], lang)}</small></a>'
                 for i in RD["items"] if keep(i, lang))
    A(f'<section class="read"><div class="wrapx"><h2>{T(RD["h"], lang)}</h2><div class="rg">{rg}</div></div></section>')

    A(f'<footer class="ftr"><div class="wrapx">{T(C.FTR["about"], lang)}<br><br>'
      f'<a href="index.html">{T(C.FTR["back"], lang)}</a>　·　<a href="https://www.markforged.tw/">markforged.tw</a></div></footer>')
    A(f"<script>{JS}</script>")
    A("</body>\n</html>\n")
    return "\n".join(P)


def text_of(h, drop_langbar=True):
    h = re.sub(r"<(style|script)[^>]*>.*?</\1>", " ", h, flags=re.S)
    h = re.sub(r"<head>.*?</head>", " ", h, flags=re.S)
    if drop_langbar:
        h = re.sub(r'<div class="langbar">.*?</div>', " ", h, flags=re.S)
    return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", " ", h)))


def gates(out):
    ok = True
    def fail(msg):
        nonlocal ok
        ok = False
        print("  ✗ " + msg)
    # L2
    cjk = re.findall(r"[一-鿿　-〿＀-￯]", text_of(out["en"]))
    fail(f"L2 英文純度：殘留 {''.join(sorted(set(cjk)))}") if cjk else print("  ✅ L2 英文純度：英文頁零 CJK／全形")
    # L3
    cnt = text_of(out["cn"])
    diff = [a for a, b in zip(cnt, _T2S.convert(cnt)) if a != b]
    fail(f"L3 簡中殘留繁體：{''.join(sorted(set(diff)))}") if diff else print("  ✅ L3 簡中：t2s 回驗零差異")
    defw = [w for w in ["国防", "军", "Fort Irwin", "Cannon", "退伍", "夜视", "战机", "aerospace-defense", "case-irwin", "ch-defense", "Defense", "defense"] if w in out["cn"]]
    fail(f"L3 簡中出現國防內容：{defw}") if defw else print("  ✅ L3 簡中：國防字眼與國防素材零")
    tw_terms = [w for w in ["列印", "治具", "航太", "积层", "雷射", "量测", "公厘", "澳洲", "影片", "工安", "控管"] if w in cnt]
    fail(f"L3 簡中台灣用語：{tw_terms}") if tw_terms else print("  ✅ L3 簡中：台灣用語零")
    # L4
    for L, h in out.items():
        q = re.findall(r"[「」『』“”\"]", text_of(h))
        fail(f"L4 引號：{L} 版有 {len(q)} 個") if q else None
    print("  ✅ L4 引號：三版可見文字零引號") if ok else None
    # L5
    ban = ["Metal X", "PX100", "65%", "ULTEM", "109 kg", "122 kg", "six colors", "six-color", "六色", "Onyx Pro", "bella", "claude", "MF-GCR"]
    for L, h in out.items():
        hit = [b for b in ban if b.lower() in h.lower()]
        fail(f"L5 禁用字：{L} 版 {hit}") if hit else None
    print("  ✅ L5 禁用字：零")
    # L6
    fx = [cid for cid, c in C.CASES.items() if c["machine"] == "fx10"]
    if sorted(fx) != ["grp", "plane"]:
        fail(f"L6 標成 FX10 的案例必須只有 GRP 與 Plane Support，現在是 {fx}")
    for cid, c in C.CASES.items():
        if c.get("machine") not in C.MACHINE:
            fail(f"L6 案例 {cid} 沒有合法機型標籤")
    for L, h in out.items():
        n_card = h.count('<article class="card')
        n_bdg = len(re.findall(r'class="bdg m(?: fx)?"', h))
        if n_card != n_bdg:
            fail(f"L6 {L} 版 {n_card} 張案例卡、{n_bdg} 個機型標籤，對不上")
    print("  ✅ L6 機型標籤：每張卡都有，FX10 只標在 GRP 與 Plane Support")
    # L7
    for L, h in out.items():
        srcs = re.findall(r'(?:src|poster)="((?:images|video)/[^"]+)"', h) + re.findall(r"url\('((?:images|video)/[^']+)'\)", h)
        miss = [s for s in set(srcs) if not os.path.exists(os.path.join(OUT, s))]
        if miss:
            fail(f"L7 {L} 版缺檔 {miss}")
        imgs = [s for s in re.findall(r'<img[^>]+src="([^"]+)"', h)]
        dup = sorted({s for s in imgs if imgs.count(s) > 1 and "poster" not in s})
        if dup:
            fail(f"L7 {L} 版同一張圖重複 {dup}")
    print("  ✅ L7 資源：圖片影片皆在、無重複圖")
    # L8
    for L, h in out.items():
        body_first = re.search(r"<body>\s*(<script[^>]*>)", h)
        if not body_first or "globalbar.js" not in body_first.group(1):
            fail(f"L8 {L} 版 <body> 後第一行不是 globalbar.js")
        if 'src="analytics.js"' not in h or 'href="https://www.markforged.tw/"' not in h:
            fail(f"L8 {L} 版缺 analytics.js 或 www 頁尾")
        lb = re.search(r'<div class="langbar">(.*?)</div>', h, flags=re.S).group(1)
        if lb.count('class="on"') != 1 or len(re.findall(r"<a ", lb)) != 3:
            fail(f"L8 {L} 版語言切換列不是三語恰一個 on")
        if len(re.findall(r'rel="alternate" hreflang=', h)) != 3:
            fail(f"L8 {L} 版 hreflang 不是三條")
    print("  ✅ L8 網站共用件：導覽列、統計、www 頁尾、三語切換、hreflang")
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

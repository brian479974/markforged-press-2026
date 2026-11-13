#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Onyx GF 橘色新色上市頁 —— 內容與產生器同檔，一份內容源產出繁中／簡中／英文三頁＋出廠閘。

2026-11-13 建立（Brian 傳原廠主視覺＋APAC Slack 上市公告：「Onyx GF Orange 新色發佈更新到 news.markforged.tw」）。
版型沿用 FX10 活動頁（build_fx10_landing.py 的 CSS／JS），網站共用件照舊：<body> 後第一行 globalbar.js、
analytics.js、三語 langbar、hreflang、頁尾 www.markforged.tw。

事實來源（每一句都對得回去）：
  · 原廠 2026-11-10 全球發表信〈Onyx GF Orange: A new shade of strength〉（hello@markforged.com）
    —— 三個理由（PLA／ABS 兩倍以上強度、免噴漆塗裝貼標、FX10／FX20 加 CFR 強度可比鋁件）、
       用途（safety-critical tooling、functional color-coding、customer-facing components、
       shop-floor visibility、match specific brand requirements）
  · APAC 2026 年 10 月夥伴通訊：橘色是 Onyx GF 第七個顏色；FX10、FX20 搭配 Hardened Plastic Nozzle；
    high-visibility safety tooling、colour-coded jigs and fixtures、error-proofing
  · 原廠 Onyx GF Material Datasheet V01（vault MF-GCR/60_Products/support/datasheets/）—— 只取不會讀錯欄的數字
    （抗拉強度 yield／break 兩列在 PDF 版面上容易對調，不寫）；規格表未依顏色分列，頁面照實註明
  · 2026-06 原廠上市信：印 Onyx GF 必須先換硬化塑料噴嘴，否則損壞列印系統
  · Subaru 案沿用 FX10 活動頁已逐句對過的寫法（原文未寫機型）

閘（任何一道失敗 exit 1）：
  L1 覆蓋率  L2 英文純度  L3 簡中（t2s 回驗、台灣用語零）  L4 引號  L5 禁用字（含過期色數 六色／six colors）
  L6 規格對帳（頁面上的每個數字都要在 SPEC_LEDGER 裡，且三語一致）  L7 資源存在、同頁不重複
  L8 網站共用件
"""
import html as _html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_fx10_landing as BASE  # noqa: E402  只借 JS 與 text_of
from content_fx10campaign_sc import cn as _cn_base  # noqa: E402
import opencc  # noqa: E402
from urllib.parse import quote  # noqa: E402

OUT = os.path.dirname(HERE)


def _live_css():
    """CSS 取自線上 FX10 活動頁的 <style>（不是 build_fx10_landing.CSS）：2026-11-13 實測建置器落後線上——
    少了 globalbar 下藏頁首 logo、卡片標題整詞斷行、手機行動區不撐寬三處全站修正，直接用建置器的 CSS 會把它們弄丟。"""
    import re as _re
    h = open(os.path.join(OUT, "fx10-it-starts-here.html"), encoding="utf-8").read()
    css = _re.search(r"<style>(.*?)</style>", h, flags=_re.S).group(1)
    for must in ("body:has(#mfg-bar) .top .logo", ".cg>*{min-width:0}"):
        if must not in css:
            sys.exit(f"✗ 線上 FX10 頁 CSS 少了 {must}，不要用它當底")
    return css


_T2S = opencc.OpenCC("t2s")

S = "onyx-gf-orange-2026-11"
LANGS = ("tw", "cn", "en")
FILES = {"tw": f"{S}.html", "cn": f"{S}-sc.html", "en": f"{S}-en.html"}
LANG_ATTR = {"tw": "zh-TW", "cn": "zh-CN", "en": "en"}
LANG_NAMES = {"tw": "繁體中文", "cn": "简体中文", "en": "English"}
MAIL = "brian.chen@markforged.com"
OR = "#F07A2A"   # 取自原廠主視覺 NEW COLOR 字色（產品色，只用在產品相關的點綴；按鈕與語言列照全站黃）

URL = {
    "onyxgf": "https://markforged.com/materials/plastics/onyx-gf",
    "subaru": "https://markforged.com/resources/blog/keeping-the-line-moving-color-coded-tooling-at-subaru",
}

# 本頁簡中站內連結
_SC_LINKS = ["fx10-it-starts-here", "automotive-am-perspective-2026-11", "fx10-sinter2-bundle", S]
_TERMS = [("橘色", "橙色"), ("橘", "橙"), ("工安", "安全"), ("玻纖", "玻纤"), ("防呆", "防错"),
          ("對外零件", "对外零件"), ("展示台", "展台"), ("上漆", "喷漆"), ("寄零件圖檔", "发零件图档"),
          ("洽詢", "咨询"), ("经销伙伴", "经销合作伙伴"),
          # 2026-11-13 逐句讀簡中版後補（tw2sp 轉成台式或轉錯的）
          ("可以直接來信，或洽當地", "可以直接发邮件给我们，或联系当地"), ("缺省", "默认"), ("就能印", "就能打印"),
          ("印好就是", "打印出来就是"), ("全球發表", "全球发布"), ("印 Onyx GF 之前", "打印 Onyx GF 之前"), ("重印", "重新打印")]


def cn(s):
    out = _cn_base(s)
    for a, b in _TERMS:
        out = out.replace(_T2S.convert(a), b).replace(a, b)
    for slug in _SC_LINKS:
        out = out.replace(f'href="{slug}.html"', f'href="{slug}-sc.html"').replace(f'href="{slug}.html#', f'href="{slug}-sc.html#')
    return out


def T(node, lang, path="?"):
    if not isinstance(node, dict):
        return node
    if lang == "cn":
        if node.get("cn"):
            return node["cn"]
        if not node.get("tw"):
            sys.exit(f"✗ L1 覆蓋率：{path} 缺 tw（cn 無從轉）")
        return cn(node["tw"])
    v = node.get(lang)
    if not v:
        sys.exit(f"✗ L1 覆蓋率：{path} 缺 {lang}")
    return v


MAIL_BODY = {
    "tw": "您好，\n\n公司：\n產業：\n零件用途：\n目前使用的機型（FX10／FX20／尚未導入）：\n所在地區（台灣／中國／香港／越南）：\n\n（如有零件圖檔請一併附上）\n",
    "cn": "您好，\n\n公司：\n行业：\n零件用途：\n目前使用的机型（FX10／FX20／尚未导入）：\n所在地区（台湾／中国／香港／越南）：\n\n（如有零件图档请一并附上）\n",
    "en": "Hello,\n\nCompany:\nIndustry:\nWhat the part does:\nPrinter in use (FX10 / FX20 / none yet):\nLocation (Taiwan / China / Hong Kong / Vietnam):\n\n(Please attach a part file if you have one.)\n",
}
SUBJ = {
    "quote": {"tw": "Onyx GF 橘色洽詢／報價", "cn": "Onyx GF 橙色咨询／报价", "en": "Onyx GF Orange enquiry / quote"},
    "part": {"tw": "Onyx GF 零件評估（寄圖檔）", "cn": "Onyx GF 零件评估（发图档）", "en": "Onyx GF part review (part file)"},
}
WHERE = {"hero": {"tw": "首屏", "cn": "首屏", "en": "hero"}, "cta": {"tw": "行動區", "cn": "行动区", "en": "contact"}}


def mailto(kind, where, lang):
    w = WHERE[where][lang]
    subj = f"{SUBJ[kind][lang]}｜{w}" if lang != "en" else f"{SUBJ[kind][lang]} | {w}"
    return f"mailto:{MAIL}?subject={quote(subj)}&body={quote(MAIL_BODY[lang])}"


META = {
    "title": {"tw": "Onyx GF 新色：橘色上市｜Markforged 媒體中心", "en": "Onyx GF, Now in Orange | Markforged Newsroom"},
    "desc": {"tw": "Onyx GF 第七個顏色：橘色。短切玻璃纖維強化尼龍、不導電，FX10 與 FX20 換上硬化塑料噴嘴就能印，適合工安治具、色碼防呆與對外展示的零件。",
             "en": "Orange is the seventh Onyx GF color: a non-conductive, chopped-glass-fiber nylon for the FX10 and FX20 with the Hardened Plastic Nozzle, made for safety tooling, color-coded error-proofing and customer-facing parts."},
    "og_title": {"tw": "Onyx GF，現在有橘色", "en": "Onyx GF, now in orange"},
    "og_desc": {"tw": "Onyx GF 第七個顏色。醒目的橘色，留給工安治具、色碼防呆，以及要拿給客戶看的零件。",
                "en": "The seventh Onyx GF color, for safety tooling, color-coded error-proofing and parts your customers will see."},
}

UI = {
    "hdr_ev": {"tw": "大中華區暨越南　媒體中心<br>News &amp; Insights", "cn": "大中华区暨越南　媒体中心<br>News &amp; Insights",
               "en": "Greater China &amp; Vietnam　Newsroom<br>News &amp; Insights"},
    "switch_label": {"tw": "語言", "cn": "语言", "en": "Language"},
    "hero_alt": {"tw": "橘色 Onyx GF 列印的治具（Markforged 原廠圖片）", "en": "A fixture printed in Onyx GF Orange (official Markforged image)"},
}

HERO = {
    "kicker": {"tw": "新色上市 ・ Onyx GF", "en": "New color · Onyx GF"},
    "h1": {"tw": "Onyx GF，<br>現在有橘色。", "en": "Onyx GF,<br>now in orange."},
    "date": {"tw": "Markforged 原廠 2026 年 11 月 10 日全球發表", "en": "Released worldwide by Markforged on November 10, 2026"},
    "sub": {"tw": "Onyx GF 的第七個顏色。同樣是短切玻璃纖維強化尼龍、同樣不導電，FX10 與 FX20 換上硬化塑料噴嘴就能印。醒目的橘色，留給工安治具、色碼防呆，以及要拿給客戶看的零件。",
            "en": "The seventh Onyx GF color. The same chopped-glass-fiber nylon, the same non-conductive properties, printed on the FX10 and FX20 with the Hardened Plastic Nozzle. Use it for safety tooling, color-coded error-proofing and the parts your customers will see."},
    "cta1": {"tw": "洽詢報價", "en": "Ask for a quote"},
    "cta2": {"tw": "看材料規格&nbsp;↓", "en": "See the specs&nbsp;↓"},
}

WHY = {
    "h": {"tw": "原廠給的三個理由", "en": "Three reasons, from Markforged"},
    "items": [
        {"b": {"tw": "工業級強度", "en": "Industrial-grade performance"},
         "s": {"tw": "原廠說法：強度是一般 PLA 或 ABS 的兩倍以上。", "en": "More than twice the strength of standard PLA or ABS, according to Markforged."}},
        {"b": {"tw": "印好就是成品色", "en": "Finished color off the bed"},
         "s": {"tw": "下了列印平台就是均勻乾淨的顏色，不必再噴漆、塗裝或貼標籤。", "en": "Clean, uniform color straight off the print bed, with no painting, coating or labeling afterward."}},
        {"b": {"tw": "可加連續纖維", "en": "Continuous fiber reinforcement"},
         "s": {"tw": "在 FX10、FX20 上搭配連續纖維強化，零件強度可與鋁件相比。", "en": "On the FX10 and FX20, add Continuous Fiber Reinforcement for parts that rival aluminum in strength."}},
    ],
}

USES = {
    "kicker": {"tw": "橘色用在哪裡", "en": "Where orange works"},
    "h": {"tw": "要被一眼看見的地方", "en": "Wherever it has to be seen"},
    "intro": {"tw": "原廠對橘色的定位很直接：工安治具、功能性色碼，以及外觀要好看、又要符合工業標準的對外零件。",
              "en": "Markforged positions orange for safety-critical tooling, functional color-coding and customer-facing parts that need to look sharp while meeting industrial standards."},
    "items": [
        {"b": {"tw": "工安治具", "en": "Safety tooling"},
         "s": {"tw": "危險區旁的護罩、擋塊與定位治具，用高辨識度的橘色列印", "en": "Guards, stops and locating fixtures near hazards, printed in high-visibility orange"}},
        {"b": {"tw": "色碼防呆", "en": "Error-proofing"},
         "s": {"tw": "治具依產線、車型或版本配色，拿錯一眼就看得出來", "en": "Fixtures coded by line, model or revision, so a wrong pick shows at a glance"}},
        {"b": {"tw": "對外零件", "en": "Customer-facing parts"},
         "s": {"tw": "要交給客戶或擺上展示台的零件，顏色直接印出來，不必再上漆", "en": "Parts that go to customers or on display come off the printer in color, with no paint"}},
        {"b": {"tw": "品牌配色", "en": "Brand colors"},
         "s": {"tw": "零件要對上企業或產品識別色時，多一個選擇", "en": "One more option when parts have to match a corporate or product color"}},
    ],
}

PALETTE = {
    "img": f"images/fx10-it-starts-here-onyxgf.jpg",
    "alt": {"tw": "原有六色 Onyx GF 線材與綠色列印治具（Markforged 原廠圖片）", "en": "The original six Onyx GF colors and a fixture printed in green (official Markforged image)"},
    "kicker": {"tw": "色盤", "en": "Palette"},
    "h": {"tw": "七種顏色，一種材料", "en": "Seven colors, one material"},
    "intro": {"tw": "橘色加入後，Onyx GF 共有紅、黃、綠、藍、灰、白、橘七色。材料相同，顏色依用途挑。",
              "en": "With orange, Onyx GF comes in seven colors: red, yellow, green, blue, gray, white and orange. One material; pick the color for the job."},
    "chips": [
        ("#D52B1E", {"tw": "紅", "en": "Red"}, False), ("#F5CF00", {"tw": "黃", "en": "Yellow"}, False),
        ("#00916F", {"tw": "綠", "en": "Green"}, False), ("#1F3FA6", {"tw": "藍", "en": "Blue"}, False),
        ("#7A7C80", {"tw": "灰", "en": "Gray"}, False), ("#F2F2F0", {"tw": "白", "en": "White"}, False),
        ("#E8601A", {"tw": "橘", "en": "Orange"}, True),
    ],
    "new": {"tw": "新色", "en": "New"},
    "note": {"tw": "色塊為螢幕示意，實際顏色以線材為準。", "en": "Swatches are approximate on screen."},
    "case": {"tw": f'實際案例：Subaru 印第安納廠把會裂的 ABS 治具改用 Onyx GF 重印，每個車型配一種顏色，作業員第一次伸手就拿對；保險桿 QR 標籤定位治具精度 0.1 mm（原文未寫機型）。<a href="{URL["subaru"]}">原廠案例（英文）&nbsp;→</a>',
             "en": f'In practice: Subaru of Indiana reprinted cracking ABS jigs in Onyx GF and gave each model its own color, so operators grab the right tool on the first pass; the bumper QR-label placement jigs hold a 0.1 mm tolerance (printer not stated in the source). <a href="{URL["subaru"]}">Read the original&nbsp;→</a>'},
}

# L6 規格對帳：頁面上出現的每個規格數字都要在這裡，值＝原廠 Onyx GF Material Datasheet V01
SPEC_LEDGER = {"3.1 GPa", "88.2 MPa", "71.8 MPa", "161 J/m", "138 °C", "1.8 MPa", "1.21 g/cm³", "125 µm", "0.1 mm"}

SPEC = {
    "kicker": {"tw": "材料規格", "en": "Specifications"},
    "h": {"tw": "Onyx GF 材料性能", "en": "Onyx GF material properties"},
    "body": {"tw": "數據取自 Markforged Onyx GF 材料規格表：FX10 列印、層厚 125 µm、預設實心填充，依 ASTM D618 調濕後於 XY 方向測試。規格表針對 Onyx GF 材料本身，未依顏色分列。",
             "en": "Figures are from the Markforged Onyx GF material datasheet: printed on an FX10 at 125 µm layer height with default solid fill, conditioned per ASTM D618 and tested in the XY orientation. The datasheet covers Onyx GF as a material and does not list figures by color."},
    "mat_h": {"tw": "機械與熱性質", "en": "Mechanical and thermal"},
    "mat": [
        ({"tw": "抗拉模數", "en": "Tensile modulus"}, "3.1 GPa", "ASTM D638"),
        ({"tw": "彎曲強度", "en": "Flexural strength"}, "88.2 MPa", "ASTM D790"),
        ({"tw": "壓縮強度", "en": "Compressive strength"}, "71.8 MPa", "ASTM D695"),
        ({"tw": "缺口 Izod 衝擊", "en": "Notched Izod impact"}, "161 J/m", "ASTM D256"),
        ({"tw": "熱變形溫度", "en": "Heat deflection temperature"}, "138 °C", "1.8 MPa"),
        ({"tw": "密度", "en": "Density"}, "1.21 g/cm³", ""),
    ],
    "use_h": {"tw": "列印條件", "en": "Printing"},
    "use": [
        ({"tw": "機型", "en": "Printers"}, {"tw": "FX10、FX20", "en": "FX10, FX20"}),
        ({"tw": "噴嘴", "en": "Nozzle"}, {"tw": "須先換裝硬化塑料噴嘴（Hardened Plastic Nozzle）", "en": "Hardened Plastic Nozzle required"}),
        ({"tw": "導電性", "en": "Conductivity"}, {"tw": "不導電", "en": "Non-conductive"}),
        ({"tw": "連續纖維", "en": "Continuous fiber"}, {"tw": "可搭配連續纖維強化", "en": "Compatible with Continuous Fiber Reinforcement"}),
    ],
    "warn": {"tw": "印 Onyx GF 之前，一定要先換上硬化塑料噴嘴。玻璃纖維比一般 Onyx 更容易磨耗噴嘴，用標準噴嘴列印會損壞列印系統。",
             "en": "Fit the Hardened Plastic Nozzle before printing Onyx GF. Glass fiber is more abrasive than standard Onyx, and printing it through a standard nozzle will damage the print system."},
    "links": {"tw": f'<a href="fx10-it-starts-here.html#fx10">FX10 規格與原廠案例&nbsp;→</a>　<a href="{URL["onyxgf"]}">原廠 Onyx GF 材料頁（英文）&nbsp;→</a>',
              "en": f'<a href="fx10-it-starts-here-en.html#fx10">FX10 specs and cases&nbsp;→</a>　<a href="{URL["onyxgf"]}">Onyx GF on markforged.com&nbsp;→</a>'},
}

CTA = {
    "h": {"tw": "把要被一眼看見的那一件，寄給我們。", "en": "Send us the part that has to stand out."},
    "p": {"tw": "寄一個零件圖檔，我們評估適不適合用 Onyx GF 列印、要不要加連續纖維，並提供報價。已經有 FX10 或 FX20 的客戶，訂購橘色線材與硬化塑料噴嘴可以直接來信，或洽當地 Markforged 經銷夥伴。",
          "en": "Send us a part file and we will check whether it suits Onyx GF, whether it needs continuous fiber, and quote it. Already running an FX10 or FX20? Order orange spools and the Hardened Plastic Nozzle by writing to us or through your local Markforged partner."},
    "btn1": {"tw": "洽詢報價", "en": "Ask for a quote"},
    "btn2": {"tw": "寄零件圖檔", "en": "Send a part file"},
    "win_label": {"tw": "你的窗口", "cn": "你的窗口", "en": "Your contact"},
    "win_name": {"tw": "陳中欣 Brian Chen", "cn": "陈中欣 Brian Chen", "en": "Brian Chen"},
    "win_title": {"tw": "Markforged 大中華區暨越南區總經理", "en": "Country Manager, Greater China and Vietnam, Markforged"},
    "win_desc": {"tw": "台灣、中國、香港、越南的 Onyx GF 與 FX 系列詢問，都可以直接找我。", "en": "For Onyx GF and FX Series enquiries in Taiwan, China, Hong Kong and Vietnam, reach me directly."},
}

READ = {
    "h": {"tw": "延伸閱讀", "en": "Further reading"},
    "items": [
        {"href": {"tw": "fx10-it-starts-here.html", "cn": "fx10-it-starts-here-sc.html", "en": "fx10-it-starts-here-en.html"},
         "t": {"tw": "不能出錯的零件，從這裡開始", "cn": "不能出错的零件，从这里开始", "en": "If it has to work, it starts here"},
         "s": {"tw": "FX10 活動頁：原廠案例、影片與 Onyx GF 色碼治具", "en": "The FX10 page: Markforged cases, films and Onyx GF color-coded tooling"}},
        {"href": {"tw": "automotive-am-perspective-2026-11.html", "cn": "automotive-am-perspective-2026-11-sc.html", "en": "automotive-am-perspective-2026-11-en.html"},
         "t": {"tw": "從研發到售後，汽車業把 3D 列印用在哪裡", "en": "From R&amp;D to aftersales: where automakers use 3D printing"},
         "s": {"tw": "本週專題 · 產業觀點", "en": "Feature · Industry perspective"}},
        {"href": {"tw": "fx10-sinter2-bundle.html", "cn": "fx10-sinter2-bundle-sc.html", "en": "fx10-sinter2-bundle-en.html"},
         "t": {"tw": "一台機器，複合材與金屬都做得到：FX10 Sinter-2 Bundle", "cn": "一台机器，复合材料与金属都能做：FX10 Sinter-2 Bundle",
               "en": "One machine, composites and metal: the FX10 Sinter-2 Bundle"},
         "s": {"tw": "主機、金屬列印引擎、清洗站、燒結爐一套四件", "en": "Printer, metal print engine, wash station and furnace"}},
    ],
}

FTR = {
    "about": {"tw": "Markforged 提供工業級積層製造系統與連續纖維複合材料，應用於航太、汽車與精密製造。本頁由 Markforged 大中華區暨越南媒體中心發布；產品資訊、圖片與數據來自 Markforged 原廠。",
              "cn": "Markforged 提供工业级增材制造系统与连续纤维复合材料，应用于航空航天、汽车与精密制造。本页由 Markforged 大中华区暨越南媒体中心发布；产品信息、图片与数据来自 Markforged 原厂。",
              "en": "Markforged builds industrial additive manufacturing systems and continuous fiber composites for aerospace, automotive and precision manufacturing. Published by the Markforged Greater China &amp; Vietnam Newsroom; product information, images and figures are from Markforged."},
    "back": {"tw": "返回媒體中心", "cn": "返回媒体中心", "en": "Back to the Newsroom"},
}

CSS_EXTRA = f"""
/* Onyx GF 橘色頁 */
.ohero{{background:#000;color:#fff;overflow:hidden;position:relative}}
.ohero .wrapx{{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:28px;min-height:max(520px,calc(100vh - 170px));min-height:max(520px,calc(100svh - 170px));position:relative;z-index:1}}
.ohero .tx{{padding:56px 0}}
.okick{{display:inline-block;color:{OR};font-size:14px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;margin-bottom:20px}}
.ohero h1{{font-size:clamp(42px,6.4vw,92px);line-height:1.05;font-weight:900;letter-spacing:-.01em}}
.ohero .bar{{width:84px;height:4px;background:{OR};margin:28px 0 20px}}
.ohero .dt{{font-size:13px;color:#9a9a9a;letter-spacing:.04em}}
.ohero p.sub{{font-size:clamp(16px,1.5vw,19px);line-height:1.75;color:rgba(255,255,255,.88);max-width:34em;margin-top:14px}}
.ohero .im{{justify-self:end;width:100%;max-width:620px}}
.ohero .im img{{width:100%}}
.why{{background:#0b0b0b;color:#fff;padding:72px 0;border-top:1px solid #1d1d1d}}
.why h2{{font-size:clamp(24px,3vw,38px);font-weight:900}}
.why .g3 > div{{border-top-color:{OR}}}
.uses{{background:var(--g1);padding:84px 0}}
.uses .sec-h{{color:#000}}
.uses h2{{font-size:clamp(30px,3.8vw,52px);font-weight:900;line-height:1.1}}
.uses p.in{{font-size:17px;color:#333;margin-top:14px;line-height:1.75;max-width:46em}}
.uses .u4 div{{border-top-color:{OR}}}
.pal{{background:#fff;padding:84px 0}}
.pal .pg2{{display:grid;grid-template-columns:1.1fr 1fr;gap:44px;align-items:center}}
.pal img{{width:100%;background:#000}}
.pal .sec-h{{color:#000}}
.pal h2{{font-size:clamp(30px,3.8vw,52px);font-weight:900;line-height:1.1}}
.pal p.in{{font-size:17px;color:#333;margin-top:14px;line-height:1.75}}
.chips{{display:grid;grid-template-columns:repeat(7,1fr);gap:10px;margin-top:26px}}
.chip{{text-align:center;font-size:13.5px;font-weight:800;color:#222}}
.chip i{{display:block;aspect-ratio:1;border-radius:50%;margin-bottom:8px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.12)}}
.chip.nw i{{box-shadow:0 0 0 3px #fff,0 0 0 5px {OR}}}
.chip small{{display:block;font-size:10.5px;font-weight:900;color:{OR};letter-spacing:.08em;text-transform:uppercase;margin-top:2px}}
.pal .nt{{font-size:12px;color:#999;margin-top:12px}}
.pal .cs{{font-size:14.5px;color:#333;line-height:1.75;margin-top:22px;padding:14px 16px;background:var(--g1);border-left:4px solid #000}}
.pal .cs a{{color:#000;font-weight:800}}
.sp{{background:#000;color:#fff;padding:88px 0}}
.sp h2{{font-size:clamp(30px,3.8vw,52px);font-weight:900;line-height:1.12;margin-top:6px}}
.sp p.b{{font-size:15px;color:#bdbdbd;margin-top:16px;line-height:1.8;max-width:56em}}
.sp .two{{display:grid;grid-template-columns:1.2fr 1fr;gap:48px;margin-top:30px}}
.sp .spec .r{{grid-template-columns:1fr auto auto}}
.sp .spec .r .v{{font-weight:800;color:#fff;text-align:right;white-space:nowrap}}
.sp .spec .r .m{{color:#7d7d7d;font-size:12.5px;text-align:right;white-space:nowrap;min-width:6.5em}}
.sp .spec2 .r{{grid-template-columns:7.5em 1fr}}
.sp .warn{{margin-top:26px;padding:16px 18px;border:1px solid {OR};border-left:6px solid {OR};font-size:14.5px;line-height:1.75;color:#eee}}
.sp .lk{{margin-top:22px;font-size:14.5px}}
.sp .lk a{{color:var(--y);font-weight:800;text-decoration:none;display:inline-block;margin:4px 0}}
@media (max-width:900px){{
 .ohero .wrapx{{grid-template-columns:1fr;min-height:0;gap:0}}
 .ohero .tx{{padding:40px 0 8px}}
 .ohero .im{{justify-self:center;max-width:360px;order:-1;margin:8px auto -28px}}   /* 手機首屏先看到橘色零件 */
 .pal .pg2,.sp .two{{grid-template-columns:1fr}}
}}
@media (max-width:560px){{
 .chips{{grid-template-columns:repeat(4,1fr)}}
 .sp .spec .r{{grid-template-columns:1fr auto}}
 .sp .spec .r .m{{display:none}}
}}
"""


def render(lang):
    E = _html.escape
    P = []
    A = P.append
    A(f'<!DOCTYPE html>\n<html lang="{LANG_ATTR[lang]}">\n<head>\n<meta charset="UTF-8">')
    A('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    A(f"<title>{T(META['title'], lang, 'title')}</title>")
    A(f'<meta name="description" content="{E(T(META["desc"], lang, "desc"))}">')
    A(f'<meta property="og:title" content="{E(T(META["og_title"], lang, "og_title"))}">')
    A(f'<meta property="og:description" content="{E(T(META["og_desc"], lang, "og_desc"))}">')
    A(f'<meta property="og:image" content="https://news.markforged.tw/images/{S}-og.jpg">')
    A('<meta property="og:type" content="article">')
    for L in LANGS:
        A(f'<link rel="alternate" hreflang="{LANG_ATTR[L]}" href="https://news.markforged.tw/{FILES[L]}">')
    A(f"<style>{_live_css()}{CSS_EXTRA}</style>")
    A('<script src="analytics.js" defer></script>')
    A("</head>\n<body>\n<script src=\"/globalbar.js\"></script>")
    A(f"<script>{BASE.JS.split(chr(10))[1]}</script>")

    links = "".join(f'<a href="{FILES[L]}"{" class=\"on\"" if L == lang else ""}>{LANG_NAMES[L]}</a>' for L in LANGS)
    A('<div class="top"><a href="index.html" class="logo"><img src="images/markforged-logo-white.png" alt="Markforged"></a>'
      f'<div class="ev">{T(UI["hdr_ev"], lang)}</div></div>')
    A(f'<div class="langbar"><span>{T(UI["switch_label"], lang)}</span>{links}</div>')

    H = HERO
    A('<section class="ohero"><div class="wrapx"><div class="tx">'
      f'<div class="okick">{T(H["kicker"], lang)}</div><h1>{T(H["h1"], lang)}</h1><div class="bar"></div>'
      f'<div class="dt">{T(H["date"], lang)}</div><p class="sub">{T(H["sub"], lang)}</p>'
      f'<div class="btns"><a class="btn y" href="{E(mailto("quote", "hero", lang))}">{T(H["cta1"], lang)}</a>'
      f'<a class="btn o" href="#specs">{T(H["cta2"], lang)}</a></div></div>'
      f'<div class="im"><img src="images/{S}-hero.jpg" alt="{E(T(UI["hero_alt"], lang))}"></div>'
      '</div></section>')

    g3 = "".join(f'<div class="rv"><b>{T(i["b"], lang)}</b><span>{T(i["s"], lang)}</span></div>' for i in WHY["items"])
    A(f'<section class="why line3"><div class="wrapx"><h2 class="rv">{T(WHY["h"], lang)}</h2><div class="g3">{g3}</div></div></section>')

    u4 = "".join(f'<div class="rv"><b>{T(i["b"], lang)}</b><span>{T(i["s"], lang)}</span></div>' for i in USES["items"])
    A(f'<section class="uses" id="uses"><div class="wrapx"><div class="rv"><div class="sec-h">{T(USES["kicker"], lang)}</div>'
      f'<h2>{T(USES["h"], lang)}</h2><p class="in">{T(USES["intro"], lang)}</p></div><div class="u4">{u4}</div></div></section>')

    PL = PALETTE
    chips = "".join(f'<div class="chip{" nw" if nw else ""}"><i style="background:{c}"></i>{T(n, lang)}'
                    f'{"<small>" + T(PL["new"], lang) + "</small>" if nw else ""}</div>' for c, n, nw in PL["chips"])
    A(f'<section class="pal" id="colors"><div class="wrapx"><div class="pg2">'
      f'<img class="rv" src="{PL["img"]}" alt="{E(T(PL["alt"], lang))}" loading="lazy">'
      f'<div class="rv"><div class="sec-h">{T(PL["kicker"], lang)}</div><h2>{T(PL["h"], lang)}</h2><p class="in">{T(PL["intro"], lang)}</p>'
      f'<div class="chips">{chips}</div><p class="nt">{T(PL["note"], lang)}</p><p class="cs">{T(PL["case"], lang)}</p></div>'
      '</div></div></section>')

    SP = SPEC
    mat = "".join(f'<div class="r"><span>{T(k, lang)}</span><span class="v">{v}</span><span class="m">{m}</span></div>' for k, v, m in SP["mat"])
    use = "".join(f'<div class="r"><span>{T(k, lang)}</span><span>{T(v, lang)}</span></div>' for k, v in SP["use"])
    A(f'<section class="sp" id="specs"><div class="wrapx"><div class="sec-h">{T(SP["kicker"], lang)}</div><h2>{T(SP["h"], lang)}</h2>'
      f'<p class="b">{T(SP["body"], lang)}</p><div class="two">'
      f'<div class="spec rv"><h3>{T(SP["mat_h"], lang)}</h3>{mat}</div>'
      f'<div class="rv"><div class="spec spec2"><h3>{T(SP["use_h"], lang)}</h3>{use}</div><div class="warn">{T(SP["warn"], lang)}</div>'
      f'<div class="lk">{T(SP["links"], lang)}</div></div>'
      '</div></div></section>')

    CT = CTA
    A(f'<section class="cta" id="contact"><div class="wrapx"><div class="cg"><div class="rv">'
      f'<h2>{T(CT["h"], lang)}</h2><p>{T(CT["p"], lang)}</p>'
      f'<div class="btns"><a class="btn k" href="{E(mailto("quote", "cta", lang))}">{T(CT["btn1"], lang)}</a>'
      f'<a class="btn ok" href="{E(mailto("part", "cta", lang))}">{T(CT["btn2"], lang)}</a></div></div>'
      f'<div class="win rv"><img src="brian-chen.jpg" alt="{E(T(CT["win_name"], lang))}"><div>'
      f'<small>{T(CT["win_label"], lang)}</small><b>{T(CT["win_name"], lang)}</b><div class="t">{T(CT["win_title"], lang)}</div>'
      f'<div class="d">{T(CT["win_desc"], lang)}</div><a href="mailto:{MAIL}">{MAIL}</a></div></div>'
      '</div></div></section>')

    rg = "".join(f'<a class="rv" href="{i["href"][lang]}"><b>{T(i["t"], lang)}</b><small>{T(i["s"], lang)}</small></a>' for i in READ["items"])
    A(f'<section class="read"><div class="wrapx"><h2>{T(READ["h"], lang)}</h2><div class="rg">{rg}</div></div></section>')

    A(f'<footer class="ftr"><div class="wrapx">{T(FTR["about"], lang)}<br><br>'
      f'<a href="index.html">{T(FTR["back"], lang)}</a>　·　<a href="https://www.markforged.tw/">markforged.tw</a></div></footer>')
    A(f"<script>{BASE.JS}</script>")
    A("</body>\n</html>\n")
    return "\n".join(P)


text_of = BASE.text_of


def gates(out):
    ok = True

    def fail(msg):
        nonlocal ok
        ok = False
        print("  ✗ " + msg)
    cjk = re.findall(r"[一-鿿　-〿＀-￯]", text_of(out["en"]))
    fail(f"L2 英文純度：殘留 {''.join(sorted(set(cjk)))}") if cjk else print("  ✅ L2 英文純度：英文頁零 CJK／全形")
    cnt = text_of(out["cn"])
    diff = [a for a, b in zip(cnt, _T2S.convert(cnt)) if a != b]
    fail(f"L3 簡中殘留繁體：{''.join(sorted(set(diff)))}") if diff else print("  ✅ L3 簡中：t2s 回驗零差異")
    tw_terms = [w for w in ["列印", "治具", "航太", "积层", "雷射", "量测", "公厘", "影片", "工安", "控管", "橘", "防呆", "洽询", "资讯"] if w in cnt]
    fail(f"L3 簡中台灣用語：{tw_terms}") if tw_terms else print("  ✅ L3 簡中：台灣用語零")
    for L, h in out.items():
        q = re.findall(r"[「」『』“”\"]", text_of(h))
        fail(f"L4 引號：{L} 版有 {len(q)} 個") if q else None
    ban = ["Metal X", "PX100", "六色", "六種", "six colors", "six-color", "800 cc", "800cc", "bella", "claude", "MF-GCR", "vault"]
    for L, h in out.items():
        hit = [b for b in ban if b.lower() in text_of(h, drop_langbar=False).lower()]
        fail(f"L5 禁用字：{L} 版 {hit}") if hit else None
    # 圖片 alt 例外：PALETTE 圖本身拍的就是原有六色，alt 照實寫「原有六色」—— 只查可見文字
    print("  ✅ L4／L5 引號與禁用字") if ok else None
    # L6 規格對帳
    for L, h in out.items():
        t = text_of(h)
        nums = set(re.findall(r"\d+(?:\.\d+)?\s?(?:GPa|MPa|J/m|°C|g/cm³|µm|mm)", t))
        stray = sorted(n for n in nums if n not in SPEC_LEDGER)
        if stray:
            fail(f"L6 {L} 版出現帳外數字 {stray}")
        missing = sorted(n for n in SPEC_LEDGER if n not in t)
        if missing:
            fail(f"L6 {L} 版少了帳上數字 {missing}")
    print("  ✅ L6 規格對帳：三語數字＝原廠規格表帳") if ok else None
    for L, h in out.items():
        srcs = re.findall(r'(?:src|poster)="((?:images|video)/[^"]+)"', h)
        miss = [s for s in set(srcs) if not os.path.exists(os.path.join(OUT, s))]
        if miss:
            fail(f"L7 {L} 版缺檔 {miss}")
        imgs = re.findall(r'<img[^>]+src="([^"]+)"', h)
        dup = sorted({s for s in imgs if imgs.count(s) > 1})
        if dup:
            fail(f"L7 {L} 版同一張圖重複 {dup}")
        for href in re.findall(r'href="([a-z0-9-]+\.html)(?:#[^"]*)?"', h):
            if not os.path.exists(os.path.join(OUT, href)) and href not in FILES.values():
                fail(f"L7 {L} 版站內連結指向不存在的頁 {href}")
        if L == "cn":
            body = re.sub(r'<div class="langbar">.*?</div>', " ", h.split("<body>", 1)[1], flags=re.S)   # 語言切換列本來就要連三語
            bad = [x for x in re.findall(r'href="([a-z0-9-]+)\.html', body) if not x.endswith("-sc") and x != "index"
                   and os.path.exists(os.path.join(OUT, x + "-sc.html"))]
            if bad:
                fail(f"L7 簡中版連到繁中頁（有簡中版卻沒用）{bad}")
    print("  ✅ L7 資源與站內連結") if ok else None
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
    print("  ✅ L8 網站共用件") if ok else None
    return ok


def main():
    out = {L: render(L) for L in LANGS}
    for L, h in out.items():
        open(os.path.join(OUT, FILES[L]), "w", encoding="utf-8").write(h)
        print(f"✓ 產出 {FILES[L]}  {len(h)//1024} KB")
    print("\n── 閘門 ──")
    if not gates(out):
        sys.exit("\n✗ 閘門未全綠")
    print("\n✅ 閘門全綠")


if __name__ == "__main__":
    main()

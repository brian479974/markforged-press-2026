# -*- coding: utf-8 -*-
"""FX10 + Sinter-2 Bundle 廣告 — 三語內容源（繁中 / 簡中 / English 的唯一真相）。

2026-10-10 建立。Brian 交辦：做一支 FX10 + Sinter-2 Bundle 的廣告，並加到 news.markforged.tw。

引言政策（G1 冒名引言閘）：
  **本文沒有任何一句直接引言** —— 沒有影片受訪者、也沒有任何一句掛在 Brian 名下。
  全文敘述體。APPROVED_QUOTES 三語皆為空陣列，閘因此無話可放行，也無話可擋。

事實出處（每一條都可回溯，無推估、無未經原廠文件背書的數字）：
  · Bundle 組成 ＝ SKU **F-PR-5505**「FX10 Sinter-2 Bundle（FX10＋Metal Kit＋Sinter-2＋Wash-1）」
    — 報價引擎自 pricebook 解價，見 MF-GCR/70_Pricing/Quotes/Intellengine/
      Quote_Intellengine_DemoUnit_FX10-Sinter2-Bundle_1Y_Q4-Special_2026-10-05.md
  · 一機雙模 / swappable metal print engine — MF-GCR/60_Products/FX10.md §1.2–1.3
  · 金屬流程 列印→清洗(Wash-1)→燒結(Sinter-2) — 同上 §1.3
  · 產品現役狀態 — MF-GCR/60_Products/_product-status-registry.md
    （FX10 / Metal Kit / Wash-1 / Sinter-2 皆現役；全文未提任何 EOL/EOS 機種）

刻意不寫的東西：
  ✗ 價格（只進 70_Pricing）
  ✗ 「15 分鐘切換」— 只見於我方 RFP 獨規論證，非原廠 datasheet
  ✗ 任何強度倍數 / 層厚 / 建構體積 / 最大零件尺寸
    — FX10 金屬有三層尺寸口徑（可列印空間／生胚／燒結後成品），講漏一層就會誤導，
      廣告頁不需要，一律不寫

影片與圖片：
  · 影片＝本次自製廣告，自託管於本 repo `video/fx10-sinter2-bundle.mp4`（不依賴 Drive 公開連結）
  · 頁面圖片全部是該影片的畫格；影片素材為 Markforged 官網原廠產品圖與原廠實拍，非 AI 生成
"""

LANGS = ("tw", "cn", "en")

MP4    = "video/fx10-sinter2-bundle.mp4"
POSTER = "images/fx10-sinter2-poster.jpg"

META = {
    "lang_attr": {"tw": "zh-TW", "cn": "zh-CN", "en": "en"},
    "file": {"tw": "fx10-sinter2-bundle.html",
             "cn": "fx10-sinter2-bundle-sc.html",
             "en": "fx10-sinter2-bundle-en.html"},
    "hero": "images/fx10-sinter2-bundle.jpg",
    "og_image": "https://news.markforged.tw/images/fx10-sinter2-bundle.jpg",
    "title": {
        "tw": "一台機器，複合材與金屬都做得到：FX10 Sinter-2 Bundle — Markforged",
        "cn": "一台机器，复合材料与金属都能做：FX10 Sinter-2 Bundle — Markforged",
        "en": "One Machine, Composites and Metal: The FX10 Sinter-2 Bundle — Markforged",
    },
    "desc": {
        "tw": "FX10 Sinter-2 Bundle 由四個部分組成：FX10 雙模式主機、可替換的 Metal Kit 金屬列印引擎、"
              "Wash-1 脫脂清洗站與 Sinter-2 高溫燒結爐。平時印連續碳纖維複合材，需要金屬件時換上金屬引擎，"
              "列印、清洗、燒結都在自己廠內完成。附 28 秒影片。",
        "cn": "FX10 Sinter-2 Bundle 由四个部分组成：FX10 双模式主机、可更换的 Metal Kit 金属打印引擎、"
              "Wash-1 脱脂清洗站与 Sinter-2 高温烧结炉。平时打印连续碳纤维复合材料，需要金属件时换上金属引擎，"
              "打印、清洗、烧结都在自己厂内完成。附 28 秒视频。",
        "en": "The FX10 Sinter-2 Bundle has four parts: the dual-mode FX10, a swappable Metal Kit "
              "print engine, the Wash-1 debinding station and the Sinter-2 furnace. Print continuous "
              "carbon fiber day to day, swap in the metal engine when you need metal parts, and run "
              "printing, washing and sintering in your own facility. Includes a 28-second film.",
    },
    "og_title": {
        "tw": "一台機器，複合材與金屬都做得到",
        "cn": "一台机器，复合材料与金属都能做",
        "en": "One Machine, Composites and Metal",
    },
    "og_desc": {
        "tw": "FX10 Sinter-2 Bundle：主機、金屬列印引擎、清洗站、燒結爐，一套四件。",
        "cn": "FX10 Sinter-2 Bundle：主机、金属打印引擎、清洗站、烧结炉，一套四件。",
        "en": "The FX10 Sinter-2 Bundle: printer, metal print engine, wash station and furnace.",
    },
}

UI = {
    "hdr_ev": {"tw": "大中華區媒體中心<br>News &amp; Insights",
               "cn": "大中华区媒体中心<br>News &amp; Insights",
               "en": "Greater China Media Hub<br>News &amp; Insights"},
    "switch_label": {"tw": "語言", "cn": "语言", "en": "Language"},
    "hero_alt": {
        "tw": "FX10 Sinter-2 Bundle 的四個組成：FX10 主機、Metal Kit、Wash-1、Sinter-2",
        "cn": "FX10 Sinter-2 Bundle 的四个组成：FX10 主机、Metal Kit、Wash-1、Sinter-2",
        "en": "The four parts of the FX10 Sinter-2 Bundle: FX10, Metal Kit, Wash-1 and Sinter-2"},
    "hero_kicker": {"tw": "產品方案 · 混合製造", "cn": "产品方案 · 混合制造",
                    "en": "Solution · Hybrid Manufacturing"},
    "hero_title": {
        "tw": "一台機器，複合材與金屬都做得到",
        "cn": "一台机器，复合材料与金属都能做",
        "en": "One Machine, Composites and Metal"},
    "hero_meta": {
        "tw": "FX10 Sinter-2 Bundle ｜ 大中華區 ｜ 2026.10.10",
        "cn": "FX10 Sinter-2 Bundle ｜ 大中华区 ｜ 2026.10.10",
        "en": "FX10 Sinter-2 Bundle | Greater China | 2026.10.10"},
    "ds_l": {"tw": "一套四件：FX10、Metal Kit、Wash-1、Sinter-2",
             "cn": "一套四件：FX10、Metal Kit、Wash-1、Sinter-2",
             "en": "Four parts: FX10, Metal Kit, Wash-1, Sinter-2"},
    "ds_r": {"tw": "複合材與金屬共用同一台主機",
             "cn": "复合材料与金属共用同一台主机",
             "en": "Composites and metal share the same printer"},
}

LEAD = {
    "p1": {
        "tw": "多數工廠導入 3D 列印時會遇到同一個岔路：複合材與金屬要不要分兩套設備。"
              "分開買，預算與場地都翻倍，而且兩條線各自閒置；只買一套，"
              "另一類零件就得繼續外包等待。",
        "cn": "多数工厂导入 3D 打印时会遇到同一个岔路：复合材料与金属要不要分两套设备。"
              "分开买，预算与场地都翻倍，而且两条线各自闲置；只买一套，"
              "另一类零件就得继续外包等待。",
        "en": "Most factories adopting 3D printing hit the same fork: do composites and metal need "
              "two separate machines? Buy both and the budget and floor space double while each "
              "line sits idle part of the time. Buy one and the other category of parts stays "
              "outsourced.",
    },
    "p2": {
        "tw": "<strong>FX10 Sinter-2 Bundle</strong> 的作法是讓兩者共用同一台主機。"
              "FX10 平時以連續碳纖維列印複合材零件；需要金屬件時換上 Metal Kit 金屬列印引擎，"
              "再由 Wash-1 與 Sinter-2 完成清洗與燒結 —— 一條完整的金屬產線，都在自己廠內。",
        "cn": "<strong>FX10 Sinter-2 Bundle</strong> 的做法是让两者共用同一台主机。"
              "FX10 平时以连续碳纤维打印复合材料零件；需要金属件时换上 Metal Kit 金属打印引擎，"
              "再由 Wash-1 与 Sinter-2 完成清洗与烧结 —— 一条完整的金属产线，都在自己厂内。",
        "en": "The <strong>FX10 Sinter-2 Bundle</strong> lets both share one printer. The FX10 runs "
              "continuous carbon fiber composites day to day; when metal parts are needed, the Metal "
              "Kit print engine swaps in, and Wash-1 and Sinter-2 handle debinding and sintering — "
              "a complete metal production line, in your own facility.",
    },
}

PROF = {
    "alt": {"tw": "陳中欣", "cn": "陈中欣", "en": "Brian Chen"},
    "name": {"tw": "陳中欣 Brian Chen", "cn": "陈中欣 Brian Chen", "en": "Brian Chen"},
    "title": {"tw": "Markforged 大中華區暨越南區總經理",
              "cn": "Markforged 大中华区暨越南区总经理",
              "en": "Country Manager, Greater China and Vietnam, Markforged"},
    "desc": {
        "tw": "負責 Markforged 在台灣、中國、香港與越南的市場，"
              "長期與航太、國防與精密製造領域的製造商合作。",
        "cn": "负责 Markforged 在台湾、中国、香港与越南的市场，"
              "长期与航空航天、国防与精密制造领域的制造商合作。",
        "en": "Responsible for Markforged across Taiwan, China, Hong Kong and Vietnam, working with "
              "manufacturers in aerospace, defence and precision manufacturing.",
    },
}

TAGS = [
    {"tw": "FX10", "cn": "FX10", "en": "FX10", "solid": True},
    {"tw": "Sinter-2", "cn": "Sinter-2", "en": "Sinter-2", "solid": True},
    {"tw": "金屬列印", "cn": "金属打印", "en": "Metal 3D Printing", "solid": False},
    {"tw": "連續碳纖維", "cn": "连续碳纤维", "en": "Continuous Carbon Fiber", "solid": False},
    {"tw": "混合製造", "cn": "混合制造", "en": "Hybrid Manufacturing", "solid": False},
]

BLOCKS = [
    {
        "kind": "mp4",
        "src": MP4,
        "poster": POSTER,
        "alt": {"tw": "FX10 Sinter-2 Bundle 廣告影片，28 秒",
                "cn": "FX10 Sinter-2 Bundle 广告视频，28 秒",
                "en": "FX10 Sinter-2 Bundle film, 28 seconds"},
        "cap": {
            "tw": "FX10 Sinter-2 Bundle ｜ 28 秒 ｜ Markforged 大中華區",
            "cn": "FX10 Sinter-2 Bundle ｜ 28 秒 ｜ Markforged 大中华区",
            "en": "FX10 Sinter-2 Bundle | 28 seconds | Markforged Greater China",
        },
    },
    {
        "kind": "sec",
        "h2": {"tw": "這一套裡面有什麼", "cn": "这一套里面有什么",
               "en": "What is in the bundle"},
        "h3": {"tw": "四個部分，涵蓋從列印到燒結的完整金屬流程",
               "cn": "四个部分，涵盖从打印到烧结的完整金属流程",
               "en": "Four parts, covering the full metal workflow from printing to sintering"},
        "paras": [
            {"tw": "FX10 Sinter-2 Bundle 是一個完整配置，不是單機加購清單。"
                   "四個部分各自負責金屬流程的一段，缺任何一段，金屬零件都無法在廠內完成。",
             "cn": "FX10 Sinter-2 Bundle 是一个完整配置，不是单机加购清单。"
                   "四个部分各自负责金属流程的一段，缺任何一段，金属零件都无法在厂内完成。",
             "en": "The FX10 Sinter-2 Bundle is a complete configuration rather than an à la carte "
                   "list. Each of the four parts owns one stage of the metal workflow; without any "
                   "one of them, metal parts cannot be finished in-house."},
        ],
        "hl": [
            {"b": {"tw": "FX10", "cn": "FX10", "en": "FX10"},
             "s": {"tw": "複合材與金屬雙模式主機。平時以連續碳纖維列印複合材零件",
                   "cn": "复合材料与金属双模式主机。平时以连续碳纤维打印复合材料零件",
                   "en": "The dual-mode printer. Runs continuous carbon fiber composites day to day"}},
            {"b": {"tw": "METAL KIT", "cn": "METAL KIT", "en": "METAL KIT"},
             "s": {"tw": "可替換的金屬列印引擎。裝上之後，同一台 FX10 就是金屬列印機",
                   "cn": "可更换的金属打印引擎。装上之后，同一台 FX10 就是金属打印机",
                   "en": "The swappable metal print engine. With it installed, the same FX10 prints "
                         "metal"}},
            {"b": {"tw": "WASH-1", "cn": "WASH-1", "en": "WASH-1"},
             "s": {"tw": "脫脂清洗站。列印完成的生胚在此去除黏結劑，才能進爐",
                   "cn": "脱脂清洗站。打印完成的生胚在此去除黏结剂，才能进炉",
                   "en": "The debinding station. Green parts have their binder removed here before "
                         "they can go into the furnace"}},
            {"b": {"tw": "SINTER-2", "cn": "SINTER-2", "en": "SINTER-2"},
             "s": {"tw": "高溫燒結爐。生胚在此燒結成緻密金屬零件，流程到此完成",
                   "cn": "高温烧结炉。生胚在此烧结成致密金属零件，流程到此完成",
                   "en": "The sintering furnace. Green parts are sintered into dense metal here, "
                         "completing the workflow"}},
        ],
    },
    {
        "kind": "sec",
        # ⚠️ 標題不用引號做強調 —— G1 冒名引言閘會把引號內容當成引言要白名單，
        #    而它那樣判是對的。該改的是我的寫法，不是閘。
        "h2": {"tw": "為什麼是混合，而不是兩套設備", "cn": "为什么是混合，而不是两套设备",
               "en": "Why hybrid rather than two machines"},
        "h3": {"tw": "同一台主機換引擎，複合材與金屬不再互相排擠預算與場地",
               "cn": "同一台主机换引擎，复合材料与金属不再互相排挤预算与场地",
               "en": "Swap the engine on one printer, and composites and metal stop competing for "
                     "budget and floor space"},
        "paras": [
            {"tw": "多數製造現場真正的需求分布是不平均的：夾治具、工裝、功能性原型這類複合材零件天天都在印，"
                   "金屬零件則是週期性出現。若為了後者單獨購置一台金屬設備，"
                   "那台機器多數時間是閒置的。",
             "cn": "多数制造现场真正的需求分布是不平均的：夹治具、工装、功能性原型这类复合材料零件天天都在打印，"
                   "金属零件则是周期性出现。若为了后者单独购置一台金属设备，"
                   "那台机器多数时间是闲置的。",
             "en": "Real demand on most shop floors is lopsided. Fixtures, tooling and functional "
                   "prototypes in composites run every day; metal parts appear in cycles. Buying a "
                   "dedicated metal machine for the latter leaves it idle most of the time."},
            {"tw": "雙模式的意義在於讓同一筆設備投資同時服務兩種需求 —— "
                   "日常產能用在複合材，金屬需求來時切換模式，後段再接上清洗與燒結。"
                   "對採購而言是一筆設備預算與一處場地；對工程而言是同一套軟體與同一個操作介面。",
             "cn": "双模式的意义在于让同一笔设备投资同时服务两种需求 —— "
                   "日常产能用在复合材料，金属需求来时切换模式，后段再接上清洗与烧结。"
                   "对采购而言是一笔设备预算与一处场地；对工程而言是同一套软件与同一个操作界面。",
             "en": "The point of dual mode is that one equipment investment serves both needs: "
                   "everyday capacity goes to composites, and the machine switches over when metal "
                   "work arrives, with washing and sintering downstream. For procurement that is "
                   "one budget line and one footprint; for engineering it is one software stack and "
                   "one interface."},
        ],
    },
]

CTA = {
    "h": {"tw": "想看實際零件或安排機台展示",
          "cn": "想看实际零件或安排机台展示",
          "en": "See parts or arrange a demonstration"},
    "p": {"tw": "若你的產線同時有複合材夾治具與金屬零件的需求，"
                "我們可以就適用零件、導入方式與廠內配置與你的團隊討論。",
          "cn": "若你的产线同时有复合材料夹治具与金属零件的需求，"
                "我们可以就适用零件、导入方式与厂内配置与你的团队讨论。",
          "en": "If your line needs both composite fixtures and metal parts, we can walk your team "
                "through candidate parts, adoption and in-house layout."},
    "btn": {"tw": "聯絡我們", "cn": "联系我们", "en": "Contact us"},
}

SRC = {
    "h": {"tw": "資料來源", "cn": "资料来源", "en": "Sources"},
    "items": [
        {"tw": "FX10 Sinter-2 Bundle 的組成（FX10＋Metal Kit＋Sinter-2＋Wash-1）取自 Markforged "
               "產品料號 F-PR-5505 的官方定義。",
         "cn": "FX10 Sinter-2 Bundle 的组成（FX10＋Metal Kit＋Sinter-2＋Wash-1）取自 Markforged "
               "产品料号 F-PR-5505 的官方定义。",
         "en": "The composition of the FX10 Sinter-2 Bundle (FX10 + Metal Kit + Sinter-2 + Wash-1) "
               "is per the official definition of Markforged part number F-PR-5505."},
        {"tw": "雙模式運作與可替換金屬列印引擎（swappable metal print engine）取自 Markforged "
               "FX10 官方產品資料。",
         "cn": "双模式运作与可更换金属打印引擎（swappable metal print engine）取自 Markforged "
               "FX10 官方产品资料。",
         "en": "Dual-mode operation and the swappable metal print engine are from official "
               "Markforged FX10 product documentation."},
        {"tw": "本文未列出規格數值。設備規格、材料清單與場地需求請以各機型官方 datasheet 與 "
               "Facilities Guide 為準，可向我們索取。",
         "cn": "本文未列出规格数值。设备规格、材料清单与场地需求请以各机型官方 datasheet 与 "
               "Facilities Guide 为准，可向我们索取。",
         "en": "No specification figures are quoted in this article. For equipment specifications, "
               "material lists and facility requirements, refer to the official datasheet and "
               "facilities guide for each model, available on request."},
        {"tw": "影片為 Markforged 大中華區自製；片中產品影像均為原廠產品圖與原廠實拍，非 AI 生成。"
               "頁面圖片為該影片畫格。",
         "cn": "视频为 Markforged 大中华区自制；片中产品影像均为原厂产品图与原厂实拍，非 AI 生成。"
               "页面图片为该视频画格。",
         "en": "The film was produced by Markforged Greater China. All product imagery in it comes "
               "from official Markforged product photography and footage, not AI generation. The "
               "images on this page are frames from that film."},
    ],
}

FTR = {
    "about": {
        "tw": "Markforged 提供工業級積層製造系統與連續纖維複合材料，應用於航太、國防、"
              "汽車與精密製造。本頁由 Markforged 大中華區媒體中心發布。",
        "cn": "Markforged 提供工业级增材制造系统与连续纤维复合材料，应用于航空航天、国防、"
              "汽车与精密制造。本页由 Markforged 大中华区媒体中心发布。",
        "en": "Markforged builds industrial additive manufacturing systems and continuous fiber "
              "composites for aerospace, defence, automotive and precision manufacturing. "
              "Published by the Markforged Greater China Media Hub.",
    },
    "back": {"tw": "返回媒體中心", "cn": "返回媒体中心", "en": "Back to the Media Hub"},
}

# G1 冒名引言閘：本文全篇敘述體，沒有任何一句直接引言 → 白名單刻意為空。
APPROVED_QUOTES = {"tw": [], "cn": [], "en": []}

DOC_TERMS = ["FX10", "Sinter-2", "Wash-1", "Metal Kit", "F-PR-5505", "Markforged", "Onyx",
             "swappable metal print engine", "Digital Forge"]

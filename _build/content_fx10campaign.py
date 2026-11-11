# -*- coding: utf-8 -*-
"""
FX10 活動頁（If it has to work, it starts here.）— 繁中／英文內容源（唯一真相）。

2026-11-11 建立。Brian 交辦：仿 HQ「FX Series Campaign-in-a-Box」的主題，在 news.markforged.tw
做一頁推廣 FX10。Brian 定案：案例全放；先做繁中與英文；簡中版另外做、拿掉國防內容
（簡中版另由 content_fx10campaign_sc.py 產出；2026-11-11 Brian「繁體中文 英文 簡體中文都要做啊」→ 三語齊，
語言例外登記已撤）。

素材來源（vault）：MF-GCR/85_Content/APAC-Shared/FX-Series-Campaign-in-a-Box-2026-11/
  · 影片＝原廠 MF_Floor Notes_Automotive／Aerospace Defense_Horizontal_110526.mp4，轉 1080p 自託管
  · 頁面圖＝上述原廠影片畫格＋vault 原廠 FX10 產品照（_assets/products/markforged/fx10/），非 AI 生成

案例事實（2026-11-11 逐條對過原廠官網原文，網址即正文連結）：
  · GRP：20–40 小時手工 → 隔夜列印；FX10 印 316L 法蘭；Revuelto 1,000 匹（官網 blog）
  · Subaru Indiana：ABS 開裂 → Onyx GF 色碼治具；1/10 mm（官網 blog）
  · Dana：七國；Rovereto 以 X7 印複材治具，>1 年無故障，成本 −70%、交期 −90%（官網 case study）
  · Plane Support：FX10＋Onyx FR-A，CASA 核准 214B 機艙空調風管；McDermott 全球最大 214B 機隊（官網新聞稿）
  · CMS：2019 成立、兩台 X7、Onyx FR（UL 94 V-0）、FAA 合規、機上娛樂改裝件（官網 case study）
  · Hangar One：碳纖複材取代鋁件；人工檢測 30–45 分鐘／件，Blacksmith 平均每件省 30 分鐘（官網 case study）
  · Fort Irwin：艙蓋塞重製約 $10,000、3 個月 → Onyx $230、17-4PH $800，本項省 $244,000（官網 case study）
  · Cannon AFB：X7；NVG 座 $100–數百、等數週 → <$5、數小時；強度與市售鋁件相當（官網 case study）
  · VA 中維吉尼亞：腕帶式握筆輔具、Smooth TPU 95A（官網 case study）

刻意不寫的東西（理由見拆解筆記）：
  ✗ Metal X（EOL）—— Fort Irwin 金屬版只寫材料不寫機型；Dana 只寫 Rovereto 的 X7 複材治具
  ✗ Hangar One「消除 65% 報廢率」—— 只出現在 HQ 信件，官網原文查無
  ✗ VA 案的機型（官網寫 Onyx Pro，GCR 不推）
  ✗ FX10 重量（HQ 簡報 109 kg、官方 datasheet 122 kg，口徑未定）；Onyx GF 顏色數（7 vs 6）
  ✗ 金屬最大零件尺寸（三層口徑，活動頁不需要）
  ✗ ULTEM 9085 FAR 25.853（屬 FX20，且原廠 ULTEM 規格表無 FST 紀錄）
"""

# ⛔ 2026-11-11 起本頁改由 build_fx10_landing.py（內容源 content_fx10landing.py）產出活動主視覺版。
#    這支是第一版文章版的內容源，只留作紀錄；用 build_article.py 重建會把線上新版蓋回舊版，所以直接擋。
import os as _os
if _os.environ.get("ARTICLE_CONTENT", "").startswith("content_fx10campaign"):
    raise SystemExit("⛔ fx10-it-starts-here 已改版為活動主視覺版：請跑 python3 _build/build_fx10_landing.py，不要用 build_article.py 重建")


LANGS = ("tw", "en")
# 簡中版另由 content_fx10campaign_sc.py 產出（拿掉國防內容，結構不同）；語言切換列與 hreflang 仍列三語
LINK_LANGS = ("tw", "cn", "en")
SHOW_SOURCES = False   # Brian 2026-09-24：資料來源段不對外顯示（出處改掛在正文連結）

S = "fx10-it-starts-here"
MP4_AUTO = f"video/{S}-automotive.mp4"
MP4_AERO = f"video/{S}-aerospace-defense.mp4"

URL = {
    "grp": "https://markforged.com/resources/blog/automotive-additive-manufacturing-high-end-fabrication",
    "subaru": "https://markforged.com/resources/blog/keeping-the-line-moving-color-coded-tooling-at-subaru",
    "dana": "https://markforged.com/resources/case-studies/dana-incorporated",
    "plane": "https://markforged.com/resources/news-events/casa-approval-for-flight-ready-3d-printed-components",
    "cms": "https://markforged.com/resources/case-studies/cabin-management-solutions",
    "hangar": "https://markforged.com/resources/case-studies/hangar-one-avionics-implements-blacksmith-for-digitizing-part-inspection",
    "irwin": "https://markforged.com/resources/case-studies/united-states-army",
    "cannon": "https://markforged.com/resources/case-studies/u-s-air-force-cannon-air-force-base",
    "va": "https://markforged.com/resources/case-studies/the-u-s-department-of-veterans-affairs",
    "ebook": "https://web-objects.markforged.com/craft/common/Markforged-Automotive-E-Book.pdf",
}


def _lk(key, lang):
    """正文內的原廠出處連結。"""
    txt = {"tw": "原廠案例（英文）&nbsp;→", "en": "Read the original&nbsp;→"}[lang]
    return f' <a href="{URL[key]}">{txt}</a>'


META = {
    "lang_attr": {"tw": "zh-TW", "cn": "zh-CN", "en": "en"},
    "file": {"tw": f"{S}.html", "cn": f"{S}-sc.html", "en": f"{S}-en.html"},
    "hero": f"images/{S}-hero.jpg",
    "og_image": f"https://news.markforged.tw/images/{S}-hero.jpg",
    "title": {
        "tw": "必須可靠的零件，從這裡開始：FX10 與汽車、航太、國防的九個原廠案例｜Markforged 媒體中心",
        "en": "If It Has to Work, It Starts Here: FX10 and Nine Markforged Cases in Automotive, "
              "Aerospace and Defense | Markforged Media Hub",
    },
    "desc": {
        "tw": "FX10 把金屬與連續碳纖維複合材放進同一台機器、放在工廠現場。本頁整理 Markforged 原廠發布的九個案例："
              "Graham Rahal Performance、Subaru、Dana、Plane Support、Cabin Management Solutions、"
              "Hangar One Avionics、美國陸軍 Fort Irwin、美國空軍 Cannon 空軍基地、美國退伍軍人事務部，附兩支原廠影片。",
        "en": "FX10 puts metal and continuous carbon fiber composites on one machine, on the factory floor. "
              "This page collects nine cases published by Markforged: Graham Rahal Performance, Subaru, Dana, "
              "Plane Support, Cabin Management Solutions, Hangar One Avionics, the U.S. Army at Fort Irwin, "
              "Cannon Air Force Base and the U.S. Department of Veterans Affairs, with two official films.",
    },
    "og_title": {
        "tw": "必須可靠的零件，從這裡開始｜FX10",
        "en": "If it has to work, it starts here | FX10",
    },
    "og_desc": {
        "tw": "汽車：性能關鍵。航太國防：任務關鍵。九個原廠案例與兩支原廠影片。",
        "en": "Automotive: performance critical. Aerospace and defense: mission critical. "
              "Nine cases and two official films.",
    },
}

UI = {
    "hdr_ev": {"tw": "大中華區媒體中心<br>News &amp; Insights",
               "en": "Greater China Media Hub<br>News &amp; Insights"},
    "switch_label": {"tw": "語言", "en": "Language"},
    "hero_alt": {"tw": "FX10 放在工廠現場（Markforged 原廠照片）",
                 "en": "FX10 on a factory floor (official Markforged photo)"},
    "hero_kicker": {"tw": "產品方案 · FX10", "en": "Solution · FX10"},
    "hero_title": {"tw": "必須可靠的零件，<br>從這裡開始",
                   "en": "If it has to work,<br>it starts here."},
    "hero_meta": {"tw": "FX10 ｜ 汽車 · 航太 · 國防 ｜ 2026.11.09",
                  "en": "FX10 | Automotive · Aerospace · Defense | 2026.11.09"},
    "ds_l": {"tw": "汽車：性能關鍵　｜　航太國防：任務關鍵",
             "en": "Automotive: Performance Critical | Aerospace &amp; Defense: Mission Critical"},
    "ds_r": {"tw": "金屬＋連續碳纖維，同一台 FX10",
             "en": "Metal and continuous carbon fiber, one FX10"},
}

LEAD = {
    "p1": {
        "tw": "汽車組裝線一停，每分鐘都是損失；衛星升空沒有重來的機會，戰機也不會等缺料。"
              "在這些地方，零件不只要做得出來，還要在需要的時候就在現場，裝上去就能用。",
        "en": "When an assembly line stops, every minute costs money. A satellite gets no second launch, "
              "and a fighter jet does not wait for back-ordered parts. In these settings a part has to "
              "exist when it is needed, on site, and work the first time it is installed.",
    },
    "p2": {
        "tw": "<strong>FX10</strong> 是 Markforged 為工廠現場設計的工業級 3D 印表機：以連續碳纖維強化複合材列印治具與零件，"
              "加裝 Metal Kit 後，同一台機器也能列印 316L、17-4PH 不鏽鋼與 H13 工具鋼。"
              "以下是 Markforged 原廠發布的九個汽車、航太與國防案例，每一則都附原文連結；"
              "案例使用的機型照原文標示。",
        "en": "<strong>FX10</strong> is the industrial 3D printer Markforged designed for the factory floor. "
              "It prints fixtures and parts in continuous-fiber-reinforced composites, and with the Metal Kit "
              "added, the same machine prints 316L and 17-4PH stainless steel and H13 tool steel. "
              "Below are nine automotive, aerospace and defense cases published by Markforged, each linked "
              "to the original, with the printer model stated as the original source gives it.",
    },
}

PROF = {
    "alt": {"tw": "陳中欣", "en": "Brian Chen"},
    "name": {"tw": "陳中欣 Brian Chen", "en": "Brian Chen"},
    "title": {"tw": "Markforged 大中華區暨越南區總經理",
              "en": "Country Manager, Greater China and Vietnam, Markforged"},
    "desc": {
        "tw": "負責 Markforged 在台灣、中國、香港與越南的市場，"
              "長期與航太、國防與精密製造領域的製造商合作。",
        "en": "Responsible for Markforged across Taiwan, China, Hong Kong and Vietnam, working with "
              "manufacturers in aerospace, defence and precision manufacturing.",
    },
}

TAGS = [
    {"tw": "FX10", "en": "FX10", "solid": True},
    {"tw": "汽車", "en": "Automotive", "solid": False},
    {"tw": "航太", "en": "Aerospace", "solid": False},
    {"tw": "國防", "en": "Defense", "solid": False},
    {"tw": "連續碳纖維", "en": "Continuous Carbon Fiber", "solid": False},
    {"tw": "金屬列印", "en": "Metal 3D Printing", "solid": False},
]

BLOCKS = [
    # ── 汽車 ───────────────────────────────────────────────────────────────
    {
        "kind": "mp4",
        "src": MP4_AUTO,
        "poster": f"images/{S}-auto-poster.jpg",
        "alt": {"tw": "Markforged 原廠影片：汽車篇，約 21 秒",
                "en": "Official Markforged film: automotive, about 21 seconds"},
        "cap": {"tw": "原廠影片 · 汽車篇 Performance Critical ｜ 約 21 秒 ｜ Markforged",
                "en": "Official film · Automotive, Performance Critical | about 21 seconds | Markforged"},
    },
    {
        "kind": "sec",
        "h2": {"tw": "汽車：性能關鍵", "en": "Automotive: Performance Critical"},
        "h3": {"tw": "產線不能停，治具和零件就得撐得住",
               "en": "When the line cannot stop, tools and parts have to hold up"},
        "paras": [
            {"tw": "<strong>Graham Rahal Performance（美國，超跑改裝｜FX10）</strong>　"
                   "過去師傅手工做一組治具、支架或排氣零件，要花 20 到 40 小時切割、成形、焊接；"
                   "導入 FX10 後，同樣的治具在 CAD 畫好、隔夜印完、隔天就用。"
                   "為 1,000 匹馬力的油電超跑 Lamborghini Revuelto 製作 X-pipe 排氣時，"
                   "GRP 用 FX10 以 316L 不鏽鋼印出法蘭，表面可直接焊接，幾乎不需後加工。" + _lk("grp", "tw"),
             "en": "<strong>Graham Rahal Performance (U.S., supercar fabrication | FX10)</strong> "
                   "A fabricator used to spend 20 to 40 hours hand-building jigs, fixtures and exhaust "
                   "components. With the FX10, the same fixtures are designed in CAD, printed overnight and "
                   "used the next day. For an X-pipe on the 1,000-horsepower hybrid Lamborghini Revuelto, "
                   "GRP printed the flanges in 316L stainless steel on the FX10: weld-ready, with almost no "
                   "post-processing." + _lk("grp", "en")},
            {"tw": "<strong>Subaru of Indiana Automotive（美國，整車組裝）</strong>　"
                   "同一條線同時組裝多個車型，治具之間只差幾公釐。原本用 ABS 列印的彩色治具耐不住產線使用、容易開裂；"
                   "改用 Onyx GF 後，每個車型配一種顏色，作業員第一次伸手就拿對治具。"
                   "用來貼保險桿 QR 追蹤標籤的定位治具，精度做到 0.1 mm。" + _lk("subaru", "tw"),
             "en": "<strong>Subaru of Indiana Automotive (U.S., vehicle assembly)</strong> "
                   "Several models run down the same line, and their tools differ by millimeters. Color-coded "
                   "jigs printed in ABS cracked under daily use; reprinted in Onyx GF, each model variant got "
                   "its own color, so operators grab the right tool on the first pass. The placement jigs for "
                   "bumper QR tracking labels hold a 0.1 mm tolerance." + _lk("subaru", "en")},
            {"tw": "<strong>Dana Incorporated（全球車用傳動與動力系統供應商｜X7）</strong>　"
                   "Dana 在七個國家的據點部署 Markforged 印表機。義大利 Rovereto 工程中心用 X7 列印加工時固定零件的複材治具，"
                   "上線超過一年沒有故障，每件治具成本降低 70%、交期縮短 90%。" + _lk("dana", "tw"),
             "en": "<strong>Dana Incorporated (global drivetrain and power systems supplier | X7)</strong> "
                   "Dana runs Markforged printers at sites in seven countries. Its engineering center in "
                   "Rovereto, Italy printed composite workholding fixtures on an X7; after more than a year "
                   "in use without failure, each fixture cost 70% less and took 90% less lead time."
                   + _lk("dana", "en")},
        ],
        "hl": [
            {"b": {"tw": "20–40 小時 → 隔夜", "en": "20–40 HOURS → OVERNIGHT"},
             "s": {"tw": "GRP：手工治具改用 FX10 列印", "en": "GRP: hand-built fixtures, now printed on FX10"}},
            {"b": {"tw": "0.1 mm", "en": "0.1 MM"},
             "s": {"tw": "Subaru：Onyx GF 色碼定位治具的精度", "en": "Subaru: tolerance of Onyx GF placement jigs"}},
            {"b": {"tw": "−70% ／ −90%", "en": "−70% / −90%"},
             "s": {"tw": "Dana：每件治具的成本／交期", "en": "Dana: cost / lead time per fixture"}},
            {"b": {"tw": "316L 法蘭", "en": "316L FLANGES"},
             "s": {"tw": "GRP：FX10 為 Revuelto 印的排氣法蘭，可直接焊接", "en": "GRP: Revuelto exhaust flanges printed on FX10, weld-ready"}},
        ],
    },
    {
        "kind": "img_2col",
        "imgs": [f"images/{S}-auto-bracket.jpg", f"images/{S}-auto-line.jpg"],
        "alts": [{"tw": "工程師在車輛引擎室安裝列印支架", "en": "An engineer fitting a printed bracket in an engine bay"},
                 {"tw": "汽車組裝線", "en": "An automotive assembly line"}],
        "cap": {"tw": "原廠影片畫格：引擎室裡的列印支架、汽車組裝線",
                "en": "Frames from the official film: a printed bracket in an engine bay, an assembly line"},
    },
    # ── Onyx GF（Brian 2026-11-11「Onyx GF 應該要加上去」）────────────────────
    # 出處：原廠 Onyx GF Material Datasheet（vault 60_Products/support/datasheets/OnyxGF-MaterialDatasheet.pdf）
    #       「Available in six colors」「non-conductive」「Compatible with Continuous Fiber Reinforcement」
    #       HDT 138 °C（1.8 MPa）；四種用法取自原廠汽車電子書 p.14。
    #       ⚠️ 電子書寫 seven colors，與規格表 six colors 不符 → 以規格表為準。
    {
        "kind": "sec",
        "h2": {"tw": "Onyx GF：工廠現場一眼分得清", "en": "Onyx GF: color you can read across the floor"},
        "h3": {"tw": "六種顏色、Onyx 等級的強度，還能加連續纖維強化",
               "en": "Six colors, Onyx-level strength, and room for continuous fiber reinforcement"},
        "paras": [
            {"tw": "Onyx GF 是以短切玻璃纖維強化的尼龍線材，保有 Onyx 的表面品質、尺寸精度與列印穩定性，而且不導電。"
                   "共有紅、黃、綠、藍、灰、白六種顏色，治具與零件直接用顏色區分，不必多一道標示工序；"
                   "需要承受更高負荷時，也能在 FX10 上加入連續纖維強化。熱變形溫度 138 °C（1.8 MPa）。"
                   "上面 Subaru 印第安納廠的色碼治具，用的就是 Onyx GF。",
             "en": "Onyx GF is a chopped-glass-fiber-filled nylon that keeps the surface finish, dimensional "
                   "accuracy and print reliability of Onyx, and is non-conductive. It comes in six colors: red, "
                   "yellow, green, blue, gray and white, so fixtures and parts are told apart by color with no "
                   "extra labeling step. For higher loads, it can be reinforced with continuous fiber on the FX10. "
                   "Heat deflection temperature is 138 °C (1.8 MPa). The color-coded jigs at Subaru of Indiana "
                   "above are printed in Onyx GF."},
        ],
        "hl": [
            {"b": {"tw": "工安警示", "en": "WORKPLACE SAFETY"},
             "s": {"tw": "危險機台旁的護罩與支架用醒目的紅、黃色列印",
                   "en": "High-visibility red and yellow guards and brackets near hazardous machinery"}},
            {"b": {"tw": "產線區分", "en": "LINE DIFFERENTIATION"},
             "s": {"tw": "A 線、B 線的治具用顏色分開，不會拿錯",
                   "en": "Tools for Line A and Line B are separated by color"}},
            {"b": {"tw": "版本控管", "en": "REVISION CONTROL"},
             "s": {"tw": "設計改版就換一個顏色印，舊版治具一眼就能淘汰",
                   "en": "Print a new revision in a new color, and old fixtures are phased out at a glance"}},
            {"b": {"tw": "工具管理", "en": "TOOL ORGANIZATION"},
             "s": {"tw": "工具板上顏色對不上，就知道少了哪一件或放錯位置",
                   "en": "A color mismatch on the shadow board shows what is missing or misplaced"}},
        ],
    },
    {
        "kind": "img_full",
        "img": f"images/{S}-onyxgf.jpg",
        "alt": {"tw": "Onyx GF 六色線材與綠色列印零件", "en": "Onyx GF spools in six colors and a part printed in green"},
        "cap": {"tw": "Onyx GF 六色線材與列印零件 ｜ Markforged 原廠圖片",
                "en": "Onyx GF in six colors, and a printed part | official Markforged images"},
    },
    # ── 航太 ───────────────────────────────────────────────────────────────
    {
        "kind": "mp4",
        "src": MP4_AERO,
        "poster": f"images/{S}-aero-poster.jpg",
        "alt": {"tw": "Markforged 原廠影片：航太國防篇，約 22 秒",
                "en": "Official Markforged film: aerospace and defense, about 22 seconds"},
        "cap": {"tw": "原廠影片 · 航太國防篇 Mission Critical ｜ 約 22 秒 ｜ Markforged",
                "en": "Official film · Aerospace &amp; Defense, Mission Critical | about 22 seconds | Markforged"},
    },
    {
        "kind": "sec",
        "h2": {"tw": "航太：任務關鍵", "en": "Aerospace: Mission Critical"},
        "h3": {"tw": "飛上去之前，零件就得通過每一道檢驗",
               "en": "Before it flies, a part has to pass every check"},
        "paras": [
            {"tw": "<strong>Plane Support × McDermott Aviation（澳洲，直升機工程與維修｜FX10）</strong>　"
                   "Plane Support 以 FX10 為核心建立航太積層製造實驗室，用具批次追溯的阻燃材料 Onyx FR-A 列印 "
                   "Bell 214B 直升機的機艙空調風管，取得澳洲民航安全局（CASA）核准，可用積層製造生產這項零件。"
                   "合作夥伴 McDermott Aviation 擁有全球最大的 214B 機隊，主要投入山林火災空中滅火。"
                   + _lk("plane", "tw")
                   + '　本站專文：<a href="casa-additive-airworthiness.html">一截風管，換來亞太第一張民航增材製造核准</a>',
             "en": "<strong>Plane Support × McDermott Aviation (Australia, helicopter engineering and "
                   "maintenance | FX10)</strong> Plane Support built an aerospace additive manufacturing lab "
                   "around the FX10 and printed cabin air-conditioning ducting for the Bell 214B in Onyx FR-A, "
                   "a flame-retardant material with lot-level traceability. The Civil Aviation Safety Authority "
                   "(CASA) approved manufacturing the part this way. Partner McDermott Aviation operates the "
                   "world's largest Bell 214B fleet, used mainly for aerial firefighting." + _lk("plane", "en")
                   + ' Our full story: <a href="casa-additive-airworthiness-en.html">One Duct, and '
                   "Asia-Pacific's First Civil Aviation Approval for Additive Manufacturing</a>"},
            {"tw": "<strong>Cabin Management Solutions（美國，私人與商務噴射機客艙系統｜X7）</strong>　"
                   "CMS 為私人與商務噴射機提供客艙管理與機上娛樂系統的維修、升級與替換，取代原廠動輒漫長的交期與高價。"
                   "公司 2019 年成立後購入兩台 X7，以 UL 94 V-0 阻燃等級的 Onyx FR 列印機上娛樂系統改裝件等最終使用零件，"
                   "符合美國聯邦航空總署（FAA）的要求。" + _lk("cms", "tw"),
             "en": "<strong>Cabin Management Solutions (U.S., cabin systems for private and business jets | "
                   "X7)</strong> CMS maintains, upgrades and replaces cabin management and in-flight "
                   "entertainment systems as a quick-turn alternative to long lead times and high costs. "
                   "Founded in 2019, it bought two X7 printers and prints end-use parts such as in-flight "
                   "entertainment retrofits in Onyx FR, rated UL 94 V-0, meeting Federal Aviation "
                   "Administration (FAA) requirements." + _lk("cms", "en")},
            {"tw": "<strong>Hangar One Avionics（美國，航電維修與安裝）</strong>　"
                   "Hangar One 以碳纖維強化複材零件取代鋁件，為直升機減重；並用 Markforged 的 Blacksmith 檢測軟體在列印過程中自動量測。"
                   "原本每件人工量測要 30 到 45 分鐘，導入後平均每件省下約 30 分鐘。" + _lk("hangar", "tw"),
             "en": "<strong>Hangar One Avionics (U.S., avionics maintenance and installation)</strong> "
                   "Hangar One replaces aluminum parts with carbon-reinforced composites to take weight out of "
                   "helicopters, and uses Markforged Blacksmith inspection software to measure parts while they "
                   "print. Manual inspection used to take 30 to 45 minutes per part; it now saves about 30 "
                   "minutes per part on average." + _lk("hangar", "en")},
        ],
        "hl": [
            {"b": {"tw": "CASA 核准", "en": "CASA APPROVAL"},
             "s": {"tw": "Plane Support：FX10＋Onyx FR-A 生產 214B 風管", "en": "Plane Support: 214B ducting on FX10 in Onyx FR-A"}},
            {"b": {"tw": "UL 94 V-0", "en": "UL 94 V-0"},
             "s": {"tw": "CMS：Onyx FR 阻燃等級，零件符合 FAA 要求", "en": "CMS: Onyx FR rating; parts meet FAA requirements"}},
            {"b": {"tw": "每件省 30 分鐘", "en": "30 MIN SAVED PER PART"},
             "s": {"tw": "Hangar One：列印中自動檢測取代人工量測", "en": "Hangar One: in-print inspection replaces manual checks"}},
            {"b": {"tw": "批次可追溯", "en": "LOT TRACEABILITY"},
             "s": {"tw": "Onyx FR-A：每批材料可追溯，備齊適航所需文件", "en": "Onyx FR-A: lot-level traceability for airworthiness records"}},
        ],
    },
    {
        "kind": "img_full",
        "img": f"images/{S}-aero-cockpit.jpg",
        "alt": {"tw": "技師在駕駛艙進行航電作業", "en": "Technicians working on cockpit avionics"},
        "cap": {"tw": "原廠影片畫格：駕駛艙航電作業", "en": "Frame from the official film: cockpit avionics work"},
    },
    # ── 國防 ───────────────────────────────────────────────────────────────
    {
        "kind": "sec",
        "h2": {"tw": "國防：任務關鍵", "en": "Defense: Mission Critical"},
        "h3": {"tw": "補給線拉長的時候，能在現場做出零件就是戰備",
               "en": "When supply lines stretch, making parts on site is readiness"},
        "paras": [
            {"tw": "<strong>美國陸軍 Fort Irwin 國家訓練中心</strong>　"
                   "一款裝在車頂、協助駕駛夜間觀察的艙蓋塞已經停產，重新製作約需 10,000 美元、交期 3 個月。"
                   "部隊改用 Markforged 以 Onyx 印出一件只花 230 美元，另以 17-4PH 不鏽鋼印出金屬版 800 美元；"
                   "單這一項應用就省下 244,000 美元。" + _lk("irwin", "tw"),
             "en": "<strong>U.S. Army, Fort Irwin National Training Center</strong> "
                   "A hatch plug that helps drivers see at night was out of production; reproducing it would "
                   "cost about $10,000 with a three-month lead time. The regiment printed one in Onyx for $230 "
                   "and a 17-4PH stainless steel version for $800. This one application saved the regiment "
                   "$244,000." + _lk("irwin", "en")},
            {"tw": "<strong>美國空軍 Cannon 空軍基地 第 27 特種作戰支援中隊（X7）</strong>　"
                   "夜視鏡固定座在訓練中容易撞壞，買一個要 100 美元到數百美元、還要等好幾週。"
                   "中隊用 X7 列印替換件，並加上可適配多種頭盔的墊片，每件成本不到 5 美元、幾小時就完成；"
                   "負責人表示強度與市售鋁製品相當。" + _lk("cannon", "tw"),
             "en": "<strong>U.S. Air Force, Cannon Air Force Base, 27th Special Operations Support Squadron "
                   "(X7)</strong> Night vision goggle mounts break in training, and a replacement costs $100 to "
                   "several hundred dollars with weeks of shipping. The squadron printed replacements on its X7, "
                   "with built-in spacers for different helmets, for under $5 each in a few hours; the specialist "
                   "in charge says they are as strong as the commercial aluminum mounts." + _lk("cannon", "en")},
            {"tw": "<strong>美國退伍軍人事務部 中維吉尼亞醫療體系</strong>　"
                   "輔具團隊與職能治療師合作，為手部抓握力不足的退伍軍人與現役軍人設計腕帶式握筆輔具，"
                   "以 Markforged 印表機和 Smooth TPU 95A 彈性材料列印，讓使用者能穩穩握住筆或觸控筆。" + _lk("va", "tw"),
             "en": "<strong>U.S. Department of Veterans Affairs, Central Virginia Health Care System</strong> "
                   "The assistive technology team works with occupational therapists to design a wrist-strap "
                   "stylus holder for veterans and service members with limited grip, printed on Markforged "
                   "printers in flexible Smooth TPU 95A so they can hold a pen or stylus securely."
                   + _lk("va", "en")},
        ],
        "hl": [
            {"b": {"tw": "$10,000 → $230", "en": "$10,000 → $230"},
             "s": {"tw": "Fort Irwin：停產艙蓋塞改用 Onyx 列印",
                   "en": "Fort Irwin: out-of-production hatch plug, printed in Onyx"}},
            {"b": {"tw": "$244,000", "en": "$244,000"},
             "s": {"tw": "Fort Irwin：單這一項應用省下的金額", "en": "Fort Irwin: saved by this one application"}},
            {"b": {"tw": "不到 $5", "en": "UNDER $5"},
             "s": {"tw": "Cannon 空軍基地：夜視鏡固定座，幾小時完成", "en": "Cannon AFB: night vision mount, in hours"}},
            {"b": {"tw": "客製輔具", "en": "CUSTOM AIDS"},
             "s": {"tw": "退伍軍人事務部：依使用者需求列印握筆腕帶", "en": "VA: stylus holders printed to each user's needs"}},
        ],
    },
    {
        "kind": "img_2col",
        "imgs": [f"images/{S}-def-nvg.jpg", f"images/{S}-def-vehicle.jpg"],
        "alts": [{"tw": "戴著夜視裝備的人員", "en": "A person wearing night vision equipment"},
                 {"tw": "人員在軍用車輛上安裝零件", "en": "Crew fitting a part on a military vehicle"}],
        "cap": {"tw": "原廠影片畫格：夜視裝備、軍用車輛現場安裝",
                "en": "Frames from the official film: night vision gear, a part fitted on a military vehicle"},
    },
    # ── 為什麼是 FX10 ───────────────────────────────────────────────────────
    {
        "kind": "sec",
        "h2": {"tw": "為什麼是 FX10", "en": "Why FX10"},
        "h3": {"tw": "金屬和連續碳纖維在同一台機器上，就放在工廠現場",
               "en": "Metal and continuous carbon fiber on one machine, right on the factory floor"},
        "paras": [
            {"tw": "上面九個案例的共同點，是零件在要用的地方做出來，不必等外包或等原廠備料。"
                   "FX10 把複材與金屬兩種製程放進同一台機器，讓這件事從一個專案變成產線上的日常。",
             "en": "What the nine cases share is that parts get made where they are used, without waiting on "
                   "an outside shop or an OEM back order. FX10 puts composite and metal processes on one "
                   "machine, so this becomes routine work on the line rather than a special project."},
        ],
        "hl": [
            {"b": {"tw": "一機雙料", "en": "TWO PROCESSES, ONE MACHINE"},
             "s": {"tw": "平時用連續碳纖維強化複材列印治具與零件；換上 Metal Kit 金屬列印引擎，同一台印 316L、17-4PH 不鏽鋼與 H13 工具鋼"
                         "（金屬件搭配 Wash-1 清洗與 Sinter-2 燒結）",
                   "en": "Continuous-fiber-reinforced composites day to day; swap in the Metal Kit print engine to "
                         "print 316L, 17-4PH stainless and H13 tool steel (metal parts finish in Wash-1 and Sinter-2)"}},
            {"b": {"tw": "印的時候就在量", "en": "MEASURES WHILE IT PRINTS"},
             "s": {"tw": "列印頭上的雷射測微器在列印過程中掃描零件，搭配 Inspection 軟體做尺寸驗證；校正時也用它量測平台上的精密溝槽並自動補償",
                   "en": "A printhead-mounted laser micrometer scans parts during printing for dimensional "
                         "verification in Inspection, and measures precision grooves in the bed to auto-calibrate"}},
            {"b": {"tw": "少人看顧", "en": "LOW-TOUCH OPERATION"},
             "s": {"tw": "自動調平、自動校正，四個獨立密封料倉自動換料，工程師與現場操作員都能上手",
                   "en": "Automatic leveling and calibration, four sealed spool bays with automatic changeover; "
                         "simple for engineers and operators alike"}},
            {"b": {"tw": "為工廠設計", "en": "BUILT FOR THE FLOOR"},
             "s": {"tw": "腔體加熱至 60 °C、精密研磨鋁製真空平台、單相一般插座供電",
                   "en": "Chamber heated to 60 °C, precision-ground aluminum vacuum bed, single-phase wall power"}},
        ],
        "paras_after": [
            {"tw": "複材可用 Onyx、Onyx FR／FR-A、Onyx ESD、Onyx GF 等材料，並可加入連續碳纖維強化。"
                   '同時需要複材與金屬零件，可參考 <a href="fx10-sinter2-bundle.html">FX10 Sinter-2 Bundle</a>。',
             "en": "Composite materials include Onyx, Onyx FR / FR-A, Onyx ESD and Onyx GF, with continuous "
                   'carbon fiber reinforcement. If you need both composite and metal parts, see the '
                   '<a href="fx10-sinter2-bundle-en.html">FX10 Sinter-2 Bundle</a>.'},
        ],
    },
    {
        "kind": "img_full",
        "img": f"images/{S}-fx10-interior.jpg",
        "alt": {"tw": "FX10 列印頭與列印平台（Markforged 原廠照片）",
                "en": "FX10 printhead and print bed (official Markforged photo)"},
        "cap": {"tw": "FX10 列印頭與列印平台 ｜ Markforged 原廠照片",
                "en": "FX10 printhead and print bed | official Markforged photo"},
    },
    {
        "kind": "factsheet",
        "h": {"tw": "FX10 主要規格", "en": "FX10 at a glance"},
        "rows": [
            {"k": {"tw": "可列印空間", "en": "Build volume"},
             "v": {"tw": "375 × 300 × 300 mm（33.8 L）", "en": "375 × 300 × 300 mm (33.8 L)"}},
            {"k": {"tw": "機台外形尺寸", "en": "Machine size"},
             "v": {"tw": "760 × 640 × 1200 mm", "en": "760 × 640 × 1200 mm"}},
            {"k": {"tw": "腔體", "en": "Build chamber"},
             "v": {"tw": "加熱至 60 °C", "en": "Heated to 60 °C"}},
            {"k": {"tw": "列印平台", "en": "Print bed"},
             "v": {"tw": "加熱、精密研磨鋁製真空平台，自動調平",
                   "en": "Heated, precision-ground aluminum vacuum bed, auto leveling"}},
            {"k": {"tw": "材料倉", "en": "Material storage"},
             "v": {"tw": "4 個 800 cc 料盤位，濕度控制，自動換料",
                   "en": "4 × 800 cc spool bays, humidity controlled, automatic changeover"}},
            {"k": {"tw": "電源", "en": "Power"},
             "v": {"tw": "單相，一般插座", "en": "Single phase, wall plug"}},
            {"k": {"tw": "複合材料", "en": "Composite materials"},
             "v": {"tw": "Onyx、Onyx FR／FR-A、Onyx ESD、Onyx GF（六色），可加連續碳纖維強化",
                   "en": "Onyx, Onyx FR / FR-A, Onyx ESD, Onyx GF (six colors), with continuous carbon fiber reinforcement"}},
            {"k": {"tw": "金屬材料", "en": "Metal materials"},
             "v": {"tw": "加購 Metal Kit：316L、17-4PH 不鏽鋼，H13 工具鋼", "en": "With the Metal Kit: 316L, 17-4PH stainless steel; H13 tool steel"}},
        ],
    },
    # ── 下載與延伸閱讀 ─────────────────────────────────────────────────────
    {
        "kind": "sec",
        "h2": {"tw": "下載與延伸閱讀", "en": "Downloads and further reading"},
        "h3": {"tw": "原廠電子書與本站相關報導", "en": "The official e-book and related stories on this site"},
        "paras": [
            {"tw": f'<a href="{URL["ebook"]}">下載原廠電子書：汽車產業的積層製造（英文 PDF，20 頁）</a>'
                   "　收錄 GRP、Subaru、Dana 三個案例與 FX10、FX20、X7 機型介紹。",
             "en": f'<a href="{URL["ebook"]}">Download the e-book: Additive Manufacturing for the Automotive '
                   "Industry (PDF, 20 pages)</a> GRP, Subaru and Dana, plus the FX10, FX20 and X7."},
            {"tw": '<a href="casa-additive-airworthiness.html">一截風管，換來亞太第一張民航增材製造核准</a>'
                   "　Plane Support 案的完整報導。",
             "en": '<a href="casa-additive-airworthiness-en.html">One Duct, and Asia-Pacific\'s First Civil '
                   "Aviation Approval for Additive Manufacturing</a> The full Plane Support story."},
            {"tw": '<a href="wescad-fx10-jigs-fixtures.html">參考治具比銑削便宜最多 75%：德國治具廠 WESCAD 導入 FX10</a>'
                   "　另一個 FX10 治具案例。",
             "en": '<a href="wescad-fx10-jigs-fixtures-en.html">Reference fixtures up to 75% cheaper than '
                   "milling: German jig maker WESCAD runs its FX10 at full capacity within two months</a> "
                   "Another FX10 fixture case."},
        ],
    },
]

CTA = {
    "h": {"tw": "預約 FX10 展示或索取報價", "en": "Book an FX10 demo or request a quote"},
    "p": {"tw": "如果你的產線或維修現場也有不能出錯的零件，寄一個零件圖檔給我們，"
                "我們可以安排測試列印與機台展示。",
          "en": "If your line or maintenance shop has parts that cannot fail, send us a part file and we can "
                "arrange a test print and a live demonstration."},
    "btn": {"tw": "寫信給我們", "en": "Email us"},
    "href": "mailto:brian.chen@markforged.com?subject=FX10%20Demo%20%2F%20Quote",
}

SRC = {
    "h": {"tw": "資料來源", "en": "Sources"},
    "items": [],   # SHOW_SOURCES=False；出處已掛在各案例正文連結
}

FTR = {
    "about": {
        "tw": "Markforged 提供工業級積層製造系統與連續纖維複合材料，應用於航太、國防、"
              "汽車與精密製造。本頁由 Markforged 大中華區媒體中心發布；案例與影片來自 Markforged 原廠。",
        "en": "Markforged builds industrial additive manufacturing systems and continuous fiber "
              "composites for aerospace, defence, automotive and precision manufacturing. "
              "Published by the Markforged Greater China Media Hub; cases and films are from Markforged.",
    },
    "back": {"tw": "返回媒體中心", "en": "Back to the Media Hub"},
}

# G5 冒名引言閘：全篇敘述體，沒有直接引言 → 白名單為空。
APPROVED_QUOTES = {"tw": [], "en": []}

DOC_TERMS = ["FX10", "FX20", "X7", "Metal Kit", "Wash-1", "Sinter-2", "Markforged", "Onyx", "Onyx GF",
             "Onyx FR", "Onyx FR-A", "Onyx ESD", "Smooth TPU 95A", "Blacksmith", "Inspection", "CASA", "FAA",
             "UL 94 V-0", "Graham Rahal Performance", "GRP", "Subaru", "Dana", "Plane Support",
             "McDermott Aviation", "Cabin Management Solutions", "CMS", "Hangar One Avionics", "Hangar One",
             "Fort Irwin", "Cannon", "Lamborghini Revuelto", "X-pipe", "Bell", "QR", "CAD", "Rovereto",
             "Digital Forge", "WESCAD", "If it has to work, it starts here.", "Performance Critical",
             "Mission Critical", "News &amp; Insights", "Build Volume", "Onyx GF", "MPa"]

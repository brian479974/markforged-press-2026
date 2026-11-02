# -*- coding: utf-8 -*-
"""SOLIDWORKS 2027 創新日 IV Day 專題演講影片 — 三語內容源（繁中 / 簡中 / English 的唯一真相）。

2026-11-03 建立。Brian 交辦：「Add to news.Markforged.tw」「中英文版都要上」（承 11-02 做好的中文旁白影片 v3 與英文旁白影片 EN v1）。
簡中＝繁中經 OpenCC tw2sp 轉換＋大陸用語替換（列印→打印、影片→视频…），不另寫一份 → 三版不會靜默走鐘。

引言政策（G1）：全文敘述體，沒有任何一句直接引言、沒有任何話掛在 Brian 名下；APPROVED_QUOTES 為空。
  演講題目不加引號（加了就變成引言要白名單）。

事實出處（全部取自已交付、已查證過的 v5 簡報與旁白影片講稿，不另加說法）：
  · 台灣產業數字 — 經濟部航太小組《台灣無人機產業發展現況與政策推動重點》2026-06-30（簡報 p3 來源行）
  · 全球案例數字 — Markforged 官方無人機產業簡報 2026（簡報 p9 來源行）；Gamma Rotors — Markforged 官方 YouTube
  · 艾斯特 ASTER-SWARM — 站上既有案例頁 aster-swarm-fpv-airframe-x7-field-edition(.html/-en.html)；艾斯特提供、抗風經中科院軍民通用中心量測驗證
  · 800 MPa／6061-T6 約 310 MPa＝材料試片值（簡報 p6 已註明）；FX20 加熱腔體最高 200°C、ULTEM 9085；X7 Field Edition 開箱到列印 < 3 分鐘（產品手冊 REV 1.5）
刻意不寫：建構體積／最大零件尺寸（FX10 金屬三層口徑，本頁不需要）、價格、任何未在簡報出現的數字。

影片與圖片：
  · 影片＝Markforged 大中華區自製（簡報＋旁白＋動態圖文），自託管 video/；中文版 7 分 41 秒、英文版 8 分 16 秒，網頁版 720p
  · 旁白以陳中欣本人聲音合成（他本人授權的聲紋）；背景無人機畫面為示意插圖，非 Markforged 產品、非任何客戶機型 → 來源欄寫明
  · 頁首照片＝iThome 2026 年 9 月專訪現場照（陳中欣手持 ASTER-SWARM 機體）；兩張封面為各自影片畫格
"""
import opencc

# 2026-11-03 Brian「不做簡體中文版」→ 只出繁中＋英文（站上艾斯特案例頁同樣是雙語）；cn 字串保留在內容源但不產頁
LANGS = ("tw", "en")
SLUG = "solidworks-2027-iv-day-drone-talk"
_TW2SP = opencc.OpenCC("tw2sp")
_CN_TERMS = [("列印", "打印"), ("影片", "视频"), ("簡報", "演示文稿"), ("简报", "演示文稿"), ("專案", "项目"), ("专案", "项目"),
             ("網頁", "网页"), ("下載", "下载"), ("試片", "试样"), ("试片", "试样"), ("夾治具", "夹治具")]


def cn(s):
    x = s
    for a, b in _CN_TERMS:
        x = x.replace(a, b)
    x = _TW2SP.convert(x)
    for a, b in _CN_TERMS:
        x = x.replace(a, b)
    return x


def L3(tw, en, cn_override=None):
    return {"tw": tw, "cn": cn_override if cn_override is not None else cn(tw), "en": en}


MP4 = {"tw": f"video/{SLUG}-tc.mp4", "cn": f"video/{SLUG}-tc.mp4", "en": f"video/{SLUG}-en.mp4"}
POSTER = {"tw": f"images/{SLUG}-poster-tc.jpg", "cn": f"images/{SLUG}-poster-tc.jpg", "en": f"images/{SLUG}-poster-en.jpg"}
PDF = {"tw": f"downloads/Markforged-SOLIDWORKS-2027-IV-Day-Drone-Talk-TC.pdf",
       "cn": f"downloads/Markforged-SOLIDWORKS-2027-IV-Day-Drone-Talk-TC.pdf",
       "en": f"downloads/Markforged-SOLIDWORKS-2027-IV-Day-Drone-Talk-EN.pdf"}
ASTER = {"tw": "aster-swarm-fpv-airframe-x7-field-edition.html", "cn": "aster-swarm-fpv-airframe-x7-field-edition.html",
         "en": "aster-swarm-fpv-airframe-x7-field-edition-en.html"}

META = {
    "lang_attr": {"tw": "zh-TW", "cn": "zh-CN", "en": "en"},
    "file": {"tw": f"{SLUG}.html", "cn": f"{SLUG}-sc.html", "en": f"{SLUG}-en.html"},
    "hero": f"images/{SLUG}.jpg",
    "og_image": f"https://news.markforged.tw/images/{SLUG}.jpg",
    "title": L3("無人載具與工業級 3D 列印：SOLIDWORKS 2027 創新日 IV Day 專題演講影片 — Markforged",
                "Unmanned Vehicles and Industrial 3D Printing: Talk Video from SOLIDWORKS 2027 IV Day Taiwan — Markforged"),
    "desc": L3("SOLIDWORKS 2027 創新日 IV Day 台北、新竹、台南三場，Markforged 陳中欣的專題演講影片：台灣無人機產業走到哪裡、"
               "無人機專案常卡在哪裡，以及一個在台灣設計、列印、組裝的 FPV 無人機案例。中文版與英文版影片，附簡報下載。",
               "Brian Chen of Markforged at SOLIDWORKS 2027 IV Day Taiwan (Taipei, Hsinchu, Tainan): where Taiwan's drone "
               "industry stands, where drone programmes stall, and an FPV airframe designed, printed and assembled in Taiwan. "
               "Video in Chinese and English, with the slides to download."),
    "og_title": L3("無人載具與工業級 3D 列印：IV Day 專題演講影片",
                   "Unmanned Vehicles and Industrial 3D Printing: IV Day Talk Video"),
    "og_desc": L3("台灣無人機產業的數字、專案卡在等零件的原因，與一個在台灣做出來的 FPV 機體案例。中文版／英文版影片。",
                  "Taiwan's drone numbers, why programmes wait on parts, and an FPV airframe built in Taiwan. In Chinese and English."),
}

UI = {
    "hdr_ev": {"tw": "大中華區媒體中心<br>News &amp; Insights",
               "cn": "大中华区媒体中心<br>News &amp; Insights",
               "en": "Greater China Media Hub<br>News &amp; Insights"},
    "switch_label": {"tw": "語言", "cn": "语言", "en": "Language"},
    "hero_alt": L3("陳中欣手持 ASTER-SWARM FPV 無人機機體，背景為 Markforged 列印機",
                   "Brian Chen holding the ASTER-SWARM FPV airframe, with Markforged printers behind him"),
    "hero_kicker": L3("活動與展會 · SOLIDWORKS 2027 創新日", "Events · SOLIDWORKS 2027 IV Day"),
    "hero_title": L3("無人載具與工業級 3D 列印：專題演講影片",
                     "Unmanned Vehicles and Industrial 3D Printing: The Talk"),
    "hero_meta": L3("SOLIDWORKS 2027 創新日 IV Day ｜ 台灣 ｜ 2026.11.03",
                    "SOLIDWORKS 2027 IV Day | Taiwan | 2026.11.03"),
    "ds_l": L3("十分鐘專題演講 · 中英文影片 · 簡報下載", "A ten-minute talk · video in Chinese and English · slides"),
    "ds_r": L3("台北 11/3 · 新竹 11/12 · 台南 11/13", "Taipei 11/3 · Hsinchu 11/12 · Tainan 11/13"),
}

LEAD = {
    "p1": L3("SOLIDWORKS 2027 創新日 IV Day 今年在台灣有台北、新竹、台南三場。Markforged 大中華區暨越南區總經理陳中欣"
             "以無人載具與工業級 3D 列印的最新趨勢與應用展望為題，用十分鐘談三件事：台灣無人機產業走到哪裡、"
             "無人機專案常卡在哪裡，以及一個在台灣設計、列印、組裝的案例。",
             "SOLIDWORKS 2027 IV Day runs three sessions in Taiwan this year: Taipei, Hsinchu and Tainan. Brian Chen, "
             "Markforged Country Manager for Greater China and Vietnam, uses ten minutes on unmanned vehicles and "
             "industrial 3D printing to cover three things: where Taiwan's drone industry stands, where drone "
             "programmes get stuck, and a case designed, printed and assembled in Taiwan."),
    "p2": L3("以下照簡報順序整理這場演講的重點，配上對應的簡報頁面；<strong>演講影片有中文版與英文版</strong>，"
             "片中直接播放兩段 Markforged 官方影片；頁末可下載簡報 PDF。",
             "Below are the key points of the talk in slide order, each with its slide. <strong>The talk video comes in "
             "Chinese and English</strong>, with two official Markforged videos played in full inside; the slides are "
             "available to download at the end of the page."),
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
    {"tw": "SOLIDWORKS", "cn": "SOLIDWORKS", "en": "SOLIDWORKS", "solid": True},
    {"tw": "IV Day", "cn": "IV Day", "en": "IV Day", "solid": True},
    {"tw": "無人機", "cn": "无人机", "en": "Drones", "solid": False},
    {"tw": "連續碳纖維", "cn": "连续碳纤维", "en": "Continuous Carbon Fiber", "solid": False},
    {"tw": "台灣案例", "cn": "台湾案例", "en": "Made in Taiwan", "solid": False},
]

# 2026-11-03 06:1x Brian 退稿：「幾分幾秒什麼內容？這種呈現方式要幹嘛？直接把簡報內容重點整理進來就好…很奇怪？很單調」
#   → 拿掉章節時間碼與片長；改成照簡報順序的 9 段重點，每段配該頁簡報畫面（中文頁放中文簡報、英文頁放英文簡報）。
def SLIDE(n):
    return {"tw": f"images/{SLUG}-p{n:02d}-tc.jpg", "cn": f"images/{SLUG}-p{n:02d}-tc.jpg", "en": f"images/{SLUG}-p{n:02d}-en.jpg"}


def SEC(h2, h3, paras):
    return {"kind": "sec", "h2": h2, "h3": h3, "paras": paras}


def IMG(n, alt_tw, alt_en):
    return {"kind": "img_full", "slide": True, "img": SLIDE(n), "alt": L3(alt_tw, alt_en),
            "cap": {"tw": f"簡報第 {n} 頁", "cn": f"演示文稿第 {n} 页", "en": f"Slide {n}"}}


BLOCKS = [
    {
        "kind": "mp4",
        "src": MP4,
        "poster": POSTER,
        "alt": L3("SOLIDWORKS 2027 創新日 IV Day 專題演講影片，中文版",
                  "SOLIDWORKS 2027 IV Day talk video, English version"),
        "cap": {"tw": "IV Day 專題演講影片（中文版）｜ Markforged 大中華區",
                "cn": "IV Day 专题演讲视频（中文版，字幕为繁体中文）｜ Markforged 大中华区",
                "en": "IV Day talk video (English) | Markforged Greater China"},
    },
    SEC(L3("台灣：無人機已經是出口數字", "In Taiwan, drones are now an export number"),
        L3("機會在供應鏈：可驗證、可量產、可持續交貨", "The opportunity is in the supply chain: verified, scalable, reliable delivery"),
        [L3("2025 年台灣無人機產值 129 億元，是前一年的 2.56 倍；2026 年前五個月出口 1.53 億美元，已超過 2025 年全年。"
            "投入的廠商超過 260 家，從零組件到整機系統整合；政府六年統籌型計畫 442 億元，目標 2030 年產值 400 億元。"
            "客戶要的是可驗證、可量產、可以持續交貨的供應商。",
            "Taiwan's drone output reached NT$12.9 billion in 2025, 2.56 times the year before; exports in the first five months "
            "of 2026 reached US$153 million, already more than all of 2025. More than 260 companies are involved, from components "
            "to full system integration, and the government's six-year programme is NT$44.2 billion, targeting NT$40 billion in "
            "output by 2030. Customers want suppliers who can verify, scale and keep delivering.")]),
    IMG(3, "簡報第 3 頁：台灣無人機產值、出口、廠商數與政府計畫", "Slide 3: Taiwan drone output, exports, companies and government programme"),
    SEC(L3("專案卡住的，通常不是設計，是零件", "Programmes stall on parts, not design"),
        L3("改版的速度，決定整個專案的速度", "Iteration speed sets the speed of the whole programme"),
        [L3("機臂、馬達座、起落架、飛控固定座、中心機架、電池固定架、酬載支架，全都是少量多樣。"
            "設計每改一次，常常就要改模具、重新加工，或再進口一次，然後就是等。",
            "Arms, motor mounts, landing gear, the avionics mount, centre frame, battery mount and payload mount are all "
            "low-volume and high-mix. Every design change often means new tooling, more machining or another import, and then you wait.")]),
    IMG(4, "簡報第 4 頁：旋翼式無人機主要結構拆解示意圖", "Slide 4: main structural parts of a multirotor drone"),
    SEC(L3("哪些零件可以直接印", "Which parts can be printed directly"),
        L3("不必為每一版開模：設計改完就排印，受力件印出來再驗證", "No new tooling for every revision: change the design, print, then test the load-bearing parts"),
        [L3("機身框架與機臂、涵道護罩與中間的馬達座、電池盒，以及內部鋪了連續碳纖維的底板，都是 Markforged 原廠展示樣品的列印檔。"
            "起落架、產線上的治具與夾具，也一樣可以印。",
            "A frame with arms, a duct guard with the motor mount at its centre, a battery box, and a base plate with continuous "
            "carbon fiber inside: all are print files of Markforged sample parts. Landing gear and the jigs and fixtures on a "
            "production line can be printed too.")]),
    IMG(5, "簡報第 5 頁：可直接列印的無人機零件", "Slide 5: drone parts that can be printed directly"),
    SEC(L3("連續纖維強化：跟一般 3D 列印最大的不同", "Continuous fiber: the biggest difference"),
        L3("纖維鋪在哪幾層、哪些區域，由你指定", "You choose the layers and regions that get fiber"),
        [L3("列印機有兩個噴頭：一個擠出 Onyx（加了短碳纖的尼龍）做外形，另一個把一整條連續碳纖維鋪進零件裡。"
            "沿纖維方向，連續碳纖維試片的拉伸強度是 800 MPa，6061-T6 鋁約為 310 MPa；這是材料試片值，實際零件取決於纖維鋪多少、往哪個方向。"
            "上下夾層、同心環、只補孔、只補外殼四種鋪法，在切層軟體裡逐層選。",
            "The printer has two nozzles: one extrudes Onyx, a nylon filled with micro carbon fiber, for the shape; the other "
            "lays a single continuous strand of carbon fiber inside the part. Along the fiber, a continuous carbon fiber test "
            "coupon reaches 800 MPa in tension, against about 310 MPa for 6061-T6 aluminium; these are coupon values, and a real "
            "part depends on how much fiber is laid and in which direction. Sandwich, concentric, holes-only and outer-wall "
            "patterns are chosen layer by layer in the slicer.")]),
    IMG(6, "簡報第 6 頁：連續纖維強化與四種鋪法", "Slide 6: continuous fiber reinforcement and four layup patterns"),
    SEC(L3("強度，用看的最清楚", "Strength is easiest to see"),
        L3("連續碳纖維鏈環，拉到 22,000 磅力才斷", "A continuous carbon fiber chain link breaks at 22,000 lbf"),
        [L3("大約是十公噸重物的拉力。影片中直接播放 Markforged 官方的鏈環拉力測試。",
            "That is about the pull of a ten-tonne weight. The video plays Markforged's official chain-link pull test in full.")]),
    IMG(7, "簡報第 7 頁：連續碳纖維鏈環拉力測試", "Slide 7: continuous carbon fiber chain-link pull test"),
    SEC(L3("從複材到金屬：三條設備線", "From composites to metal: three equipment lines"),
        L3("FX10、FX20、X7", "FX10, FX20 and X7"),
        [L3("FX10 從複合材料起步，加裝 Metal Kit 就能印金屬，再接 Wash-1 脫脂、Sinter-2 燒結，就是完整的金屬流程。"
            "FX20 是大尺寸機型，加熱腔體最高 200°C，可以印 ULTEM 9085 高溫材料。"
            "X7 是連續纖維的主力機型；野戰版 X7 Field Edition 整台裝在強化運輸箱裡，開箱到開始列印不到三分鐘。",
            "FX10 starts with composites; add the Metal Kit and it prints metal, with Wash-1 debinding and Sinter-2 sintering "
            "completing the metal workflow. FX20 is the large-format machine, with a heated chamber up to 200°C, and prints "
            "ULTEM 9085. X7 is the continuous fiber workhorse; the X7 Field Edition ships in a rugged transit case and goes from "
            "unboxing to printing in under three minutes.")]),
    IMG(8, "簡報第 8 頁：FX10、FX20、X7 三條設備線", "Slide 8: the FX10, FX20 and X7 equipment lines"),
    SEC(L3("全球的無人機製造商，已經這樣做", "Drone makers worldwide already do this"),
        L3("數字都是他們自己公開發佈的", "These are their own published numbers"),
        [L3("印度 Raphe mPhibr 工裝交期縮短 60%；美國 BRINC 的第一線應急無人機，主要結構件採用列印；"
            "日本 BODUK 的爬牆式巡檢無人機，生產時間減少 50–66%；日本 AeroG Lab 零件成本降低 90%，交期從兩三週縮到一兩天。"
            "印度 Gamma Rotors 的列印機從一台增加到十台以上，影片中播放他們的自述。",
            "Raphe mPhibr in India cut tooling lead time by 60%; BRINC in the US prints the main structural parts of its "
            "first-responder drones; BODUK in Japan cut production time for its wall-climbing inspection drones by 50–66%; "
            "AeroG Lab in Japan cut part cost by 90% and lead time from two or three weeks to one or two days. Gamma Rotors in "
            "India grew from one printer to more than ten, and the video plays them telling it in their own words.")]),
    IMG(9, "簡報第 9 頁：全球四家無人機製造商案例", "Slide 9: four drone makers worldwide"),
    {"kind": "sec",
     "h2": L3("台灣案例：艾斯特 ASTER-SWARM", "Taiwan case: ASTER-SWARM"),
     "h3": L3("通過九級風抗風測試，機體在台灣設計、列印、組裝", "Force 9 wind test passed; designed, printed and assembled in Taiwan"),
     "paras": [
        L3("FPV 無人機飛行時，幾秒內就要全油門加速、急轉、俯衝；一般線材印的機體，容易機臂彎曲、結構共振、沿層線開裂，"
           "馬達座一帶受熱慢慢變形。另一條路是 CNC 碳板，強度夠，但每改一次設計就要重新開料、再等一次交期。",
           "An FPV drone goes to full throttle, turns hard and dives within seconds. Frames printed in ordinary filament tend "
           "to flex at the arms, resonate, crack along layer lines and deform around the motor mounts as they heat up. The "
           "alternative, CNC carbon plate, is strong enough, but every design change means a new cut and another wait."),
        {"tw": f'艾斯特物聯科技以 X7 Field Edition 列印，連續碳纖維集中在機臂根部與馬達座，機體拆成五個標準模組；'
               f'原型機通過蒲福九級風抗風測試，經中科院軍民通用中心量測驗證。<a href="{ASTER["tw"]}">完整案例 →</a>',
         "cn": cn('艾斯特物聯科技以 X7 Field Edition 列印，連續碳纖維集中在機臂根部與馬達座，機體拆成五個標準模組；'
                  '原型機通過蒲福九級風抗風測試，經中科院軍民通用中心量測驗證。') + f'<a href="{ASTER["cn"]}">完整案例 →</a>',
         "en": f'ASTER Technology printed the airframe on the X7 Field Edition, with continuous carbon fiber concentrated at the '
               f'arm roots and motor mounts and the airframe split into five standard modules. The prototype passed a Beaufort '
               f'force 9 wind test, measured and verified by a unit of NCSIST. <a href="{ASTER["en"]}">Full case →</a>'},
     ]},
    IMG(13, "簡報第 13 頁：艾斯特 ASTER-SWARM 的測試結果", "Slide 13: ASTER-SWARM test results"),
    SEC(L3("設計越來越快，瓶頸移到製造", "Faster design moves the bottleneck to manufacturing"),
        L3("Markforged 自己也用 SOLIDWORKS 設計列印機", "Markforged designs its own printers in SOLIDWORKS"),
        [L3("Premium 做設計、PDM 管檔案、Simulation 做模擬，當時新產品開發週期縮到六個月以內。"
            "接下來 AI 會讓候選設計變多，生成式設計、拓樸最佳化一次就能出好幾個版本；但關鍵設計還是要做出來、裝上去、飛一次。"
            "設計端變快，製造端就要跟上同一個節拍。",
            "Premium for design, PDM for files and Simulation for analysis cut the new-product development cycle to under six "
            "months at the time. AI will multiply candidate designs, with generative design and topology optimisation producing "
            "several versions at once; but the key design still has to be built, fitted and flown. When design speeds up, "
            "manufacturing has to keep the same pace.")]),
    IMG(14, "簡報第 14 頁：設計端的 SOLIDWORKS 與 AI", "Slide 14: SOLIDWORKS and AI on the design side"),
    {
        "kind": "sec",
        "h2": L3("簡報下載", "Download the slides"),
        "h3": L3("十五頁，PDF", "Fifteen slides, PDF"),
        "paras": [
            {"tw": f'<a href="{PDF["tw"]}">下載中文版簡報（PDF）</a> ・ <a href="{PDF["en"]}">English slides (PDF)</a>',
             "cn": f'<a href="{PDF["cn"]}">下载中文版演示文稿（PDF，繁体中文）</a> ・ <a href="{PDF["en"]}">English slides (PDF)</a>',
             "en": f'<a href="{PDF["en"]}">Download the slides (PDF)</a> · <a href="{PDF["tw"]}">Chinese version (PDF)</a>'},
        ],
    },
]

CTA = {
    "h": L3("帶一個零件來，讓我們幫你評估", "Bring a part, and let us assess it"),
    "p": L3("帶一張圖，或一個不涉機密的 STL 檔，告訴我們用途、受力、溫度和數量，我們評估印不印得出來、用什麼材料、要多久；"
            "如果加工或開模比較划算，我們也會照實說。",
            "Bring a drawing or a non-confidential STL file, and tell us the use, loads, temperature and quantity. We will "
            "assess whether it can be printed, in which material and how long it takes; if machining or tooling is the "
            "better deal, we will say so."),
    "btn": {"tw": "聯絡我們", "cn": "联系我们", "en": "Contact us"},
}

SRC = {
    "h": {"tw": "資料來源", "cn": "资料来源", "en": "Sources"},
    "items": [
        L3("台灣無人機產業數字：經濟部航太小組《台灣無人機產業發展現況與政策推動重點》，2026 年 6 月 30 日。",
           "Taiwan drone industry figures: Ministry of Economic Affairs (Taiwan), Aerospace Industry Development Office, "
           "status of Taiwan's drone industry and policy priorities, 30 June 2026."),
        L3("全球案例數字取自 Markforged 官方無人機產業簡報（2026），各案基準不同，為該案條件下的結果。",
           "Global case figures are from Markforged's official drone industry deck (2026); baselines differ by case, "
           "and each figure applies to that case's conditions."),
        L3("鏈環拉力測試與 Gamma Rotors 影片片段取自 Markforged 官方 YouTube 頻道。",
           "The chain-link pull test and Gamma Rotors footage are from Markforged's official YouTube channel."),
        L3("艾斯特 ASTER-SWARM 測試結果由艾斯特物聯科技提供；抗風測試經中科院軍民通用中心量測驗證。頁首照片為 iThome 2026 年 9 月專訪現場。",
           "ASTER-SWARM test results were provided by ASTER Technology; the wind test was measured and verified by a unit "
           "of NCSIST. The header photo is from an iThome interview in September 2026."),
        L3("影片為 Markforged 大中華區依演講簡報自製；旁白以陳中欣本人聲音合成。背景的無人機畫面為示意插圖，"
           "不是 Markforged 產品，也不是任何客戶機型；產品影像為原廠素材。",
           "The video was produced by Markforged Greater China from the talk's slides; the narration was synthesised "
           "from Brian Chen's own voice. The drone backgrounds are illustrations, not Markforged products or any "
           "customer's aircraft; product imagery is official Markforged material."),
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

APPROVED_QUOTES = {"tw": [], "cn": [], "en": []}

DOC_TERMS = ["Markforged", "SOLIDWORKS", "IV Day", "ASTER-SWARM", "ASTER", "X7 Field Edition", "FX10", "FX20", "X7",
             "Onyx", "Metal Kit", "Wash-1", "Sinter-2", "ULTEM", "Raphe mPhibr", "BRINC", "BODUK", "AeroG Lab",
             "Gamma Rotors", "NCSIST", "STL", "FPV", "iThome"]

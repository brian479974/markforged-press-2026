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

LANGS = ("tw", "cn", "en")
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
    "ds_l": L3("中文版 7 分 41 秒 · 英文版 8 分 16 秒", "Chinese 7 min 41 s · English 8 min 16 s"),
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
    "p2": L3("本頁收錄這場演講的影片版：以簡報內容配上旁白與動態圖文，<strong>中文版與英文版各一支</strong>，"
             "片中直接播放兩段 Markforged 官方影片；頁末附簡報 PDF 下載。",
             "This page carries the video version of the talk: the slides with narration and motion graphics, "
             "<strong>one in Chinese and one in English</strong>, with two official Markforged videos played in full "
             "inside. The slides are available to download at the end of the page."),
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

# 章節：起點取自兩支影片各自的場景時間軸（_qa/cues.json 的 scenes.a），中英文長度不同各算各的
_CH = [  # (中文起點, 英文起點, 繁中, 英文)
    ("0:00", "0:00", "開場：一架無人機從設計到出任務要多久", "Opening: how long from design to mission"),
    ("0:29", "0:33", "台灣無人機產業的數字", "Taiwan's drone industry in numbers"),
    ("1:00", "1:09", "瓶頸：專案卡在等零件", "The bottleneck: waiting for parts"),
    ("1:27", "1:35", "哪些零件可以直接印", "Which parts can be printed directly"),
    ("1:55", "2:03", "連續纖維強化", "Continuous fiber reinforcement"),
    ("2:42", "2:59", "強度實測：鏈環拉力影片", "Strength on film: the chain-link pull test"),
    ("3:16", "3:36", "三條設備線", "Three equipment lines"),
    ("3:51", "4:11", "全球無人機製造商的做法", "What drone makers worldwide are doing"),
    ("4:18", "4:42", "Gamma Rotors 客戶自述", "Gamma Rotors in their own words"),
    ("5:05", "5:28", "台灣案例：艾斯特 ASTER-SWARM", "Taiwan case: ASTER-SWARM"),
    ("6:33", "7:11", "設計端：SOLIDWORKS 與 AI", "The design side: SOLIDWORKS and AI"),
    ("7:05", "7:39", "回到開場的問題", "Back to the opening question"),
]

BLOCKS = [
    {
        "kind": "mp4",
        "src": MP4,
        "poster": POSTER,
        "alt": L3("SOLIDWORKS 2027 創新日 IV Day 專題演講影片，中文版 7 分 41 秒",
                  "SOLIDWORKS 2027 IV Day talk video, English version, 8 minutes 16 seconds"),
        "cap": {"tw": "IV Day 專題演講影片 ｜ 中文版 7 分 41 秒 ｜ Markforged 大中華區",
                "cn": "IV Day 专题演讲视频 ｜ 中文版 7 分 41 秒（字幕为繁体中文）｜ Markforged 大中华区",
                "en": "IV Day talk video | English version, 8 min 16 s | Markforged Greater China"},
    },
    {
        "kind": "sec",
        "h2": L3("影片章節", "Chapters"),
        "h3": L3("十五頁簡報，十二個段落", "Fifteen slides in twelve chapters"),
        "paras": [L3("時間為影片中的起點。鏈環拉力測試與 Gamma Rotors 兩段是 Markforged 官方影片，片中直接播放原音。",
                     "Times are where each chapter starts in the video. The chain-link pull test and Gamma Rotors "
                     "segments are official Markforged videos, played with their original audio.")],
        "hl": [{"b": {"tw": a, "cn": a, "en": b}, "s": L3(c, d)} for a, b, c, d in _CH],
    },
    {
        "kind": "sec",
        "h2": L3("台灣的數字，與專案真正的瓶頸", "Taiwan's numbers, and the real bottleneck"),
        "h3": L3("機會在供應鏈；改版的速度，決定整個專案的速度",
                 "The opportunity is in the supply chain; iteration speed sets programme speed"),
        "paras": [
            L3("2025 年台灣無人機產值 129 億元，是前一年的 2.56 倍；2026 年前五個月出口 1.53 億美元，已超過 2025 年全年。"
               "投入的廠商超過 260 家，政府六年統籌型計畫 442 億元，目標 2030 年產值 400 億元。",
               "Taiwan's drone output reached NT$12.9 billion in 2025, 2.56 times the year before; exports in the first "
               "five months of 2026 reached US$153 million, already more than all of 2025. More than 260 companies are "
               "involved, and the government's six-year programme is NT$44.2 billion, targeting NT$40 billion in output by 2030."),
            L3("做過無人機專案的人都知道，最常卡住的不是設計，而是零件：機臂、馬達座、起落架、飛控固定座、中心機架、"
               "電池固定架、酬載支架，全都是少量多樣。設計每改一次，常常就要改模具、重新加工或再進口一次。",
               "Anyone who has run a drone programme knows the hold-up is usually parts, not design: arms, motor mounts, "
               "landing gear, the avionics mount, centre frame, battery mount and payload mount are all low-volume and "
               "high-mix. Each design change often means new tooling, more machining or another import."),
        ],
    },
    {
        "kind": "sec",
        "h2": L3("連續纖維與三條設備線", "Continuous fiber and three equipment lines"),
        "h3": L3("在你指定的層與區域鋪進連續碳纖維", "Continuous carbon fiber, laid in the layers and regions you choose"),
        "paras": [
            L3("Markforged 的列印機有兩個噴頭：一個擠出 Onyx（加了短碳纖的尼龍）做外形，另一個把一整條連續碳纖維鋪進零件裡。"
               "沿纖維方向，連續碳纖維試片的拉伸強度是 800 MPa，6061-T6 鋁約為 310 MPa；這是材料試片值，"
               "實際零件取決於纖維鋪多少、往哪個方向。",
               "Markforged printers have two nozzles: one extrudes Onyx, a nylon filled with micro carbon fiber, for the "
               "shape; the other lays a single continuous strand of carbon fiber inside the part. Along the fiber, a "
               "continuous carbon fiber test coupon reaches 800 MPa in tension, against about 310 MPa for 6061-T6 "
               "aluminium. These are coupon values; a real part depends on how much fiber is laid and in which direction."),
        ],
        "hl": [
            {"b": L3("FX10", "FX10"), "s": L3("從複合材料起步，加裝 Metal Kit 印金屬，接 Wash-1 脫脂與 Sinter-2 燒結",
                                               "Starts with composites; add the Metal Kit for metal, with Wash-1 debinding and Sinter-2 sintering")},
            {"b": L3("FX20", "FX20"), "s": L3("大尺寸、加熱腔體最高 200°C，可印 ULTEM 9085 高溫材料",
                                               "Large format, heated chamber up to 200°C, prints ULTEM 9085")},
            {"b": L3("X7", "X7"), "s": L3("連續纖維主力機型；X7 Field Edition 裝在強化運輸箱裡，開箱到列印不到三分鐘",
                                           "The continuous fiber workhorse; the X7 Field Edition ships in a rugged case, unbox to print in under three minutes")},
        ],
    },
    {
        "kind": "sec",
        "h2": L3("全球案例，與台灣自己的案例", "Global cases, and one from Taiwan"),
        "h3": L3("數字都是各家公開發佈的；台灣案例由艾斯特物聯科技提供",
                 "The figures are each company's own published numbers; the Taiwan case is provided by ASTER Technology"),
        "paras": [
            L3("印度 Raphe mPhibr 工裝交期縮短 60%；美國 BRINC 的第一線應急無人機，主要結構件採用列印；日本 BODUK 的爬牆式巡檢無人機，"
               "生產時間減少 50–66%；日本 AeroG Lab 零件成本降低 90%，交期從兩三週縮到一兩天。印度 Gamma Rotors 的列印機從一台增加到十台以上。",
               "Raphe mPhibr in India cut tooling lead time by 60%; BRINC in the US prints the main structural parts of its "
               "first-responder drones; BODUK in Japan cut production time for its wall-climbing inspection drones by 50–66%; "
               "AeroG Lab in Japan cut part cost by 90% and lead time from two or three weeks to one or two days. Gamma Rotors "
               "in India grew from one printer to more than ten."),
            {"tw": f'艾斯特物聯科技的 FPV 無人機 ASTER-SWARM 以 X7 Field Edition 列印，連續碳纖維集中在機臂根部與馬達座，機體拆成五個模組；'
                   f'原型機通過蒲福九級風抗風測試，經中科院軍民通用中心量測驗證，機體在台灣設計、列印、組裝。'
                   f'<a href="{ASTER["tw"]}">完整案例 →</a>',
             "cn": cn('艾斯特物聯科技的 FPV 無人機 ASTER-SWARM 以 X7 Field Edition 列印，連續碳纖維集中在機臂根部與馬達座，機體拆成五個模組；'
                      '原型機通過蒲福九級風抗風測試，經中科院軍民通用中心量測驗證，機體在台灣設計、列印、組裝。')
                   + f'<a href="{ASTER["cn"]}">完整案例 →</a>',
             "en": f'ASTER Technology printed its ASTER-SWARM FPV airframe on the X7 Field Edition, with continuous carbon fiber '
                   f'concentrated at the arm roots and motor mounts and the airframe split into five modules. The prototype passed '
                   f'a Beaufort force 9 wind test, measured and verified by a unit of NCSIST, and was designed, printed and '
                   f'assembled in Taiwan. <a href="{ASTER["en"]}">Full case →</a>'},
        ],
    },
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

# -*- coding: utf-8 -*-
"""FX10 活動頁「活動主視覺版」內容源（2026-11-11 第二版，取代文章版 content_fx10campaign*.py）。

Brian：「這個頁面要做得更盛大一點、更有吸引力才對」「裡面的內容請模擬專家行銷專家做評鑒並優化他」。
→ 獨立 B2B 工業行銷專家評鑑（總分約 5.4／10，前五大問題：主張與證據對不上、轉換點只有一個、
  開場鉤子與證據脫鉤、文章骨架套不進活動版、沒有「我的零件適不適合」入口）→ 本檔依評鑑重寫。

事實來源與限制同文章版（逐條對過原廠官網原文，連結即出處）：
  · 只有 GRP、Plane Support 是 FX10；Dana、CMS、Cannon 是 X7；Subaru、Hangar One 原文未寫機型；
    Fort Irwin、退伍軍人事務部標「Markforged 平台」（Fort Irwin 金屬版原文機型為已停產機種，不寫）
  · 不寫：Metal X／PX100、Hangar One 65%、FX10 重量、ULTEM FAR 25.853；Onyx GF 依原廠規格表六色
  · 簡中（cn）：tw 文字經 content_fx10campaign_sc.cn() 轉大陸用語；defense=True 的項目整個不出
  · 不用引號包句子（網站冒名引言閘）

語言：tw 必填、en 必填；cn 預設由 tw 自動轉，必要時給 "cn" 覆寫。
"""
from urllib.parse import quote

S = "fx10-it-starts-here"
LANGS = ("tw", "cn", "en")
FILES = {"tw": f"{S}.html", "cn": f"{S}-sc.html", "en": f"{S}-en.html"}
LANG_ATTR = {"tw": "zh-TW", "cn": "zh-CN", "en": "en"}
LANG_NAMES = {"tw": "繁體中文", "cn": "简体中文", "en": "English"}
MAIL = "brian.chen@markforged.com"

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

# ── 詢價信（不同位置用不同主旨，方便分辨詢問從哪一段來）────────────────────
MAIL_BODY = {
    "tw": "您好，\n\n產業：\n零件用途：\n預計材料：\n所在地區（台灣／中國／香港／越南）：\n\n（如有零件圖檔請一併附上）\n",
    "cn": "您好，\n\n行业：\n零件用途：\n预计材料：\n所在地区（台湾／中国／香港／越南）：\n\n（如有零件图档请一并附上）\n",
    "en": "Hello,\n\nIndustry:\nWhat the part does:\nIntended material:\nLocation (Taiwan / China / Hong Kong / Vietnam):\n\n(Please attach a part file if you have one.)\n",
}
SUBJ = {
    "demo": {"tw": "FX10 預約展示／索取報價", "cn": "FX10 预约演示／索取报价", "en": "FX10 demo / quote"},
    "part": {"tw": "FX10 零件評估（寄圖檔）", "cn": "FX10 零件评估（发图档）", "en": "FX10 part review (part file)"},
}


def mailto(kind, where, lang):
    subj = f"{SUBJ[kind][lang]}｜{where}" if lang != "en" else f"{SUBJ[kind][lang]} | {where}"
    return f"mailto:{MAIL}?subject={quote(subj)}&body={quote(MAIL_BODY[lang])}"


META = {
    "title": {"tw": "不能出錯的零件，從這裡開始｜FX10｜Markforged 媒體中心",
              "cn": "不能出错的零件，从这里开始｜FX10｜Markforged 媒体中心",
              "en": "If It Has to Work, It Starts Here | FX10 | Markforged Media Hub"},
    "desc": {"tw": "FX10 把連續碳纖維複材與金屬列印放進同一台機器、放在工廠現場。汽車、航太、國防九個 Markforged 原廠案例，每個數字都標明機型與原文出處。",
             "cn": "FX10 把连续碳纤维复合材料与金属打印放进同一台设备、放在工厂现场。汽车与航空航天六个 Markforged 原厂案例，每个数字都标明机型与原文出处。",
             "en": "FX10 puts continuous carbon fiber composites and metal printing on one machine, on the factory floor. Nine Markforged cases across automotive, aerospace and defense, each figure labeled with the printer and source."},
    "og_title": {"tw": "不能出錯的零件，從這裡開始｜FX10", "cn": "不能出错的零件，从这里开始｜FX10",
                 "en": "If it has to work, it starts here | FX10"},
    "og_desc": {"tw": "隔夜印好的治具、可直接焊接的 316L 法蘭、取得澳洲民航核准的直升機風管，都出自 FX10。",
                "cn": "隔夜打印完成的夹具、可直接焊接的 316L 法兰、获澳大利亚民航批准的直升机风管，都出自 FX10。",
                "en": "Fixtures printed overnight, weld-ready 316L flanges and CASA-approved helicopter ducting, all made on the FX10."},
}

UI = {
    "hdr_ev": {"tw": "大中華區媒體中心<br>News &amp; Insights", "cn": "大中华区媒体中心<br>News &amp; Insights",
               "en": "Greater China Media Hub<br>News &amp; Insights"},
    "switch_label": {"tw": "語言", "cn": "语言", "en": "Language"},
    "nav": [
        ("#ch-auto", {"tw": "汽車", "en": "Automotive"}, False),
        ("#onyx-gf", {"tw": "Onyx GF", "en": "Onyx GF"}, False),
        ("#ch-aero", {"tw": "航太", "en": "Aerospace"}, False),
        ("#ch-def", {"tw": "國防", "en": "Defense"}, True),
        ("#fx10", {"tw": "FX10 規格", "en": "FX10 specs"}, False),
        ("#contact", {"tw": "預約展示", "en": "Book a demo"}, False),
    ],
    "machine_note": {"tw": "機型照原文標示", "en": "Printer as stated in the source"},
    "read_original": {"tw": "原廠案例（英文）&nbsp;→", "en": "Read the original&nbsp;→"},
    "video_cap_auto": {"tw": "原廠影片 · 汽車篇 Performance Critical ｜ 約 21 秒",
                       "en": "Official film · Automotive, Performance Critical | about 21 seconds"},
    "video_cap_aero": {"tw": "原廠影片 · 航太國防篇 Mission Critical ｜ 約 22 秒",
                       "en": "Official film · Aerospace &amp; Defense, Mission Critical | about 22 seconds"},
    "hero_alt": {"tw": "FX10 取出一整盤列印零件（Markforged 原廠影片畫面）",
                 "en": "A full plate of parts coming off an FX10 (frame from an official Markforged film)"},
}

HERO = {
    "kicker": {"tw": "FX10 ・ 工業級複材＋金屬 3D 列印", "en": "FX10 · Industrial composite + metal 3D printing"},
    "h1": {"tw": "不能出錯的零件，<br>從這裡開始。", "cn": "不能出错的零件，<br>从这里开始。",
           "en": "If it has to work,<br>it starts here."},
    "sub": {"tw": "FX10 把連續碳纖維複材與金屬列印放進同一台機器、放在工廠現場。隔夜印好的治具、可直接焊接的 316L 法蘭、取得澳洲民航核准的直升機風管，都出自這台機器。",
            "cn": "FX10 把连续碳纤维复合材料与金属打印放进同一台设备、放在工厂现场。隔夜打印完成的夹具、可直接焊接的 316L 法兰、获澳大利亚民航批准的直升机风管，都出自这台设备。",
            "en": "FX10 puts continuous carbon fiber composites and metal printing on one machine, on the factory floor. Fixtures printed overnight, weld-ready 316L flanges, CASA-approved helicopter ducting: all made on this machine."},
    "cta1": {"tw": "預約展示／索取報價", "cn": "预约演示／索取报价", "en": "Book a demo / Get a quote"},
    "cta2": {"tw": "看九個原廠案例&nbsp;↓", "cn": "看六个原厂案例&nbsp;↓", "en": "See the nine cases&nbsp;↓"},
}

TICKER = ["Performance Critical", "Mission Critical", "Zero Compromise", "If it has to work, it starts here"]

FX10_LINE = {
    "h": {"tw": "FX10：一台機器，兩種製程，就放在工廠現場", "en": "FX10: one machine, two processes, right on the factory floor"},
    "items": [
        {"b": {"tw": "一機雙料", "en": "Composites and metal"},
         "s": {"tw": "連續碳纖維複材印治具與零件；換上 Metal Kit，同一台印 316L、17-4PH 與 H13",
               "en": "Continuous-fiber composite fixtures and parts; swap in the Metal Kit and the same machine prints 316L, 17-4PH and H13"}},
        {"b": {"tw": "邊印邊量", "cn": "边打印边测量", "en": "Measures while it prints"},
         "s": {"tw": "列印頭上的雷射測微器在列印中掃描零件，搭配 Inspection 軟體驗證尺寸",
               "en": "A printhead-mounted laser micrometer scans parts during printing for dimensional checks in Inspection"}},
        {"b": {"tw": "為工廠設計", "en": "Built for the floor"},
         "s": {"tw": "腔體加熱至 60 °C、自動調平與自動換料、單相一般插座供電",
               "en": "Chamber heated to 60 °C, automatic leveling and material changeover, single-phase wall power"}},
    ],
}

STATS = {
    "h": {"tw": "原廠案例實績", "en": "Results from Markforged cases"},
    "note": {"tw": "數字取自 Markforged 原廠案例原文；機型照原文標示，並非每一案都是 FX10。",
             "en": "Figures are from the original Markforged case studies; the printer is labeled as the source states it, and not every case is an FX10."},
    "items": [
        {"n": {"tw": "20–40 小時 → 隔夜", "en": "20–40 hrs → overnight"},
         "l": {"tw": "手工治具改成 CAD 畫好、隔夜印完", "en": "Hand-built fixtures, now designed in CAD and printed overnight"},
         "src": {"tw": "GRP ・ FX10", "en": "GRP · FX10"}, "fx10": True},
        {"n": {"tw": "CASA 核准", "en": "CASA approved"},
         "l": {"tw": "Bell 214B 機艙空調風管獲准以積層製造生產", "en": "Bell 214B cabin ducting approved for additive production"},
         "src": {"tw": "Plane Support ・ FX10", "en": "Plane Support · FX10"}, "fx10": True},
        {"n": {"tw": "−70% ／ −90%", "en": "−70% / −90%"},
         "l": {"tw": "每件治具的成本／交期", "en": "Cost / lead time per fixture"},
         "src": {"tw": "Dana ・ X7", "en": "Dana · X7"}},
        {"n": {"tw": "0.1 mm", "en": "0.1 mm"},
         "l": {"tw": "Onyx GF 保險桿標籤定位治具的精度", "en": "Tolerance of Onyx GF bumper-label jigs"},
         "src": {"tw": "Subaru ・ 原文未寫機型", "en": "Subaru · printer not stated"}},
        {"n": {"tw": "約 30 分鐘", "en": "~30 min"},
         "l": {"tw": "每件省下的人工量測時間", "en": "Manual inspection time saved per part"},
         "src": {"tw": "Hangar One ・ 原文未寫機型", "en": "Hangar One · printer not stated"}},
        {"n": {"tw": "$244,000", "en": "$244,000"},
         "l": {"tw": "停產艙蓋塞這一項應用省下的金額", "en": "Saved by one application: an out-of-production hatch plug"},
         "src": {"tw": "Fort Irwin ・ Markforged 平台", "en": "Fort Irwin · Markforged platform"}, "defense": True},
        {"n": {"tw": "UL 94 V-0", "en": "UL 94 V-0"},
         "l": {"tw": "Onyx FR 阻燃等級，零件符合 FAA 要求", "en": "Onyx FR rating; parts meet FAA requirements"},
         "src": {"tw": "CMS ・ X7", "en": "CMS · X7"}, "cn_only": True},
    ],
}

FINDER = {
    "h": {"tw": "你的零件是哪一種？", "en": "What kind of part is yours?"},
    "sub": {"tw": "點一下，直接看同類零件的原廠案例。", "en": "Jump straight to Markforged cases with parts like yours."},
    "items": [
        {"t": {"tw": "產線治具與夾具", "en": "Line fixtures and jigs"}, "c": "GRP · Subaru · Dana", "href": "#case-grp"},
        {"t": {"tw": "色碼治具", "en": "Color-coded tooling"}, "c": "Subaru · Onyx GF", "href": "#onyx-gf"},
        {"t": {"tw": "可直接焊接的金屬件", "en": "Weld-ready metal parts"}, "c": "GRP · 316L", "href": "#case-grp"},
        {"t": {"tw": "阻燃、適航零件", "en": "Flame-retardant, flight parts"}, "c": "Plane Support · CMS", "href": "#case-plane"},
        {"t": {"tw": "以複材取代鋁件", "en": "Composites in place of aluminum"}, "c": "Hangar One", "href": "#case-hangar"},
        {"t": {"tw": "停產備件", "en": "Out-of-production spares"}, "c": "Fort Irwin", "href": "#case-irwin", "defense": True},
    ],
}

# ── 案例 ─────────────────────────────────────────────────────────────────
# machine：fx10 / x7 / ns（原文未寫）/ platform（Markforged 平台）
MACHINE = {"fx10": {"tw": "FX10", "en": "FX10"}, "x7": {"tw": "X7", "en": "X7"},
           "ns": {"tw": "原文未寫機型", "en": "Printer not stated"},
           "platform": {"tw": "Markforged 平台", "en": "Markforged platform"}}

CASES = {
    "grp": {"img": f"images/{S}-case-grp.jpg", "machine": "fx10", "featured": True,
            "alt": {"tw": "GRP 為 Lamborghini Revuelto 製作的 X-pipe 排氣管", "en": "GRP's X-pipe exhaust for a Lamborghini Revuelto"},
            "tags": {"tw": "超跑改裝 ・ 美國", "en": "Supercar fabrication · U.S."},
            "title": {"tw": "Graham Rahal Performance：手工 20–40 小時的治具，改成隔夜印好",
                      "en": "Graham Rahal Performance: from 20–40 hours of hand fabrication to fixtures printed overnight"},
            "body": {"tw": "師傅過去要花 20 到 40 小時切割、成形、焊接一組治具、支架或排氣零件；導入 FX10 後，CAD 畫好、隔夜印完、隔天就用。為 1,000 匹馬力的油電超跑 Lamborghini Revuelto 製作 X-pipe 排氣時，GRP 用 FX10 以 316L 不鏽鋼印出法蘭，表面可直接焊接，幾乎不需後加工。",
                     "en": "A fabricator used to spend 20 to 40 hours cutting, shaping and welding jigs, fixtures and exhaust components. With the FX10, they are designed in CAD, printed overnight and used the next day. For an X-pipe on the 1,000-horsepower hybrid Lamborghini Revuelto, GRP printed the flanges in 316L stainless steel on the FX10: weld-ready, with almost no post-processing."},
            "metric": {"tw": "20–40 小時 → 隔夜", "en": "20–40 hrs → overnight"}, "url": URL["grp"]},
    "subaru": {"img": f"images/{S}-case-subaru.jpg", "machine": "ns", "material": "Onyx GF",
               "alt": {"tw": "Subaru 印第安納廠組裝線", "en": "Assembly line at Subaru of Indiana Automotive"},
               "tags": {"tw": "整車組裝 ・ 美國", "en": "Vehicle assembly · U.S."},
               "title": {"tw": "Subaru of Indiana：ABS 治具會裂，改用六色 Onyx GF",
                         "en": "Subaru of Indiana: ABS jigs cracked, so they switched to six-color Onyx GF"},
               "body": {"tw": "同一條線同時組裝多個車型，治具之間只差幾公釐。改用 Onyx GF 後，每個車型配一種顏色，作業員第一次伸手就拿對；保險桿 QR 追蹤標籤的定位治具，精度做到 0.1 mm。",
                        "en": "Several models share one line and their tools differ by millimeters. Reprinted in Onyx GF, each model variant got its own color, so operators grab the right tool on the first pass; the bumper QR-label placement jigs hold a 0.1 mm tolerance."},
               "metric": {"tw": "0.1 mm", "en": "0.1 mm"}, "url": URL["subaru"]},
    "dana": {"img": f"images/{S}-case-dana.jpg", "machine": "x7",
             "alt": {"tw": "Dana 以複材列印的工件夾持齒輪治具", "en": "Composite workholding gear fixture printed by Dana"},
             "tags": {"tw": "車用傳動系統 ・ 義大利", "en": "Drivetrain systems · Italy"},
             "title": {"tw": "Dana：工件夾持治具自己印，上線一年以上沒壞",
                       "en": "Dana: in-house workholding fixtures, more than a year in service without failure"},
             "body": {"tw": "全球傳動與動力系統供應商 Dana 在七個國家部署 Markforged 印表機。義大利 Rovereto 工程中心用 X7 印的複材治具，上線超過一年沒有故障，每件治具成本降 70%、交期縮短 90%。",
                      "en": "Global drivetrain and power systems supplier Dana runs Markforged printers in seven countries. Composite fixtures printed on an X7 at its Rovereto, Italy engineering center ran for over a year without failure, at 70% lower cost and 90% shorter lead time per fixture."},
             "metric": {"tw": "−70% ／ −90%", "en": "−70% / −90%"}, "url": URL["dana"]},
    "plane": {"img": "images/casa-214b-parts.jpg", "machine": "fx10", "featured": True,
              "alt": {"tw": "以 FX10 列印的 Bell 214B 機艙空調風管", "en": "Bell 214B cabin ducting printed on the FX10"},
              "tags": {"tw": "直升機工程與維修 ・ 澳洲", "en": "Helicopter engineering and MRO · Australia"},
              "title": {"tw": "Plane Support：直升機風管用 FX10 印，取得 CASA 核准",
                        "en": "Plane Support: helicopter ducting printed on the FX10, approved by CASA"},
              "body": {"tw": "Plane Support 以 FX10 為核心建立航太積層製造實驗室，用具批次追溯的阻燃材料 Onyx FR-A 印 Bell 214B 機艙空調風管，取得澳洲民航安全局（CASA）核准，可用積層製造生產這項零件。合作夥伴 McDermott Aviation 擁有全球最大的 214B 機隊，主要投入山林火災空中滅火。",
                       "en": "Plane Support built an aerospace additive lab around the FX10 and printed Bell 214B cabin air-conditioning ducting in Onyx FR-A, a flame-retardant material with lot-level traceability. The Civil Aviation Safety Authority (CASA) approved manufacturing the part this way. Partner McDermott Aviation operates the world's largest Bell 214B fleet, used mainly for aerial firefighting."},
              "metric": {"tw": "CASA 核准", "en": "CASA approved"}, "url": URL["plane"],
              "extra": {"tw": '<a href="casa-additive-airworthiness.html">本站專文：一截風管，換來亞太第一張民航增材製造核准&nbsp;→</a>',
                        "cn": '<a href="casa-additive-airworthiness-sc.html">本站专文：一截风管，换来亚太第一张民航增材制造批准&nbsp;→</a>',
                        "en": '<a href="casa-additive-airworthiness-en.html">Our full story: one duct, and Asia-Pacific\'s first civil aviation approval for additive manufacturing&nbsp;→</a>'}},
    "cms": {"img": f"images/{S}-case-cms.jpg", "machine": "x7", "material": "Onyx FR",
            "alt": {"tw": "公務機", "en": "A business jet"},
            "tags": {"tw": "私人與商務航空 ・ 美國", "en": "Private and business aviation · U.S."},
            "title": {"tw": "Cabin Management Solutions：公務機客艙改裝件，用阻燃 Onyx FR 印",
                      "en": "Cabin Management Solutions: business-jet cabin retrofits printed in flame-retardant Onyx FR"},
            "body": {"tw": "CMS 為私人與商務噴射機維修、升級與替換客艙管理和機上娛樂系統。2019 年成立後購入兩台 X7，以 UL 94 V-0 阻燃等級的 Onyx FR 印機上娛樂系統改裝件等最終使用零件，符合美國聯邦航空總署（FAA）要求。",
                     "cn": "CMS 为私人飞机与公务机维修、升级与替换客舱管理和机上娱乐系统。2019 年成立后购入两台 X7，以 UL 94 V-0 阻燃等级的 Onyx FR 打印机上娱乐系统改装件等最终使用零件，符合美国联邦航空管理局（FAA）要求。",
                     "en": "CMS maintains, upgrades and replaces cabin management and in-flight entertainment systems for private and business jets. Founded in 2019, it bought two X7 printers and prints end-use parts such as in-flight entertainment retrofits in Onyx FR, rated UL 94 V-0, meeting Federal Aviation Administration (FAA) requirements."},
            "metric": {"tw": "UL 94 V-0", "en": "UL 94 V-0"}, "url": URL["cms"]},
    "hangar": {"img": f"images/{S}-case-hangar.jpg", "machine": "ns",
               "alt": {"tw": "Hangar One 以複材列印的座艙控制台零件", "en": "Cockpit console parts printed in composites by Hangar One"},
               "tags": {"tw": "航電維修與安裝 ・ 美國", "en": "Avionics MRO and installation · U.S."},
               "title": {"tw": "Hangar One Avionics：以碳纖維複材取代鋁件，量測搬進列印過程",
                         "en": "Hangar One Avionics: carbon composites in place of aluminum, with inspection moved into the print"},
               "body": {"tw": "以碳纖維強化複材零件取代鋁件，為直升機減重；並用 Markforged 的 Blacksmith 檢測軟體在列印過程中自動量測。原本每件人工量測要 30 到 45 分鐘，導入後平均每件省下約 30 分鐘。",
                        "en": "Hangar One replaces aluminum parts with carbon-reinforced composites to take weight out of helicopters, and uses Markforged Blacksmith inspection software to measure parts while they print. Manual inspection used to take 30 to 45 minutes per part; it now saves about 30 minutes per part on average."},
               "metric": {"tw": "每件省約 30 分鐘", "en": "~30 min saved per part"}, "url": URL["hangar"]},
    "irwin": {"img": f"images/{S}-case-irwin.jpg", "machine": "platform", "defense": True,
              "alt": {"tw": "美國陸軍車隊", "en": "U.S. Army vehicles"},
              "tags": {"tw": "國家訓練中心 ・ 美國陸軍", "en": "National Training Center · U.S. Army"},
              "title": {"tw": "美國陸軍 Fort Irwin：停產的艙蓋塞，自己印回來",
                        "en": "U.S. Army, Fort Irwin: an out-of-production hatch plug, printed back into service"},
              "body": {"tw": "協助駕駛夜間觀察的艙蓋塞已停產，重新製作約需 10,000 美元、交期 3 個月。部隊改用 Markforged 以 Onyx 印一件 230 美元，另以 17-4PH 不鏽鋼印出金屬版 800 美元；單這一項應用就省下 244,000 美元。",
                       "en": "A hatch plug that helps drivers see at night was out of production; reproducing it would cost about $10,000 with a three-month lead time. The regiment printed one in Onyx for $230 and a 17-4PH stainless steel version for $800. This one application saved the regiment $244,000."},
              "metric": {"tw": "$10,000 → $230", "en": "$10,000 → $230"}, "url": URL["irwin"]},
    "cannon": {"img": f"images/{S}-case-cannon.jpg", "machine": "x7", "defense": True,
               "alt": {"tw": "美國空軍空中加油畫面", "en": "U.S. Air Force aerial refueling"},
               "tags": {"tw": "第 27 特種作戰支援中隊 ・ 美國空軍", "en": "27th Special Operations Support Squadron · U.S. Air Force"},
               "title": {"tw": "美國空軍 Cannon 基地：夜視鏡固定座，幾小時印好",
                         "en": "U.S. Air Force, Cannon AFB: night vision mounts printed in hours"},
               "body": {"tw": "夜視鏡固定座在訓練中容易撞壞，買一個 100 美元到數百美元、還要等好幾週。中隊用 X7 印替換件並加上適配多種頭盔的墊片，每件不到 5 美元、幾小時完成；負責人表示強度與市售鋁件相當。",
                        "en": "Night vision goggle mounts break in training, and a replacement costs $100 to several hundred dollars with weeks of shipping. The squadron printed replacements on its X7, with spacers for different helmets, for under $5 each in a few hours; the specialist in charge says they are as strong as the commercial aluminum mounts."},
               "metric": {"tw": "不到 $5", "en": "Under $5"}, "url": URL["cannon"]},
    "va": {"img": f"images/{S}-case-va.jpg", "machine": "platform", "defense": True,
           "alt": {"tw": "腕帶式握筆輔具", "en": "A wrist-strap stylus holder"},
           "tags": {"tw": "醫療輔具 ・ 美國退伍軍人事務部", "en": "Assistive technology · U.S. Department of Veterans Affairs"},
           "title": {"tw": "美國退伍軍人事務部：為握力不足的人，客製握筆輔具",
                     "en": "U.S. Department of Veterans Affairs: custom stylus holders for limited grip"},
           "body": {"tw": "中維吉尼亞醫療體系的輔具團隊與職能治療師合作，為抓握力不足的退伍軍人與現役軍人設計腕帶式握筆輔具，以 Smooth TPU 95A 彈性材料列印，讓使用者能穩穩握住筆或觸控筆。",
                    "en": "The Central Virginia assistive technology team works with occupational therapists to design a wrist-strap stylus holder for veterans and service members with limited grip, printed in flexible Smooth TPU 95A so they can hold a pen or stylus securely."},
           "metric": {"tw": "客製輔具", "en": "Custom aids"}, "url": URL["va"]},
}

CHAPTERS = [
    {"id": "ch-auto", "no": "01", "big": "Performance Critical.", "img": f"images/{S}-ch-auto.jpg",
     "h": {"tw": "汽車：性能關鍵", "en": "Automotive: Performance Critical"},
     "intro": {"tw": "產線不停，治具就不能先倒下。超跑改裝廠、整車組裝線、跨國傳動系統供應商，三家都把治具改成自己印。",
               "en": "When the line can't stop, the tooling can't fail. A supercar fabricator, a vehicle assembly plant and a global drivetrain supplier now print their own fixtures."},
     "video": {"src": f"video/{S}-automotive.mp4", "poster": f"images/{S}-auto-poster.jpg", "cap": "video_cap_auto"},
     "cases": ["grp", "subaru", "dana"], "cta_where": {"tw": "汽車", "cn": "汽车", "en": "Automotive"}},
    {"id": "ch-aero", "no": "02", "big": "Mission Critical.", "img": f"images/{S}-ch-aero.jpg",
     "h": {"tw": "航太：任務關鍵", "en": "Aerospace: Mission Critical"},
     "intro": {"tw": "飛上去之前，每一件都要過關。一家取得澳洲民航核准，一家符合美國 FAA 要求，一家把量測搬進列印過程。",
               "en": "Before it flies, every part has to pass. One shop earned CASA approval, one meets FAA requirements, and one moved inspection into the print itself."},
     "video": {"src": f"video/{S}-aerospace-defense.mp4", "poster": f"images/{S}-aero-poster.jpg", "cap": "video_cap_aero",
               "defense": True},
     "cases": ["plane", "cms", "hangar"], "cta_where": {"tw": "航太", "cn": "航空航天", "en": "Aerospace"}},
    {"id": "ch-def", "no": "03", "big": "Mission Critical.", "img": f"images/{S}-ch-defense.jpg", "defense": True,
     "h": {"tw": "國防：任務關鍵", "en": "Defense: Mission Critical"},
     "intro": {"tw": "補給線拉長時，做得出零件就是戰備。停產的艙蓋塞、訓練中撞壞的夜視鏡座、為握力不足的退伍軍人設計的握筆輔具，全都自己印出來。",
               "en": "When supply lines stretch, making parts is readiness. An out-of-production hatch plug, night vision mounts broken in training, grip aids for veterans: all printed in-house."},
     "cases": ["irwin", "cannon", "va"], "cta_where": {"tw": "國防", "en": "Defense"}},
]

CH_CTA = {"tw": "你的產線也有這種零件？寄圖檔給我們&nbsp;→", "en": "Have a part like this? Send us the file&nbsp;→"}

ONYX = {
    "img": f"images/{S}-onyxgf.jpg",
    "alt": {"tw": "Onyx GF 六色線材與綠色列印零件（Markforged 原廠圖片）", "en": "Onyx GF in six colors and a printed part (official Markforged images)"},
    "kicker": {"tw": "材料焦點", "en": "Material spotlight"},
    "h": {"tw": "Onyx GF：顏色就是管理", "en": "Onyx GF: color is the control system"},
    "intro": {"tw": "六色 Onyx GF 讓治具一眼看出屬於哪條線、哪個版本、哪個危險區；Subaru 印第安納廠的色碼治具就是用它印的。",
              "en": "Six colors show which line, which revision and which hazard zone a fixture belongs to. Subaru of Indiana's color-coded jigs are printed in it."},
    "facts": {"tw": "短切玻璃纖維強化尼龍 ・ 不導電 ・ 紅黃綠藍灰白六色 ・ 可加連續纖維強化 ・ 熱變形溫度 138 °C（1.8 MPa）",
              "en": "Chopped-glass-fiber nylon · Non-conductive · Red, yellow, green, blue, gray, white · Continuous fiber compatible · HDT 138 °C (1.8 MPa)"},
    "uses": [
        {"b": {"tw": "工安警示", "en": "Workplace safety"}, "s": {"tw": "危險機台旁的護罩與支架用醒目的紅、黃色列印", "en": "High-visibility red and yellow guards near hazardous machinery"}},
        {"b": {"tw": "產線區分", "en": "Line differentiation"}, "s": {"tw": "A 線、B 線的治具用顏色分開，不會拿錯", "en": "Tools for Line A and Line B separated by color"}},
        {"b": {"tw": "版本控管", "en": "Revision control"}, "s": {"tw": "改版就換一個顏色印，舊版治具一眼就能淘汰", "en": "New revision, new color: old fixtures are phased out at a glance"}},
        {"b": {"tw": "工具管理", "en": "Tool organization"}, "s": {"tw": "工具板上顏色對不上，就知道少了哪一件", "en": "A color mismatch on the shadow board shows what is missing"}},
    ],
}

PRODUCT = {
    "img": f"images/{S}-fx10.jpg",
    "alt": {"tw": "FX10（Markforged 原廠產品照）", "en": "FX10 (official Markforged product photo)"},
    "kicker": {"tw": "為什麼是 FX10", "en": "Why FX10"},
    "h": {"tw": "一台機器，兩種製程，<br>就在你的廠房。", "en": "One machine. Composites and metal.<br>On your floor."},
    "body": {"tw": "平時用連續碳纖維複材印治具與零件；換上 Metal Kit 金屬列印引擎，同一台印 316L、17-4PH 不鏽鋼與 H13 工具鋼，金屬件再經 Wash-1 清洗與 Sinter-2 燒結完成。列印頭上的雷射測微器邊印邊量，自動調平、自動換料，工程師與現場操作員都能上手。",
             "en": "Print continuous-fiber composite fixtures and parts every day; swap in the Metal Kit print engine and the same machine prints 316L and 17-4PH stainless steel and H13 tool steel, with metal parts finished in Wash-1 and Sinter-2. A printhead laser micrometer measures while it prints, with automatic leveling and material changeover that engineers and operators can both run."},
    "specs_h": {"tw": "FX10 主要規格", "en": "FX10 at a glance"},
    "specs": [
        ({"tw": "可列印空間", "en": "Build volume"}, {"tw": "375 × 300 × 300 mm（33.8 L）", "en": "375 × 300 × 300 mm (33.8 L)"}),
        ({"tw": "機台外形尺寸", "cn": "设备外形尺寸", "en": "Machine size"}, {"tw": "760 × 640 × 1200 mm", "en": "760 × 640 × 1200 mm"}),
        ({"tw": "腔體", "en": "Build chamber"}, {"tw": "加熱至 60 °C", "en": "Heated to 60 °C"}),
        ({"tw": "列印平台", "en": "Print bed"}, {"tw": "加熱、精密研磨鋁製真空平台，自動調平", "en": "Heated, precision-ground aluminum vacuum bed, auto leveling"}),
        ({"tw": "材料倉", "en": "Material storage"}, {"tw": "4 個 800 cc 料盤位，濕度控制，自動換料", "en": "4 × 800 cc spool bays, humidity controlled, automatic changeover"}),
        ({"tw": "電源", "en": "Power"}, {"tw": "單相，一般插座", "en": "Single phase, wall plug"}),
        ({"tw": "複合材料", "en": "Composite materials"}, {"tw": "Onyx、Onyx FR／FR-A、Onyx ESD、Onyx GF（六色），可加連續碳纖維強化", "en": "Onyx, Onyx FR / FR-A, Onyx ESD, Onyx GF (six colors), with continuous carbon fiber reinforcement"}),
        ({"tw": "金屬材料", "en": "Metal materials"}, {"tw": "加購 Metal Kit：316L、17-4PH 不鏽鋼，H13 工具鋼", "en": "With the Metal Kit: 316L, 17-4PH stainless steel; H13 tool steel"}),
    ],
    "bundle": {"tw": '同時要做複材與金屬零件？<a href="fx10-sinter2-bundle.html">看 FX10 Sinter-2 Bundle&nbsp;→</a>',
               "cn": '同时要做复合材料与金属零件？<a href="fx10-sinter2-bundle-sc.html">看 FX10 Sinter-2 Bundle&nbsp;→</a>',
               "en": 'Need both composite and metal parts? <a href="fx10-sinter2-bundle-en.html">See the FX10 Sinter-2 Bundle&nbsp;→</a>'},
}

STEPS = {
    "h": {"tw": "下一步怎麼走", "en": "What happens next"},
    "items": [
        {"b": {"tw": "寄零件圖檔", "en": "Send a part file"}, "s": {"tw": "附上產業、零件用途、預計材料與所在地區", "en": "With your industry, what the part does, the material and your location"}},
        {"b": {"tw": "測試列印", "en": "Test print"}, "s": {"tw": "我們依你的零件安排測試列印", "en": "We arrange a test print of your part"}},
        {"b": {"tw": "機台展示與報價", "en": "Demo and quote"}, "s": {"tw": "安排 FX10 機台展示，並提供報價", "en": "We set up an FX10 demonstration and quote it"}},
    ],
}

CTA = {
    "h": {"tw": "把最不能出錯的那一件，寄給我們。", "en": "Send us the part that can't fail."},
    "p": {"tw": "寄一個零件圖檔，我們可以安排測試列印與 FX10 機台展示，並提供報價。來信請附產業、零件用途、預計材料與所在地區（台灣、中國、香港、越南）。",
          "en": "Send us a part file and we can arrange a test print and a live FX10 demonstration, and quote it. Tell us your industry, what the part does, the material you have in mind, and where you are: Taiwan, China, Hong Kong or Vietnam."},
    "btn1": {"tw": "預約展示／索取報價", "cn": "预约演示／索取报价", "en": "Book a demo / Get a quote"},
    "btn2": {"tw": "寄零件圖檔", "cn": "发零件图档", "en": "Send a part file"},
    "ebook": {"tw": f'還在研究？<a href="{URL["ebook"]}">下載原廠汽車產業電子書（英文 PDF，20 頁）&nbsp;→</a>',
              "cn": f'还在研究？<a href="{URL["ebook"]}">下载原厂汽车行业电子书（英文 PDF，20 页）&nbsp;→</a>',
              "en": f'Still researching? <a href="{URL["ebook"]}">Download the automotive e-book (PDF, 20 pages)&nbsp;→</a>'},
    "win_label": {"tw": "你的窗口", "cn": "你的窗口", "en": "Your contact"},
    "win_name": {"tw": "陳中欣 Brian Chen", "cn": "陈中欣 Brian Chen", "en": "Brian Chen"},
    "win_title": {"tw": "Markforged 大中華區暨越南區總經理", "en": "Country Manager, Greater China and Vietnam, Markforged"},
    "win_desc": {"tw": "台灣、中國、香港、越南的 FX10 展示與報價，都可以直接找我。", "en": "For FX10 demos and quotes in Taiwan, China, Hong Kong and Vietnam, reach me directly."},
}

READ = {
    "h": {"tw": "延伸閱讀", "en": "Further reading"},
    "items": [
        {"href": {"tw": "casa-additive-airworthiness.html", "cn": "casa-additive-airworthiness-sc.html", "en": "casa-additive-airworthiness-en.html"},
         "t": {"tw": "一截風管，換來亞太第一張民航增材製造核准", "cn": "一截风管，换来亚太第一张民航增材制造批准",
               "en": "One duct, and Asia-Pacific's first civil aviation approval for additive manufacturing"},
         "s": {"tw": "Plane Support 案完整報導", "en": "The full Plane Support story"}},
        {"href": {"tw": "wescad-fx10-jigs-fixtures.html", "en": "wescad-fx10-jigs-fixtures-en.html"}, "no_cn": True,
         "t": {"tw": "參考治具比銑削便宜最多 75%：德國治具廠 WESCAD 導入 FX10",
               "en": "Reference fixtures up to 75% cheaper than milling: WESCAD runs its FX10 at full capacity"},
         "s": {"tw": "另一個 FX10 治具案例", "en": "Another FX10 fixture case"}},
        {"href": {"tw": "fx10-sinter2-bundle.html", "cn": "fx10-sinter2-bundle-sc.html", "en": "fx10-sinter2-bundle-en.html"},
         "t": {"tw": "一台機器，複合材與金屬都做得到：FX10 Sinter-2 Bundle", "cn": "一台机器，复合材料与金属都能做：FX10 Sinter-2 Bundle",
               "en": "One machine, composites and metal: the FX10 Sinter-2 Bundle"},
         "s": {"tw": "主機、金屬列印引擎、清洗站、燒結爐一套四件", "en": "Printer, metal print engine, wash station and furnace"}},
    ],
}

FTR = {
    "about": {"tw": "Markforged 提供工業級積層製造系統與連續纖維複合材料，應用於航太、國防、汽車與精密製造。本頁由 Markforged 大中華區媒體中心發布；案例、影片與照片來自 Markforged 原廠，數字取自原廠案例原文。",
              "cn": "Markforged 提供工业级增材制造系统与连续纤维复合材料，应用于航空航天、汽车与精密制造。本页由 Markforged 大中华区媒体中心发布；案例、视频与照片来自 Markforged 原厂，数字取自原厂案例原文。",
              "en": "Markforged builds industrial additive manufacturing systems and continuous fiber composites for aerospace, defense, automotive and precision manufacturing. Published by the Markforged Greater China Media Hub; cases, films and photos are from Markforged, and figures are taken from the original case studies."},
    "back": {"tw": "返回媒體中心", "cn": "返回媒体中心", "en": "Back to the Media Hub"},
}

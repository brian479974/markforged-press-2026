# -*- coding: utf-8 -*-
"""news.markforged.tw ── Markforged 委任壹科技為香港獨家代理（2026-09-24 發布會活動報導）

內容來源：2026-09-24 發布會現場錄音逐字稿（1:52:00 · 424 段全讀）＋ 現場攝影。
繁中版用語：**台灣專業用語**（積層製造／列印／夾治具／智慧製造）——Brian 2026-09-24 指示。
簡中版用大陸用語（增材製造／打印），英文版 additive manufacturing。

⚠️ 刻意不寫進本文的（有出處但不採用）：
  · Stratasys 併購 —— 母公司股權事項，未經核可不入對外稿
  · 「逾三萬客戶／三十萬台」—— 與可查證口徑量級不符
  · 「150 瓦」—— 現場同一數字先後指向兩款機型，來源互斥
  · 衛星「全球首台」宣稱 —— 未取得書面查證
  · X7 Field Edition 國防應用 · Metal X／PX100（EOL／EOS）
"""
LANGS = ("tw", "cn", "en")

META = {
    "lang_attr": {"tw": "zh-TW", "cn": "zh-CN", "en": "en"},
    "file": {"tw": "unotech-hk-launch.html",
             "cn": "unotech-hk-launch-sc.html",
             "en": "unotech-hk-launch-en.html"},
    "hero": "images/unotech-hk-launch-principals.jpg",
    "og_image": "https://news.markforged.tw/images/unotech-hk-launch-principals.jpg",
    "title": {
        "tw": "Markforged 委任壹科技為香港獨家代理：發布會現場示範連續纖維增強技術 — Markforged",
        "cn": "Markforged 委任壹科技为香港独家代理：发布会现场演示连续纤维增强技术 — Markforged",
        "en": "Markforged Appoints Unotech as Exclusive Hong Kong Distributor — Markforged",
    },
    "desc": {
        "tw": "Markforged 於香港生產力促進局舉行發布會，委任壹科技有限公司為香港獨家代理。"
              "現場示範連續纖維增強技術，並公布材料數據：連續碳纖維零件抗拉強度達 800 MPa。"
              "香港理工大學分享紅點設計獎得獎的一體成型自行車座墊案例。",
        "cn": "Markforged 于香港生产力促进局举行发布会，委任壹科技有限公司为香港独家代理。"
              "现场演示连续纤维增强技术，并公布材料数据：连续碳纤维零件抗拉强度达 800 MPa。"
              "香港理工大学分享红点设计奖获奖的一体成型自行车座垫案例。",
        "en": "Markforged has appointed Unotech Limited as its exclusive distributor in Hong Kong, "
              "announced at a launch event at HKPC. The programme included a live demonstration of "
              "Continuous Fiber Reinforcement and a Red Dot-winning saddle developed at PolyU.",
    },
    "og_title": {
        "tw": "Markforged 委任壹科技為香港獨家代理",
        "cn": "Markforged 委任壹科技为香港独家代理",
        "en": "Markforged Appoints Unotech as Exclusive Hong Kong Distributor",
    },
    "og_desc": {
        "tw": "連續碳纖維零件抗拉強度 800 MPa，拉力測試到 22,200 磅才斷裂。",
        "cn": "连续碳纤维零件抗拉强度 800 MPa，拉力测试到 22,200 磅才断裂。",
        "en": "Continuous carbon fiber parts reach 800 MPa tensile strength, breaking at 22,200 lbf.",
    },
}

UI = {
    "hdr_ev": {"tw": "大中華區媒體中心<br>News &amp; Insights",
               "cn": "大中华区媒体中心<br>News &amp; Insights",
               "en": "Greater China Media Hub<br>News &amp; Insights"},
    "switch_label": {"tw": "語言", "cn": "语言", "en": "Language"},
    "hero_alt": {
        "tw": "Markforged 與壹科技管理層於發布會現場的 FX10 系統前合影",
        "cn": "Markforged 与壹科技管理层于发布会现场的 FX10 系统前合影",
        "en": "Markforged and Unotech leadership at the launch event, beside an FX10 system"},
    "hero_kicker": {"tw": "夥伴發布 · 香港", "cn": "伙伴发布 · 香港",
                    "en": "Partner Announcement · Hong Kong"},
    "hero_title": {
        "tw": "Markforged 委任壹科技為香港獨家代理",
        "cn": "Markforged 委任壹科技为香港独家代理",
        "en": "Markforged Appoints Unotech as Exclusive Hong Kong Distributor"},
    "hero_meta": {
        "tw": "Markforged × 壹科技 Unotech ｜ 香港生產力促進局 ｜ 2026.09.24",
        "cn": "Markforged × 壹科技 Unotech ｜ 香港生产力促进局 ｜ 2026.09.24",
        "en": "Markforged x Unotech | HKPC, Hong Kong | 2026.09.24"},
    "ds_l": {"tw": "連續碳纖維零件抗拉強度 800 MPa",
             "cn": "连续碳纤维零件抗拉强度 800 MPa",
             "en": "800 MPa tensile strength with continuous carbon fiber"},
    "ds_r": {"tw": "現場示範 FX10 實機列印與 Eiger 雲端平台",
             "cn": "现场演示 FX10 实机打印与 Eiger 云端平台",
             "en": "Live FX10 print and Eiger cloud platform demonstration"},
}

LEAD = {
    # 2026-09-24 Brian 親糾：原開場「香港的製造業版圖往北移…」是我自己想的評論式引言，
    # 沒有出處、也不是新聞導語。改為壹科技官方定稿新聞稿的導語結構（人事時地＋議程）。
    "p1": {
        "tw": "<strong>【香港，2026 年 9 月 24 日】</strong>工業級積層製造企業 Markforged 今日宣布，"
              "正式委任<strong>壹科技有限公司（Unotech Limited）</strong>為其香港獨家代理商，"
              "由壹科技全面承接 Markforged 工業級 3D 列印產品在香港的銷售、技術支援與應用開發服務。"
              "委任發布會同日於香港生產力促進局（HKPC）Inno Network 舉行，"
              "由雙方管理層主持開幕及剪綵儀式，並設技術簡報、實機示範、用家案例分享與問答環節。",
        "cn": "<strong>【香港，2026 年 9 月 24 日】</strong>工业级增材制造企业 Markforged 今日宣布，"
              "正式委任<strong>壹科技有限公司（Unotech Limited）</strong>为其香港独家代理商，"
              "由壹科技全面承接 Markforged 工业级 3D 打印产品在香港的销售、技术支持与应用开发服务。"
              "委任发布会同日于香港生产力促进局（HKPC）Inno Network 举行，"
              "由双方管理层主持开幕及剪彩仪式，并设技术简报、实机演示、用户案例分享与问答环节。",
        "en": "<strong>HONG KONG, 24 September 2026</strong> — Markforged, the industrial additive "
              "manufacturing company, today appointed <strong>Unotech Limited</strong> as its "
              "exclusive distributor in Hong Kong. Unotech takes on sales, technical support and "
              "application development for Markforged's industrial 3D printing products across the "
              "territory. The appointment was announced at a launch event held the same day at HKPC "
              "Inno Network, opened with a ribbon-cutting by both companies' management and followed "
              "by a technical briefing, a live machine demonstration, a customer case study and Q&amp;A.",
    },
}


QUOTE = {
    # 出處：壹科技官方定稿新聞稿（Unotech官方新聞稿_繁中_2026-09-24.docx），Brian 具名引言首句。
    "text": {
        "tw": "「香港作為大灣區的科技與貿易樞紐，客戶結構橫跨多個高端製造領域。"
              "我們選擇壹科技作為獨家合作夥伴，正是看中其深厚的本地技術能量與優異的售後服務覆蓋範圍。」",
        "cn": "“香港作为大湾区的科技与贸易枢纽，客户结构横跨多个高端制造领域。"
              "我们选择壹科技作为独家合作伙伴，正是看中其深厚的本地技术能量与优异的售后服务覆盖范围。”",
        "en": "“Hong Kong is a technology and trading hub for the Greater Bay Area, with a customer "
              "base spanning multiple high-end manufacturing sectors. We chose Unotech as our "
              "exclusive partner for its depth of local technical capability and the strength of "
              "its after-sales coverage.”",
    },
    "attr": {
        "tw": "陳中欣 ｜ Markforged 大中華區暨越南區總經理",
        "cn": "陈中欣 ｜ Markforged 大中华区暨越南区总经理",
        "en": "Brian Chen | Country Manager, Greater China and Vietnam, Markforged",
    },
}


PROF = None   # 活動報導不掛作者卡（Brian 是消息來源）；具名觀點文才掛


TAGS = [
    {"tw": "香港", "cn": "香港", "en": "Hong Kong", "solid": True},
    {"tw": "連續纖維增強", "cn": "连续纤维增强", "en": "Continuous Fiber Reinforcement", "solid": True},
    {"tw": "獨家代理", "cn": "独家代理", "en": "Exclusive Distributor", "solid": False},
    {"tw": "FX10", "cn": "FX10", "en": "FX10", "solid": False},
    {"tw": "航空維修", "cn": "航空维修", "en": "MRO", "solid": False},
]

BLOCKS = [
    {
        "kind": "sec",
        "h2": {"tw": "連續纖維增強",
               "cn": "连续纤维增强",
               "en": "Continuous Fiber Reinforcement"},
        "h3": {"tw": "連續纖維，不是短切纖維", "cn": "连续纤维，不是短切纤维",
               "en": "Continuous fiber, not chopped fiber"},
        "paras": [
            {"tw": "發布會技術環節聚焦 Markforged 的連續纖維增強（Continuous Fiber Reinforcement，CFR）技術。"
                   "它在列印過程中把連續的碳纖維、Kevlar 或高強度高溫玻璃纖維鋪放到零件內部，"
                   "讓成品的強度與剛性接近金屬加工件，可以直接用在夾治具、機械手夾爪、產線輔具"
                   "與功能性終端零件上。",
             "cn": "发布会技术环节聚焦 Markforged 的连续纤维增强（Continuous Fiber Reinforcement，CFR）技术。"
                   "它在打印过程中把连续的碳纤维、Kevlar 或高强度高温玻璃纤维铺放到零件内部，"
                   "让成品的强度与刚性接近金属加工件，可以直接用在夹治具、机械手夹爪、产线辅具"
                   "与功能性终端零件上。",
             "en": "The technical session centred on Continuous Fiber Reinforcement (CFR). During "
                   "the build, continuous strands of carbon fiber, Kevlar or high-strength "
                   "high-temperature glass fiber are laid inside the part, bringing strength and "
                   "stiffness close to machined metal. Parts go straight into fixtures, robotic "
                   "grippers, line tooling and functional end-use applications."},
            {"tw": "會上引述的材料數據顯示，基礎材料 Onyx 配合連續碳纖維增強後，抗拉強度可達 800 MPa；"
                   "作為對照，常用於結構件的鋁合金 6061-T6 為 308 MPa，一般 ABS 塑料約 30 MPa。"
                   "現場並播放原廠拉力測試影片，一件連續纖維增強零件拉到 22,200 磅才斷裂 —— 約 10 公噸。",
             "cn": "会上引述的材料数据显示，基础材料 Onyx 配合连续碳纤维增强后，抗拉强度可达 800 MPa；"
                   "作为对照，常用于结构件的铝合金 6061-T6 为 308 MPa，一般 ABS 塑料约 30 MPa。"
                   "现场并播放原厂拉力测试视频，一件连续纤维增强零件拉到 22,200 磅才断裂 —— 约 10 公吨。",
             "en": "Material figures cited at the event: Onyx reinforced with continuous carbon "
                   "fiber reaches 800 MPa tensile strength. For comparison, 6061-T6 aluminium, a "
                   "common structural alloy, is 308 MPa, and general-purpose ABS around 30 MPa. A "
                   "tensile test film shown on the day recorded a reinforced part breaking at "
                   "22,200 lbf — roughly 10 tonnes."},
        ],
        "hl": [
            {"b": {"tw": "800 MPa", "cn": "800 MPa", "en": "800 MPa"},
             "s": {"tw": "Onyx ＋ 連續碳纖維　抗拉強度",
                   "cn": "Onyx ＋ 连续碳纤维　抗拉强度",
                   "en": "Onyx with continuous carbon fiber, tensile"}},
            {"b": {"tw": "308 MPa", "cn": "308 MPa", "en": "308 MPa"},
             "s": {"tw": "鋁合金 6061-T6　抗拉強度",
                   "cn": "铝合金 6061-T6　抗拉强度",
                   "en": "6061-T6 aluminium, tensile"}},
            {"b": {"tw": "22,200 磅", "cn": "22,200 磅", "en": "22,200 lbf"},
             "s": {"tw": "拉力測試斷裂值（約 10 公噸）",
                   "cn": "拉力测试断裂值（约 10 公吨）",
                   "en": "Tensile test at failure (about 10 tonnes)"}},
        ],
        "paras_after": [
            {"tw": "複合材料之外，Markforged 的金屬積層製造方案採用列印、清洗、燒結三階段流程："
                   "先以金屬粉與黏結劑製成的線材列印出生胚，用溶劑清洗去除第一階段黏結材料，"
                   "再送進燒結爐完成緻密化。與使用鬆散金屬粉的金屬 3D 列印製程不同，"
                   "這條流程全程不需要處理鬆散金屬粉。零件與支撐之間會自動列印一層陶瓷離型材料，"
                   "燒結後呈粉狀，便於分離、也有助於控制收縮與尺寸精度；"
                   "收縮率由雲端軟體依所選材料自動補償，不需要使用者自行放大模型或試誤。",
             "cn": "复合材料之外，Markforged 的金属增材制造方案采用打印、清洗、烧结三阶段流程："
                   "先以金属粉与黏结剂制成的线材打印出生坯，用溶剂清洗去除第一阶段黏结材料，"
                   "再送进烧结炉完成致密化。与使用松散金属粉的金属 3D 打印制程不同，"
                   "这条流程全程不需要处理松散金属粉。零件与支撑之间会自动打印一层陶瓷离型材料，"
                   "烧结后呈粉状，便于分离、也有助于控制收缩与尺寸精度；"
                   "收缩率由云端软件依所选材料自动补偿，不需要使用者自行放大模型或试错。",
             "en": "Beyond composites, Markforged's metal additive process runs in three stages: print, wash, sinter. A filament of metal powder and binder is printed into a green part, solvent washing removes the first-stage binder, and a furnace densifies the part. Unlike metal 3D printing systems that rely on loose powder, this route never requires handling loose metal powder. A ceramic release layer is printed automatically between the part and its supports; after sintering it remains powdered, which makes separation easy and helps control shrinkage and dimensional accuracy. Shrinkage is compensated automatically by the cloud software according to the selected material, so users do not scale models by hand or work it out by trial and error."},
        ],
    },
    {
        # Brian 2026-09-24 21:07 補傳：技術簡報環節全場照 —— 比擺拍大合照更能交代活動規模。
        "kind": "img_full",
        "img": "images/unotech-hk-launch-briefing-room.jpg",
        "alt": {"tw": "發布會技術簡報環節，台上為 Markforged 大中華區暨越南區總經理陳中欣",
                "cn": "发布会技术简报环节，台上为 Markforged 大中华区暨越南区总经理陈中欣",
                "en": "The technical briefing, with Markforged's Country Manager for Greater China "
                      "and Vietnam, Brian Chen, presenting"},
        "cap": {"tw": "技術簡報環節，業界、學研及傳媒代表出席。",
                "cn": "技术简报环节，业界、学研及传媒代表出席。",
                "en": "The technical briefing, attended by industry, academic and media representatives."},
    },
    {
        # 2026-09-24 Brian：「這一張跟打開的一張合在一起不就好了」——揭幕前／揭幕後對照。
        # 兩張都是直式，用 3:4 配對；直式硬套 4:3 會把蝴蝶結與機台頂部切掉。
        "kind": "img_2col",
        "ratio": "34",
        "imgs": ["images/unotech-hk-launch-ribbon.jpg",
                 "images/unotech-hk-launch-fx10-printing.jpg"],
        "alts": [
            {"tw": "剪綵揭幕前，FX10 系統以紅絨布覆蓋置於會場中央",
             "cn": "剪彩揭幕前，FX10 系统以红绒布覆盖置于会场中央",
             "en": "Before the unveiling: the FX10 under a red drape at the centre of the room"},
            {"tw": "揭幕後的 FX10 系統，機殼開啟可見列印床與龍門",
             "cn": "揭幕后的 FX10 系统，机壳开启可见打印床与龙门",
             "en": "After the unveiling: the FX10 with its hood open, print bed and gantry visible"},
        ],
        "cap": {"tw": "揭幕前後的 FX10。壹科技的系統工程師於會上示範實機操作，"
                      "以 Onyx 材料當場列印加入與未加入連續碳纖維的兩件樣品供與會者比較。",
                "cn": "揭幕前后的 FX10。壹科技的系统工程师于会上演示实机操作，"
                      "以 Onyx 材料当场打印加入与未加入连续碳纤维的两件样品供与会者比较。",
                "en": "The FX10 before and after the unveiling. Unotech's systems engineers ran a "
                      "live print during the event, producing two Onyx samples for comparison — "
                      "one with continuous carbon fiber, one without."},
    },
    {
        "kind": "sec",
        "h2": {"tw": "實機示範",
               "cn": "实机演示",
               "en": "Live demonstration"},
        "h3": {"tw": "工程師拿得到數字去做判斷，不是拿一句「很結實」去說服人",
               "cn": "工程师拿得到数字去做判断，不是拿一句“很结实”去说服人",
               "en": "Engineers decide on numbers, not on being told a part is strong"},
        "paras": [
            {"tw": "壹科技的系統工程師在會上示範 FX10 的實際操作，用 Onyx 材料當場列印兩件樣品 —— "
                   "一件加入連續碳纖維增強、一件不加，讓與會者直接比較。",
             "cn": "壹科技的系统工程师在会上演示 FX10 的实际操作，用 Onyx 材料当场打印两件样品 —— "
                   "一件加入连续碳纤维增强、一件不加，让与会者直接比较。",
             "en": "Unotech's system engineers demonstrated the FX10 live, printing two samples in "
                   "Onyx — one reinforced with continuous carbon fiber, one without — so the "
                   "audience could compare them directly."},
            {"tw": "同場演示 Eiger 雲端切片與列印管理平台：上傳 STL 檔後，平台會即時顯示零件尺寸、"
                   "預估列印時間、成品重量、材料用量與成本，使用者可以調整層厚、填充密度與纖維鋪放位置，"
                   "並逐層預覽切片結果。Eiger 另有離線版本，供未接入網路的生產環境使用。"
                   "這一點在問答環節被追問到投資回報怎麼估算時再次被提出 —— "
                   "成本試算不必另外做表，上傳檔案時系統就算好了。",
             "cn": "同场演示 Eiger 云端切片与打印管理平台：上传 STL 文件后，平台会即时显示零件尺寸、"
                   "预估打印时间、成品重量、材料用量与成本，使用者可以调整层厚、填充密度与纤维铺放位置，"
                   "并逐层预览切片结果。Eiger 另有离线版本，供未接入网络的生产环境使用。"
                   "这一点在问答环节被追问到投资回报怎么估算时再次被提出 —— "
                   "成本试算不必另外做表，上传文件时系统就算好了。",
             "en": "The same session covered Eiger, the cloud slicing and print management platform. "
                   "Once an STL is uploaded, Eiger reports part dimensions, estimated print time, "
                   "finished weight, material consumption and cost. Users adjust layer height, "
                   "infill and fiber routing, and preview the slice layer by layer. An offline "
                   "version is available for production environments without network access. The "
                   "point returned during Q&amp;A, when an attendee asked how to estimate return on "
                   "investment: the costing is produced at upload, not in a separate spreadsheet."},
        ],
    },
    {
        "kind": "sec",
        "h2": {"tw": "用家案例 · 香港理工大學",
               "cn": "用户案例 · 香港理工大学",
               "en": "Customer case: PolyU"},
        "h3": {"tw": "一體成型的座墊：舒適度未必是第一優先，安全才是",
               "cn": "一体成型的座垫：舒适度未必是第一优先，安全才是",
               "en": "A saddle printed in one piece: comfort is not the first priority, safety is"},
        "paras": [
            {"tw": "發布會邀請香港理工大學時裝及紡織學院的研究團隊，分享以 Markforged 連續纖維技術"
                   "開發自行車座墊的過程。該座墊於 2024 年獲德國紅點設計獎（Design Concept 組別）認可，"
                   "並已取得發明專利。",
             "cn": "发布会邀请香港理工大学时装及纺织学院的研究团队，分享以 Markforged 连续纤维技术"
                   "开发自行车座垫的过程。该座垫于 2024 年获德国红点设计奖（Design Concept 组别）认可，"
                   "并已取得发明专利。",
             "en": "A research team from PolyU's School of Fashion and Textiles presented a bicycle "
                   "saddle developed with Markforged continuous fiber technology. The design was "
                   "recognised with a Red Dot Award (Design Concept) in 2024 and holds an "
                   "invention patent."},
            {"tw": "構想源自紡織業的間隔織物（spacer fabric，俗稱三明治網布）結構 —— "
                   "這種夾層織物受壓時緩衝、放開後回彈，常見於運動鞋鞋面。"
                   "團隊把這個概念轉化成座墊內部的 S 形緩衝結構，再以連續碳纖維提供支撐強度，"
                   "讓整張座墊可以一體成型列印，不必像市售產品那樣組裝金屬支架與多種材料。"
                   "座墊表面採 C 形孔洞設計改善透氣，成品重量約 190 餘公克。",
             "cn": "构想源自纺织业的间隔织物（spacer fabric，俗称三明治网布）结构 —— "
                   "这种夹层织物受压时缓冲、放开后回弹，常见于运动鞋鞋面。"
                   "团队把这个概念转化成座垫内部的 S 形缓冲结构，再以连续碳纤维提供支撑强度，"
                   "让整张座垫可以一体成型打印，不必像市售产品那样组装金属支架与多种材料。"
                   "座垫表面采 C 形孔洞设计改善透气，成品重量约 190 余克。",
             "en": "The concept came from spacer fabric, the sandwich-structured textile used in "
                   "athletic shoe uppers, which compresses under load and springs back when "
                   "released. The team translated it into an S-shaped cushioning structure inside "
                   "the saddle, with continuous carbon fiber carrying the structural load. That "
                   "allowed the whole saddle to be printed in one piece, without the metal rails "
                   "and multi-material assembly of a commercial product. C-shaped perforations on "
                   "the surface improve ventilation. The finished saddle weighs about 190 grams."},
        ],
        "hl": [
            {"b": {"tw": "190 公克", "cn": "190 克", "en": "190 g"},
             "s": {"tw": "一體成型座墊成品重量", "cn": "一体成型座垫成品重量",
                   "en": "Finished one-piece saddle"}},
            {"b": {"tw": "250 公斤 × 10 次", "cn": "250 公斤 × 10 次", "en": "250 kg x 10"},
             "s": {"tw": "人工臀部模具壓力測試，每次停留 10 秒",
                   "cn": "人工臀部模具压力测试，每次停留 10 秒",
                   "en": "Compression test with an artificial buttock form, 10 s per cycle"}},
            {"b": {"tw": "逾 1,500 公里", "cn": "逾 1,500 公里", "en": "1,500 km+"},
             "s": {"tw": "真人實測近兩年，座墊未見破損",
                   "cn": "真人实测近两年，座垫未见破损",
                   "en": "Nearly two years of rider testing, no failure"}},
        ],
        "paras_after": [
            {"tw": "驗證方面，團隊以碳纖維骨架外覆矽膠製作人工臀部模具，施加 250 公斤載荷重複下壓十次、"
                   "每次停留十秒，座墊卸載後回復原狀；另由團隊成員進行真人長期實測，"
                   "近兩年累計騎乘里程逾 1,500 公里，座墊未見破損。"
                   "項目由該校五人團隊主導，跨院系與工業中心及 3D 列印研究設施（U3DP）合作完成。",
             "cn": "验证方面，团队以碳纤维骨架外覆硅胶制作人工臀部模具，施加 250 公斤载荷重复下压十次、"
                   "每次停留十秒，座垫卸载后回复原状；另由团队成员进行真人长期实测，"
                   "近两年累计骑乘里程逾 1,500 公里，座垫未见破损。"
                   "项目由该校五人团队主导，跨院系与工业中心及 3D 打印研究设施（U3DP）合作完成。",
             "en": "For validation the team built an artificial buttock form with a carbon fiber "
                   "skeleton under a silicone skin, applying a 250 kg load ten times with a "
                   "ten-second hold; the saddle returned to shape after unloading. A team member "
                   "also ran long-term rider testing, accumulating more than 1,500 km over nearly "
                   "two years without failure. The five-person team worked across faculties with "
                   "the university's Industrial Centre and its 3D printing research facility "
                   "(U3DP)."},
            {"tw": "團隊代表在會上指出，就自行車座墊而言，舒適度未必是第一優先，安全才是 —— "
                   "這正是選用連續碳纖維的原因：既提供支撐強度，也讓成品維持輕量。",
             "cn": "团队代表在会上指出，就自行车座垫而言，舒适度未必是第一优先，安全才是 —— "
                   "这正是选用连续碳纤维的原因：既提供支撑强度，也让成品维持轻量。",
             "en": "As the team put it, comfort is not necessarily the first priority for a bicycle "
                   "saddle — safety is. That is exactly why continuous carbon fiber was chosen: it "
                   "carries the structural load while keeping the part light."},
        ],
    },
    {
        "kind": "img_full",
        "img": "images/unotech-hk-launch-group.jpg",
        "alt": {"tw": "發布會與會者合影", "cn": "发布会与会者合影",
                "en": "Attendees at the launch event"},
        "cap": {"tw": "發布會設交流環節，業界、學研及傳媒代表出席。",
                "cn": "发布会设交流环节，业界、学研及传媒代表出席。",
                "en": "The event closed with a networking session attended by industry, academic "
                      "and media representatives."},
    },
    {
        "kind": "sec",
        "h2": {"tw": "市場背景",
               "cn": "市场背景",
               "en": "Market context"},
        "h3": {"tw": "訂單來了，卡住的不是機器，是等外發的那一批零件",
               "cn": "订单来了，卡住的不是机器，是等外发的那一批零件",
               "en": "When the orders arrive, the bottleneck is not the machines \u2014 it is the parts out for subcontract"},
        "paras": [
            {"tw": "本地製造與工程單位近年同時面對交期壓縮、以及小批量多規格訂單比重上升兩項壓力，"
                   "其中受影響最直接的是工裝 —— 夾具、治具、檢具與自動化夾爪。"
                   "這類零件多為單件或極小批量，規格隨產品改版而變動。會上指出，CNC 外發加工的交期通常以週計算，開模則以月計算，任何修改都要從頭再來一次。",
             "cn": "本地制造与工程单位近年同时面对交期压缩、以及小批量多规格订单比重上升两项压力，"
                   "其中受影响最直接的是工装 —— 夹具、治具、检具与自动化夹爪。"
                   "这类零件多为单件或极小批量，规格随产品改版而变动。会上指出，CNC 外发加工的交期通常以周计算，开模则以月计算，任何修改都要从头再来一次。",
             "en": "Local manufacturers and engineering units face two pressures at once: "
                   "compressed lead times, and a rising share of small-batch, multi-specification "
                   "orders. Tooling takes the brunt — fixtures, jigs, gauges and robotic grippers. "
                   "These are usually one-offs or very small batches whose specifications change "
                   "with each product revision, and outsourced machining is quoted in weeks."},
            {"tw": "積層製造的作用在於把這一段產能移回廠內：設計改完就重新列印，"
                   "不必重新開模或排隊等外發加工；零件也可以用數位檔案形式保存，按需列印，"
                   "取代實體備件庫存。對廠房面積有限、人力成本偏高、交期要求緊湊的香港製造環境，"
                   "這個差異相對明顯。",
             "cn": "增材制造的作用在于把这一段产能移回厂内：设计改完就重新打印，"
                   "不必重新开模或排队等外发加工；零件也可以用数字文件形式保存，按需打印，"
                   "取代实体备件库存。对厂房面积有限、人力成本偏高、交期要求紧凑的香港制造环境，"
                   "这个差异相对明显。",
             "en": "Additive manufacturing moves that segment back inside the plant: revise the "
                   "design and print again, with no new tooling and no queue at an outside shop. "
                   "Parts can also be held as digital files and printed on demand, replacing "
                   "physical spares inventory. For Hong Kong — limited floor space, high labour "
                   "cost, tight delivery requirements — the difference is pronounced."},
            {"tw": "壹科技表示已投入示範設備並完成人員訓練，"
                   "重點行業鎖定航空維修、電子製造、醫療器材與精密工程。"
                   "會上說明的導入方式是：客戶挑出交期最長、成本最高的零件，簽署保密協議後交由壹科技評估，"
                   "把零件數位化並列印出實體件，直接上線驗證是否符合需求。",
             "cn": "壹科技表示已投入示范设备并完成人员培训，"
                   "重点行业锁定航空维修、电子制造、医疗器材与精密工程。"
                   "会上说明的导入方式是：客户挑出交期最长、成本最高的零件，签署保密协议后交由壹科技评估，"
                   "把零件数字化并打印出实体件，直接上线验证是否符合需求。",
             "en": "Unotech has already installed demonstration equipment and completed staff "
                   "training, targeting aviation MRO, electronics manufacturing, medical devices "
                   "and precision engineering. The adoption path set out at the event: the customer "
                   "identifies the part with the longest lead time and highest cost, signs an NDA, "
                   "and hands it to Unotech for assessment. The part is digitised, printed, and "
                   "validated in the customer's own line."},
        ],
    },
    # ── 以下五塊為通訊社／企業正式新聞稿標準件，內容全數取自 2026-09-24 活動報導稿 v1 ──
    {
        # 引言逐字取自壹科技官方定稿新聞稿（Unotech官方新聞稿_繁中_2026-09-24.docx）。
        # 引號內一字未改 —— 官方已核可的具名引言，不做改寫、不做用語在地化。
        "kind": "quotes",
        "items": [
            {
                "img": "images/unotech-hk-launch-ivan-speaking.jpg",
                "alt": {"tw": "壹科技有限公司銷售總監 Ivan Siu 於發布會發言",
                        "cn": "壹科技有限公司销售总监 Ivan Siu 于发布会发言",
                        "en": "Ivan Siu, Sales Director of Unotech Limited, speaking at the event"},
                "text": {
                    "tw": "「我們非常榮幸能與工業 3D 打印領先品牌 Markforged 建立獨家合作關係。"
                          "憑藉 Markforged 在增材製造領域的技術優勢，我們有信心為香港市場帶來"
                          "更具成本效益、可靠且創新的製造選擇。壹科技的本地技術團隊將主攻航空維修、"
                          "電子製造、醫療器材與精密工程等重點行業，這與連續纖維技術對強度與即時交付"
                          "的高要求完美契合。我們將持續強化本地技術能量，全力支援香港智能製造市場的"
                          "長遠發展。」",
                    "cn": "“我们非常荣幸能与工业 3D 打印领先品牌 Markforged 建立独家合作关系。"
                          "凭借 Markforged 在增材制造领域的技术优势，我们有信心为香港市场带来"
                          "更具成本效益、可靠且创新的制造选择。壹科技的本地技术团队将主攻航空维修、"
                          "电子制造、医疗器材与精密工程等重点行业，这与连续纤维技术对强度与即时交付"
                          "的高要求完美契合。我们将持续强化本地技术能量，全力支援香港智能制造市场的"
                          "长远发展。”",
                    "en": "“We are honoured to enter an exclusive partnership with Markforged, a "
                          "leading brand in industrial 3D printing. With Markforged's technical "
                          "strengths in additive manufacturing, we are confident we can bring Hong "
                          "Kong more cost-effective, reliable and innovative manufacturing options. "
                          "Our local technical team will focus on aviation MRO, electronics "
                          "manufacturing, medical devices and precision engineering — sectors whose "
                          "demands on strength and turnaround align closely with continuous fiber "
                          "technology. We will keep building local technical capability to support "
                          "the long-term development of smart manufacturing in Hong Kong.”",
                },
                "name": {"tw": "Ivan Siu", "cn": "Ivan Siu", "en": "Ivan Siu"},
                "title": {"tw": "壹科技有限公司　銷售總監",
                          "cn": "壹科技有限公司　销售总监",
                          "en": "Sales Director, Unotech Limited"},
            },
            {
                "img": "images/unotech-hk-launch-brian-speaking.jpg",
                "alt": {"tw": "Markforged 大中華區暨越南區總經理陳中欣於發布會發言",
                        "cn": "Markforged 大中华区暨越南区总经理陈中欣于发布会发言",
                        "en": "Brian Chen, Country Manager for Greater China and Vietnam, speaking"},
                "text": {
                    "tw": "「香港作為大灣區的科技與貿易樞紐，客戶結構橫跨多個高端製造領域。"
                          "我們選擇壹科技作為獨家合作夥伴，正是看中其深厚的本地技術能量與優異的"
                          "售後服務覆蓋範圍。獨家代理將使責任更為集中，客戶只需對接單一窗口，"
                          "便能獲得全方位的專業保障。Markforged 在大中華區累積的豐富應用案例與"
                          "材料驗證資料，亦將直接賦能香港團隊，共同協助本地醫療機構、航空與"
                          "精密工程客戶提升運作效率。」",
                    "cn": "“香港作为大湾区的科技与贸易枢纽，客户结构横跨多个高端制造领域。"
                          "我们选择壹科技作为独家合作伙伴，正是看中其深厚的本地技术能量与优异的"
                          "售后服务覆盖范围。独家代理将使责任更为集中，客户只需对接单一窗口，"
                          "便能获得全方位的专业保障。Markforged 在大中华区累积的丰富应用案例与"
                          "材料验证资料，亦将直接赋能香港团队，共同协助本地医疗机构、航空与"
                          "精密工程客户提升运作效率。”",
                    "en": "“Hong Kong is a technology and trading hub for the Greater Bay Area, with "
                          "a customer base spanning multiple high-end manufacturing sectors. We chose "
                          "Unotech as our exclusive partner for its depth of local technical "
                          "capability and the strength of its after-sales coverage. An exclusive "
                          "distributorship concentrates accountability: customers deal with a single "
                          "point of contact and get end-to-end professional cover. The application "
                          "cases and material validation data Markforged has built up across Greater "
                          "China will feed directly into the Hong Kong team, helping local medical, "
                          "aviation and precision engineering customers raise operating efficiency.”",
                },
                "name": {"tw": "陳中欣 Brian Chen", "cn": "陈中欣 Brian Chen", "en": "Brian Chen"},
                "title": {"tw": "Markforged　大中華區暨越南區總經理",
                          "cn": "Markforged　大中华区暨越南区总经理",
                          "en": "Country Manager, Greater China and Vietnam, Markforged"},
            },
        ],
    },
    {
        "kind": "factsheet",
        "h": {"tw": "活動資料", "cn": "活动资料", "en": "Event details"},
        "rows": [
            {"k": {"tw": "日期", "cn": "日期", "en": "Date"},
             "v": {"tw": "2026 年 9 月 24 日（星期四）",
                   "cn": "2026 年 9 月 24 日（星期四）",
                   "en": "Thursday, 24 September 2026"}},
            {"k": {"tw": "時間", "cn": "时间", "en": "Time"},
             "v": {"tw": "14:00 – 18:00", "cn": "14:00 – 18:00", "en": "14:00 – 18:00"}},
            {"k": {"tw": "地點", "cn": "地点", "en": "Venue"},
             "v": {"tw": "HKPC Inno Network，生產力大樓 1 樓",
                   "cn": "HKPC Inno Network，生产力大楼 1 楼",
                   "en": "HKPC Inno Network, 1/F, HKPC Building"}},
            {"k": {"tw": "地址", "cn": "地址", "en": "Address"},
             "v": {"tw": "九龍塘達之路 78 號", "cn": "九龙塘达之路 78 号",
                   "en": "78 Tat Chee Avenue, Kowloon Tong, Hong Kong"}},
            {"k": {"tw": "流程", "cn": "流程", "en": "Programme"},
             "v": {"tw": "嘉賓簽到｜開幕及剪綵儀式｜工業 3D 列印技術簡報｜實機示範｜"
                         "用家案例分享｜問答環節｜交流酒會",
                   "cn": "嘉宾签到｜开幕及剪彩仪式｜工业 3D 打印技术简报｜实机演示｜"
                         "用户案例分享｜问答环节｜交流酒会",
                   "en": "Registration · Opening and ribbon-cutting · Technical briefing on "
                         "industrial 3D printing · Live machine demonstration · Customer case "
                         "study · Q&amp;A · Networking reception"}},
        ],
    },
    {
        "kind": "about",
        "cols": [
            {"h": {"tw": "關於 Markforged", "cn": "关于 Markforged", "en": "About Markforged"},
             "p": {"tw": "Markforged 為工業級積層製造企業，成立於 2013 年，透過 Digital Forge "
                         "數位製造平台及連續纖維增強（CFR）技術，讓製造業在生產現場直接製造"
                         "高強度終端零件、夾治具與備品，以縮短供應鏈、降低庫存並提升產能韌性。"
                         "產品線涵蓋工業級複合材料及金屬積層製造系統，應用範圍包括航太、汽車、"
                         "電子、醫療器材及精密工程。",
                   "cn": "Markforged 为工业级增材制造企业，成立于 2013 年，透过 Digital Forge "
                         "数字制造平台及连续纤维增强（CFR）技术，让制造业在生产现场直接制造"
                         "高强度终端零件、夹治具与备品，以缩短供应链、降低库存并提升产能韧性。"
                         "产品线涵盖工业级复合材料及金属增材制造系统，应用范围包括航空航天、"
                         "汽车、电子、医疗器材及精密工程。",
                   "en": "Markforged is an industrial additive manufacturing company founded in "
                         "2013. Through the Digital Forge platform and Continuous Fiber "
                         "Reinforcement (CFR), manufacturers produce high-strength end-use parts, "
                         "tooling and spares at the point of production, shortening supply chains, "
                         "reducing inventory and improving capacity resilience. Its product line "
                         "covers industrial composite and metal additive manufacturing systems, "
                         "used in aerospace, automotive, electronics, medical devices and "
                         "precision engineering."}},
            {"h": {"tw": "關於壹科技有限公司", "cn": "关于壹科技有限公司",
                   "en": "About Unotech Limited"},
             "p": {"tw": "壹科技有限公司（Unotech Limited）為香港的工業技術方案供應商，引進"
                         "智慧製造與 3D 列印技術，向本地科研、教育及製造機構提供設備供應、"
                         "應用開發及技術支援服務。",
                   "cn": "壹科技有限公司（Unotech Limited）为香港的工业技术方案供应商，引进"
                         "智能制造与 3D 打印技术，向本地科研、教育及制造机构提供设备供应、"
                         "应用开发及技术支持服务。",
                   "en": "Unotech Limited is a Hong Kong industrial technology solutions provider. "
                         "It brings smart manufacturing and 3D printing technology to local "
                         "research, education and manufacturing institutions, offering equipment "
                         "supply, application development and technical support."}},
        ],
    },
    {
        # 2026-09-24 Brian 親糾：標題不要寫「傳媒查詢及索取高解析度圖片」，就是媒體聯絡窗口。
        # 欄位照壹科技官方定稿新聞稿的「傳媒聯絡」段：只有電話與電郵。
        "kind": "contact",
        "h": {"tw": "媒體聯絡", "cn": "媒体联络", "en": "Media contact"},
        "org": {"tw": "壹科技有限公司　Unotech Limited",
                "cn": "壹科技有限公司　Unotech Limited",
                "en": "Unotech Limited"},
        "lines": {
            "tw": '電郵：<a href="mailto:dery.chen@uno-tech.com.hk">dery.chen@uno-tech.com.hk</a>'
                  '<br>電話：5532 1843',
            "cn": '电邮：<a href="mailto:dery.chen@uno-tech.com.hk">dery.chen@uno-tech.com.hk</a>'
                  '<br>电话：5532 1843',
            "en": 'Email: <a href="mailto:dery.chen@uno-tech.com.hk">dery.chen@uno-tech.com.hk</a>'
                  '<br>Tel: +852 5532 1843',
        },
    },
]

CTA = {
    # 2026-09-24 Brian：「結尾寫得不好，重寫要人看得懂的專業文字」。
    # 原稿「香港的客戶想從一個零件開始試」是口語自語，且條件句堆疊。改為直述句：
    # 先講事實（誰負責什麼），再講讀者能做什麼。
    "href": "https://www.uno-tech.com.hk",
    "h": {"tw": "香港的服務窗口",
          "cn": "香港的服务窗口",
          "en": "Point of contact in Hong Kong"},
    "p": {"tw": "即日起，Markforged 產品在香港的銷售、技術支援與應用開發由壹科技有限公司負責，"
                "並由其本地工程團隊提供安裝、教育訓練與應用開發。"
                "需要評估零件可行性、安排實機測試或索取技術資料，可直接與壹科技聯繫。",
          "cn": "即日起，Markforged 产品在香港的销售、技术支持与应用开发由壹科技有限公司负责，"
                "并由其本地工程团队提供安装、培训与应用开发。"
                "需要评估零件可行性、安排实机测试或索取技术资料，可直接与壹科技联系。",
          "en": "Markforged's sales, technical support and application development in Hong Kong "
                "are now handled by Unotech Limited, whose local engineering team covers "
                "installation, training and application development. For a feasibility assessment "
                "on a specific part, a machine trial or technical documentation, contact Unotech "
                "directly."},
    "btn": {"tw": "前往壹科技", "cn": "前往壹科技", "en": "Visit Unotech"},
}


# 2026-09-24 Brian：網站不顯示「資料來源」段（內部嚴謹痕跡不進對外文件）。
# SRC 內容保留當取材帳，只是不輸出到頁面。
SHOW_SOURCES = False

SRC = {
    "h": {"tw": "資料來源", "cn": "资料来源", "en": "Sources"},
    "items": [
        {"tw": "活動事實、技術說明與材料數據，取自 2026 年 9 月 24 日發布會現場全程錄音（1 小時 52 分）。",
         "cn": "活动事实、技术说明与材料数据，取自 2026 年 9 月 24 日发布会现场全程录音（1 小时 52 分）。",
         "en": "Event facts, technical explanations and material figures are taken from the full "
               "recording of the 24 September 2026 launch event (1 hour 52 minutes)."},
        {"tw": "文中兩段具名直接引語（Ivan Siu、陳中欣）取自壹科技 2026 年 9 月 24 日發布的"
               "官方新聞稿，引號內未經改寫；簡體中文與英文版為譯文。",
         "cn": "文中两段具名直接引语（Ivan Siu、陈中欣）取自壹科技 2026 年 9 月 24 日发布的"
               "官方新闻稿，引号内未经改写；简体中文与英文版为译文。",
         "en": "The two attributed quotations (Ivan Siu, Brian Chen) are taken from "
               "Unotech's official press release of 24 September 2026 and are reproduced "
               "without alteration; the Chinese and English editions are translations."},
        {"tw": "紅點設計獎（Design Concept 組別）得獎年份、專利狀態、測試方法與里程數據，"
               "由香港理工大學研究團隊於會上提出。",
         "cn": "红点设计奖（Design Concept 组别）获奖年份、专利状态、测试方法与里程数据，"
               "由香港理工大学研究团队于会上提出。",
         "en": "The Red Dot Award (Design Concept) year, patent status, test methodology and "
               "mileage figures were presented by the PolyU research team at the event."},
        {"tw": "文中照片為 2026 年 9 月 24 日活動現場攝影。",
         "cn": "文中照片为 2026 年 9 月 24 日活动现场摄影。",
         "en": "Photographs were taken at the event on 24 September 2026."},
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

# G5 冒名引言閘白名單 —— 每一句都要有出處。
# 2026-09-24 改版：兩段具名引言**全部改用壹科技官方定稿新聞稿的版本**
#   （`Unotech官方新聞稿_繁中_2026-09-24.docx`，Brian 2026-09-24 18:26 提供）。
# 原先用的是我從現場錄音改寫的版本 —— 有出處但非官方核可口徑，已退場。
# 引號內一字未改；簡中為 OpenCC 轉換，英文為翻譯（頁面「資料來源」段已聲明）。
APPROVED_QUOTES = {
    # 「很結實」＝ Brian 當天簡報 p13 原話（「工程師拿得到數字去做判斷，而不是拿一句『很結實』
    # 去說服人」），本文用作段落標題，出處＝`72_Decks/2026-09-24_Unotech-HK-Launch` 繁中 31p。
    "tw": ["很結實",
        "我們非常榮幸能與工業 3D 打印領先品牌 Markforged 建立獨家合作關係。憑藉 Markforged 在增材製造"
        "領域的技術優勢，我們有信心為香港市場帶來更具成本效益、可靠且創新的製造選擇。壹科技的本地技術"
        "團隊將主攻航空維修、電子製造、醫療器材與精密工程等重點行業，這與連續纖維技術對強度與即時交付"
        "的高要求完美契合。我們將持續強化本地技術能量，全力支援香港智能製造市場的長遠發展。",
        "香港作為大灣區的科技與貿易樞紐，客戶結構橫跨多個高端製造領域。我們選擇壹科技作為獨家合作夥伴，"
        "正是看中其深厚的本地技術能量與優異的售後服務覆蓋範圍。獨家代理將使責任更為集中，客戶只需對接"
        "單一窗口，便能獲得全方位的專業保障。Markforged 在大中華區累積的豐富應用案例與材料驗證資料，"
        "亦將直接賦能香港團隊，共同協助本地醫療機構、航空與精密工程客戶提升運作效率。",
    ],
    "cn": ["很结实",
        "我们非常荣幸能与工业 3D 打印领先品牌 Markforged 建立独家合作关系。凭借 Markforged 在增材制造"
        "领域的技术优势，我们有信心为香港市场带来更具成本效益、可靠且创新的制造选择。壹科技的本地技术"
        "团队将主攻航空维修、电子制造、医疗器材与精密工程等重点行业，这与连续纤维技术对强度与即时交付"
        "的高要求完美契合。我们将持续强化本地技术能量，全力支援香港智能制造市场的长远发展。",
        "香港作为大湾区的科技与贸易枢纽，客户结构横跨多个高端制造领域。我们选择壹科技作为独家合作伙伴，"
        "正是看中其深厚的本地技术能量与优异的售后服务覆盖范围。独家代理将使责任更为集中，客户只需对接"
        "单一窗口，便能获得全方位的专业保障。Markforged 在大中华区累积的丰富应用案例与材料验证资料，"
        "亦将直接赋能香港团队，共同协助本地医疗机构、航空与精密工程客户提升运作效率。",
    ],
    "en": [
        "We are honoured to enter an exclusive partnership with Markforged, a leading brand in "
        "industrial 3D printing. With Markforged's technical strengths in additive manufacturing, "
        "we are confident we can bring Hong Kong more cost-effective, reliable and innovative "
        "manufacturing options. Our local technical team will focus on aviation MRO, electronics "
        "manufacturing, medical devices and precision engineering — sectors whose demands on "
        "strength and turnaround align closely with continuous fiber technology. We will keep "
        "building local technical capability to support the long-term development of smart "
        "manufacturing in Hong Kong.",
        "Hong Kong is a technology and trading hub for the Greater Bay Area, with a customer base "
        "spanning multiple high-end manufacturing sectors. We chose Unotech as our exclusive partner "
        "for its depth of local technical capability and the strength of its after-sales coverage. "
        "An exclusive distributorship concentrates accountability: customers deal with a single "
        "point of contact and get end-to-end professional cover. The application cases and material "
        "validation data Markforged has built up across Greater China will feed directly into the "
        "Hong Kong team, helping local medical, aviation and precision engineering customers raise "
        "operating efficiency.",
    ],
}

DOC_TERMS = ["Markforged", "Unotech", "壹科技", "壹科技有限公司", "Unotech Limited",
             "Onyx", "FX10", "Eiger", "Kevlar", "CFR", "Continuous Fiber Reinforcement",
             "HKPC", "Inno Network", "PolyU", "U3DP", "Red Dot", "spacer fabric",
             "Design Concept", "STL", "NDA", "6061-T6", "ABS"]

# ── G6 原稿覆蓋率閘的兩個宣告 ────────────────────────────────────────────────
# 2026-09-24 事故：網頁版靜默砍掉原稿五個段落（含壹科技唯一一段引言、傳媒查詢），
# 而五道閘全綠 —— 因為它們量的是「三個語版彼此對齊」，沒有一道量「對齊事實來源」。
SOURCE_MD = ("/Users/brian/Library/Mobile Documents/iCloud~md~obsidian/Documents/MF-GCR/"
             "84_Media-PR/Unotech-HK-Launch-2026-09/"
             "Markforged-Unotech-HK發布會_活動報導稿_繁中_v1_2026-09-24.md")

# 來源稿有、網頁版刻意不出現的 token —— 每一條都要寫得出理由，否則就是漏稿。
COVERAGE_EXEMPT = {
    "Additive Manufacturing": "繁中版依 Brian 2026-09-24 指示走台灣專業用語「積層製造」，不附英文對照；"
                              "英文版本身即為 additive manufacturing。",
    "Red Dot": "繁中版寫「德國紅點設計獎」（台灣通用譯名）；英文版保留 Red Dot Award。",
    "www.uno-tech.com.hk": "Brian 2026-09-24 指示：媒體聯絡窗口只留電郵與電話，不放網址、"
                           "不寫「索取高解析度圖片」。",
}

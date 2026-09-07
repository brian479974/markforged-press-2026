# -*- coding: utf-8 -*-
"""廣編稿三語內容源 —— 繁中 / 簡中 / English 的唯一真相。

2026-09-07 重寫（v2）。兩個變更原因：

1. **引言只能用 Brian 真的說過的話。**
   v1 有 10 處掛他名字的直接引言，全部是我代寫的。Brian 指出其中
   「大家都在搶同一個東西。不是模型，是身體。」根本不是他說過的話。
   v2 只保留兩處引言，兩處都出自他 2026-09-07 對本稿的口述：
     Q1 AI 目前的蓬勃發展在軟體、在晶片、在算力；真正致勝的關鍵、
        現在正在發生、未來最重要的，是 AI 的實體化。
     Q2 現在大家都在講 AI，輔助設計、協助設計及各種相關應用，
        但最大的挑戰是 AI 實體化 —— 把軟體變成硬體、把虛擬的變成實體。
   其餘一律改為記者敘述體與具名觀點轉述，不加引號、不冒名。

2. **用語專業化。** 去口語：「做得出來」→可製造性、「找不到人」→人力短缺、
   「一年能試幾個方向」→年度可驗證的技術路線數量。

簡中用語依 mf-formal-doc 大陸公文規範；引號用 “ ”。
"""

LANGS = ("tw", "cn", "en")

META = {
    "lang_attr": {"tw": "zh-TW", "cn": "zh-CN", "en": "en"},
    "file": {"tw": "physical-ai-body.html",
             "cn": "physical-ai-body-sc.html",
             "en": "physical-ai-body-en.html"},
    "title": {
        "tw": "AI 競爭的下一階段：焦點正從算力移向實體化 — Markforged",
        "cn": "AI 竞争的下一阶段：焦点正从算力移向实体化 — Markforged",
        "en": "The next phase of AI competition: from compute to physical realisation — Markforged",
    },
    "desc": {
        "tw": "軟體、晶片與算力之外，決定 Physical AI 能走多遠的是製造端。Markforged 大中華區暨越南區總經理陳中欣談 AI 實體化的三項結構限制。",
        "cn": "软件、芯片与算力之外，决定 Physical AI 能走多远的是制造端。Markforged 大中华区暨越南区总经理陈中欣谈 AI 实体化的三项结构限制。",
        "en": "Beyond software, silicon and compute, what determines how far Physical AI can go is manufacturing. Brian Chen, Markforged Country Manager for Greater China and Vietnam, on the three structural constraints of physical realisation.",
    },
    "og_title": {
        "tw": "AI 競爭的下一階段：焦點正從算力移向實體化",
        "cn": "AI 竞争的下一阶段：焦点正从算力移向实体化",
        "en": "The next phase of AI competition: from compute to physical realisation",
    },
    "og_desc": {
        "tw": "決定 Physical AI 能走多遠的，是製造端的可製造性、迭代週期與供應鏈成熟度。",
        "cn": "决定 Physical AI 能走多远的，是制造端的可制造性、迭代周期与供应链成熟度。",
        "en": "What determines how far Physical AI can go: manufacturability, iteration cycles and supply chain maturity.",
    },
}

UI = {
    "hdr_ev": {"tw": "大中華區媒體中心<br>News &amp; Insights",
               "cn": "大中华区媒体中心<br>News &amp; Insights",
               "en": "Greater China Media Hub<br>News &amp; Insights"},
    "switch_label": {"tw": "語言", "cn": "语言", "en": "Language"},
    "hero_alt": {"tw": "Markforged FX10 工業級積層製造系統設置於產線現場，後方為工業機器人",
                 "cn": "Markforged FX10 工业级增材制造系统设置于产线现场，后方为工业机器人",
                 "en": "A Markforged FX10 industrial additive manufacturing system on a production floor with industrial robots behind it"},
    "hero_kicker": {"tw": "產業觀點 · Physical AI", "cn": "产业观点 · Physical AI",
                    "en": "Industry Perspective · Physical AI"},
    "hero_title": {
        "tw": "AI 競爭的下一階段：<br>焦點正從算力移向實體化",
        "cn": "AI 竞争的下一阶段：<br>焦点正从算力移向实体化",
        "en": "The next phase of AI competition:<br>from compute to physical realisation",
    },
    "hero_meta": {
        "tw": "專訪 Markforged 大中華區暨越南區總經理　陳中欣 Brian Chen",
        "cn": "专访 Markforged 大中华区暨越南区总经理　陈中欣 Brian Chen",
        "en": "An interview with Brian Chen, Country Manager for Greater China and Vietnam, Markforged",
    },
    "ds_l": {"tw": "2026 年 9 月 7 日", "cn": "2026 年 9 月 7 日", "en": "7 September 2026"},
    "ds_r": {"tw": "台灣 · 中國 · 香港 · 越南", "cn": "台湾 · 中国 · 香港 · 越南",
             "en": "Taiwan · China · Hong Kong · Vietnam"},
}

LEAD = {
    "p1": {
        "tw": "2026 年 8 月 19 日至 22 日，台北國際自動化工業大展與 TAIROS 於南港展覽館舉行，886 家廠商進駐 3,506 個攤位。同一週，2026 世界機器人大會在北京亦莊召開。九月，深圳市發布《推動智能機器人產業高質量發展工作方案（2026—2028 年）》，將人形機器人本體與核心零部件自主化列為重點攻關方向。",
        "cn": "2026 年 8 月 19 日至 22 日，台北国际自动化工业大展与 TAIROS 于南港展览馆举行，886 家厂商进驻 3,506 个展位。同一周，2026 世界机器人大会在北京亦庄召开。九月，深圳市发布《推动智能机器人产业高质量发展工作方案（2026—2028 年）》，将人形机器人本体与核心零部件自主化列为重点攻关方向。",
        "en": "From 19 to 22 August 2026, Automation Taipei and TAIROS ran at the Nangang Exhibition Center, with 886 exhibitors across 3,506 booths. The same week, the 2026 World Robot Conference convened in Yizhuang, Beijing. In September, Shenzhen released its Work Plan for High-Quality Development of the Intelligent Robotics Industry (2026–2028), naming humanoid robot bodies and self-sufficiency in core components as priority areas.",
    },
    "p2": {
        "tw": "三項事件分屬不同市場，指向同一個結構命題：當 Physical AI 從實驗室走向量產，決定其發展速度的不再只是模型與算力，而是製造端能否如期交付具備結構性能的實體。Markforged 大中華區暨越南區總經理陳中欣的職責範圍涵蓋台灣、中國、香港與越南，正好橫跨這條實體供應鏈的多個環節。",
        "cn": "三项事件分属不同市场，指向同一个结构命题：当 Physical AI 从实验室走向量产，决定其发展速度的不再只是模型与算力，而是制造端能否如期交付具备结构性能的实体。Markforged 大中华区暨越南区总经理陈中欣的职责范围涵盖台湾、中国、香港与越南，正好横跨这条实体供应链的多个环节。",
        "en": "The three events sit in different markets but point to one structural question. As Physical AI moves from the laboratory into volume production, its pace is no longer set by models and compute alone, but by whether manufacturing can deliver structurally capable physical parts on schedule. Brian Chen, Markforged's Country Manager for Greater China and Vietnam, covers Taiwan, China, Hong Kong and Vietnam — spanning several links in that physical supply chain.",
    },
}

# 引言 1 —— Brian 2026-09-07 口述，professionalised，未加料
QUOTE = {
    "text": {"tw": "「AI 目前的蓬勃發展集中在軟體、晶片與算力。真正的致勝關鍵此刻正在發生，而未來最重要的一件事，是 AI 的實體化。」",
             "cn": "“AI 目前的蓬勃发展集中在软件、芯片与算力。真正的致胜关键此刻正在发生，而未来最重要的一件事，是 AI 的实体化。”",
             "en": "“The current surge in AI is concentrated in software, silicon and compute. The decisive factor is being settled right now, and the single most important thing ahead is the physical realisation of AI.”"},
    "attr": {"tw": "陳中欣 · Markforged 大中華區暨越南區總經理",
             "cn": "陈中欣 · Markforged 大中华区暨越南区总经理",
             "en": "Brian Chen · Country Manager, Greater China and Vietnam, Markforged"},
}

PROF = {
    "alt": {"tw": "陳中欣 Brian Chen", "cn": "陈中欣 Brian Chen", "en": "Brian Chen"},
    "name": {"tw": "陳中欣 Brian Chen", "cn": "陈中欣 Brian Chen", "en": "Brian Chen"},
    "title": {"tw": "Markforged 大中華區暨越南區總經理",
              "cn": "Markforged 大中华区暨越南区总经理",
              "en": "Country Manager, Greater China and Vietnam, Markforged"},
    "desc": {"tw": "負責台灣、中國、香港、越南四個市場的業務發展、通路體系與技術方案。",
             "cn": "负责台湾、中国、香港、越南四个市场的业务发展、渠道体系与技术方案。",
             "en": "Responsible for business development, channel structure and technical solutions across Taiwan, China, Hong Kong and Vietnam."},
}

TAGS = [
    {"tw": "Physical AI", "cn": "Physical AI", "en": "Physical AI", "solid": True},
    {"tw": "智慧製造", "cn": "智能制造", "en": "Smart Manufacturing", "solid": True},
    {"tw": "彈性生產", "cn": "柔性生产", "en": "Flexible Production", "solid": False},
    {"tw": "產線優化", "cn": "产线优化", "en": "Line Optimisation", "solid": False},
    {"tw": "供應韌性", "cn": "供应韧性", "en": "Supply Resilience", "solid": False},
]

BLOCKS = [
    {"kind": "sec",
     "h2": {"tw": "產業焦點的位移", "cn": "产业焦点的位移", "en": "A shift in focus"},
     "h3": {"tw": "投資集中於軟體與算力，實體化尚未形成對應的產業能力",
            "cn": "投资集中于软件与算力，实体化尚未形成对应的产业能力",
            "en": "Investment has concentrated on software and compute; physical realisation has yet to build matching industrial capacity"},
     "paras": [
       {"tw": "過去三年，AI 領域的資本與人才高度集中於三個方向：模型與軟體框架、半導體製程與晶片架構、資料中心與算力基礎設施。三者的產業鏈已相對成熟，投資邏輯與評價方式也已建立。",
        "cn": "过去三年，AI 领域的资本与人才高度集中于三个方向：模型与软件框架、半导体工艺与芯片架构、数据中心与算力基础设施。三者的产业链已相对成熟，投资逻辑与评价方式也已建立。",
        "en": "Over the past three years, capital and talent in AI have concentrated in three directions: models and software frameworks, semiconductor process and chip architecture, and data centre and compute infrastructure. The supply chains behind all three are comparatively mature, with established investment logic and valuation methods."},
       {"tw": "Physical AI 的定義則要求另一種能力。當人工智慧的輸出必須以實體形式存在——機器人本體、機構件、末端執行器、感測器承載結構——其產出速度即受限於製造端的可製造性、迭代週期與供應鏈成熟度。這三項限制目前尚未獲得與軟體端相稱的產業投入。",
        "cn": "Physical AI 的定义则要求另一种能力。当人工智能的输出必须以实体形式存在——机器人本体、机构件、末端执行器、传感器承载结构——其产出速度即受限于制造端的可制造性、迭代周期与供应链成熟度。这三项限制目前尚未获得与软件端相称的产业投入。",
        "en": "Physical AI demands a different capability. Where the output of artificial intelligence must exist in physical form — robot bodies, structural components, end effectors, sensor mounts — the rate of output is bounded by three constraints on the manufacturing side: manufacturability, iteration cycle, and supply chain maturity. None of the three has yet attracted industrial investment on a scale comparable to software."},
     ]},

    {"kind": "sec",
     "h2": {"tw": "限制一 · 可製造性", "cn": "限制一 · 可制造性", "en": "Constraint one · Manufacturability"},
     "h3": {"tw": "生成式設計輸出的幾何，多數超出減材製程的加工範圍",
            "cn": "生成式设计输出的几何，多数超出减材工艺的加工范围",
            "en": "Most geometry produced by generative design falls outside the reach of subtractive processes"},
     "paras": [
       {"tw": "拓撲優化與生成式設計已進入量產工程流程。其演算結果的共同特徵，是以材料分布效率為目標所產生的非直覺幾何：連續曲面、內部點陣結構、封閉於零件內部的流道。這類幾何的力學效率來自於它並不遵循減材製造的成形邏輯。",
        "cn": "拓扑优化与生成式设计已进入量产工程流程。其算法结果的共同特征，是以材料分布效率为目标所产生的非直觉几何：连续曲面、内部点阵结构、封闭于零件内部的流道。这类几何的力学效率来自于它并不遵循减材制造的成形逻辑。",
        "en": "Topology optimisation and generative design have entered production engineering workflows. Their outputs share a characteristic: non-intuitive geometry driven by material distribution efficiency — continuous surfaces, internal lattice structures, channels enclosed within the part. The mechanical efficiency of such geometry derives precisely from the fact that it does not follow the forming logic of subtractive manufacturing."},
       {"tw": "減材製程存在刀具可及性的物理限制。當演算結果無法以既有製程成形，工程單位通常回退至可加工版本，於是設計效益在製程階段被折減。此一折減多數未被量化紀錄，亦未反映於 AI 導入的效益評估中。",
        "cn": "减材工艺存在刀具可及性的物理限制。当算法结果无法以既有工艺成形，工程单位通常回退至可加工版本，于是设计效益在工艺阶段被折减。此一折减多数未被量化记录，亦未反映于 AI 导入的效益评估中。",
        "en": "Subtractive processes carry a physical limit on tool access. Where an algorithmic result cannot be formed by existing processes, engineering teams typically revert to a machinable version, and the design benefit is discounted at the process stage. That discount is rarely quantified or recorded, and seldom appears in assessments of the return on AI adoption."},
       {"tw": "對機器人應用而言，此一折減直接反映於性能。機構件質量經力臂放大後轉為驅動負載，並影響續航與定位精度。輕量化在此並非設計偏好，而是規格條件。",
        "cn": "对机器人应用而言，此一折减直接反映于性能。机构件质量经力臂放大后转为驱动负载，并影响续航与定位精度。轻量化在此并非设计偏好，而是规格条件。",
        "en": "In robotics the discount shows up directly in performance. Structural mass is amplified by the lever arm into actuator load, and carries through to runtime and positioning accuracy. Light weight here is not a design preference but a specification requirement."},
     ]},

    {"kind": "img_2col",
     "imgs": ["images/eoat-packaging.jpg", "images/cobot-gripper.jpg"],
     "alts": [{"tw": "以連續碳纖維複合材料製作的產線末端執行器", "cn": "以连续碳纤维复合材料制作的产线末端执行器",
               "en": "Production end-of-arm tooling made in continuous carbon fibre composite"},
              {"tw": "客製化協作型機器人夾爪", "cn": "定制化协作型机器人夹爪",
               "en": "Customised collaborative robot gripper"}],
     "cap": {"tw": "左：食品包裝產線之機器人末端執行器（材料 Onyx；FX10／FX20／X7）。右：Harvestance 客製化協作型機器人夾爪（材料 Onyx；FX20）。圖片來源：Markforged 官方 Application Spotlight",
             "cn": "左：食品包装产线之机器人末端执行器（材料 Onyx；FX10／FX20／X7）。右：Harvestance 定制化协作型机器人夹爪（材料 Onyx；FX20）。图片来源：Markforged 官方 Application Spotlight",
             "en": "Left: end-of-arm tooling for a food packaging line (Onyx; FX10 / FX20 / X7). Right: Harvestance customised collaborative robot gripper (Onyx; FX20). Images: Markforged official Application Spotlight"}},

    {"kind": "sec",
     "h2": {"tw": "限制二 · 迭代週期", "cn": "限制二 · 迭代周期", "en": "Constraint two · Iteration cycle"},
     "h3": {"tw": "軟硬體迭代節奏不對稱，決定年度可驗證的技術路線數量",
            "cn": "软硬件迭代节奏不对称，决定年度可验证的技术路线数量",
            "en": "An asymmetry in cadence sets how many technical paths can be validated in a year"},
     "paras": [
       {"tw": "軟體迭代的邊際成本趨近於零，版本週期以日計。硬體則不然：機構件的每一次修改均需重新設計、重新發包、重新驗證，週期以週或月計。此一節奏差異在原型階段影響有限，進入場景驗證階段後則成為主要瓶頸。",
        "cn": "软件迭代的边际成本趋近于零，版本周期以日计。硬件则不然：机构件的每一次修改均需重新设计、重新发包、重新验证，周期以周或月计。此一节奏差异在原型阶段影响有限，进入场景验证阶段后则成为主要瓶颈。",
        "en": "The marginal cost of software iteration approaches zero and version cycles run in days. Hardware does not behave that way: every change to a structural component requires redesign, requoting and revalidation, on cycles measured in weeks or months. The difference in cadence has limited effect during prototyping, but becomes the dominant bottleneck once scenario validation begins."},
       {"tw": "以深圳方案設定的目標為例，2026 年底前需開放至少十個真實場景進入常態運行。每一個場景的環境條件不同，對應的機構調整即構成一輪硬體回饋。十個場景意味著至少十輪機構迭代，其總時程直接取決於實體件的交付週期。",
        "cn": "以深圳方案设定的目标为例，2026 年底前需开放至少十个真实场景进入常态运行。每一个场景的环境条件不同，对应的机构调整即构成一轮硬件反馈。十个场景意味着至少十轮机构迭代，其总时程直接取决于实体件的交付周期。",
        "en": "Take the target set in Shenzhen's plan: at least ten real scenarios in routine operation by the end of 2026. Each scenario presents different environmental conditions, and each corresponding mechanical adjustment constitutes a round of hardware feedback. Ten scenarios imply at least ten rounds of mechanical iteration, and the total schedule depends directly on the lead time for physical parts."},
       {"tw": "美國機器人公司 Haddington Dynamics 的公開案例提供了量化參照。該公司將 Dexter 機械臂之多數結構件改以積層製造生產，零件數自 800 件降至 70 件以下，整機組裝時程縮短至一日內完成。該機械臂之運動精度要求為 50 微米。依原廠公開資料，設備導入後約三週即完成整機碳纖維結構之重新設計。",
        "cn": "美国机器人公司 Haddington Dynamics 的公开案例提供了量化参照。该公司将 Dexter 机械臂之多数结构件改以增材制造生产，零件数自 800 件降至 70 件以下，整机装配时程缩短至一日内完成。该机械臂之运动精度要求为 50 微米。依原厂公开资料，设备导入后约三周即完成整机碳纤维结构之重新设计。",
        "en": "A published case from US robotics company Haddington Dynamics offers a quantified reference. The company moved most structural components of its Dexter arm to additive production, reducing part count from 800 to under 70 and shortening full assembly to within a day. The arm's motion accuracy requirement is 50 micrometres. According to published material, the complete carbon fibre structural redesign was finished roughly three weeks after the equipment was installed."},
     ],
     "hl": [
       {"b": {"tw": "800 → 70", "cn": "800 → 70", "en": "800 → 70"},
        "s": {"tw": "Dexter 機械臂結構件數量<br>整機組裝縮短至一日內",
              "cn": "Dexter 机械臂结构件数量<br>整机装配缩短至一日内",
              "en": "Structural part count, Dexter arm<br>Full assembly within one day"}},
       {"b": {"tw": "約 3 週", "cn": "约 3 周", "en": "~3 weeks"},
        "s": {"tw": "自設備導入至完成<br>整機碳纖維結構重新設計",
              "cn": "自设备导入至完成<br>整机碳纤维结构重新设计",
              "en": "From installation to completed<br>carbon fibre structural redesign"}},
     ]},

    {"kind": "img_full",
     "img": "images/robotic-arm-7axis.jpg",
     "alt": {"tw": "結構件以連續碳纖維複合材料製作之七軸機械臂",
             "cn": "结构件以连续碳纤维复合材料制作之七轴机械臂",
             "en": "Seven-axis robot arm with structural components in continuous carbon fibre composite"},
     "cap": {"tw": "Haddington Dynamics Dexter 七軸機械臂，多數結構件改以積層製造生產。圖片來源：Markforged 官方 Application Spotlight",
             "cn": "Haddington Dynamics Dexter 七轴机械臂，多数结构件改以增材制造生产。图片来源：Markforged 官方 Application Spotlight",
             "en": "The Haddington Dynamics Dexter seven-axis arm, with most structural components moved to additive production. Image: Markforged official Application Spotlight"}},

    {"kind": "sec",
     "h2": {"tw": "限制三 · 供應鏈成熟度", "cn": "限制三 · 供应链成熟度",
            "en": "Constraint three · Supply chain maturity"},
     "h3": {"tw": "樣機成熟度與量產成熟度屬於不同的工程問題",
            "cn": "样机成熟度与量产成熟度属于不同的工程问题",
            "en": "Prototype maturity and volume maturity are different engineering problems"},
     "paras": [
       {"tw": "2026 世界機器人大會後，產業界普遍形成一項評估：人形機器人的硬體已趨成熟，後續瓶頸在於泛化能力不足。此一判斷在演算法層面成立，但在製造層面需要區分。",
        "cn": "2026 世界机器人大会后，产业界普遍形成一项评估：人形机器人的硬件已趋成熟，后续瓶颈在于泛化能力不足。此一判断在算法层面成立，但在制造层面需要区分。",
        "en": "After the 2026 World Robot Conference, a broad assessment took hold: humanoid hardware is approaching maturity, and the remaining bottleneck is weak generalisation. The judgement holds at the algorithmic level, but requires a distinction at the manufacturing level."},
       {"tw": "Markforged 的觀察是，目前達到成熟的是展示樣機，而非量產供應鏈。單台可由工程團隊以手工方式完成的機構，與年產萬台、須逐台維持運動精度並支援改款的機構，屬於兩種不同性質的工程問題：前者取決於設計與組裝能力，後者取決於供應鏈的一致性與反應速度。",
        "cn": "Markforged 的观察是，目前达到成熟的是展示样机，而非量产供应链。单台可由工程团队以手工方式完成的机构，与年产万台、须逐台维持运动精度并支持改款的机构，属于两种不同性质的工程问题：前者取决于设计与装配能力，后者取决于供应链的一致性与响应速度。",
        "en": "Markforged's reading is that what has matured is the demonstration prototype, not the production supply chain. A mechanism a single engineering team can hand-build, and a mechanism produced at ten thousand units a year while holding motion accuracy unit by unit and supporting design revisions, are two different classes of engineering problem. The first turns on design and assembly capability; the second on the consistency and responsiveness of a supply chain."},
       {"tw": "深圳方案的技術攻關方向可作為對照。該方案將人形機器人本體與核心零部件自主化列為重點，其資源配置指向的是實體製造能力，而非模型能力。",
        "cn": "深圳方案的技术攻关方向可作为对照。该方案将人形机器人本体与核心零部件自主化列为重点，其资源配置指向的是实体制造能力，而非模型能力。",
        "en": "The technical priorities in Shenzhen's plan offer a point of comparison. By naming humanoid robot bodies and self-sufficiency in core components as focus areas, the plan directs resources at physical manufacturing capability rather than model capability."},
     ]},

    {"kind": "sec",
     "h2": {"tw": "區域產業定位", "cn": "区域产业定位", "en": "Regional positioning"},
     "h3": {"tw": "精密機械與工裝供應能力，是實體化最直接的產業基礎",
            "cn": "精密机械与工装供应能力，是实体化最直接的产业基础",
            "en": "Precision machining and tooling supply form the most direct industrial base for physical realisation"},
     "paras": [
       {"tw": "2026 年 8 月，中華民國全國工業總會發布年度白皮書，主題為「轉折」。該白皮書調查 161 個產業公會，缺工以 76.6% 之關切度連續三年居首，產業轉型以 75.7% 居次，並建議政府檢討「重科技、輕傳產」之政策配置。",
        "cn": "2026 年 8 月，台湾全国工业总会发布年度白皮书，主题为“转折”。该白皮书调查 161 个产业公会，缺工以 76.6% 之关切度连续三年居首，产业转型以 75.7% 居次，并建议当局检讨“重科技、轻传产”之政策配置。",
        "en": "In August 2026 Taiwan's Chinese National Federation of Industries published its annual white paper under the theme “Turning Point.” Surveying 161 industry associations, it recorded labour shortage as the leading concern for a third consecutive year at 76.6%, with industrial transformation second at 75.7%, and recommended a review of policy weighted toward high technology at the expense of traditional industry."},
       {"tw": "陳中欣認為，兩項數據與 Physical AI 的產業需求存在直接對應。實體化所需的能力——精密機械加工、結構件製造、工裝夾具供應、快速換線——正是區域內機械產業長期累積的基礎。就產業定位而言，機械業並非人工智慧的替代對象，而是 Physical AI 量產化過程中的必要環節。",
        "cn": "陈中欣认为，两项数据与 Physical AI 的产业需求存在直接对应。实体化所需的能力——精密机械加工、结构件制造、工装夹具供应、快速换线——正是区域内机械产业长期积累的基础。就产业定位而言，机械业并非人工智能的替代对象，而是 Physical AI 量产化过程中的必要环节。",
        "en": "Chen sees a direct correspondence between those figures and the industrial requirements of Physical AI. The capabilities physical realisation depends on — precision machining, structural component production, fixture and tooling supply, rapid changeover — are precisely what the region's machinery sector has built over decades. In positioning terms, machinery is not what artificial intelligence displaces; it is a necessary link in bringing Physical AI to volume."},
       {"tw": "他同時指出此一定位的前提條件：交付週期需自以週計縮短至以日計，非標準件供應需自外部委外轉為現場自主。前提未達成之前，機器人企業將轉向具備該能力的供應者。",
        "cn": "他同时指出此一定位的前提条件：交付周期需自以周计缩短至以日计，非标件供应需自外部委外转为现场自主。前提未达成之前，机器人企业将转向具备该能力的供应者。",
        "en": "He also states the precondition attached to that position: lead times must move from weeks to days, and the supply of non-standard parts from external outsourcing to on-site production. Until that is met, robotics companies will turn to suppliers who already meet it."},
       {"tw": "就人力短缺而言，其解方亦不在人力供給端。當既有人力的單位產出需提升，前提是工裝與治具能於當日到位，而非排入外部產能佇列。",
        "cn": "就人力短缺而言，其解方亦不在人力供给端。当既有人力的单位产出需提升，前提是工装与夹具能于当日到位，而非排入外部产能队列。",
        "en": "On labour shortage, the answer likewise does not sit on the supply side of labour. Raising output per existing worker depends on tooling and fixtures being available the same day, rather than queued behind external capacity."},
     ],
     "hl": [
       {"b": {"tw": "76.6%", "cn": "76.6%", "en": "76.6%"},
        "s": {"tw": "缺工關切度，連續三年居首<br>（工總 2026 白皮書，161 個公會）",
              "cn": "缺工关切度，连续三年居首<br>（工总 2026 白皮书，161 个公会）",
              "en": "Labour shortage, top concern for a third year<br>(CNFI 2026 white paper, 161 associations)"}},
       {"b": {"tw": "75.7%", "cn": "75.7%", "en": "75.7%"},
        "s": {"tw": "產業轉型關切度<br>居同一調查第二位",
              "cn": "产业转型关切度<br>居同一调查第二位",
              "en": "Industrial transformation<br>second in the same survey"}},
     ]},

    # 引言 2 —— Brian 2026-09-07 口述原意，professionalised
    {"kind": "sec",
     "h2": {"tw": "結語", "cn": "结语", "en": "In closing"},
     "h3": {"tw": "實體化是目前 AI 產業最大的未解挑戰",
            "cn": "实体化是目前 AI 产业最大的未解挑战",
            "en": "Physical realisation is the largest unresolved challenge in AI today"},
     "paras": [
       {"tw": "「現階段的產業討論高度集中於 AI 輔助設計、協助設計及各類延伸應用。但真正最大的挑戰是 AI 實體化——把軟體變成硬體，把虛擬的東西變成實體。」陳中欣表示。",
        "cn": "“现阶段的产业讨论高度集中于 AI 辅助设计、协助设计及各类延伸应用。但真正最大的挑战是 AI 实体化——把软件变成硬件，把虚拟的东西变成实体。”陈中欣表示。",
        "en": "“Industry discussion right now is heavily concentrated on AI-assisted design, design support and the applications that extend from them,” Chen says. “But the real challenge is the physical realisation of AI — turning software into hardware, turning the virtual into the physical.”"},
     ]},

    {"kind": "sec",
     "h2": {"tw": "解決方向", "cn": "解决方向", "en": "The approach"},
     "h3": {"tw": "將結構件供應能力配置於產線端",
            "cn": "将结构件供应能力配置于产线端",
            "en": "Placing structural part supply at the line"},
     "paras": [
       {"tw": "Markforged 之工業級積層製造系統以連續纖維複合材料為核心，供製造企業於生產現場自主生產具結構性能之機構件、治具夾具、末端執行器與產線輔具。FX10 與 FX20 定位於產線級應用，X7 與 X7 FE 定位於設計驗證與高頻迭代；FX10 可加裝 Metal Kit，於同一設備平台切換複合材料與金屬列印。",
        "cn": "Markforged 之工业级增材制造系统以连续纤维复合材料为核心，供制造企业于生产现场自主生产具结构性能之机构件、工装夹具、末端执行器与产线辅具。FX10 与 FX20 定位于产线级应用，X7 与 X7 FE 定位于设计验证与高频迭代；FX10 可加装 Metal Kit，于同一设备平台切换复合材料与金属打印。",
        "en": "Markforged's industrial additive manufacturing systems are built around continuous fibre composites, enabling manufacturers to produce structurally capable mechanical components, fixtures and tooling, end effectors and line aids on their own floor. The FX10 and FX20 are positioned for production-level applications; the X7 and X7 FE for design validation and high-frequency iteration. The FX10 accepts a Metal Kit, switching between composite and metal printing on a single equipment platform."},
       {"tw": "此一配置改變的並非單一零件的取得方式，而是設計變更與實體交付之間的時間差。當該時間差自以週計壓縮至以日計，硬體迭代週期方能與軟體週期對齊。",
        "cn": "此一配置改变的并非单一零件的取得方式，而是设计变更与实体交付之间的时间差。当该时间差自以周计压缩至以日计，硬件迭代周期方能与软件周期对齐。",
        "en": "What this changes is not how a single part is sourced, but the lag between a design change and a delivered physical part. Only when that lag compresses from weeks to days can the hardware iteration cycle align with the software cycle."},
     ]},
]

CTA = {
    "h": {"tw": "AI 實體化・製造新紀元 — VIP 專屬體驗日",
          "cn": "AI 实体化・制造新纪元 — VIP 专属体验日",
          "en": "Making AI Physical — VIP Experience Day"},
    "p": {"tw": "由 Markforged 原廠工程師進行現場操作演示，並針對實際應用場景進行方案評估。場次可安排於台灣、中國、香港或越南，採邀請審核制。",
          "cn": "由 Markforged 原厂工程师进行现场操作演示，并针对实际应用场景进行方案评估。场次可安排于台湾、中国、香港或越南，采邀请审核制。",
          "en": "A live demonstration conducted by Markforged engineers, with solution assessment against your actual application. Sessions can be arranged in Taiwan, China, Hong Kong or Vietnam, by invitation and review."},
    "btn": {"tw": "申請 VIP 體驗名額 →", "cn": "申请 VIP 体验名额 →", "en": "Request a VIP session →"},
}

SRC = {
    "h": {"tw": "資料來源", "cn": "资料来源", "en": "Sources"},
    "items": [
      {"tw": "2026 台北國際自動化工業大展／TAIROS：2026 年 8 月 19 至 22 日，台北南港展覽館一、二館；886 家廠商、3,506 個攤位",
       "cn": "2026 台北国际自动化工业大展／TAIROS：2026 年 8 月 19 至 22 日，台北南港展览馆一、二馆；886 家厂商、3,506 个展位",
       "en": "Automation Taipei / TAIROS 2026: 19–22 August 2026, Taipei Nangang Exhibition Center Halls 1 and 2; 886 exhibitors, 3,506 booths"},
      {"tw": "2026 世界機器人大會：2026 年 8 月 19 至 23 日，北京亦莊；主題「人機共生，產需共融」",
       "cn": "2026 世界机器人大会：2026 年 8 月 19 至 23 日，北京亦庄；主题“人机共生，产需共融”",
       "en": "World Robot Conference 2026: 19–23 August 2026, Yizhuang, Beijing; theme “Human-Robot Coexistence”"},
      {"tw": "深圳市《推動智能機器人產業高質量發展工作方案（2026—2028 年）》，2026 年 9 月發布",
       "cn": "深圳市《推动智能机器人产业高质量发展工作方案（2026—2028 年）》，2026 年 9 月发布",
       "en": "Shenzhen, Work Plan for High-Quality Development of the Intelligent Robotics Industry (2026–2028), published September 2026"},
      {"tw": "中華民國全國工業總會《2026 工總白皮書》，2026 年 8 月發布；主題「轉折」，調查 161 個產業公會",
       "cn": "台湾全国工业总会《2026 工总白皮书》，2026 年 8 月发布；主题“转折”，调查 161 个产业公会",
       "en": "Chinese National Federation of Industries, 2026 White Paper, published August 2026; theme “Turning Point,” surveying 161 industry associations"},
      {"tw": "Haddington Dynamics 7-Axis Robotic Arm、Production End-of-Arm-Tooling、Harvestance Customized Cobot Gripper：Markforged 官方 Application Spotlight",
       "cn": "Haddington Dynamics 7-Axis Robotic Arm、Production End-of-Arm-Tooling、Harvestance Customized Cobot Gripper：Markforged 官方 Application Spotlight",
       "en": "Haddington Dynamics 7-Axis Robotic Arm; Production End-of-Arm-Tooling; Harvestance Customized Cobot Gripper — Markforged official Application Spotlights"},
    ],
}

FTR = {
    "about": {"tw": "Markforged, Inc. 為工業級積層製造系統供應商，以連續纖維複合材料與金屬解決方案，供製造企業於生產現場自主生產功能性零件、工裝與備品。",
              "cn": "Markforged, Inc. 为工业级增材制造系统供应商，以连续纤维复合材料与金属解决方案，供制造企业于生产现场自主生产功能性零件、工装与备品。",
              "en": "Markforged, Inc. supplies industrial additive manufacturing systems, using continuous fibre composite and metal solutions to enable manufacturers to produce functional parts, tooling and spares on their own floor."},
    "back": {"tw": "← 回到 News &amp; Insights", "cn": "← 回到 News &amp; Insights",
             "en": "← Back to News &amp; Insights"},
}


# ── G5 引言白名單 ────────────────────────────────────────────────────
# 只有 Brian 2026-09-07 親口說過的兩段話可以加引號掛他的名字。
# 任何引號內文字若不在此白名單（或 DOC_TERMS）內，build 直接失敗。
APPROVED_QUOTES = {
    "tw": ["AI 目前的蓬勃發展集中在軟體、晶片與算力。真正的致勝關鍵此刻正在發生，而未來最重要的一件事，是 AI 的實體化。",
           "現階段的產業討論高度集中於 AI 輔助設計、協助設計及各類延伸應用。但真正最大的挑戰是 AI 實體化——把軟體變成硬體，把虛擬的東西變成實體。"],
    "cn": ["AI 目前的蓬勃发展集中在软件、芯片与算力。真正的致胜关键此刻正在发生，而未来最重要的一件事，是 AI 的实体化。",
           "现阶段的产业讨论高度集中于 AI 辅助设计、协助设计及各类延伸应用。但真正最大的挑战是 AI 实体化——把软件变成硬件，把虚拟的东西变成实体。"],
    "en": ["The current surge in AI is concentrated in software, silicon and compute. The decisive factor is being settled right now, and the single most important thing ahead is the physical realisation of AI.",
           "Industry discussion right now is heavily concentrated on AI-assisted design, design support and the applications that extend from them,",
           "But the real challenge is the physical realisation of AI — turning software into hardware, turning the virtual into the physical."],
}

# 引用自公開文件的專有名詞，非個人引言
DOC_TERMS = ["人形機器人本體", "核心零部件自主化", "重科技、輕傳產", "轉折", "人機共生，產需共融",
             "人形机器人本体", "核心零部件自主化", "重科技、轻传产", "转折", "人机共生，产需共融",
             "Turning Point", "Human-Robot Coexistence"]

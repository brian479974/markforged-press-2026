# -*- coding: utf-8 -*-
"""Sidus Space 低軌衛星影片 — 三語內容源（繁中 / 簡中 / English 的唯一真相）。

2026-09-16 建立。Brian 交辦：把 Markforged × Sidus Space 影片放上 news.markforged.tw，
切角＝近期熱門的低軌衛星。

引言政策（G5 冒名引言閘）：
  本文**沒有任何一句話掛在 Brian 名下**。兩處直接引言都是影片受訪者的原話，
  逐字取自 Markforged 官方影片，並附時間出處：
    Carol Craig（Sidus Space 創辦人暨執行長）— 原片 6:50
    Tony Boschi（Sidus Space 首席設計審查）   — 原片 3:15
  其餘一律敘述體。

事實出處：
  · 影片內容 — Markforged 官方 YouTube《We 3D Printed a Satellite with Sidus Space.》
  · 在軌狀態 — Sidus Space 投資人公告（2026-09-16 查證）
      LizzieSat-1 2024-03 / -2 2024-12 / -3 2025-03-14（Transporter-13, LEO, Vandenberg）
      下一顆 Transporter-18, Vandenberg, NET 2026-10
  · Onyx FR-A + Carbon Fiber FR-A NCAMP — MF-GCR/60_Products/support/Application-Quick-Map.md
  ⚠️ 原片字卡寫「2023 年發射」已過時；本文以在軌現況陳述，並在來源區標明。

圖片：全部取自 Markforged 官方影片畫格（原廠素材，非 AI 生成）。
"""

LANGS = ("tw", "cn", "en")

V_TW = "https://drive.google.com/file/d/1aqlqCfCoqD32d3k1uVY8gv0qMUa_Cw5D/view"
V_SC = "https://drive.google.com/file/d/173ImdF_fv3M1Kpm6f4tBT2iC5IM80Igx/view"
V_EN = "https://drive.google.com/file/d/1GkDlACC91STyimQfGBwiboOnvXc-xPF9/view"
YT_WATCH = "https://youtu.be/QQLlK5pETtA"
# Drive 內嵌播放器（檔案已設 anyone/reader，可直接在頁面播放）
E_TW = "https://drive.google.com/file/d/1aqlqCfCoqD32d3k1uVY8gv0qMUa_Cw5D/preview"
E_SC = "https://drive.google.com/file/d/173ImdF_fv3M1Kpm6f4tBT2iC5IM80Igx/preview"
E_EN = "https://drive.google.com/file/d/1GkDlACC91STyimQfGBwiboOnvXc-xPF9/preview"

META = {
    "lang_attr": {"tw": "zh-TW", "cn": "zh-CN", "en": "en"},
    "file": {"tw": "sidus-satellite.html",
             "cn": "sidus-satellite-sc.html",
             "en": "sidus-satellite-en.html"},
    "hero": "images/sidus-leo-orbit.jpg",
    "og_image": "https://news.markforged.tw/images/sidus-leo-orbit.jpg",
    "title": {
        "tw": "我們 3D 列印了一顆衛星：Sidus Space 的低軌衛星 LizzieSat — Markforged",
        "cn": "我们 3D 打印了一颗卫星：Sidus Space 的低轨卫星 LizzieSat — Markforged",
        "en": "We 3D Printed a Satellite: Sidus Space's LEO satellite LizzieSat — Markforged",
    },
    "desc": {
        "tw": "三顆 LizzieSat 已在低軌運行。Sidus Space 用連續碳纖維與 Onyx 印出整顆衛星的結構，"
              "材料先在國際太空站外部掛了一年、零劣化。附繁中／簡中／英文字幕精華影片。",
        "cn": "三颗 LizzieSat 已在低轨运行。Sidus Space 用连续碳纤维与 Onyx 打印出整颗卫星的结构，"
              "材料先在国际空间站外部挂了一年、零劣化。附繁中／简中／英文字幕精华视频。",
        "en": "Three LizzieSats are already operating in low Earth orbit. Sidus Space printed the "
              "satellite's structure in continuous carbon fiber and Onyx — after the material spent "
              "a year outside the International Space Station with no degradation.",
    },
    "og_title": {
        "tw": "我們 3D 列印了一顆衛星：Sidus Space 的低軌衛星 LizzieSat",
        "cn": "我们 3D 打印了一颗卫星：Sidus Space 的低轨卫星 LizzieSat",
        "en": "We 3D Printed a Satellite: Sidus Space's LEO satellite LizzieSat",
    },
    "og_desc": {
        "tw": "材料在國際太空站外部掛了一年，取回後與剛下機台的件看不出差別。",
        "cn": "材料在国际空间站外部挂了一年，取回后与刚下机器的件看不出差别。",
        "en": "The material spent a year outside the ISS and came back indistinguishable from a "
              "part fresh off the machine.",
    },
}

UI = {
    "hdr_ev": {"tw": "大中華區媒體中心<br>News &amp; Insights",
               "cn": "大中华区媒体中心<br>News &amp; Insights",
               "en": "Greater China Media Hub<br>News &amp; Insights"},
    "switch_label": {"tw": "語言", "cn": "语言", "en": "Language"},
    "hero_alt": {
        "tw": "地球低軌道上運行中的衛星群示意畫面",
        "cn": "地球低轨道上运行中的卫星群示意画面",
        "en": "Satellites operating in low Earth orbit"},
    "hero_kicker": {"tw": "產業案例 · 低軌衛星", "cn": "产业案例 · 低轨卫星",
                    "en": "Case Study · LEO Satellites"},
    "hero_title": {
        "tw": "我們 3D 列印了一顆衛星",
        "cn": "我们 3D 打印了一颗卫星",
        "en": "We 3D Printed a Satellite"},
    "hero_meta": {
        "tw": "Sidus Space × Markforged ｜ LizzieSat ｜ 2026.09.16",
        "cn": "Sidus Space × Markforged ｜ LizzieSat ｜ 2026.09.16",
        "en": "Sidus Space × Markforged | LizzieSat | 2026.09.16"},
    "ds_l": {"tw": "三顆 LizzieSat 已在低軌運行",
             "cn": "三颗 LizzieSat 已在低轨运行",
             "en": "Three LizzieSats already operating in LEO"},
    "ds_r": {"tw": "下一顆排 SpaceX Transporter-18，最快 2026 年 10 月",
             "cn": "下一颗排 SpaceX Transporter-18，最快 2026 年 10 月",
             "en": "Next on SpaceX Transporter-18, no earlier than October 2026"},
}

LEAD = {
    "p1": {
        "tw": "低軌衛星是這兩年製造業最擁擠的賽道之一。台灣、中國與越南都在組供應鏈，"
              "但多數討論停在通訊酬載與地面設備，很少有人談<strong>衛星本體的結構要怎麼造</strong>。",
        "cn": "低轨卫星是这两年制造业最拥挤的赛道之一。台湾、中国与越南都在组供应链，"
              "但多数讨论停在通信载荷与地面设备，很少有人谈<strong>卫星本体的结构要怎么造</strong>。",
        "en": "LEO satellites are one of the most crowded races in manufacturing right now. Supply "
              "chains are forming across Taiwan, China and Vietnam, but most of the conversation "
              "stops at communications payloads and ground equipment. Far less of it asks "
              "<strong>how the satellite's own structure gets built</strong>.",
    },
    "p2": {
        "tw": "美國衛星製造商 Sidus Space 給了一個具體答案：整顆衛星的結構用連續碳纖維與 Onyx 列印，"
              "而且不是實驗品 —— LizzieSat-1、-2、-3 已經在低軌道上運行。",
        "cn": "美国卫星制造商 Sidus Space 给了一个具体答案：整颗卫星的结构用连续碳纤维与 Onyx 打印，"
              "而且不是实验品 —— LizzieSat-1、-2、-3 已经在低轨道上运行。",
        "en": "US satellite manufacturer Sidus Space has a concrete answer: print the entire "
              "structure in continuous carbon fiber and Onyx. And it is not an experiment — "
              "LizzieSat-1, -2 and -3 are already operating in low Earth orbit.",
    },
}

QUOTE = {
    "text": {
        "tw": "「老實說，如果沒有 Markforged，我不認為我們會在做這件事。」",
        "cn": "“老实说，如果没有 Markforged，我不认为我们会在做这件事。”",
        "en": "“I don't think we would be doing this if it wasn't for Markforged, honestly.”",
    },
    "attr": {
        "tw": "Carol Craig ｜ Sidus Space 創辦人暨執行長",
        "cn": "Carol Craig ｜ Sidus Space 创始人兼首席执行官",
        "en": "Carol Craig | Founder and CEO, Sidus Space",
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
    {"tw": "低軌衛星", "cn": "低轨卫星", "en": "LEO Satellites", "solid": True},
    {"tw": "連續碳纖維", "cn": "连续碳纤维", "en": "Continuous Carbon Fiber", "solid": True},
    {"tw": "Onyx FR-A", "cn": "Onyx FR-A", "en": "Onyx FR-A", "solid": False},
    {"tw": "航太", "cn": "航空航天", "en": "Aerospace", "solid": False},
    {"tw": "輕量化", "cn": "轻量化", "en": "Lightweighting", "solid": False},
]

BLOCKS = [
    {
        "kind": "sec",
        "h2": {"tw": "為什麼衛星結構特別難", "cn": "为什么卫星结构特别难",
               "en": "Why satellite structures are hard"},
        "h3": {"tw": "整顆衛星不能超過 100 公斤，而結構每減一公克，酬載就多一公克",
               "cn": "整颗卫星不能超过 100 公斤，而结构每减一克，载荷就多一克",
               "en": "The whole satellite must stay under 100 kg — and every gram out of the "
                     "structure is a gram of payload in"},
        "paras": [
            {"tw": "衛星的重量上限是硬的。電池、電腦與各種必要元件本來就吃掉大部分配額，"
                   "留給結構的空間很窄。Sidus Space 的設計工程師在片中說明，"
                   "他們的作法不只是把零件做輕，而是連結構本身的設計一起改 —— "
                   "減下來的每一分重量，直接換成可以多裝的酬載。",
             "cn": "卫星的重量上限是硬的。电池、计算机与各种必要元件本来就吃掉大部分配额，"
                   "留给结构的空间很窄。Sidus Space 的设计工程师在片中说明，"
                   "他们的做法不只是把零件做轻，而是连结构本身的设计一起改 —— "
                   "减下来的每一分重量，直接换成可以多装的载荷。",
             "en": "The mass budget is hard-capped. Batteries, computers and the rest of the bus "
                   "already consume most of it, leaving very little for structure. Sidus Space's "
                   "design engineer explains in the film that their approach is not only to make "
                   "parts lighter but to change the structure itself — every gram taken out becomes "
                   "a gram of payload."},
            {"tw": "而發射與在軌環境並不寬容：發射瞬間要承受 5G 負載，入軌後要面對太陽輻射，"
                   "以及向陽面與背陽面之間的劇烈溫差。",
             "cn": "而发射与在轨环境并不宽容：发射瞬间要承受 5G 载荷，入轨后要面对太阳辐射，"
                   "以及向阳面与背阳面之间的剧烈温差。",
             "en": "And neither launch nor orbit is forgiving: 5 g of load at launch, then solar "
                   "radiation and severe temperature swings between the sunlit and shadowed sides."},
        ],
        "hl": [
            {"b": {"tw": "3 顆在軌", "cn": "3 颗在轨", "en": "3 IN ORBIT"},
             "s": {"tw": "LizzieSat-1、-2、-3 已在低軌運行；下一顆排 SpaceX Transporter-18，"
                         "最快 2026 年 10 月自 Vandenberg 發射",
                   "cn": "LizzieSat-1、-2、-3 已在低轨运行；下一颗排 SpaceX Transporter-18，"
                         "最快 2026 年 10 月自 Vandenberg 发射",
                   "en": "LizzieSat-1, -2 and -3 are operating in LEO; the next is on SpaceX "
                         "Transporter-18, NET October 2026 from Vandenberg"}},
            {"b": {"tw": "強度接近鋁", "cn": "强度接近铝", "en": "STRENGTH ≈ ALUMINIUM"},
             "s": {"tw": "連續碳纖維貫穿整個衛星結構，片中原話是 strength similar to aluminum",
                   "cn": "连续碳纤维贯穿整个卫星结构，片中原话是 strength similar to aluminum",
                   "en": "Continuous carbon fiber runs through the entire structure — their words: "
                         "strength similar to aluminum"}},
        ],
    },
    {
        "kind": "img_full",
        "img": "images/sidus-onyx-iss-experiment.jpg",
        "alt": {"tw": "以 Onyx 列印的樣品固定架，裝載於送上國際太空站的材料曝露實驗模組",
                "cn": "以 Onyx 打印的样品固定架，装载于送上国际空间站的材料暴露实验模组",
                "en": "Sample holders printed in Onyx, mounted in the materials exposure experiment "
                      "flown to the International Space Station"},
        "cap": {"tw": "以 Onyx 快速打樣的樣品固定架，隨材料曝露實驗送上國際太空站。畫面：Markforged",
                "cn": "以 Onyx 快速打样的样品固定架，随材料暴露实验送上国际空间站。画面：Markforged",
                "en": "Sample holders rapid-prototyped in Onyx, flown on a materials exposure "
                      "experiment to the ISS. Image: Markforged"},
    },
    {
        "kind": "sec",
        "h2": {"tw": "先有證據，才有衛星", "cn": "先有证据，才有卫星",
               "en": "The evidence came first"},
        "h3": {"tw": "材料在國際太空站外部掛了一年，取回後與剛下機台的件看不出差別",
               "cn": "材料在国际空间站外部挂了一年，取回后与刚下机器的件看不出差别",
               "en": "A year outside the ISS — and the parts came back indistinguishable from new"},
        "paras": [
            {"tw": "LizzieSat 之前，Sidus Space 先做了一個飛行測試平台：用 Onyx 快速打樣出樣品固定架，"
                   "隨材料曝露實驗送上國際太空站，再取回地面檢視。",
             "cn": "LizzieSat 之前，Sidus Space 先做了一个飞行测试平台：用 Onyx 快速打样出样品固定架，"
                   "随材料暴露实验送上国际空间站，再取回地面检视。",
             "en": "Before LizzieSat, Sidus Space built a flight test platform: sample holders "
                   "rapid-prototyped in Onyx, flown on a materials exposure experiment to the ISS, "
                   "then brought back down and inspected."},
            {"tw": "原訂曝露期約 15 週，實際在外面待了整整一年。同一批的白色對照件被太陽曬到明顯劣化，"
                   "Onyx 件則沒有出現任何劣化。",
             "cn": "原订暴露期约 15 周，实际在外面待了整整一年。同一批的白色对照件被太阳晒到明显劣化，"
                   "Onyx 件则没有出现任何劣化。",
             "en": "The exposure was planned for about 15 weeks; it ran a full year. White control "
                   "parts in the same batch degraded visibly under the sun. The Onyx parts showed "
                   "no degradation at all."},
            {"tw": "Sidus Space 首席設計審查 Tony Boschi 在片中形容取回的狀態："
                   "「剛從機台下來的件，跟在太空待了一年的件，沒有差別。」",
             "cn": "Sidus Space 首席设计审查 Tony Boschi 在片中形容取回的状态："
                   "“刚从机器下来的件，跟在太空待了一年的件，没有差别。”",
             "en": "Tony Boschi, Sidus Space's Lead Design Checker, describes what came back: "
                   "“There's no difference between a part that's just come off the machine and "
                   "what's been out in space for a year.”"},
        ],
        "hl": [
            {"b": {"tw": "365 天", "cn": "365 天", "en": "365 DAYS"},
             "s": {"tw": "原訂約 15 週的曝露期，實際在國際太空站外部待了一年",
                   "cn": "原订约 15 周的暴露期，实际在国际空间站外部待了一年",
                   "en": "An exposure planned for roughly 15 weeks ran a full year outside the ISS"}},
            {"b": {"tw": "零劣化", "cn": "零劣化", "en": "NO DEGRADATION"},
             "s": {"tw": "同批白色對照件明顯劣化，Onyx 件未出現任何劣化",
                   "cn": "同批白色对照件明显劣化，Onyx 件未出现任何劣化",
                   "en": "White control parts in the same batch degraded visibly; the Onyx parts "
                         "did not"}},
        ],
        "paras_after": [
            {"tw": "這份結果才是 LizzieSat 把 Markforged 當成結構基礎的理由 —— 順序是先有飛行驗證，才有衛星。",
             "cn": "这份结果才是 LizzieSat 把 Markforged 当成结构基础的理由 —— 顺序是先有飞行验证，才有卫星。",
             "en": "That result is why LizzieSat uses Markforged as its structural base. The order "
                   "matters: flight evidence first, satellite second."},
        ],
    },
    {
        "kind": "img_2col",
        "imgs": ["images/sidus-satellite-assembly.jpg", "images/sidus-printed-structure.jpg"],
        "alts": [
            {"tw": "衛星酬載模組組裝中，framework 採列印件",
             "cn": "卫星载荷模组组装中，框架采用打印件",
             "en": "A satellite payload module during assembly, built on printed structure"},
            {"tw": "列印結構件上的金屬嵌入孔特寫",
             "cn": "打印结构件上的金属嵌入孔特写",
             "en": "Close-up of a metal insert in a printed structural part"},
        ],
        "cap": {"tw": "左：酬載模組組裝。右：列印結構件的嵌入孔特寫。畫面：Markforged",
                "cn": "左：载荷模组组装。右：打印结构件的嵌入孔特写。画面：Markforged",
                "en": "Left: payload module assembly. Right: a metal insert in a printed structural "
                      "part. Images: Markforged"},
    },
    {
        "kind": "sec",
        "h2": {"tw": "為什麼是列印，不是機加工", "cn": "为什么是打印，不是机加工",
               "en": "Why printing, not machining"},
        "h3": {"tw": "有些幾何機加工做不出來，而設計一改，隔天就有新零件",
               "cn": "有些几何机加工做不出来，而设计一改，隔天就有新零件",
               "en": "Some geometry cannot be machined — and a design change turns into parts "
                     "the next day"},
        "paras": [
            {"tw": "為了拿掉螺絲的重量，Sidus Space 把扣合特徵直接設計進結構件裡：零件落進槽位後自行鎖定，"
                   "鎖上之後就再也拉不開。片中說明，這個特徵的一端可以機加工，另一端則完全做不出來，"
                   "而列印件每一次都能穩定達到需要的公差。",
             "cn": "为了拿掉螺丝的重量，Sidus Space 把扣合特征直接设计进结构件里：零件落进槽位后自行锁定，"
                   "锁上之后就再也拉不开。片中说明，这个特征的一端可以机加工，另一端则完全做不出来，"
                   "而打印件每一次都能稳定达到需要的公差。",
             "en": "To take the weight of screws out of the assembly, Sidus Space designed the "
                   "fastening feature into the structure itself: the part drops into a slot, locks "
                   "in place, and cannot be pulled apart afterwards. As explained in the film, one "
                   "end of that feature could be machined — the other end could never be — and the "
                   "printed parts hit the required tolerance every time."},
            {"tw": "速度是第二個理由。用鋁的話，一個設計變更要走完變更、製造與組裝；"
                   "改用列印，變更當天重印，隔天就有全新零件。",
             "cn": "速度是第二个理由。用铝的话，一个设计变更要走完变更、制造与组装；"
                   "改用打印，变更当天重新打印，隔天就有全新零件。",
             "en": "Speed is the second reason. In aluminium, one design change has to pass through "
                   "redesign, machining and assembly. Printed, the change is reprinted the same day "
                   "and there are brand-new parts the next."},
        ],
        "hl": [
            {"b": {"tw": "比一張紙薄", "cn": "比一张纸薄", "en": "THINNER THAN PAPER"},
             "s": {"tw": "內部鎖固設計的公差裕度：差幾千分之一吋就會鬆脫",
                   "cn": "内部锁固设计的公差裕度：差几千分之一英寸就会松脱",
                   "en": "The locking design's tolerance window: a few thousandths of an inch off "
                         "and it comes apart"}},
            {"b": {"tw": "一天", "cn": "一天", "en": "ONE DAY"},
             "s": {"tw": "設計變更到拿到全新零件所需的時間",
                   "cn": "设计变更到拿到全新零件所需的时间",
                   "en": "From design change to brand-new parts in hand"}},
        ],
    },
    {
        "kind": "sec",
        "h2": {"tw": "材料可追溯性", "cn": "材料可追溯性", "en": "Material traceability"},
        "h3": {"tw": "航太與國防採購要的不只是強度，還要能追回到材料是怎麼做出來的",
               "cn": "航空航天与国防采购要的不只是强度，还要能追回到材料是怎么做出来的",
               "en": "Aerospace and defence buyers need more than strength — they need to trace "
                     "the material back"},
        "paras": [
            {"tw": "Sidus Space 目前以 Onyx FR 阻燃材料列印，並採用 Onyx FR-A。"
                   "FR-A 的 A 代表材料具備完整可追溯性 —— 片中直言，這是許多公司的硬性要求。"
                   "萬一出現分析預期之外的裂紋或剪切，可以一路追回材料的製造過程、找出問題並修正。",
             "cn": "Sidus Space 目前以 Onyx FR 阻燃材料打印，并采用 Onyx FR-A。"
                   "FR-A 的 A 代表材料具备完整可追溯性 —— 片中直言，这是许多公司的硬性要求。"
                   "万一出现分析预期之外的裂纹或剪切，可以一路追回材料的制造过程、找出问题并修正。",
             "en": "Sidus Space now prints with Onyx FR, a fire retardant material, and also uses "
                   "Onyx FR-A. The A designation carries full material traceability — stated plainly "
                   "in the film as a hard requirement at many companies. If a crack or shear appears "
                   "where the analysis said it should not, the material's production history can be "
                   "traced back, the cause found and corrected."},
            {"tw": "值得一併留意的是，Onyx FR-A 與 Carbon Fiber FR-A 已在 Markforged X7 上通過 NCAMP 認證，"
                   "對走航太資格認證流程的製造商而言，這條路徑是現成的。",
             "cn": "值得一并留意的是，Onyx FR-A 与 Carbon Fiber FR-A 已在 Markforged X7 上通过 NCAMP 认证，"
                   "对走航空航天资格认证流程的制造商而言，这条路径是现成的。",
             "en": "Worth noting alongside this: Onyx FR-A and Carbon Fiber FR-A are NCAMP qualified "
                   "on the Markforged X7, which gives manufacturers working through aerospace "
                   "qualification an existing path."},
        ],
    },
    {
        "kind": "video",
        # 主播放器＝我方三語字幕精華版，每個語言頁播自己那一支
        "src": {"tw": E_TW, "cn": E_SC, "en": E_EN},
        "alt": {"tw": "Markforged × Sidus Space 精華版影片，繁體中文字幕",
                "cn": "Markforged × Sidus Space 精华版视频，简体中文字幕",
                "en": "Markforged × Sidus Space highlights film with English subtitles"},
        "cap": {
            "tw": "精華版 4 分 12 秒，繁體中文字幕（本頁版本）。"
                  f"其他語言：<a href=\"{V_SC}\">簡體中文</a>　·　<a href=\"{V_EN}\">English</a>　"
                  f"｜　原始完整影片 7 分 50 秒（英語）：<a href=\"{YT_WATCH}\">Markforged 官方頻道</a>",
            "cn": "精华版 4 分 12 秒，简体中文字幕（本页版本）。"
                  f"其他语言：<a href=\"{V_TW}\">繁体中文</a>　·　<a href=\"{V_EN}\">English</a>　"
                  f"｜　原始完整视频 7 分 50 秒（英语）：<a href=\"{YT_WATCH}\">Markforged 官方频道</a>",
            "en": "The 4:12 highlights cut with English subtitles (this page's version). "
                  f"Other languages: <a href=\"{V_TW}\">Traditional Chinese</a> · "
                  f"<a href=\"{V_SC}\">Simplified Chinese</a> | "
                  f"Full original film, 7:50: <a href=\"{YT_WATCH}\">Markforged official channel</a>",
        },
    },
]

CTA = {
    "h": {"tw": "把這條路徑帶進你的專案",
          "cn": "把这条路径带进你的项目",
          "en": "Bring this path into your programme"},
    "p": {"tw": "低軌衛星、無人機或任何有嚴格重量與環境限制的結構件，"
                "我們可以就材料選擇、認證路徑與導入方式與你的團隊討論。",
          "cn": "低轨卫星、无人机或任何有严格重量与环境限制的结构件，"
                "我们可以就材料选择、认证路径与导入方式与你的团队讨论。",
          "en": "For LEO satellites, UAVs or any structure under hard mass and environmental "
                "constraints, we can walk your team through material selection, qualification "
                "paths and adoption."},
    "btn": {"tw": "聯絡我們", "cn": "联系我们", "en": "Contact us"},
}

SRC = {
    "h": {"tw": "資料來源", "cn": "资料来源", "en": "Sources"},
    "items": [
        {"tw": "Markforged 官方影片《We 3D Printed a Satellite with Sidus Space.》"
               "（2023 年發布）。本文引用的兩處直接引言均逐字取自該片。",
         "cn": "Markforged 官方视频《We 3D Printed a Satellite with Sidus Space.》"
               "（2023 年发布）。本文引用的两处直接引言均逐字取自该片。",
         "en": "Markforged official film, We 3D Printed a Satellite with Sidus Space. (published "
               "2023). Both direct quotations in this article are verbatim from that film."},
        {"tw": "在軌狀態與後續發射時程取自 Sidus Space 投資人公告（2026 年 9 月查證）："
               "LizzieSat-1 於 2024 年 3 月、LizzieSat-2 於 2024 年 12 月、"
               "LizzieSat-3 於 2025 年 3 月 14 日隨 SpaceX Transporter-13 自 Vandenberg 進入低軌；"
               "下一顆排定 SpaceX Transporter-18，最快 2026 年 10 月。",
         "cn": "在轨状态与后续发射时程取自 Sidus Space 投资人公告（2026 年 9 月查证）："
               "LizzieSat-1 于 2024 年 3 月、LizzieSat-2 于 2024 年 12 月、"
               "LizzieSat-3 于 2025 年 3 月 14 日随 SpaceX Transporter-13 自 Vandenberg 进入低轨；"
               "下一颗排定 SpaceX Transporter-18，最快 2026 年 10 月。",
         "en": "In-orbit status and the upcoming launch are from Sidus Space investor announcements "
               "(verified September 2026): LizzieSat-1 in March 2024, LizzieSat-2 in December 2024 "
               "and LizzieSat-3 on 14 March 2025 aboard SpaceX Transporter-13 from Vandenberg; the "
               "next is manifested on SpaceX Transporter-18, no earlier than October 2026."},
        {"tw": "原片中提到的發射時程為發布當時資訊，已非現況；本文一律以上述在軌狀態為準。",
         "cn": "原片中提到的发射时程为发布当时信息，已非现况；本文一律以上述在轨状态为准。",
         "en": "The launch timing mentioned in the film reflects information at the time of "
               "publication and is superseded by the in-orbit status above."},
        {"tw": "Onyx FR-A 與 Carbon Fiber FR-A 的 NCAMP 認證狀態取自 Markforged 材料資料。",
         "cn": "Onyx FR-A 与 Carbon Fiber FR-A 的 NCAMP 认证状态取自 Markforged 材料资料。",
         "en": "NCAMP qualification status for Onyx FR-A and Carbon Fiber FR-A is from Markforged "
               "material documentation."},
        {"tw": "文中圖片均為 Markforged 官方影片畫格。",
         "cn": "文中图片均为 Markforged 官方视频画格。",
         "en": "All images in this article are frames from the official Markforged film."},
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

# G5 冒名引言閘白名單 —— 每一句都要有出處，且本文無任何一句掛在 Brian 名下。
APPROVED_QUOTES = {
    "tw": [
        "老實說，如果沒有 Markforged，我不認為我們會在做這件事。",   # Carol Craig · 原片 6:50
        "剛從機台下來的件，跟在太空待了一年的件，沒有差別。",          # Tony Boschi · 原片 3:15
    ],
    "cn": [
        "老实说，如果没有 Markforged，我不认为我们会在做这件事。",
        "刚从机器下来的件，跟在太空待了一年的件，没有差别。",
    ],
    "en": [
        "I don't think we would be doing this if it wasn't for Markforged, honestly.",
        "There's no difference between a part that's just come off the machine and what's been "
        "out in space for a year.",
    ],
}

DOC_TERMS = ["LizzieSat", "Onyx", "Onyx FR", "Onyx FR-A", "Carbon Fiber FR-A", "NCAMP",
             "Transporter-13", "Transporter-18", "Vandenberg", "Sidus Space", "Markforged",
             "strength similar to aluminum", "We 3D Printed a Satellite with Sidus Space."]

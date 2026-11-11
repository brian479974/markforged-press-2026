# -*- coding: utf-8 -*-
"""本週專題・產業觀點：汽車業的 3D 列印（2026-11-11）— 三語內容源（繁中為底，簡中自動轉、英文另寫）。

Brian：「https://markforged.com/icp/automotive 本週專題報導做一個頁面出來」「產業觀點」→「產業觀點開始做 照你的建議」
（建議＝編輯部專題不署名、首頁只在卡片標本週專題不動結構、沿用全幅版型但精簡成專題感）。

骨架＝原廠汽車產業頁三段（Iterate／Produce／Service Better）＋七類應用。案例逐條對過原廠原文（連結即出處）：
  · Larsen Motorsports（X7，原文明寫）：280 mph 噴射動力直線加速賽車；客製方向盤交期 8→2 天；實測比鋁件硬；Simulation
  · Garry Rogers Motorsport（標 Markforged 平台；原文為 2013 年預購的早期碳纖維機）：澳洲最老車隊；無 CNC；
    剎車導風管母模 1,000 澳幣（約 670 美元）／兩週 → 75 澳幣（約 50 美元）／24 小時；約一半以上為最終使用件
  · Dunlop Systems and Components（標 Markforged 平台；原文為桌上型機種）：外包等兩三週；半年做出的治具比過去五年多；
    整體省下數萬美元；替大型車廠電動車專案做治具
  · GRP（FX10）、Subaru（原文未寫機型，Onyx GF）：同 FX10 活動頁
  · Dana（X7）：百年以上行動產業供應商；七國部署；雲端 Eiger 共用 CAD、列印參數與生產資料（原廠汽車電子書 p.4）；
    Rovereto 治具 >1 年無故障、成本 −70%、交期 −90%
刻意不用：
  ✗ SDHQ Off-Road 的 93%／99%：原廠應用頁寫「快 99%、成本低 93%」，原廠 2026-08 部落格寫「時間少 93%、成本少 99%」，
    兩份原廠資料對調 → 不用；且其機型為 GCR 不推的機種
  ✗ Dunlop 經理的直接引言（網站冒名引言閘；改為敘述）
  ✗ Metal X（Dana、Fort Irwin 原文有，一律不寫機型名）
"""
from urllib.parse import quote

S = "automotive-am-perspective-2026-11"
LANGS = ("tw", "cn", "en")
FILES = {"tw": f"{S}.html", "cn": f"{S}-sc.html", "en": f"{S}-en.html"}
LANG_ATTR = {"tw": "zh-TW", "cn": "zh-CN", "en": "en"}
LANG_NAMES = {"tw": "繁體中文", "cn": "简体中文", "en": "English"}
MAIL = "brian.chen@markforged.com"

URL = {
    "icp": "https://markforged.com/icp/automotive",
    "larsen": "https://markforged.com/resources/case-studies/jet-dragster-teams-replacing-metal-parts-with-3d-printed-composites",
    "grm": "https://markforged.com/resources/case-studies/garry-rogers-motorsport",
    "dunlop": "https://markforged.com/resources/news-events/dunlop",
    "fixture24": "https://markforged.com/resources/blog/the-24-hour-fixture-how-high-performance-automotive-shops-are-bypassing-the-machine-shop",
    "subaru": "https://markforged.com/resources/blog/keeping-the-line-moving-color-coded-tooling-at-subaru",
    "dana": "https://markforged.com/resources/case-studies/dana-incorporated",
    "ebook": "https://web-objects.markforged.com/craft/common/Markforged-Automotive-E-Book.pdf",
}

MAIL_BODY = {
    "tw": "您好，\n\n產業：\n零件或治具用途：\n預計材料：\n所在地區（台灣／中國／香港／越南）：\n\n（如有圖檔請一併附上）\n",
    "cn": "您好，\n\n行业：\n零件或夹具用途：\n预计材料：\n所在地区（台湾／中国／香港／越南）：\n\n（如有图档请一并附上）\n",
    "en": "Hello,\n\nIndustry:\nWhat the part or fixture does:\nIntended material:\nLocation (Taiwan / China / Hong Kong / Vietnam):\n\n(Please attach a file if you have one.)\n",
}
SUBJ = {
    "demo": {"tw": "汽車專題｜預約 FX10 展示／報價", "cn": "汽车专题｜预约 FX10 演示／报价", "en": "Automotive feature | FX10 demo / quote"},
    "part": {"tw": "汽車專題｜寄零件圖檔評估", "cn": "汽车专题｜发零件图档评估", "en": "Automotive feature | part file review"},
}


def mailto(kind, lang):
    return f"mailto:{MAIL}?subject={quote(SUBJ[kind][lang])}&body={quote(MAIL_BODY[lang])}"


META = {
    "title": {"tw": "從研發到售後，汽車業把 3D 列印用在哪裡｜本週專題｜Markforged 媒體中心",
              "cn": "从研发到售后，汽车业把 3D 打印用在哪里｜本周专题｜Markforged 媒体中心",
              "en": "From R&amp;D to Service: Where Automotive Puts 3D Printing to Work | Weekly Feature | Markforged Media Hub"},
    "desc": {"cn": "本周专题・产业观点：依 Markforged 原厂汽车行业资料，拆解汽车业在研发、产线、售后三个环节怎么用 3D 打印，附大众、Larsen Motorsports、Garry Rogers Motorsport、Dunlop、GRP、Subaru、小岛冲压、Dana 原厂案例与大众中文字幕视频。",
             "tw": "本週專題・產業觀點：依 Markforged 原廠汽車產業資料，拆解汽車業在研發、產線、售後三個環節怎麼用 3D 列印，附 Volkswagen、Larsen Motorsports、Garry Rogers Motorsport、Dunlop、GRP、Subaru、小島沖壓、Dana 原廠案例與福斯中文字幕影片。",
             "en": "Weekly feature, industry perspective: how automotive uses 3D printing in R&amp;D, on the line and in service, with Markforged cases from Volkswagen, Larsen Motorsports, Garry Rogers Motorsport, Dunlop, GRP, Subaru, Kojima and Dana."},
    "og_title": {"tw": "從研發到售後，汽車業把 3D 列印用在哪裡", "en": "From R&amp;D to service: where automotive puts 3D printing to work"},
    "og_desc": {"cn": "大众模具吊具 60 公斤减到 4 公斤、喷射赛车方向盘交期 8 天变 2 天、刹车导风管母模两周变 24 小时。",
                "tw": "福斯模具吊具 60 公斤減到 4 公斤、噴射賽車方向盤交期 8 天變 2 天、剎車導風管母模兩週變 24 小時。",
                "en": "Volkswagen die lifters cut from 60 kg to 4, a jet dragster steering wheel in 2 days instead of 8, a brake duct pattern in 24 hours instead of two weeks."},
}

UI = {
    "hdr_ev": {"tw": "大中華區媒體中心<br>News &amp; Insights", "cn": "大中华区媒体中心<br>News &amp; Insights",
               "en": "Greater China Media Hub<br>News &amp; Insights"},
    "switch_label": {"tw": "語言", "cn": "语言", "en": "Language"},
    "read_original": {"tw": "原廠案例（英文）&nbsp;→", "en": "Read the original&nbsp;→"},
    "machine_note": {"tw": "機型照原文標示", "en": "Printer as stated in the source"},
    "hero_alt": {"tw": "Larsen Motorsports 的噴射動力直線加速賽車（Markforged 原廠照片）",
                 "en": "Larsen Motorsports jet dragster (official Markforged photo)"},
}

HERO = {
    "kicker": {"tw": "本週專題 ・ 產業觀點", "cn": "本周专题 ・ 产业观点", "en": "Weekly feature · Industry perspective"},
    "h1": {"tw": "從研發到售後，<br>汽車業把 3D 列印<br>用在哪裡", "cn": "从研发到售后，<br>汽车业把 3D 打印<br>用在哪里",
           "en": "From R&amp;D to service:<br>where automotive puts<br>3D printing to work"},
    "sub": {"tw": "汽車業的 3D 列印，價值不只在原型。Markforged 原廠把它拆成三段：研發迭代、產線製造、售後服務，從三級供應商到整車廠都用得上。本期用八個原廠案例，一段一段看實際做法。",
            "en": "In automotive, 3D printing is worth far more than prototypes. Markforged breaks it into three stages, iterating in R&amp;D, producing on the line and serving in the field, with value that scales from Tier 3 suppliers to OEMs. This week we walk through each stage with eight Markforged cases."},
    "meta": {"tw": "2026.11.11 ｜ 汽車 ｜ 編輯部", "cn": "2026.11.11 ｜ 汽车 ｜ 编辑部", "en": "2026.11.11 | Automotive | Editorial"},
}

CHAIN = {
    "h": {"tw": "原廠的拆法：汽車業的三段價值", "en": "The Markforged view: three stages of value"},
    "items": [
        {"no": "01", "en_big": "Iterate Better", "b": {"tw": "研發", "en": "R&amp;D"},
         "s": {"tw": "迭代更多輪，在量產前把概念與治具修好；過去不敢做的複雜設計，現在做得出來",
               "en": "More iterations to refine concepts and tooling before production, and complex designs you could not reasonably take on before"}},
        {"no": "02", "en_big": "Produce Better", "b": {"tw": "產線", "en": "Production"},
         "s": {"tw": "產線急需的零件在需要時上線，降低停機與重新開治具的風險，以耐用的列印治具取代臨時拼湊的工裝",
               "en": "Production-critical parts on the line when needed, less downtime and retooling risk, and robust printed fixtures in place of makeshift tooling"}},
        {"no": "03", "en_big": "Service Better", "b": {"tw": "售後", "en": "Service"},
         "s": {"tw": "在離需求最近的地方做替換件與服務件，修得更快，服務體驗更好",
               "en": "Replacement and service parts made close to where they are needed, for faster repairs and a better service experience"}},
    ],
}

APPS = {
    "h": {"tw": "汽車產線最常印的治具與工具", "en": "The fixtures and tools automotive lines print most"},
    "src": {"tw": "整理自 Markforged 原廠汽車產業資料", "en": "From Markforged automotive industry material"},
    "groups": [
        {"h": {"tw": "組裝治具", "en": "Assembly jigs and fixtures"},
         "items": {"tw": "車門對位 ・ 儀表板定位 ・ 座椅安裝 ・ 線束佈線 ・ 擋風玻璃與保險桿安裝",
                   "cn": "车门对位 ・ 仪表板定位 ・ 座椅安装 ・ 线束布线 ・ 挡风玻璃与保险杠安装",
                   "en": "Door alignment · Dashboard positioning · Seat mounting · Wiring harness routing · Windshield and bumper installation"}},
        {"h": {"tw": "檢具", "cn": "检具", "en": "Inspection fixtures"},
         "items": {"tw": "段差與間隙量規 ・ 通止規 ・ 孔位檢具 ・ 焊道檢具",
                   "cn": "段差与间隙量规 ・ 通止规 ・ 孔位检具 ・ 焊道检具",
                   "en": "Panel gap and flushness gauges · Go/no-go gauges · Hole location checks · Weld bead inspection"}},
        {"h": {"tw": "製造輔具", "en": "Manufacturing aids"},
         "items": {"tw": "機器人末端工具 ・ 真空吸盤夾爪 ・ 輸送帶導引與分流件 ・ 感測器支架 ・ 遮蔽與噴塗治具",
                   "cn": "机器人末端工具 ・ 真空吸盘夹爪 ・ 输送带导引与分流件 ・ 传感器支架 ・ 遮蔽与喷涂夹具",
                   "en": "Robot end-of-arm tooling · Vacuum grippers · Conveyor guides and diverters · Sensor brackets · Masking and painting tools"}},
        {"h": {"tw": "焊接與黏著治具", "cn": "焊接与粘接夹具", "en": "Welding and bonding fixtures"},
         "items": {"tw": "點焊導引 ・ 黏膠固化治具 ・ 密封膠導引",
                   "cn": "点焊导引 ・ 胶粘剂固化夹具 ・ 密封胶导引",
                   "en": "Spot welding guides · Adhesive curing fixtures · Seam sealing guides"}},
        {"h": {"tw": "維修工具", "cn": "维修工具", "en": "Maintenance and repair tools"},
         "items": {"tw": "客製扳手 ・ 引擎吊架 ・ 剎車碟對位治具 ・ 變速箱對位工具",
                   "cn": "定制扳手 ・ 发动机吊架 ・ 刹车盘对位夹具 ・ 变速箱对位工具",
                   "en": "Custom spanners and wrenches · Engine lifting brackets · Brake rotor alignment jigs · Transmission alignment tools"}},
    ],
}

MACHINE = {"fx10": {"tw": "FX10", "en": "FX10"}, "x7": {"tw": "X7", "en": "X7"},
           "ns": {"tw": "原文未寫機型", "en": "Printer not stated"},
           "platform": {"tw": "Markforged 平台", "en": "Markforged platform"}}

CASES = {
    "larsen": {"img": f"images/{S}-larsen-wheels.jpg", "machine": "x7", "material": "Onyx",
               "alt": {"tw": "原本的鋁製方向盤與 3D 列印的碳纖維複材方向盤", "en": "The original aluminum steering wheel and the 3D printed composite one"},
               "tags": {"tw": "噴射動力直線加速賽 ・ 美國", "en": "Jet dragster racing · U.S."},
               "title": {"tw": "Larsen Motorsports：為一位車手量身做方向盤，交期從 8 天變 2 天",
                         "en": "Larsen Motorsports: a steering wheel fitted to one driver, in 2 days instead of 8"},
               "body": {"tw": "時速 280 英里的噴射動力直線加速賽車，市售蝴蝶型方向盤照標準手型製作，車手 Josette Roach 搆不到關鍵按鍵。車隊改用 X7 以 Onyx 為基材、在受力路徑上鋪連續碳纖維，量身印出方向盤，零件交期從 8 天縮到 2 天；實測比原本的鋁製方向盤更硬，受力時不變形。設計階段先用 Simulation 軟體預測受力，不必實體印十個版本找破壞點。",
                        "en": "A jet dragster runs at 280 mph, and its off-the-shelf butterfly steering wheel is built to standard hand dimensions, so driver Josette Roach could not reliably reach critical controls. The team printed a fitted wheel on an X7, with Onyx as the base and continuous carbon fiber laid along the load paths, cutting part lead time from 8 days to 2. In real-world testing it was stiffer than the aluminum original, which flexed under load. Simulation software predicted the loads up front, so the team did not need to print ten intermediate versions to find the failure point."},
               "metric": {"tw": "8 天 → 2 天", "en": "8 days → 2"}, "url": URL["larsen"]},
    "grm": {"img": f"images/{S}-grm.jpg", "machine": "platform",
            "alt": {"tw": "Garry Rogers Motorsport 賽車", "en": "A Garry Rogers Motorsport race car"},
            "tags": {"tw": "賽車隊 ・ 澳洲", "en": "Racing team · Australia"},
            "title": {"tw": "Garry Rogers Motorsport：剎車導風管母模，從兩週變 24 小時",
                      "en": "Garry Rogers Motorsport: a brake duct pattern in 24 hours instead of two weeks"},
            "body": {"tw": "澳洲歷史最悠久的賽車隊沒有 CNC，複雜的低量零件以往都得外包。工程師依 CFD 模擬建議改出的複雜外形，做一次就是一筆錢和兩週；改用 Markforged 碳纖維列印後，一個剎車導風管的玻璃纖維模具母模，從 1,000 澳幣（約 670 美元）、兩週，變成 75 澳幣（約 50 美元）、24 小時。現在車隊印的零件約一半以上直接裝上車，包括門鎖蓋、變速箱殼、方向盤握把與攝影機座。",
                     "en": "Australia's oldest motorsport team has no CNC machining, so low-volume complex parts used to be outsourced. Complex shapes suggested by the engineers' CFD software cost money and two weeks each time. With Markforged carbon fiber printing, a brake duct pattern for a fiberglass mold went from AUD 1,000 (about USD 670) and two weeks to AUD 75 (about USD 50) and 24 hours. Around half or more of what the team now prints is end-use, including door lock covers, gearbox housings, steering wheel handles and camera mounts."},
            "metric": {"tw": "兩週 → 24 小時", "en": "2 weeks → 24 hours"}, "url": URL["grm"]},
    "dunlop": {"img": f"images/{S}-dunlop.jpg", "machine": "platform",
               "alt": {"tw": "Dunlop Systems and Components 廠區", "en": "Dunlop Systems and Components site"},
               "tags": {"tw": "汽車零組件 ・ 英國", "en": "Automotive components · U.K."},
               "title": {"tw": "Dunlop Systems and Components：治具自己做，半年做出的比過去五年還多",
                         "en": "Dunlop Systems and Components: more tooling in six months than in the previous five years"},
               "body": {"tw": "英國汽車零組件廠 Dunlop 過去把內部與客戶用治具外包，一等就是兩三週，客戶一改規格又要重來，團隊成了瓶頸。改用 Markforged 以 Onyx 與連續碳纖維自己列印治具後，近六個月做出的治具比過去五年還多，整體省下數萬美元；替一家大型車廠打造電動車時，專用治具也是自己印的。",
                        "en": "U.K. automotive component maker Dunlop used to outsource internal and customer tooling, waiting two or three weeks each time, only for the customer to change the spec. Printing its own tooling in Onyx and continuous carbon fiber on Markforged, the team produced more tooling in six months than in the previous five years and saved tens of thousands of dollars; when it helped build an electric vehicle for a large automaker, the custom tooling was printed in-house too."},
               "metric": {"tw": "半年 ＞ 五年", "en": "6 months > 5 years"}, "url": URL["dunlop"]},
    "grp": {"img": "images/fx10-it-starts-here-case-grp.jpg", "machine": "fx10",
            "alt": {"tw": "GRP 為 Lamborghini Revuelto 製作的 X-pipe 排氣管", "en": "GRP's X-pipe exhaust for a Lamborghini Revuelto"},
            "tags": {"tw": "超跑改裝 ・ 美國", "en": "Supercar fabrication · U.S."},
            "title": {"tw": "Graham Rahal Performance：手工 20–40 小時的治具，改成隔夜印好",
                      "en": "Graham Rahal Performance: fixtures printed overnight instead of 20–40 hours by hand"},
            "body": {"tw": "超跑改裝廠 GRP 以 FX10 印複材與金屬治具，CAD 畫好、隔夜印完、隔天就用，把過去花在手工治具的數百小時拿回來做工程與交車。",
                     "en": "Supercar fabricator GRP prints composite and metal fixtures on the FX10: designed in CAD, printed overnight, used the next day, reclaiming hundreds of hours once spent hand-building fixtures."},
            "metric": {"tw": "20–40 小時 → 隔夜", "en": "20–40 hrs → overnight"}, "url": URL["fixture24"]},
    "subaru": {"img": "images/fx10-it-starts-here-case-subaru.jpg", "machine": "ns", "material": "Onyx GF",
               "alt": {"tw": "Subaru 印第安納廠組裝線", "en": "Assembly line at Subaru of Indiana Automotive"},
               "tags": {"tw": "整車組裝 ・ 美國", "en": "Vehicle assembly · U.S."},
               "title": {"tw": "Subaru of Indiana：多車型共線，用顏色分辨治具", "en": "Subaru of Indiana: telling jigs apart by color on a mixed-model line"},
               "body": {"tw": "同一條線同時組裝多個車型，治具之間只差幾公釐；改用六色 Onyx GF 後，每個車型配一種顏色，作業員第一次伸手就拿對，保險桿 QR 標籤定位治具精度 0.1 mm。",
                        "en": "Several models share one line and their jigs differ by millimeters. Printed in six-color Onyx GF, each model gets its own color, so operators grab the right tool on the first pass; the bumper QR-label jigs hold 0.1 mm."},
               "metric": {"tw": "0.1 mm", "en": "0.1 mm"}, "url": URL["subaru"]},
    "vw": {"img": f"images/{S}-vw-card.jpg", "machine": "platform", "featured": True,
           "alt": {"tw": "Volkswagen Autoeuropa 沖壓區的模具吊具", "cn": "大众 Autoeuropa 冲压车间的模具吊具", "en": "A die lifter in the Volkswagen Autoeuropa stamping area"},
           "tags": {"tw": "整車廠 ・ 葡萄牙", "cn": "整车厂 ・ 葡萄牙", "en": "Vehicle plant · Portugal"},
           "title": {"tw": "Volkswagen Autoeuropa：沖壓區的模具吊具，從 60 公斤減到 4 公斤",
                     "cn": "大众 Autoeuropa：冲压车间的模具吊具，从 60 公斤减到 4 公斤",
                     "en": "Volkswagen Autoeuropa: die lifters cut from 60 kg to 4 kg"},
           "body": {"tw": "福斯葡萄牙帕爾梅拉廠 2014 年導入 3D 列印，2024 年 6 月再導入連續碳纖維列印。第一個成功案例在沖壓區：模具吊具從 60 公斤減到 4 公斤，同時改善人因、效率與永續性。之後陸續推到車身廠的 Y 型管接頭、塗裝廠機器人用的耐化學高張力環、物流的通用料盤，並準備推廣到整個福斯集團。",
                    "cn": "大众葡萄牙帕尔梅拉工厂 2014 年引入 3D 打印，2024 年 6 月再引入连续碳纤维打印。第一个成功案例在冲压车间：模具吊具从 60 公斤减到 4 公斤，同时改善人体工程学、效率与可持续性。之后陆续推广到车身车间的 Y 型管接头、涂装车间机器人用的耐化学高张力环、物流的通用料盘，并准备推广到整个大众集团。",
                    "en": "Volkswagen's Palmela plant in Portugal introduced 3D printing in 2014 and continuous carbon fiber printing in June 2024. The first success was in stamping: die lifters went from 60 kg to just 4, improving ergonomics, efficiency and sustainability. It has since spread to a Y-connector for pipes in the body shop, a chemically resistant high-tension ring for paint shop robots and a universal tray in logistics, ready to be transferred across the Volkswagen Group."},
           "metric": {"tw": "60 公斤 → 4 公斤", "cn": "60 公斤 → 4 公斤", "en": "60 kg → 4 kg"},
           "url": "https://www.youtube.com/watch?v=0GITnf0jLDM",
           "url_label": {"tw": "公開影片（YouTube）&nbsp;→", "cn": "公开视频（YouTube）&nbsp;→", "en": "Public video (YouTube)&nbsp;→"},
           "extra": {"tw": '<a href="europe-oem-continuous-fiber-vw-claas-thyssenkrupp.html">本站專文：三家歐洲大廠的連續纖維現場&nbsp;→</a>',
                     "en": '<a href="europe-oem-continuous-fiber-vw-claas-thyssenkrupp-en.html">Our story: continuous fiber at three European manufacturers&nbsp;→</a>'}},
    "kojima": {"img": "images/kojima-robot-hands-card.jpg", "machine": "platform",
               "alt": {"tw": "小島沖壓工業以 3D 列印製作的機器人夾爪", "en": "Robot hands 3D printed by Kojima Industries"},
               "tags": {"tw": "汽車零組件 ・ 日本", "en": "Automotive components · Japan"},
               "title": {"tw": "小島沖壓工業：機器人夾爪自己印，交期從 14 天變 1 天",
                         "en": "Kojima Industries: in-house robot hands, lead time from 14 days to 1"},
               "body": {"tw": "日本愛知的汽車零組件廠小島沖壓工業，改用 Markforged 3D 列印在廠內製作機器人夾爪；夾爪維持產線所需強度又明顯減重，機器人不必選用過大的規格。零件成本降低 67%，交期從 14 天縮短為 1 天。",
                        "en": "Aichi-based automotive component maker Kojima Industries prints its robot hands in-house on Markforged. The hands keep the strength the line needs while losing weight, so robots no longer have to be oversized. Part cost fell 67% and lead time went from 14 days to 1."},
               "metric": {"tw": "−67% ／ 14 天 → 1 天", "en": "−67% / 14 days → 1"}, "url": "kojima-robot-hands.html",
               "url_lang": {"tw": "kojima-robot-hands.html", "cn": "kojima-robot-hands-sc.html", "en": "kojima-robot-hands-en.html"},
               "url_label": {"tw": "本站專文&nbsp;→", "cn": "本站专文&nbsp;→", "en": "Our full story&nbsp;→"}},
    "dana": {"img": "images/fx10-it-starts-here-case-dana.jpg", "machine": "x7", "featured": True,
             "alt": {"tw": "Dana 以複材列印的工件夾持治具", "en": "Composite workholding fixture printed by Dana"},
             "tags": {"tw": "車用傳動與動力系統 ・ 全球", "en": "Drivetrain and power systems · Global"},
             "title": {"tw": "Dana：七個國家的據點，共用同一套設計與列印參數",
                       "en": "Dana: one set of designs and print settings, shared across seven countries"},
             "body": {"tw": "百年以上的行動產業供應商 Dana 在七個國家部署 Markforged 印表機，透過雲端平台 Eiger 在各地工程據點之間共用 CAD 設計、列印參數與生產資料，需要時就近印出治具與零件。義大利 Rovereto 工程中心用 X7 印的複材治具，上線超過一年沒有故障，每件治具成本降 70%、交期縮短 90%。",
                      "en": "Dana, a mobility supplier with more than a century of history, runs Markforged printers in seven countries and uses the cloud-based Eiger platform to share CAD designs, print settings and production data between engineering hubs, so each site prints tools and parts where they are needed. Composite fixtures printed on an X7 at its Rovereto, Italy engineering center ran for over a year without failure, at 70% lower cost and 90% shorter lead time per fixture."},
             "metric": {"tw": "7 國同步", "en": "7 countries, in sync"}, "url": URL["dana"]},
}

CHAPTERS = [
    {"id": "ch-iterate", "no": "01", "big": "Iterate Better.", "h": {"tw": "研發：迭代更快，敢做更複雜的設計", "en": "R&amp;D: faster iterations, bolder designs"},
     "intro": {"tw": "研發階段最貴的是等待。外包一個低量、複雜的零件要等幾週，工程師就少改幾輪。把列印搬進自己的工作室，每一輪迭代從以週計變成以天計。",
               "en": "In R&amp;D, waiting is the most expensive part. Every few weeks spent waiting on an outsourced low-volume part is a few fewer design rounds. Bring printing in-house and each iteration is measured in days, not weeks."},
     "cases": ["larsen", "grm"]},
    {"id": "ch-produce", "no": "02", "big": "Produce Better.", "h": {"tw": "產線：治具不再等外包，停機風險跟著降", "en": "Production: tooling without the wait, and less downtime risk"},
     "intro": {"tw": "產線上最常卡住的往往不是設備，是治具與工裝。外包一次等兩三週，客戶一改規格又要重來。把治具做在廠內，改版當天就能換上線。",
               "en": "What holds up a line is often not the equipment but the fixtures and tooling. Outsourcing means two or three weeks each time, and a spec change starts the clock again. Make fixtures in-house and a revision can be on the line the same day."},
     "video": {"src": {"tw": f"video/{S}-vw-tw.mp4", "cn": f"video/{S}-vw-sc.mp4", "en": f"video/{S}-vw-en.mp4"},
               "poster": f"images/{S}-vw-poster.jpg",
               "cap": {"tw": '影片：Volkswagen Autoeuropa（英文旁白，約 100 秒，中文字幕：Markforged 大中華區）｜<a href="https://www.youtube.com/watch?v=0GITnf0jLDM">公開版本（YouTube）</a>',
                       "cn": '视频：大众 Autoeuropa（英文旁白，约 100 秒，中文字幕：Markforged 大中华区）｜<a href="https://www.youtube.com/watch?v=0GITnf0jLDM">公开版本（YouTube）</a>',
                       "en": 'Film: Volkswagen Autoeuropa (English narration, about 100 seconds) | <a href="https://www.youtube.com/watch?v=0GITnf0jLDM">Public version (YouTube)</a>'}},
     "cases": ["vw", "dunlop", "grp", "subaru", "kojima"]},
    {"id": "ch-service", "no": "03", "big": "Service Better.", "h": {"tw": "售後：替換件做在離需求最近的地方", "en": "Service: replacement parts made close to where they are needed"},
     "intro": {"tw": "原廠的說法是：把售後服務變成競爭優勢。在需要的地點直接做替換件與服務件，維修更快；前提是設計檔與列印參數能在各地同步，每個廠印出來的件都一樣。",
               "en": "The Markforged view is to turn service into a competitive advantage: make replacement and service parts where they are needed for faster repairs. That only works if designs and print settings stay in sync between sites, so every site prints the same part."},
     "cases": ["dana"]},
]

VIEW = {
    "kicker": {"tw": "編輯部觀點", "cn": "编辑部观点", "en": "Our take"},
    "h": {"tw": "給大中華區與越南製造業的三個問題", "en": "Three questions for manufacturers in Greater China and Vietnam"},
    "items": [
        {"tw": "你的治具與工裝，外包一次要等多久？規格改一次，又要再等多久？",
         "en": "How long does an outsourced fixture take today, and how long again after a spec change?"},
        {"tw": "產線上有哪些零件，一壞就停整條線？它們有沒有現成的設計檔？",
         "en": "Which parts stop the whole line when they fail, and do you have design files for them?"},
        {"tw": "售後與維修件，有沒有可能在離客戶最近的廠區直接做出來？",
         "en": "Could your service and repair parts be made at the site closest to the customer?"},
    ],
}

ADOPT = {"tw": f'原廠汽車產業頁列出的採用者，包括 Bentley、Porsche、Toyota、Harley-Davidson 等車廠與品牌。<a href="{URL["icp"]}">看原廠汽車產業頁（英文）&nbsp;→</a>',
         "en": f'Adopters listed on the Markforged automotive page include Bentley, Porsche, Toyota and Harley-Davidson. <a href="{URL["icp"]}">See the automotive industry page&nbsp;→</a>'}

CTA = {
    "h": {"tw": "從一個治具開始。", "cn": "从一个夹具开始。", "en": "Start with one fixture."},
    "p": {"tw": "寄一個零件或治具圖檔，我們可以安排測試列印與 FX10 機台展示，並提供報價。來信請附產業、用途、預計材料與所在地區（台灣、中國、香港、越南）。",
          "en": "Send us a part or fixture file and we can arrange a test print and a live FX10 demonstration, and quote it. Tell us your industry, what it does, the material you have in mind and where you are: Taiwan, China, Hong Kong or Vietnam."},
    "btn1": {"tw": "預約展示／索取報價", "cn": "预约演示／索取报价", "en": "Book a demo / Get a quote"},
    "btn2": {"tw": "寄零件圖檔", "cn": "发零件图档", "en": "Send a part file"},
    "more": {"tw": '想看更多 FX10 實績？<a href="fx10-it-starts-here.html">看 FX10 活動頁的九個原廠案例&nbsp;→</a>',
             "cn": '想看更多 FX10 实绩？<a href="fx10-it-starts-here-sc.html">看 FX10 活动页的原厂案例&nbsp;→</a>',
             "en": 'Want more FX10 results? <a href="fx10-it-starts-here-en.html">See nine Markforged cases on the FX10 page&nbsp;→</a>'},
    "ebook": {"tw": f'延伸閱讀：<a href="{URL["ebook"]}">原廠汽車產業電子書（英文 PDF，20 頁）&nbsp;→</a>',
              "cn": f'延伸阅读：<a href="{URL["ebook"]}">原厂汽车行业电子书（英文 PDF，20 页）&nbsp;→</a>',
              "en": f'Further reading: <a href="{URL["ebook"]}">the automotive e-book (PDF, 20 pages)&nbsp;→</a>'},
}

READ = {
    "h": {"tw": "延伸閱讀", "en": "Further reading"},
    "items": [
        {"href": {"tw": "fx10-it-starts-here.html", "cn": "fx10-it-starts-here-sc.html", "en": "fx10-it-starts-here-en.html"},
         "t": {"tw": "不能出錯的零件，從這裡開始：FX10 活動頁", "cn": "不能出错的零件，从这里开始：FX10 活动页", "en": "If it has to work, it starts here: the FX10 page"},
         "s": {"tw": "汽車、航太、國防九個原廠案例", "cn": "汽车与航空航天原厂案例", "en": "Nine Markforged cases"}},
        {"href": {"tw": "europe-oem-continuous-fiber-vw-claas-thyssenkrupp.html", "en": "europe-oem-continuous-fiber-vw-claas-thyssenkrupp-en.html"}, "no_cn": True,
         "t": {"tw": "吊具從 60 公斤減到 4 公斤：三家歐洲大廠的連續纖維現場", "en": "A lifting device cut from 60 kg to 4 kg: continuous fiber at three European manufacturers"},
         "s": {"tw": "Volkswagen、CLAAS、thyssenkrupp", "en": "Volkswagen, CLAAS, thyssenkrupp"}},
        {"href": {"tw": "wescad-fx10-jigs-fixtures.html", "en": "wescad-fx10-jigs-fixtures-en.html"}, "no_cn": True,
         "t": {"tw": "參考治具比銑削便宜最多 75%：德國治具廠 WESCAD 導入 FX10", "en": "Reference fixtures up to 75% cheaper than milling: WESCAD and the FX10"},
         "s": {"tw": "另一個 FX10 治具案例", "en": "Another FX10 fixture case"}},
    ],
}

FTR = {
    "about": {"tw": "本週專題由 Markforged 大中華區媒體中心編輯部整理，架構與案例取自 Markforged 原廠汽車產業頁與原廠案例原文，數字照原文，機型照原文標示。",
              "en": "This weekly feature was compiled by the Markforged Greater China Media Hub from the Markforged automotive industry page and original case studies; figures and printer models are as stated in the sources."},
    "back": {"tw": "返回媒體中心", "cn": "返回媒体中心", "en": "Back to the Media Hub"},
}

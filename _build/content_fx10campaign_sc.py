# -*- coding: utf-8 -*-
"""FX10 活動頁 — 簡中版內容源（2026-11-11）。

Brian 指示：「簡體中文需要另外做把國防內容拿掉」→ 隔一則：「繁體中文 英文 簡體中文都要做啊」。
所以簡中版和繁英版結構不同，不能放進同一支內容源（G2 結構同形閘會擋），另檔產出：
  · 文字以繁中版（content_fx10campaign.py）為唯一來源，OpenCC tw2sp 轉簡＋下方大陸用語表逐條修正
  · 拿掉的國防內容：航太國防篇原廠影片（畫面含夜視裝備、軍車、火箭）、國防段三案（Fort Irwin、
    Cannon 空軍基地、退伍軍人事務部）與其數字卡、國防畫格圖、國防標籤、開場「戰機」一句、
    作者卡與頁尾公司介紹裡的「國防」
  · 保留：汽車三案、航太三案（皆民航／商務航空）、為什麼是 FX10、規格表、延伸閱讀
  · 語言切換列仍列三語（LINK_LANGS），繁英頁也連得到簡中頁
"""
import copy
import opencc

import content_fx10campaign as T

_cv = opencc.OpenCC("tw2sp")

# tw2sp 沒轉或轉錯的大陸用語（長詞先換）
TERMS = [
    ("积层制造", "增材制造"), ("雷射测微器", "激光测微仪"), ("雷射", "激光"),
    ("航太", "航空航天"), ("复材", "复合材料"), ("治具", "夹具"), ("品质", "质量"),
    ("量测", "测量"), ("公厘", "毫米"), ("澳洲民航安全局", "澳大利亚民航安全局"), ("澳洲", "澳大利亚"),
    ("美国联邦航空总署", "美国联邦航空管理局"), ("油电超跑", "混动超跑"), ("一般插座", "普通插座"),
    ("少人看顾", "少人值守"), ("影片画格", "视频画面"), ("隔夜印完", "隔夜打印完成"),
    ("印出", "打印出"), ("印的排气法兰", "打印的排气法兰"), ("同一台印", "同一台打印"),
    ("接口", "界面"),
    # 2026-11-11 逐句讀過後補：tw2sp 轉錯意思的
    ("为内核创建", "为核心建立"), ("具批量追溯", "具批次追溯"), ("批量可追溯", "批次可追溯"),
    ("适航所需文档", "适航所需文件"), ("视频画格", "视频画面"),
    # 大陸慣用說法
    ("私人与商务喷射机", "私人飞机与公务机"), ("展示或索取报价", "演示或索取报价"), ("报导", "报道"),
    ("碳纤维强化", "碳纤维增强"), ("机台外形尺寸", "设备外形尺寸"), ("作业员", "操作员"), ("据点", "基地"),
    ("山林火灾", "森林火灾"), ("保险杆", "保险杠"), ("汽车产业的增材制造", "汽车行业的增材制造"),
    ("核准", "批准"),
    ("工安警示", "安全警示"), ("版本控管", "版本管理"), ("工具板", "工具看板"),
    ("纤维强化", "纤维增强"), ("换一个颜色印", "换一个颜色打印"), ("危险机台", "危险设备"),   # 與本站 CASA 簡中專文標題一致（「一截风管，换来亚太第一张民航增材制造批准」）
]


def cn(s):
    out = _cv.convert(s)
    for a, b in TERMS:
        out = out.replace(a, b)
    # 站內連結改指簡中版（有簡中版的才改）
    out = out.replace('href="casa-additive-airworthiness.html"', 'href="casa-additive-airworthiness-sc.html"')
    out = out.replace('href="fx10-sinter2-bundle.html"', 'href="fx10-sinter2-bundle-sc.html"')
    return out


def fill(node):
    """所有 {"tw": ...} 節點補上 cn。"""
    if isinstance(node, dict):
        if "tw" in node and isinstance(node["tw"], str):
            node["cn"] = cn(node["tw"])
        for v in node.values():
            fill(v)
    elif isinstance(node, list):
        for v in node:
            fill(v)
    return node


LANGS = ("cn",)
LINK_LANGS = ("tw", "cn", "en")
SHOW_SOURCES = False
S = T.S

META = fill(copy.deepcopy(T.META))
META["lang_attr"]["cn"] = "zh-CN"
META["file"]["cn"] = f"{S}-sc.html"
META["title"]["cn"] = "必须可靠的零件，从这里开始：FX10 与汽车、航空航天的六个原厂案例｜Markforged 媒体中心"
META["desc"]["cn"] = ("FX10 把金属与连续碳纤维复合材料放进同一台设备、放在工厂现场。本页整理 Markforged 原厂发布的六个案例："
                      "Graham Rahal Performance、Subaru、Dana、Plane Support、Cabin Management Solutions、"
                      "Hangar One Avionics，附原厂视频。")
META["og_desc"]["cn"] = "汽车：性能关键。航空航天：任务关键。六个原厂案例与原厂视频。"

UI = fill(copy.deepcopy(T.UI))
UI["hero_meta"]["cn"] = "FX10 ｜ 汽车 · 航空航天 ｜ 2026.11.09"
UI["ds_l"]["cn"] = "汽车：性能关键　｜　航空航天：任务关键"
UI["hero_alt"]["cn"] = "FX10 放在工厂现场（Markforged 原厂照片）"

LEAD = fill(copy.deepcopy(T.LEAD))
LEAD["p1"]["cn"] = ("汽车装配线一停，每分钟都是损失；卫星升空没有重来的机会，航班也不会等缺件。"
                    "在这些地方，零件不只要做得出来，还要在需要的时候就在现场，装上去就能用。")
LEAD["p2"]["cn"] = ("<strong>FX10</strong> 是 Markforged 为工厂现场设计的工业级 3D 打印机：以连续碳纤维增强复合材料打印夹具与零件，"
                    "加装 Metal Kit 后，同一台设备也能打印 316L、17-4PH 不锈钢与 H13 工具钢。"
                    "以下是 Markforged 原厂发布的六个汽车与航空航天案例，每一则都附原文链接；"
                    "案例使用的机型按原文标示。")

PROF = fill(copy.deepcopy(T.PROF))
PROF["desc"]["cn"] = "负责 Markforged 在台湾、中国、香港与越南的市场，长期与航空航天与精密制造领域的制造商合作。"

TAGS = [fill(copy.deepcopy(g)) for g in T.TAGS if g["tw"] != "國防"]

# 拿掉國防內容：航太國防篇影片、國防段、國防畫格
_drop_src = {T.MP4_AERO}
BLOCKS = []
for b in copy.deepcopy(T.BLOCKS):
    if b["kind"] == "mp4" and b["src"] in _drop_src:
        continue
    if b["kind"] == "sec" and b["h2"]["tw"].startswith("國防"):
        continue
    if b["kind"] == "img_2col" and any("def-" in x for x in b["imgs"]):
        continue
    BLOCKS.append(fill(b))

for b in BLOCKS:
    if b["kind"] == "sec" and b["h2"]["tw"] == "為什麼是 FX10":
        b["paras"][0]["cn"] = ("上面六个案例的共同点，是零件在要用的地方做出来，不必等外协或等原厂备件。"
                               "FX10 把复合材料与金属两种工艺放进同一台设备，让这件事从一个项目变成产线上的日常。")
        b["hl"][1]["b"]["cn"] = "边打印边测量"
    if b["kind"] == "sec" and b["h2"]["tw"] == "下載與延伸閱讀":
        # WESCAD 沒有簡中版 → 標明連到繁體中文頁
        b["paras"][2]["cn"] = b["paras"][2]["cn"].replace("另一个 FX10 夹具案例。", "另一个 FX10 夹具案例（繁体中文页面）。")

CTA = fill(copy.deepcopy(T.CTA))
CTA["btn"]["cn"] = "发邮件给我们"
CTA["p"]["cn"] = "如果你的产线或维修现场也有不能出错的零件，发一个零件图档给我们，我们可以安排测试打印与设备演示。"

SRC = {"h": {"cn": "资料来源"}, "items": []}

FTR = fill(copy.deepcopy(T.FTR))
FTR["about"]["cn"] = ("Markforged 提供工业级增材制造系统与连续纤维复合材料，应用于航空航天、汽车与精密制造。"
                      "本页由 Markforged 大中华区媒体中心发布；案例与视频来自 Markforged 原厂。")

APPROVED_QUOTES = {"cn": []}
DOC_TERMS = T.DOC_TERMS

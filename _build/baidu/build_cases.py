"""Generate the CASES data block of baidu/index.html from the site's own case library.

Source: ../../case-library.html (same dataset as www.markforged.tw/cases.html: Markforged official
case studies / application spotlights / videos, each with the official link).
Output: rewrites the text between  /* CASES:BEGIN */  and  /* CASES:END */  in ../../baidu/index.html,
and copies the needed case images into ../../baidu/assets/cases/.

Rules for a Baidu (mainland China) landing page — every exclusion below was decided 2026-10-29:
  - official cases only (dealer cases excluded)
  - no defence / military / UAV / space / US-government cases; no media & imaging
  - no case whose core is a discontinued machine (Metal X, PX100 binder jetting, Blacksmith)
  - bullets that mention discontinued machines/materials, ABS/6061 strength comparisons or
    absolute claims (第一/唯一/首個) are dropped; a case with no quantified bullet left is dropped
  - the equipment line lists only current machines (X7 / X7 FE / FX10 / FX20) and their materials
  - traditional Chinese -> simplified + mainland terms (cn_localize logic: terms first, then t2s)
The 15 hand-edited cases (CURATED) keep their wording; their library entries are skipped.

Usage:  ~/gmail-bot/venv3/bin/python3 _build/baidu/build_cases.py
"""
import html, json, os, re, shutil
import opencc

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LIB = os.path.join(ROOT, "case-library.html")
PAGE = os.path.join(ROOT, "baidu", "index.html")
IMG_SRC = os.path.join(ROOT, "images", "cases")
IMG_DST = os.path.join(ROOT, "baidu", "assets", "cases")

T2S = opencc.OpenCC("t2s")
TERMS = [("備品備件", "备件"), ("彈性製造", "柔性制造"), ("矽膠", "硅胶"), ("公克", "克"), ("公尺", "米"), ("偵測", "检测"),
         ("鎖付", "紧固"), ("擠型", "挤压型材"), ("機師", "机加工技师"), ("煞車", "刹车"), ("訓練", "培训"), ("夾治具", "夹具"), ("治具", "夹具"), ("3D 列印", "3D 打印"), ("列印機", "打印机"), ("印表機", "打印机"), ("列印", "打印"),
         ("客製化", "定制"), ("客製", "定制"), ("機臺", "设备"), ("機台", "设备"), ("工具機", "机床"), ("製程", "工艺"),
         ("射出成型", "注塑成型"), ("專案", "项目"), ("數位化", "数字化"), ("數位", "数字"), ("軟體", "软件"), ("硬體", "硬件"),
         ("介面", "界面"), ("網路", "网络"), ("雲端", "云端"), ("檔案", "文件"), ("資料", "数据"), ("品質", "质量"),
         ("最佳化", "优化"), ("雷射", "激光"), ("塑膠", "塑料"), ("支援", "支持"), ("透過", "通过"), ("航太", "航空航天"),
         ("分散式", "分布式"), ("備品", "备件"), ("量測", "测量"), ("程式", "程序"), ("螢幕", "屏幕"), ("伺服器", "服务器"),
         ("影片", "视频"), ("訊號", "信号"), ("積層製造", "增材制造"), ("製造", "制造"), ("交期", "交期"), ("營運", "运营"),
         ("行銷", "营销"), ("採購", "采购"), ("模組", "模块"), ("鈑金", "钣金"), ("碳纖", "碳纤"), ("玻纖", "玻纤")]
PUNCT = [("「", "“"), ("」", "”"), ("『", "‘"), ("』", "’")]


def sc(t):
    for a, b in TERMS:
        t = t.replace(a, b)
    for a, b in PUNCT:
        t = t.replace(a, b)
    return T2S.convert(t)


EOL = re.compile(r"Metal X|Mark Two|Onyx One|Onyx Pro|\bX3\b|\bX5\b|Blacksmith|PX100|Sinter-1|Inconel|Copper|銅|Mark X")
BADCASE = re.compile(r"無人機|美國|軍|國防|衛星|NASA|DARPA|太空|UAV|戰|退伍軍人")
BADBUL = re.compile(r"ABS|6061|可比|強度接近鋁|第一|唯一|首個|首款|官方摘要未列出|競品")
METALWORD = re.compile(r"17-4|H13|316L|不鏽鋼|工具鋼|金屬")
SKIP_SEC = {"國防與公共部門", "媒體與影像"}
# decided by hand 2026-10-29 (see 交接文件 四-5): metal core / Metal X data / no Markforged-driven result / duplicate video
SKIP_TITLES = ("Guhring UK｜金屬增材製造新業務", "Azoth 3D", "Caldwell Manufacturing", "CADDS Group", "Dixie Iron Works",
               "Labman Automation", "Wilson Benesch", "Larsen Motorsports｜噴氣式賽車客制方向盤")
IND = {"航太與太空": "air", "汽車與賽車": "auto", "電子與半導體": "elec", "能源與油氣": "energy", "醫療與生命科學": "medu",
       "食品包裝與消費品": "pack", "機器人與自動化": "robot", "工業製造與工具機": "mfg", "教育與研究": "medu"}
IND_NAME = {"air": "航空", "auto": "汽车", "elec": "电子与半导体", "energy": "能源", "medu": "医疗与教育", "pack": "包装与消费品",
            "robot": "机器人与自动化", "mfg": "工业制造"}
MNC = ("Dana Incorporated", "Siemens", "Vestas", "Brooks Automation", "Canon", "FESTO", "Saint-Gobain", "Wärtsilä", "Eaton",
       "Yamaha", "Suntory", "Stanley Black")
EQ_MAP = {"X7": "X7", "X7 Field Edition": "X7 Field Edition", "FX10": "FX10", "FX20": "FX20", "Onyx": "Onyx", "Onyx FR": "Onyx FR",
          "Onyx ESD": "Onyx ESD", "Onyx GF": "Onyx GF", "Onyx FR-A": "Onyx FR-A", "Continuous Carbon Fiber": "连续碳纤维",
          "Continuous Carbon Fiber FR": "连续碳纤维 FR", "Continuous Carbon Fiber FR-A": "连续碳纤维 FR-A", "Fiberglass": "玻璃纤维",
          "HSHT Fiberglass": "HSHT 高温高强度玻纤", "Aramid Fiber (Kevlar)": "芳纶纤维", "Nylon White": "尼龙白",
          "Smooth TPU 95A": "Smooth TPU 95A", "ULTEM": "ULTEM™ 9085", "Vega": "Vega", "Eiger": "Eiger", "Digital Forge": "Digital Forge",
          "Simulation": "仿真功能", "Digital Source": "Digital Source", "316L Stainless Steel": "316L 不锈钢"}
METAL_ON_FX10 = {"17-4PH Stainless Steel": "17-4PH 不锈钢", "H13 Tool Steel": "H13 工具钢"}

# auto entries get no headline badge: auto-extraction picked baselines (old price / old lead time) and wrong signs
# 15 hand-edited entries (keep wording); "lib" = library title prefix to skip
CURATED = json.load(open(os.path.join(os.path.dirname(__file__), "cases_curated.json"), encoding="utf-8"))


def parse_lib():
    s = open(LIB, encoding="utf-8").read()
    parts = re.split(r'<div class="lib-sec" id="ind-(\d+)">', s)
    out = []
    for k in range(1, len(parts), 2):
        body = parts[k + 1]
        sec = re.search(r"<h2>([^<]+)</h2>", body).group(1)
        for a in re.findall(r'(?s)<article class="lc">(.*?)</article>', body):
            g = lambda p: (re.search(p, a, re.S).group(1) if re.search(p, a, re.S) else "")
            out.append({"sec": sec, "img": g(r'<img src="images/cases/([^"]+)"'), "kind": html.unescape(g(r'<p class="lc-meta"><b>([^<]+)</b>')),
                        "app": html.unescape(g(r'<p class="lc-meta"><b>[^<]+</b>([^<]*)</p>')),
                        "title": html.unescape(re.sub("<[^>]+>", "", g(r"<h3>(.*?)</h3>"))),
                        "bul": [html.unescape(re.sub("<[^>]+>", "", x)) for x in re.findall(r"<li>(.*?)</li>", a)],
                        "eq": html.unescape(g(r'<p class="lc-eq">機台／材料：(.*?)</p>')), "link": g(r'<div class="lc-links"><a href="([^"]+)"')})
    return out


def badge(b):
    m = (re.search(r"(\d+(?:\.\d+)?)\s*%", b) or re.search(r"(\d+(?:\.\d+)?)\s*倍", b) or re.search(r"(1/\d+)", b)
         or re.search(r"([€$£]\s?[\d,]+(?:\.\d+)?)", b) or re.search(r"(\d+(?:\.\d+)?)\s*(天|小时|周)", b))
    if not m:
        return ""
    t = m.group(0).replace(" ", "")
    if t.endswith("%"):
        if re.search(r"节省|降低|减少|缩短|降幅|减轻|下降|降至", b):
            return "−" + t
        if re.search(r"提升|提高|增加|加快", b):
            return "+" + t
    return t


def eqline(eq):
    toks = [x.strip() for x in eq.split("、") if x.strip()]
    keep = [EQ_MAP[t] for t in toks if t in EQ_MAP]
    if "FX10" in toks:
        keep += [METAL_ON_FX10[t] for t in toks if t in METAL_ON_FX10]
    return "、".join(dict.fromkeys(keep))


def main():
    lib = parse_lib()
    skip_titles = set(c["lib"] for c in CURATED if c.get("lib"))
    cases, imgs, dropped = [], set(), []
    for c in CURATED:
        cases.append({k: v for k, v in c.items() if k != "lib"})
    for c in lib:
        why = None
        if c["kind"].startswith("經銷"): why = "dealer"
        elif c["sec"] in SKIP_SEC: why = c["sec"]
        elif BADCASE.search(c["title"] + "".join(c["bul"])): why = "defence/uav/space/us-gov"
        elif "Metal X" in c["eq"] and "Onyx" not in c["eq"] and "Fiber" not in c["eq"]: why = "metal-x core"
        elif any(c["title"].startswith(t) for t in SKIP_TITLES) or "Blacksmith" in c["title"]: why = "by hand"
        elif any(c["title"].startswith(t) for t in skip_titles): why = "curated"
        bul = [sc(b) for b in c["bul"] if not EOL.search(b) and not BADBUL.search(b)
               and not (METALWORD.search(b) and "FX10" not in c["eq"])]
        if not why and not bul: why = "no data"
        if why:
            dropped.append((c["title"], why)); continue
        who, _, desc = c["title"].partition("｜")
        g = IND[c["sec"]]
        tags = (["mnc"] if any(m in who for m in MNC) else [])
        cases.append({"c": tags, "g": g, "img": "assets/cases/" + c["img"], "who": sc(who), "ind": IND_NAME[g] + " · " + sc(c["app"]),
                      "num": "", "t": sc(desc), "b": bul, "cardB": bul[:2], "eq": eqline(c["eq"]),
                      "kind": "客户成功案例" if c["kind"].startswith("客戶") else ("官方视频" if "影片" in c["kind"] else "应用焦点"),
                      "url": c["link"]})
        imgs.add(c["img"])
    os.makedirs(IMG_DST, exist_ok=True)
    for f in sorted(imgs):
        shutil.copy2(os.path.join(IMG_SRC, f), os.path.join(IMG_DST, f))
    js = "  var CASES = " + json.dumps(cases, ensure_ascii=False, indent=1) + ";\n"
    p = open(PAGE, encoding="utf-8").read()
    a, b = p.index("/* CASES:BEGIN */"), p.index("/* CASES:END */")
    p = p[:a] + "/* CASES:BEGIN */\n" + js + "  " + p[b:]
    open(PAGE, "w", encoding="utf-8").write(p)
    from collections import Counter
    print("cases", len(cases), "| mnc", sum("mnc" in c["c"] for c in cases), "| fb", sum("fb" in c["c"] for c in cases))
    print("by industry", dict(Counter(c["g"] for c in cases)))
    print("dropped", len(dropped), dict(Counter(w for _, w in dropped)))


if __name__ == "__main__":
    main()

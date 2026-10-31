"""由媒體中心首頁 index.html 產生英文版首頁 index-en.html（2026-10-26 建立）

為什麼有這支：導覽列的「中｜EN」在媒體中心首頁按 EN，原本只有導覽列變英文，
下面的新聞列表還是中文（首頁沒有英文版）。英文版首頁一律由這支從中文首頁衍生，
不手改 —— 中文首頁新增／修改卡片後重跑一次，英文版才會跟上。

規則：
- 卡片依分類分區、同一類依發佈日期新到舊（news_order.py，2026-10-28 起）；有 -en.html 的才列，連到英文版，標題／摘要取英文文章本身的
  og:title／meta description（不另外翻譯）。沒有英文版的卡片不列。
- 卡片的分類標籤與地點是中文首頁手寫的，英文對照放在下面兩張表；
  遇到表裡沒有的中文 → 直接失敗（exit 1），不准把中文漏進英文頁。
- 產出後檢查可見文字裡不得有任何中文字。

用法：python3 _build/build_hub_en.py      （在 repo 根目錄或任何位置執行皆可）
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / 'index.html', ROOT / 'index-en.html'

TAG_EN = {
    '客戶案例 · 國防': 'Customer Story · Defense',
    '客戶案例 · 汽車治具': 'Customer Story · Automotive Fixtures',
    '客戶案例 · 汽車內裝': 'Customer Story · Automotive Interiors',
    '產業報導 · 歐洲製造': 'Industry News · European Manufacturing',
    '客戶案例 · 軌道交通': 'Customer Story · Rail',
    '產業報導 · 國防後勤': 'Industry News · Defense Logistics',
    '客戶案例 · 汽車零件': 'Customer Story · Automotive Parts',
    '產業分析 · 分散式製造': 'Industry Analysis · Distributed Manufacturing',
    '產業報導 · 國防供應鏈': 'Industry News · Defence Supply Chain',
    '產業報導 · 適航增材製造': 'Industry News · Airworthy Additive Manufacturing',
    '市場觀點 · 供應鏈安全': 'Perspective · Supply-Chain Security',
    '產品方案 · 混合製造': 'Product Solution · Hybrid Manufacturing',
    'Partner · 越南總代理': 'Partner · Vietnam Master Distributor',
    'Partner · 香港獨家代理': 'Partner · Hong Kong Exclusive Distributor',
    '合作簽署 · 廣東中山': 'Partnership · Zhongshan, Guangdong',
    '活動報導 · 廣東': 'Event Report · Guangdong',
    '產業專訪 · Physical AI': 'Interview · Physical AI',
    'Case Study · 低軌衛星': 'Case Study · LEO Satellite',
    '產業觀點 · 生產韌性': 'Industry Insight · Production Resilience',  # 2026-10-31 非紅觀點文 v3（Bella）
}
LOC_EN = {
    '客戶案例 · 台灣': 'Customer Story · Taiwan',
    '客戶案例 · 英國': 'Customer Story · United Kingdom',
    '客戶案例 · 挪威': 'Customer Story · Norway',
    '客戶案例 · 德國': 'Customer Story · Germany',
    '客戶案例 · 日本': 'Customer Story · Japan',
    '產業報導 · 葡萄牙／德國': 'Industry News · Portugal / Germany',
    '客戶案例 · 法國': 'Customer Story · France',
    '產業報導 · 韓國浦項': 'Industry News · Pohang, Korea',
    '客戶案例 · 日本愛知縣': 'Customer Story · Aichi, Japan',
    '產業分析 · 美國 / 大中華區': 'Industry Analysis · US / Greater China',
    '產業報導 · 美國密西根州': 'Industry News · Michigan, USA',
    '產業報導 · 澳洲昆士蘭': 'Industry News · Queensland, Australia',
    '作者觀點 · 台灣': 'Perspective · Taiwan',
    '產業觀點 · 台灣': 'Industry Insight · Taiwan',  # 2026-10-31 非紅觀點文卡片（10-31 首發時漏登，產生器因此一直跑不動）
    '台灣 · 中國 · 香港': 'Taiwan · China · Hong Kong',
    'Liberty Flexible Workspaces，伯斯，澳洲': 'Liberty Flexible Workspaces, Perth, Australia',
    '越南': 'Vietnam',
    '香港': 'Hong Kong',
    'Markforged 大中華區 · 廣東中山': 'Markforged Greater China · Zhongshan, Guangdong',
    'Markforged 大中華區 · 廣東': 'Markforged Greater China · Guangdong',
    '原載 iThome · 台灣': 'Originally published in iThome · Taiwan',
    '台灣 · 中國 · 香港 · 越南': 'Taiwan · China · Hong Kong · Vietnam',
    '軍事技術學院，河內，越南': 'Military Technical Academy, Hanoi, Vietnam',
}
# 卡片標題預設取英文文章的 og:title；og:title 是社群用的另一個切角、跟中文卡片對不上時，在這裡指定
TITLE_EN = {
    'land-forces-2026-executive-roundtable-en.html': 'How long could a nation sustain itself if the chain broke',
}
DESC_EN = ('Official newsroom of Markforged Greater China and Vietnam: press releases, '
           'event reports, customer stories and industry insights.')
# 首頁固定區塊（頁首、回娘家專區、策略報告）的中英對照；每一條都必須剛好命中一次
FIXED = [
    ('<html lang="zh-TW">', '<html lang="en">'),
    ('<a href="index.html" class="nav-brand">', '<a href="index-en.html" class="nav-brand">'),
    ('<p class="hero-subtitle">大中華區暨越南　新聞稿 · 活動報導 · 產業觀點<br>\n'
     '      <span style="opacity:.7;">News, Event Reports &amp; Industry Insights</span></p>',
     '<p class="hero-subtitle">Press Releases · Event Reports · Industry Insights</p>'),
    ('<h2 class="featured-title">AI 實體化時代：NVIDIA GTC 2026 × Markforged<br>戰略藍圖</h2>',
     '<h2 class="featured-title">The Physical AI Era: NVIDIA GTC 2026 × Markforged<br>Strategic Blueprint</h2>'),
    ('<p class="featured-summary">37 頁深度策略報告：從兆元算力基礎設施到廠房車間的實體革命，分析 Markforged 在 AI 實體化時代的策略定位與行動方案。</p>',
     '<p class="featured-summary">A 37-page strategy report, from trillion-dollar compute infrastructure to the physical revolution on the factory floor: where Markforged stands in the Physical AI era, and what it plans to do.</p>'),
    ('下載完整報告 (PDF)', 'Download the full report (PDF, in Chinese)'),
    ('<a href="https://www.markforged.tw/">www.markforged.tw</a>　·　<a href="https://markforged.com"',
     '<a href="https://www.markforged.tw/?lang=en">www.markforged.tw</a> · <a href="https://markforged.com"'),
]
CJK = re.compile(r'[㐀-鿿＀-￯　-〿]')


def fail(msg):
    print('❌ ' + msg)
    sys.exit(1)


def meta(t, pat):
    m = re.search(pat, t)
    return html.unescape(m.group(1)) if m else None


def en_card(block, href, problems):
    """把一張中文卡片換成英文版；回傳 None 代表沒有英文版、不列"""
    en_href = href[:-5] + '-en.html'
    p = ROOT / en_href
    if not p.exists():
        return None
    e = p.read_text(encoding='utf-8')
    title = meta(e, r'<meta property="og:title" content="([^"]*)"') or meta(e, r'<title>([^<]*)</title>')
    desc = meta(e, r'<meta name="description" content="([^"]*)"')
    if not title or not desc:
        problems.append(f'{en_href}：缺 og:title／description')
        return block
    title = TITLE_EN.get(en_href) or re.sub(r'\s+(—|\|)\s+Markforged( Newsroom)?$', '', title)
    out = block.replace(f'href="{href}"', f'href="{en_href}"', 1)

    def sub_one(pat, repl_fn, label):
        nonlocal out
        m = re.search(pat, out, re.S)
        if not m:
            problems.append(f'{href}：找不到{label}')
            return
        out = out[:m.start(1)] + repl_fn(m.group(1)) + out[m.end(1):]

    def tr(table, label):
        def f(zh):
            zh = zh.strip()
            if not CJK.search(zh):
                return zh
            if zh not in table:
                problems.append(f'{href}：{label}「{zh}」沒有英文對照，請加進 {label} 表')
                return zh
            return table[zh]
        return f

    sub_one(r'class="press-tag">([^<]*)<', tr(TAG_EN, 'TAG_EN'), '分類標籤')
    sub_one(r'</svg>\s*([^<]*?)\s*</span>', tr(LOC_EN, 'LOC_EN'), '地點')
    sub_one(r'class="press-card-title">(.*?)</h2>', lambda _: html.escape(title, quote=False), '標題')
    sub_one(r'class="press-card-summary">(.*?)</p>', lambda _: html.escape(desc, quote=False), '摘要')
    return out


def build():
    t = SRC.read_text(encoding='utf-8')
    # 回娘家區塊（PROGRAMS:START～END）由 homecoming 的 stage.py 直接產中英兩版，這裡沿用英文首頁現有那段，不翻譯
    pm = re.compile(r'  <!-- PROGRAMS:START.*?<!-- PROGRAMS:END -->', re.S)
    zh_prog, en_prog = pm.search(t), pm.search(OUT.read_text(encoding='utf-8')) if OUT.exists() else None
    if zh_prog and not en_prog:
        fail('中文首頁有回娘家區塊，英文首頁沒有 —— 先跑 homecoming 的 stage.py 產英文版')
    if zh_prog:
        t = t[:zh_prog.start()] + en_prog.group(0) + t[zh_prog.end():]
    for zh, en in FIXED:
        n = t.count(zh)
        if n != 1:
            fail(f'固定區塊對照命中 {n} 次（應為 1）：{zh[:40]}… —— 中文首頁改版了，請更新 FIXED 表')
        t = t.replace(zh, en)
    # 頁首 meta：<title> 到 <style> 之間整段換成英文版
    head_en = (
        '<title>Markforged Newsroom — Greater China &amp; Vietnam</title>\n'
        f'  <meta name="description" content="{DESC_EN}" />\n'
        '  <meta name="author" content="Markforged Taiwan" />\n'
        '  <meta name="robots" content="index, follow" />\n'
        '  <link rel="canonical" href="https://news.markforged.tw/index-en.html" />\n'
        '  <link rel="alternate" hreflang="zh-Hant" href="https://news.markforged.tw/" />\n'
        '  <link rel="alternate" hreflang="en" href="https://news.markforged.tw/index-en.html" />\n'
        '  <meta property="og:type" content="website" />\n'
        '  <meta property="og:url" content="https://news.markforged.tw/index-en.html" />\n'
        '  <meta property="og:title" content="Markforged Newsroom — Greater China &amp; Vietnam" />\n'
        f'  <meta property="og:description" content="{DESC_EN}" />\n'
        '  <meta property="og:image" content="https://markforged.com/wp-content/uploads/2023/03/FX10-Hero.png" />\n'
        '  <meta property="og:locale" content="en_US" />\n'
        '  <meta property="og:site_name" content="Markforged Taiwan" />\n'
        '  <meta name="twitter:card" content="summary_large_image" />\n'
        '  <meta name="twitter:title" content="Markforged Newsroom — Greater China &amp; Vietnam" />\n'
        f'  <meta name="twitter:description" content="{DESC_EN}" />\n'
        '  <meta name="twitter:image" content="https://markforged.com/wp-content/uploads/2023/03/FX10-Hero.png" />\n'
        '  ')
    t, n = re.subn(r'<title>.*?(?=<style>)', lambda m: head_en, t, count=1, flags=re.S)
    if n != 1:
        fail('頁首找不到 <title> … <style> 區段')
    # 卡片
    problems, kept, dropped = [], [], []
    parts = re.split(r'((?:<!-- CARD:[^>]*-->\s*)?<a href="([^"]+)" class="press-card(?: wide)?">.*?</a>\n)', t, flags=re.S)
    rebuilt = []
    i = 0
    while i < len(parts):
        if i % 3 == 1:
            block, href = parts[i], parts[i + 1]
            new = en_card(block, href, problems)
            if new is None:
                dropped.append(href)
            else:
                kept.append(href)
                rebuilt.append(new)
            i += 2
            continue
        rebuilt.append(parts[i])
        i += 1
    t = ''.join(rebuilt)
    if problems:
        fail('卡片無法轉成英文：\n   ' + '\n   '.join(problems))
    # 依分類分區、同一類依發佈日期新到舊（規則與分類表見 news_order.py／news_categories.json）
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import news_order
    try:
        t, _, _ = news_order.render(t, 'en')
    except news_order.NewsOrderError as ex:
        fail(f'英文首頁分類排序失敗：\n   {ex}')
    if not kept:
        fail('一張英文卡片都沒有，解析一定出錯了')
    # 可見文字不得有中文
    vis = re.sub(r'<(style|script)[^>]*>.*?</\1>', '', t, flags=re.S)
    vis = re.sub(r'<!--.*?-->', '', vis, flags=re.S)
    vis = re.sub(r'<[^>]+>', '\n', vis)
    left = sorted({ln.strip() for ln in vis.split('\n') if CJK.search(ln)})
    attrs = re.findall(r'(?:alt|title|content|aria-label)="([^"]*)"', re.sub(r'<(style|script)[^>]*>.*?</\1>', '', t, flags=re.S))
    left += sorted({a for a in attrs if CJK.search(a)})
    if left:
        fail('英文首頁還有中文：\n   ' + '\n   '.join(left[:20]))
    OUT.write_text(t, encoding='utf-8')
    print(f'✅ index-en.html：列出 {len(kept)} 張英文卡片；沒有英文版、不列 {len(dropped)} 張：{", ".join(dropped)}')


if __name__ == '__main__':
    build()

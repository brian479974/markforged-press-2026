import json, sys
from playwright.sync_api import sync_playwright
URL = sys.argv[1]; OUT = "/tmp/baidu_demo_qa"
import os; os.makedirs(OUT, exist_ok=True)
M_UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1"
res = {}
def T(name, cond, info=""):
    res[name] = bool(cond); print(("PASS " if cond else "FAIL ") + name, info)
with sync_playwright() as p:
    b = p.chromium.launch()
    for mode, kw in [("pc", dict(viewport={"width": 1366, "height": 860})),
                     ("m", dict(user_agent=M_UA, viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True))]:
        ctx = b.new_context(**kw); ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=URL.split("/baidu")[0])
        pg = ctx.new_page(); errs = []
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append(str(e)))
        bad_req = []
        pg.on("requestfailed", lambda r: bad_req.append(r.url) if "hits.sh" not in r.url else None)
        pg.on("response", lambda r: bad_req.append(f"{r.status} {r.url}") if r.status >= 400 and "localhost" in r.url else None)
        pg.goto(URL, wait_until="load"); pg.wait_for_timeout(2600)
        T(f"{mode}: 無橫向溢出", pg.evaluate("document.documentElement.scrollWidth <= innerWidth + 1"), pg.evaluate("[document.documentElement.scrollWidth, innerWidth]"))
        T(f"{mode}: 計數器跑完", pg.evaluate("Array.from(document.querySelectorAll('[data-count]')).map(e=>e.textContent).join('|')") == "10,000|70")
        pg.screenshot(path=f"{OUT}/{mode}_first.png")
        # anchors exist
        missing = pg.evaluate("Array.from(document.querySelectorAll('a[href^=\"#\"]')).map(a=>a.getAttribute('href')).filter(h=>h.length>1 && !document.querySelector(h))")
        T(f"{mode}: 內部錨點都存在", not missing, missing)
        # sticky header stays
        pg.evaluate("scrollTo(0, 2000)"); pg.wait_for_timeout(500)
        T(f"{mode}: 頂欄捲動後仍在畫面頂端", pg.evaluate("Math.round(document.getElementById('hd').getBoundingClientRect().top) === 0"))
        if mode == "m":
            T("m: 底部固定條出現", pg.evaluate("document.getElementById('sticky').classList.contains('show')"))
            pg.click("#burger"); pg.wait_for_timeout(400)
            T("m: 選單展開", pg.evaluate("document.getElementById('nav').classList.contains('open')"))
            pg.screenshot(path=f"{OUT}/m_menu.png")
            pg.click("#nav a[href='#materials']"); pg.wait_for_timeout(900)
            T("m: 點選單後收合並跳到材料", pg.evaluate("!document.getElementById('nav').classList.contains('open') && Math.abs(document.getElementById('materials').getBoundingClientRect().top) < 120"))
        # tabs
        pg.click("[data-tab='p-metal']"); pg.wait_for_timeout(600)
        T(f"{mode}: 材料分頁切換", pg.evaluate("document.getElementById('p-metal').classList.contains('on') && !document.getElementById('p-cf').classList.contains('on')"))
        pg.locator("#materials").screenshot(path=f"{OUT}/{mode}_materials.png")
        # details
        pg.locator(".prod .more summary").first.click(); pg.wait_for_timeout(300)
        T(f"{mode}: 規格展開", pg.evaluate("document.querySelector('.prod .more').open"))
        # form: empty submit
        pg.evaluate("document.getElementById('form').scrollIntoView()"); pg.wait_for_timeout(500)
        pg.click("#lead .submit"); pg.wait_for_timeout(400)
        nbad = pg.evaluate("document.querySelectorAll('#lead .fld.bad').length")
        T(f"{mode}: 空表單送出擋下 6 欄", nbad == 6, nbad)
        T(f"{mode}: 空表單不跳成功", not pg.evaluate("document.getElementById('m-ok').classList.contains('show')"))
        pg.locator("#lead").screenshot(path=f"{OUT}/{mode}_form_err.png")
        # bad phone
        pg.fill("#f-tel", "12345"); pg.locator("#f-tel").blur()
        T(f"{mode}: 錯誤手機號被擋", "11 位" in pg.inner_text("#f-tel ~ .msg"))
        # valid fill + free email hint
        pg.fill("#f-name", "张三"); pg.fill("#f-tel", "13800138000"); pg.fill("#f-wx", "zhangsan_test")
        pg.fill("#f-co", "示范精密机械有限公司"); pg.fill("#f-mail", "test@qq.com"); pg.locator("#f-mail").blur()
        T(f"{mode}: 免費信箱給提示不擋", "公司邮箱" in pg.inner_text("#f-mail ~ .msg") and not pg.evaluate("document.getElementById('f-mail').closest('.fld').classList.contains('bad')"))
        pg.select_option("#f-ind", "工业设备")
        reqs = []
        pg.on("request", lambda r: reqs.append(r.method + " " + r.url))
        pg.click("#lead .submit"); pg.wait_for_timeout(300)
        T(f"{mode}: 未勾隱私不送", not pg.evaluate("document.getElementById('m-ok').classList.contains('show')"))
        pg.check("#f-agree"); pg.click("#lead .submit"); pg.wait_for_timeout(700)
        T(f"{mode}: 有效表單跳成功視窗", pg.evaluate("document.getElementById('m-ok').classList.contains('show')"))
        T(f"{mode}: 送出時沒有任何網路請求", not [r for r in reqs if "hits.sh" not in r], reqs)
        pg.screenshot(path=f"{OUT}/{mode}_ok.png")
        T(f"{mode}: 送出後表單清空", pg.evaluate("document.getElementById('f-name').value === ''"))
        pg.click("#m-ok [data-close]"); pg.wait_for_timeout(300)
        # privacy modal
        pg.click("#agree a"); pg.wait_for_timeout(300)
        T(f"{mode}: 隱私視窗開啟", pg.evaluate("document.getElementById('m-privacy').classList.contains('show')"))
        pg.keyboard.press("Escape"); pg.wait_for_timeout(200)
        # copy wechat
        pg.evaluate("document.getElementById('contact').scrollIntoView()"); pg.wait_for_timeout(400)
        pg.click("[data-copy]"); pg.wait_for_timeout(400)
        T(f"{mode}: 複製微信提示", "brian479974" in pg.inner_text("#toast"))
        # discussion tool
        pg.click("#toolBtn"); pg.check("#showNo"); pg.wait_for_timeout(300)
        T(f"{mode}: 區塊編號顯示 12 個", pg.evaluate("Array.from(document.querySelectorAll('.secno')).filter(e=>getComputedStyle(e).display!=='none').length") == 12)
        pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(500)
        pg.screenshot(path=f"{OUT}/{mode}_secno.png")
        pg.uncheck("#showNo"); pg.click("#toolBtn")
        # zip link
        st = pg.evaluate("fetch('assets/Markforged_landing-page-assets_2026-10-29.zip',{method:'HEAD'}).then(r=>r.status)")
        T(f"{mode}: 素材包可下載", st == 200, st)
        # full page
        pg.evaluate("document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'))"); pg.wait_for_timeout(900)
        pg.add_style_tag(content=".hd{position:relative!important}.sticky,.totop,.tool{display:none!important}")
        pg.screenshot(path=f"{OUT}/{mode}_full.png", full_page=True)
        T(f"{mode}: 無 JS 錯誤", not errs, errs)
        T(f"{mode}: 無失敗請求", not bad_req, bad_req)
        ctx.close()
    b.close()
json.dump(res, open(f"{OUT}/qa.json", "w"), ensure_ascii=False, indent=1)
print("TOTAL", sum(res.values()), "/", len(res))

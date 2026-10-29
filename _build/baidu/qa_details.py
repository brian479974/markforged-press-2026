import sys
from playwright.sync_api import sync_playwright
URL = sys.argv[1]; OUT = "/tmp/baidu_demo_qa"
import os; os.makedirs(OUT, exist_ok=True)
M_UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1"
ok = 0; tot = 0
def T(n, c, i=""):
    global ok, tot; tot += 1; ok += bool(c); print(("PASS " if c else "FAIL ") + n, i if not c else "")
with sync_playwright() as p:
    b = p.chromium.launch()
    for mode, kw in [("pc", dict(viewport={"width": 1366, "height": 860})),
                     ("m", dict(user_agent=M_UA, viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True))]:
        ctx = b.new_context(**kw); pg = ctx.new_page(); errs = []; ext = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("request", lambda r: ext.append(r.url) if ("markforged.com" in r.url) else None)
        pg.goto(URL, wait_until="load"); pg.wait_for_timeout(800)
        for k in ["fx10", "fx20", "x7", "x7fe"]:
            pg.evaluate(f"document.querySelector('.prod [data-prod=\"{k}\"]').scrollIntoView()"); pg.wait_for_timeout(150)
            pg.click(f".prod [data-prod='{k}']"); pg.wait_for_timeout(450)
            rows = pg.evaluate("document.querySelectorAll('#dt table.spec tbody tr').length")
            T(f"{mode}: {k} 詳情開啟且有規格表", pg.evaluate("document.getElementById('m-detail').classList.contains('show')") and rows >= 8, rows)
            if k == "fx10": pg.screenshot(path=f"{OUT}/{mode}_detail_fx10.png")
            if k == "x7":
                pg.click("#dt [data-mat='kevlar']"); pg.wait_for_timeout(400)
                T(f"{mode}: 詳情內點材料跳材料說明", "芳纶" in pg.inner_text("#dt h3"))
                pg.click("#dt [data-prod='x7fe']"); pg.wait_for_timeout(400)
                T(f"{mode}: 材料說明內點機型跳回機型", "X7 Field Edition" in pg.inner_text("#dt h3"))
            pg.click("#m-detail .dt-x"); pg.wait_for_timeout(250)
            T(f"{mode}: {k} 關閉後解鎖捲動", pg.evaluate("document.body.style.overflow===''") and not pg.evaluate("document.getElementById('m-detail').classList.contains('show')"))
        pg.evaluate("document.getElementById('onyxgf').scrollIntoView()"); pg.wait_for_timeout(1500)
        T(f"{mode}: Onyx GF 影片可載入", pg.evaluate("document.querySelector('#onyxgf video').readyState") >= 1, pg.evaluate("document.querySelector('#onyxgf video').readyState"))
        T(f"{mode}: Onyx GF 六色線材圖已載入", pg.evaluate("(()=>{const i=document.querySelector('#onyxgf .ogf-pic img');return i.complete&&i.naturalWidth>0})()"))
        pg.evaluate("document.querySelectorAll('#onyxgf .rv').forEach(e=>e.classList.add('in'))"); pg.wait_for_timeout(900)
        pg.locator("#onyxgf").screenshot(path=f"{OUT}/{mode}_onyxgf.png")
        pg.click("#onyxgf [data-mat='onyx-gf']"); pg.wait_for_timeout(400)
        T(f"{mode}: Onyx GF 材料詳情", "Onyx GF" in pg.inner_text("#dt h3") and pg.evaluate("document.querySelectorAll('#dt .kv div').length") == 5)
        pg.keyboard.press("Escape"); pg.wait_for_timeout(150)
        keys = pg.evaluate("Array.from(document.querySelectorAll('#materials [data-mat]')).map(b=>b.getAttribute('data-mat'))")
        T(f"{mode}: 材料按鈕 14 個", len(keys) == 14, len(keys))
        for k in keys:
            pg.evaluate(f"document.querySelector('#materials [data-mat=\"{k}\"]').closest('.panel').classList.add('on')")
            pg.evaluate(f"document.querySelector('#materials [data-mat=\"{k}\"]').click()"); pg.wait_for_timeout(200)
            good = pg.evaluate("document.getElementById('m-detail').classList.contains('show') && document.querySelectorAll('#dt .al li').length>=3")
            T(f"{mode}: 材料 {k} 說明", good)
            if k == "nylon-white-fs": pg.screenshot(path=f"{OUT}/{mode}_detail_nylon.png")
            pg.keyboard.press("Escape"); pg.wait_for_timeout(120)
        pg.evaluate("document.querySelectorAll('.panel').forEach((p,i)=>p.classList.toggle('on', i===0))")
        pg.evaluate("document.querySelector('.prod [data-prod=\"fx20\"]').click()"); pg.wait_for_timeout(400)
        pg.click("#dt [data-goform]"); pg.wait_for_timeout(1300)
        T(f"{mode}: 詳情內「咨询」關窗並捲到表單", (not pg.evaluate("document.getElementById('m-detail').classList.contains('show')")) and abs(pg.evaluate("document.getElementById('form').getBoundingClientRect().top")) < 140)
        T(f"{mode}: 案例篩選數量 全部15/跨國10/食品6", pg.evaluate("Array.from(document.querySelectorAll('.cf span')).map(x=>x.textContent).join(',')") == "15,10,6", pg.evaluate("Array.from(document.querySelectorAll('.cf span')).map(x=>x.textContent).join(',')"))
        vis = lambda: pg.evaluate("Array.from(document.querySelectorAll('#caseTrack .case')).filter(e=>getComputedStyle(e).display!=='none').length")
        if mode == "pc":
            T("pc: 預設顯示 6 則並有查看全部", vis() == 6 and pg.is_visible("#caseMore"), vis())
            pg.evaluate("document.getElementById('cases').scrollIntoView()"); pg.click("#caseMore"); pg.wait_for_timeout(300)
            T("pc: 查看全部後 15 則", vis() == 15, vis())
        else:
            T("m: 手機預設 15 則可滑", vis() == 15, vis())
        pg.evaluate("document.getElementById('cases').scrollIntoView()"); pg.click(".cf[data-cf='fb']"); pg.wait_for_timeout(300)
        T(f"{mode}: 食品飲料篩選 6 則", vis() == 6, vis())
        pg.click(".cf[data-cf='mnc']"); pg.wait_for_timeout(300)
        T(f"{mode}: 跨國企業篩選 10 則", vis() == 10, vis())
        pg.screenshot(path=f"{OUT}/{mode}_cases_mnc.png")
        pg.locator("#caseTrack .case").first.click(); pg.wait_for_timeout(400)
        T(f"{mode}: 案例彈窗有完整數據", pg.evaluate("document.getElementById('m-detail').classList.contains('show') && document.querySelectorAll('#dt .al li').length>=2"))
        pg.screenshot(path=f"{OUT}/{mode}_case_detail.png")
        pg.keyboard.press("Escape"); pg.wait_for_timeout(150)
        T(f"{mode}: 沒有向 markforged.com 發出任何請求", not ext, ext)
        T(f"{mode}: 無 JS 錯誤", not errs, errs)
        ctx.close()
    b.close()
print("TOTAL", ok, "/", tot)

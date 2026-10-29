# /baidu/ 百度落地頁全功能示範頁 · 工具

- 頁面源檔：`../../baidu/index.html`（手寫，無產生器；改這裡就是改源頭，頁尾與「讨论工具」裡的版號跟著改）
- `qa_basic.py <URL>`：手機＋電腦各 21 項基本點測（表單驗證、選單、分頁、複製、彈窗、區塊編號、素材包）。「無失敗請求」那 2 項是腳本自己發 HEAD 請求造成，素材包用 GET 驗
- `qa_details.py <URL>`：機型／材料詳情、Onyx GF 專區、案例篩選（全部 15／跨國 10／食品 6）、不向 markforged.com 發請求
- `build_offline.py --out <file.html>`：把示範頁打包成單一離線 HTML（圖與字型內嵌、影片改封面、拿掉計數器）
- `qr_decode.swift <png…>`：用 macOS Vision 解二維碼（本機沒有 OpenCV，Chromium 無頭模式也沒有 BarcodeDetector）

本機預覽：在 repo 根目錄 `python3 -m http.server 8765`，再對 `http://localhost:8765/baidu/index.html` 跑點測。
交接說明：vault `團隊共享/CoCo致Bella_百度落地頁改版交接_2026-10-29.md`

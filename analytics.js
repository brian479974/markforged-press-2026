/* news.markforged.tw — 頁面瀏覽統計 beacon
 *
 * 2026-09-07 建立。設計原則：
 *  1. 供應商可換：只改 PROVIDER 與 ID，文章 HTML 不必動。
 *  2. 不放 cookie、不做跨站識別 —— 與本站以 BCC 保護收件人隱私的立場一致，
 *     台灣個資法／GDPR 下不需要同意橫幅。
 *  3. 尊重 Do Not Track 與 Global Privacy Control。
 *  4. 失敗靜默，絕不影響文章閱讀。
 *
 * ⚠️ 已知限制（不要假裝沒有）：
 *  · GA4 與 Cloudflare 的 beacon 網域在中國大陸被阻擋，
 *    CN 讀者的瀏覽**量不到**。本站發信名單有 83 位在 CN。
 *  · 統計的是「載入頁面的瀏覽器」，不是「人」。同一人多裝置會重複計。
 */
(function () {
  "use strict";

  // ── 設定（唯一要改的地方）────────────────────────────────────
  var PROVIDER = "none";   // "ga4" | "cloudflare" | "none"
  var GA4_ID = "";         // 例 "G-XXXXXXXXXX"
  var CF_TOKEN = "";       // Cloudflare Web Analytics 的 token
  // ────────────────────────────────────────────────────────────

  // 尊重使用者的不追蹤意願
  var dnt = navigator.doNotTrack === "1" || window.doNotTrack === "1" ||
            navigator.msDoNotTrack === "1" ||
            (navigator.globalPrivacyControl === true);
  if (dnt || PROVIDER === "none") { return; }

  function load(src, attrs) {
    try {
      var s = document.createElement("script");
      s.async = true;
      s.src = src;
      if (attrs) { Object.keys(attrs).forEach(function (k) { s.setAttribute(k, attrs[k]); }); }
      s.onerror = function () { /* 靜默：網路被擋不影響閱讀 */ };
      document.head.appendChild(s);
    } catch (e) { /* 靜默 */ }
  }

  if (PROVIDER === "ga4" && GA4_ID) {
    load("https://www.googletagmanager.com/gtag/js?id=" + GA4_ID);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    // anonymize_ip + 不用 cookie 做跨站廣告
    window.gtag("config", GA4_ID, {
      anonymize_ip: true,
      allow_google_signals: false,
      allow_ad_personalization_signals: false
    });
  } else if (PROVIDER === "cloudflare" && CF_TOKEN) {
    load("https://static.cloudflareinsights.com/beacon.min.js",
         { "data-cf-beacon": '{"token":"' + CF_TOKEN + '"}' });
  }
})();

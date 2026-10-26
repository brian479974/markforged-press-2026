/* news.markforged.tw 全站頂端導覽列（2026-10-26 建立）
 *
 * 為什麼有這支：從 www.markforged.tw 點「新聞」進到媒體中心之後，整個新聞站沒有任何一條
 * 回官網的路（文章底部的 markforged.tw 不帶 www，指到一台連不上的舊主機）。
 * 這條導覽列與官網同一套：logo 回官網首頁、各項連到官網對應頁，「新聞」是目前位置。
 *
 * 用法：每頁 <body> 之後第一行放
 *   <script src="/globalbar.js"></script>
 * 同步載入、在原地插入，首屏就有導覽列、不會跳版。
 * 語言依檔名：-sc.html → 簡中，-en.html → 英文（官網連結加 ?lang=en），其餘繁中。
 * 官網的選單項目改了，這裡要跟著改（對照 www 的 shared.js NAV_HTML）。
 */
(function () {
  if (document.getElementById('mfg-bar')) return;
  var W = 'https://www.markforged.tw/';
  var path = location.pathname;
  var lang = /-sc\.html$/.test(path) ? 'sc' : (/-en\.html$/.test(path) ? 'en' : 'tc');
  var T = {
    tc: { products: '產品', solutions: '解決方案', materials: '材料', cases: '案例', news: '新聞',
          about: '關於', contact: '聯絡', quote: '立即詢價', menu: '選單', home: 'Markforged 官網首頁',
          metal: 'FX10 金屬方案（Sinter-2 套組）',
          sol: ['國防與政府', '航太與國防', '汽車製造', '工業設備', '醫療', '電子製造', '能源',
                '教育與研究', '消費品製造', '食品飲料', '包裝機械', '產品開發', '查看全部 →'] },
    sc: { products: '产品', solutions: '解决方案', materials: '材料', cases: '案例', news: '新闻',
          about: '关于', contact: '联系', quote: '立即询价', menu: '菜单', home: 'Markforged 官网首页',
          metal: 'FX10 金属方案（Sinter-2 套组）',
          sol: ['国防与政府', '航天与国防', '汽车制造', '工业设备', '医疗', '电子制造', '能源',
                '教育与研究', '消费品制造', '食品饮料', '包装机械', '产品开发', '查看全部 →'] },
    en: { products: 'Products', solutions: 'Solutions', materials: 'Materials', cases: 'Cases', news: 'News',
          about: 'About', contact: 'Contact', quote: 'Request a Quote', menu: 'Menu', home: 'Markforged Taiwan home',
          metal: 'FX10 Metal Solution (Sinter-2 Bundle)',
          sol: ['Federal & Defense', 'Aerospace & Defense', 'Automotive', 'Industrial Equipment', 'Medical',
                'Electronics', 'Energy', 'Education & Research', 'Consumer Goods', 'Food & Beverage',
                'Packaging Machinery', 'Product Development', 'View All →'] }
  }[lang];
  var q = lang === 'en' ? '?lang=en' : '';
  var u = function (p) { return W + p + q; };
  var solPages = ['defense', 'aerospace', 'automotive', 'industrial', 'medical', 'electronics', 'energy',
                  'education', 'cpg', 'food', 'packaging', 'product-dev', 'solutions'];
  var isHub = /^\/(index\.html)?$/.test(path);
  var a = function (href, text, extra) { return '<a href="' + href + '"' + (extra || '') + '>' + text + '</a>'; };

  var html =
    '<nav id="mfg-bar" class="mfg-' + lang + '" aria-label="Markforged">' +
      '<a class="mfg-logo" href="' + u('') + '" aria-label="' + T.home + '" title="' + T.home + '">' +
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1283.6 273.6" role="img" aria-hidden="true" fill="#FFFFFF"><path d="M420.7,67.5l-2,2l-45.5,110.9h-2L325.7,69.5l-2-2H302l-2,2v134.6l2,2h15.8l2-2v-95h2l39.6,95l2,2h17.8l2-2l39.6-95h2v95l2,2h15.8l2-2V69.5l-2-2H420.7z M535.8,115.9c-3.1-3.6-7.2-6.2-12.3-8c-5.1-1.8-11.3-2.7-18.7-2.7c-7.4,0-13.6,0.9-18.7,2.7c-5.1,1.8-9.2,4.1-12.3,6.9c-3.1,2.8-5.3,6-6.6,9.6c-1.3,3.6-2,7.1-2,10.5l2,2h15.8l2-2c0-4,1.5-6.9,4.6-8.9c3.1-2,8.1-3,15.1-3c7,0,12,1.2,15.1,3.7c3.1,2.4,4.6,7.2,4.6,14.1v4l-2,2c-1.6-0.3-3.3-0.6-5.1-1c-1.6-0.3-3.5-0.5-5.6-0.7c-2.2-0.2-4.5-0.3-7-0.3c-6.5,0-12.4,0.6-17.7,1.9c-5.3,1.3-9.9,3.2-13.7,5.7c-3.8,2.6-6.8,5.9-8.9,9.9c-2.1,4-3.2,8.7-3.2,14.1c0,9.9,2.9,17.6,8.6,23.2c5.7,5.6,14.1,8.4,25,8.4c5,0,9.2-0.6,12.7-1.9c3.4-1.3,6.3-2.6,8.5-4.1c2.5-1.7,4.7-3.7,6.5-5.9h2l2,7.9l2,2h13.8l2-2v-55.4c0-7.4-0.7-13.8-2-19.3C541.1,124,538.9,119.5,535.8,115.9z M524.6,170.5c0,5.9-2.3,10.7-6.9,14.3c-4.6,3.6-10.9,5.4-18.8,5.4c-5.9,0-10.4-1.1-13.4-3.2c-3-2.1-4.5-5.7-4.5-10.7c0-5,2-8.9,6.1-11.7c4.1-2.8,10.6-4.2,19.6-4.2c2.5,0,4.7,0.1,6.6,0.3c1.9,0.2,3.6,0.4,5,0.7c1.6,0.4,3,0.7,4.2,1l2,2V170.5z M608.7,107.2c-3.4,0-6.4,0.2-9,0.7c-2.6,0.5-4.8,1.1-6.8,2c-2,0.9-3.8,1.9-5.3,3.2c-1.6,1.3-3.1,2.6-4.5,4.1h-2l-2-7.9l-2-2h-13.8l-2,2v94.9l2,2H579l2-2v-49.4c0-5.9,0.6-10.8,1.8-14.6c1.2-3.8,2.9-6.9,5.1-9.1c2.2-2.2,4.9-3.8,8.1-4.6c3.2-0.9,6.7-1.3,10.7-1.3h9.9l2-2v-13.8l-2-2H608.7z M680.9,150.7l27.7-27.7v-13.8l-2-2h-5.9l-4,2l-45.5,45.5h-2V69.6l-2-2h-15.8l-2,2v134.5l2,2h15.8l2-2v-19.8l2-4l13.8-13.8h2l29.7,37.6l4,2h7.9l2-2v-13.8l-29.7-37.6V150.7z M941,107.2c-3.4,0-6.4,0.2-9,0.7c-2.6,0.5-4.8,1.1-6.8,2c-2,0.9-3.8,1.9-5.3,3.2c-1.6,1.3-3.1,2.6-4.5,4.1h-2l-2-7.9l-2-2h-13.8l-2,2v94.9l2,2h15.8l2-2v-49.4c0-5.9,0.6-10.8,1.8-14.6c1.2-3.8,2.9-6.9,5.1-9.1c2.2-2.2,4.9-3.8,8.1-4.6c3.2-0.9,6.7-1.3,10.7-1.3h9.9l2-2v-13.8l-2-2H941z M1030.9,107.2l-2,2l-2,7.9h-2c-1.7-2.2-3.8-4.2-6.1-5.9c-2.1-1.5-4.8-2.8-8-4.1c-3.2-1.3-7.1-1.9-11.6-1.9c-7,0-13.2,1.3-18.5,3.9c-5.3,2.6-9.9,6.1-13.6,10.7c-3.8,4.5-6.6,10-8.5,16.3c-1.9,6.3-2.9,13.2-2.9,20.6c0,7.4,1,14.2,2.9,20.6c1.9,6.3,4.7,11.8,8.5,16.3c3.8,4.5,8.3,8.1,13.6,10.7c5.3,2.6,11.5,3.9,18.5,3.9c4.5,0,8.3-0.6,11.6-1.9c3.2-1.3,5.9-2.6,8-4.1c2.4-1.7,4.4-3.7,6.1-5.9h2c0,10.9-2,19.3-6.1,25c-4.1,5.7-10.6,8.6-19.6,8.6c-5,0-9.1-0.7-12.2-2c-3.1-1.3-5.6-4-7.6-7.9l-2-2h-15.8l-2,2c1.1,7.9,4.9,14.5,11.6,19.8c6.7,5.3,16,7.9,28,7.9c5.9,0,11.6-0.9,17.1-2.8c5.5-1.8,10.3-4.9,14.5-9.1c4.2-4.2,7.6-9.7,10.1-16.5c2.5-6.8,3.8-15.1,3.8-25v-85l-2-2H1030.9z M1020.1,182.4c-4.6,5.3-10.9,7.9-18.8,7.9c-7.9,0-14.2-2.9-18.8-8.6c-4.6-5.7-6.9-14.1-6.9-25c0-10.9,2.3-19.3,6.9-25c4.6-5.7,10.9-8.6,18.8-8.6c7.9,0,14.2,2.6,18.8,7.9c4.6,5.3,6.9,13.8,6.9,25.7C1027,168.5,1024.7,177.1,1020.1,182.4z M234.9,64.5c-3.4-2.1-7.7-2.2-11.2-0.2L21.8,180.9v-16.8L198.2,62.3c3.5-2,5.6-5.8,5.4-9.8c-0.1-3.8-2.3-7.3-5.6-9.2l-36.2-20.9c-3.4-1.9-7.5-1.9-10.9,0L21.8,96.9V80.1l110.9-64c4-2.3,4-8.2,0-10.5l-7-4c-3.6-2.1-8-2.1-11.5,0L5.5,64.4C2.1,66.3,0,69.9,0,73.8v41.8c0,3.8,1.9,7.4,5.1,9.5c3.4,2.1,7.7,2.2,11.2,0.2l140-80.8l14.5,8.4L5.5,148.3c-3.4,1.9-5.5,5.6-5.5,9.4v41.8c0,3.8,1.9,7.4,5.1,9.5c3.4,2.1,7.7,2.2,11.2,0.2L218.2,92.7v16.8L41.8,211.3c-3.4,1.9-5.5,5.5-5.5,9.4c0,3.9,2.1,7.5,5.5,9.4l36.4,21c3.4,1.9,7.5,1.9,10.9,0l129.1-74.5v16.8l-110.9,64c-4,2.3-4,8.2,0,10.5l7,4c3.6,2.1,8,2.1,11.5,0l108.8-62.8c3.4-1.9,5.5-5.5,5.5-9.4V158c0-3.8-1.9-7.4-5.1-9.5c-3.4-2.1-7.7-2.2-11.2-0.2l-140,80.8l-14.5-8.4l165.5-95.5c3.4-1.9,5.5-5.5,5.5-9.4V74C240,70.2,238.1,66.6,234.9,64.5z M1139.7,120.6c-3.7-4.7-8.4-8.4-14.1-11.2c-5.7-2.8-12.6-4.2-20.5-4.2c-7.9,0-14.7,1.4-20.5,4.2c-5.7,2.8-10.5,6.5-14.1,11.2c-3.7,4.7-6.4,10.2-8.2,16.4c-1.8,6.3-2.7,12.8-2.7,19.7c0,7.4,1,14.2,3,20.6c2,6.3,4.9,11.8,8.9,16.3c4,4.5,8.9,8.1,14.8,10.7c5.9,2.6,12.9,3.9,20.8,3.9c5.9,0,11.2-0.8,15.9-2.4c4.7-1.6,8.7-3.8,12.1-6.5c3.4-2.8,6-5.9,7.9-9.5c1.9-3.6,3.1-7.3,3.7-11.3l-2-2h-15.8l-2,2c-1.1,2.5-2.3,4.5-3.7,6c-1.4,1.5-3,2.7-4.7,3.6c-1.8,0.9-3.6,1.5-5.5,1.8c-1.9,0.3-3.9,0.5-5.8,0.5c-5.9,0-10.6-1.1-14-3.2c-3.4-2.1-6-4.5-7.7-7.2c-1.7-2.7-2.8-5.3-3.3-7.9c-0.5-2.6-0.7-4.4-0.7-5.4l2-2h65.3l2-2v-5.9c0-6.9-0.9-13.4-2.7-19.7C1146.2,130.7,1143.4,125.2,1139.7,120.6z M1126.9,148.8h-43.5l-2-2c0-1.4,0.2-3.5,0.7-6.2c0.5-2.7,1.5-5.3,3.1-7.9c1.6-2.6,4-4.8,7.1-6.7c3.2-1.9,7.4-2.9,12.9-2.9c5.4,0,9.7,1,12.9,2.9c3.2,1.9,5.5,4.2,7.1,6.7c1.6,2.6,2.6,5.2,3.1,7.9c0.5,2.7,0.7,4.8,0.7,6.2L1126.9,148.8z M868,119.1c-4.1-4.5-9.1-7.9-14.9-10.3c-5.9-2.4-12.5-3.6-19.9-3.6c-7.4,0-14,1.2-19.9,3.6c-5.9,2.4-10.8,5.8-14.9,10.3c-4.1,4.5-7.2,9.9-9.4,16.2c-2.2,6.3-3.3,13.4-3.3,21.4s1.1,15,3.3,21.4c2.2,6.3,5.3,11.7,9.4,16.2c4.1,4.5,9.1,7.9,14.9,10.3c5.9,2.4,12.5,3.6,19.9,3.6c7.4,0,14-1.2,19.9-3.6c5.9-2.4,10.8-5.8,14.9-10.3c4.1-4.5,7.2-9.9,9.4-16.2c2.2-6.3,3.3-13.4,3.3-21.4s-1.1-15-3.3-21.4C875.2,129,872.1,123.6,868,119.1z M853.7,181.7c-4.7,5.7-11.6,8.6-20.6,8.6c-9,0-15.8-2.9-20.6-8.6c-4.7-5.7-7.1-14.1-7.1-25c0-10.9,2.4-19.3,7.1-25c4.7-5.7,11.6-8.6,20.6-8.6c9,0,15.8,2.9,20.6,8.6c4.7,5.7,7.1,14.1,7.1,25C860.8,167.6,858.5,175.9,853.7,181.7z M762.9,71.6c-3.4,0-6.8,0.5-10.2,1.5c-3.4,1-6.3,2.5-8.9,4.6c-2.6,2.1-4.6,4.8-6.2,8c-1.6,3.2-2.4,7.1-2.4,11.6v7.9l-2,2h-13.8l-2,2V123l2,2h13.8l2,2v77.1l2,2h15.8l2-2V127l2-2h19.8l2-2v-13.8l-2-2H757l-2-2v-7.9c0-3,0.8-5.1,2.5-6.2c1.6-1.1,3.5-1.7,5.4-1.7h15.8l2-2V73.6l-2-2H762.9z M1246.5,67.7h-15.8l-2,2v47.5h-2c-1.7-2.2-3.8-4.2-6.1-5.9c-2.1-1.5-4.8-2.8-8-4.1c-3.2-1.3-7.1-1.9-11.6-1.9c-7,0-13.2,1.3-18.5,3.9c-5.3,2.6-9.9,6.1-13.6,10.7c-3.8,4.5-6.6,10-8.5,16.3c-1.9,6.3-2.9,13.2-2.9,20.6c0,7.4,1,14.2,2.9,20.6c1.9,6.3,4.7,11.8,8.5,16.3c3.8,4.5,8.3,8.1,13.6,10.7c5.3,2.6,11.5,3.9,18.5,3.9c4.5,0,8.3-0.6,11.6-1.9c3.2-1.3,5.9-2.6,8-4.1c2.4-1.7,4.4-3.7,6.1-5.9h2l2,7.9l2,2h13.8l2-2V69.6L1246.5,67.7z M1221.8,182.4c-4.6,5.3-10.9,7.9-18.8,7.9c-7.9,0-14.2-2.9-18.8-8.6c-4.6-5.7-6.9-14.1-6.9-25c0-10.9,2.3-19.3,6.9-25c4.6-5.7,10.9-8.6,18.8-8.6c7.9,0,14.2,2.6,18.8,7.9c4.6,5.3,6.9,13.8,6.9,25.7C1228.7,168.5,1226.4,177.1,1221.8,182.4z"/></svg>' +
      '</a>' +
      '<button class="mfg-ham" type="button" aria-label="' + T.menu + '" aria-expanded="false" aria-controls="mfg-links"><span></span><span></span><span></span></button>' +
      '<ul class="mfg-links" id="mfg-links">' +
        '<li class="mfg-dd">' + a(u('products.html'), T.products) +
          '<div class="mfg-drop">' + a(u('fx10.html'), 'FX10') + a(u('fx10-metal.html'), T.metal) +
          a(u('fx20.html'), 'FX20') + a(u('x7fe.html'), 'X7 Field Edition') + '</div></li>' +
        '<li class="mfg-dd">' + a(u('solutions.html'), T.solutions) +
          '<div class="mfg-drop">' + solPages.map(function (p, i) { return a(u(p + '.html'), T.sol[i]); }).join('') + '</div></li>' +
        '<li>' + a(u('materials.html'), T.materials) + '</li>' +
        '<li>' + a(u('cases.html'), T.cases) + '</li>' +
        '<li>' + a('/', T.news, ' class="mfg-on"' + (isHub ? ' aria-current="page"' : '')) + '</li>' +
        '<li>' + a(u('about.html'), T.about) + '</li>' +
        '<li>' + a(u('contact.html'), T.contact) + '</li>' +
        '<li class="mfg-cta-m">' + a(u('contact.html'), T.quote) + '</li>' +
      '</ul>' +
      a(u('contact.html'), T.quote, ' class="mfg-cta"') +
    '</nav>';

  var font = lang === 'sc' ? "'PingFang SC','Noto Sans SC'" : "'PingFang TC','Noto Sans TC'";
  var css =
    '#mfg-bar{box-sizing:border-box;position:sticky;top:0;z-index:1000;display:flex;align-items:center;height:64px;padding:0 24px;margin:0;' +
      'background:#000;border-bottom:1px solid #1f1f1f;font-family:"Helvetica Neue",Helvetica,Arial,' + font + ',sans-serif;' +
      '-webkit-font-smoothing:antialiased;line-height:1.3;text-align:left}' +
    '#mfg-bar *{box-sizing:border-box;margin:0;padding:0}' +
    '#mfg-bar a{text-decoration:none;border:0}' +
    '#mfg-bar .mfg-logo{display:flex;align-items:center;flex-shrink:0;margin-right:16px;line-height:0}' +
    '#mfg-bar .mfg-logo svg{display:block;height:30px;width:auto}' +
    '#mfg-bar .mfg-links{display:flex;list-style:none;margin:0 auto;min-width:0}' +
    '#mfg-bar .mfg-links>li{position:relative}' +
    '#mfg-bar .mfg-links>li>a{display:flex;align-items:center;height:64px;padding:0 14px;color:#fff;font-size:13px;' +
      'font-weight:600;letter-spacing:.5px;text-transform:uppercase;white-space:nowrap;transition:color .2s}' +
    '#mfg-bar .mfg-links>li>a:hover,#mfg-bar .mfg-links>li>a.mfg-on{color:#FFFF00}' +
    '#mfg-bar .mfg-drop{display:none;position:absolute;top:100%;left:0;min-width:220px;padding:8px 0;background:#fff;' +
      'border:1px solid #e0e0e0;border-top:3px solid #FFFF00;box-shadow:0 8px 32px rgba(0,0,0,.12)}' +
    '#mfg-bar .mfg-dd:hover .mfg-drop,#mfg-bar .mfg-dd:focus-within .mfg-drop{display:block}' +
    '#mfg-bar .mfg-drop a{display:block;padding:11px 24px;color:#000;font-size:13px;font-weight:500;letter-spacing:.3px;transition:all .15s}' +
    '#mfg-bar .mfg-drop a:hover{background:#FFFF00;padding-left:28px}' +
    '#mfg-bar .mfg-cta{flex-shrink:0;padding:9px 18px;background:#FFFF00;color:#000;font-size:12px;font-weight:800;' +
      'letter-spacing:.8px;text-transform:uppercase;white-space:nowrap;transition:background .2s}' +
    '#mfg-bar .mfg-cta:hover{background:#fff}' +
    '#mfg-bar .mfg-cta-m{display:none}' +
    '#mfg-bar .mfg-ham{display:none;flex-direction:column;align-items:center;justify-content:center;min-width:44px;min-height:44px;' +
      'margin-left:auto;padding:8px;background:none;border:0;cursor:pointer}' +
    '#mfg-bar .mfg-ham span{display:block;width:22px;height:2px;margin:5px 0;background:#fff;transition:.3s}' +
    '#mfg-bar.mfg-open .mfg-ham span:nth-child(1){transform:translateY(12px) rotate(45deg)}' +
    '#mfg-bar.mfg-open .mfg-ham span:nth-child(2){opacity:0}' +
    '#mfg-bar.mfg-open .mfg-ham span:nth-child(3){transform:translateY(-12px) rotate(-45deg)}' +
    '@media (max-width:960px){' +
      '#mfg-bar{padding:0 16px}' +
      '#mfg-bar .mfg-logo svg{height:27px}' +
      '#mfg-bar .mfg-ham{display:flex}' +
      '#mfg-bar .mfg-cta{display:none}' +
      '#mfg-bar .mfg-links{display:none;position:fixed;top:64px;left:0;right:0;bottom:0;flex-direction:column;margin:0;' +
        'padding:16px;background:#000;overflow-y:auto}' +
      '#mfg-bar.mfg-open .mfg-links{display:flex}' +
      '#mfg-bar .mfg-links>li>a{height:52px;padding:0 10px;font-size:14px}' +
      '#mfg-bar .mfg-dd:hover .mfg-drop,#mfg-bar .mfg-dd:focus-within .mfg-drop{display:none}' +
      '#mfg-bar .mfg-cta-m{display:block;margin-top:16px}' +
      '#mfg-bar .mfg-links>li.mfg-cta-m>a{display:inline-flex;height:auto;padding:13px 28px;background:#FFFF00;color:#000;font-size:14px;font-weight:800;letter-spacing:.8px}' +
    '}' +
    /* 原本各頁頁首上的 logo 與導覽列重複，收起來；「媒體中心」字樣留著當欄目名稱 */
    '.hdr .hdr-logo,.hdr>img{display:none!important}' +
    '.hdr{justify-content:flex-start!important}' +
    '.hdr .hdr-ev{text-align:left!important}' +
    '.hdr a.mfg-hub{color:inherit;text-decoration:none}' +
    '.hdr a.mfg-hub:hover .hdr-ev{color:#FFFF00}' +
    '.header .brand,.header .logo-text{display:none!important}' +
    /* 媒體中心首頁自己的欄目列（News／Programs／Insights）接在導覽列下方 */
    'nav.nav{top:64px!important}' +
    'nav.nav .nav-brand{display:none!important}' +
    'nav.nav .nav-links{margin:0 auto}' +
    '@media (max-width:960px){nav.nav{position:relative!important;top:0!important}}';

  var st = document.createElement('style');
  st.id = 'mfg-bar-css';
  st.textContent = css;
  (document.head || document.documentElement).appendChild(st);

  var me = document.currentScript;
  if (me) me.insertAdjacentHTML('beforebegin', html);
  else document.body.insertAdjacentHTML('afterbegin', html);

  var bar = document.getElementById('mfg-bar');
  var ham = bar.querySelector('.mfg-ham');
  ham.addEventListener('click', function () {
    var open = bar.classList.toggle('mfg-open');
    ham.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.documentElement.style.overflow = open ? 'hidden' : '';
  });

  /* 文章頁首的「媒體中心」字樣改成可點，回媒體中心首頁 */
  document.addEventListener('DOMContentLoaded', function () {
    var ev = document.querySelector('.hdr .hdr-ev');
    if (ev && !ev.closest('a')) {
      var link = document.createElement('a');
      link.className = 'mfg-hub';
      link.href = '/';
      ev.parentNode.insertBefore(link, ev);
      link.appendChild(ev);
    }
  });
})();

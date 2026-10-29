"""Make a single-file offline copy of the Baidu landing-page demo (news.markforged.tw/baidu/).

One-off dated script (2026-10-29). Source of truth is ~/markforged-press/baidu/index.html;
this only packages it so the agency can open it without network access (China may not reach
GitHub Pages reliably).

What it changes (and nothing else):
  - every assets/<file> reference (img src, data-qr, JS strings, CSS url) -> data URI
  - the Onyx GF <video> -> its poster image + a note (an 8.8 MB video would bloat the file)
  - the asset-pack download link -> text pointing to the email attachment
  - drops /analytics.js (page-view counter; meaningless offline)
  - demo ribbon text says this is the offline copy of the same design

Usage:
  ./venv3/bin/python3 _build_baidu_offline_from_demo_20261029.py --out <file.html>
"""
import argparse, base64, mimetypes, os, re

SRC = os.path.expanduser("~/markforged-press/baidu/index.html")
ASSETS = os.path.expanduser("~/markforged-press/baidu/assets")


def data_uri(rel):
    path = os.path.join(ASSETS, rel)
    mime = mimetypes.guess_type(path)[0] or ("font/ttf" if rel.endswith(".ttf") else "application/octet-stream")
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()


def build(out):
    s = open(SRC, encoding="utf-8").read()
    n0 = len(s)
    # 1) video -> poster + note
    s, nv = re.subn(r'<video[^>]*poster="assets/onyxgf_poster\.jpg"[^>]*>.*?</video>',
                    '<img src="assets/onyxgf_poster.jpg" alt="Onyx GF 官方影片画面" style="width:100%;display:block;border-bottom:4px solid #FFFF00">',
                    s, flags=re.S)
    assert nv == 1, nv
    s = s.replace("Markforged 官方影片 · 认识 Onyx GF（28 秒，中文字幕）",
                  "Markforged 官方影片 · 认识 Onyx GF（28 秒，中文字幕）· 离线版只放画面，影片请在示范页播放")
    # 2) asset-pack link -> text
    s, nz = re.subn(r'<a href="assets/Markforged_landing-page-assets_2026-10-29\.zip" download>[^<]*</a>',
                    '<span style="display:block;margin:6px 0">素材包：见邮件附件</span>', s)
    assert nz == 1, nz
    # 3) analytics off
    s = s.replace('<script src="/analytics.js" defer></script>', "")
    # 4) ribbon
    s = s.replace('<b>示范页面</b><span class="hide-m"> · 百度落地页改版讨论用</span> · 表单不会送出任何资料',
                  '<b>示范页面（离线版）</b><span class="hide-m"> · 与 news.markforged.tw/baidu 同一份设计</span> · 表单不会送出任何资料')
    # 5) inline every remaining assets/<file>
    refs = sorted(set(re.findall(r'assets/([A-Za-z0-9_./-]+\.(?:jpg|jpeg|png|ttf))', s)))
    cache = {r: data_uri(r) for r in refs}
    s = re.sub(r'assets/([A-Za-z0-9_./-]+\.(?:jpg|jpeg|png|ttf))', lambda m: cache[m.group(1)], s)
    left = re.findall(r'assets/[A-Za-z0-9_./-]+', s)
    assert not left, left
    open(out, "w", encoding="utf-8").write(s)
    print(f"inlined {len(refs)} files; {n0//1024} KB -> {len(s)//1024} KB -> {out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    build(ap.parse_args().out)

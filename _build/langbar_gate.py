#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""佈署閘：有多語版本的頁面，語言列必須合站上標準。

規則（只管「有兄弟檔」的頁面，單語頁不強迫多語）：
  同一個 slug 只要存在 -sc 或 -en 兄弟檔，三版都必須有標準語言列
  ——版位在 header 與 hero 之間、有語言標籤、三版互指、hreflang 齊、html lang 正確。

  用法：langbar_gate.py <目錄> [<目錄> ...]
  exit 1 ＝ 有違規，不准佈署。

  三態輸出：PASS（合標準）／FAIL（違規）／SKIP（單語頁，本閘不管）
  —— 查不了不等於沒問題，所以讀不到的檔案算 FAIL 不算 SKIP。
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import langbar as LB  # noqa: E402


def audit(dirs):
    fails, passes, skips = [], [], []
    for d in dirs:
        d = Path(d)
        if not d.is_dir():
            fails.append(f"{d}：不是目錄，查不了")
            continue
        slugs = sorted({p.stem[:-3] if p.stem.endswith("-sc") else
                        p.stem[:-3] if p.stem.endswith("-en") else p.stem
                        for p in d.glob("*.html")})
        for slug in slugs:
            F = LB.files(slug)
            present = {L: d / f for L, f in F.items() if (d / f).exists()}
            if len(present) < 2:
                skips.append(f"{d.name}/{slug}：單語頁，本閘不管")
                continue
            missing = [F[L] for L in LB.LANGS if L not in present]
            if missing:
                fails.append(f"{d.name}/{slug}：有兄弟檔卻缺 {missing}")
            for L, p in present.items():
                try:
                    html = p.read_text(encoding="utf-8")
                except Exception as e:                       # 讀不到＝查不了＝FAIL
                    fails.append(f"{p}：讀取失敗 {e}")
                    continue
                bad = LB.check(html, slug, L)
                (fails if bad else passes).extend(bad or [f"{d.name}/{F[L]}"])
    return fails, passes, skips


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    fails, passes, skips = audit(argv[1:])
    for s in skips:
        print(f"  ⏭  SKIP {s}")
    for p in passes:
        print(f"  ✅ PASS {p}")
    for f in fails:
        print(f"  ❌ FAIL {f}")
    print(f"\n{'❌ 語言列閘未過，不准佈署' if fails else '✅ 語言列閘全過'}"
          f"（PASS {len(passes)} · FAIL {len(fails)} · SKIP {len(skips)}）")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

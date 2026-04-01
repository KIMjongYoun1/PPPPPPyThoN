#!/usr/bin/env python3
"""따라치기 파일에 섹션별 [설명] 한 줄 삽입 (중복 시 스킵)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 섹션 제목 줄(정규식) → 바로 아래에 넣을 [설명]
SECTIONS: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(r"^#\s*──\s*import\s*──"),
        "[설명] pandas·sklearn 등 시험에 필요한 모듈만 import 한다.",
    ),
    (
        re.compile(r"^#\s*──\s*BASE\s*URL"),
        "[설명] Datamanim raw URL 앞부분. 뒤에 `/폴더/파일.csv` 만 붙여 read_csv 한다.",
    ),
    (
        re.compile(r"^#\s*──\s*1\.\s*데이터\s*로드"),
        "[설명] train·test(또는 x/y) 표를 URL에서 읽는다.",
    ),
    (
        re.compile(r"^#\s*──\s*2\.\s*EDA"),
        "[설명] shape·컬럼·결측·정답 분포 등을 출력해 전처리 전에 구조를 본다.",
    ),
    (
        re.compile(r"^#\s*──\s*3\.\s*ID"),
        "[설명] ID 는 제출용으로만 두고 X 에서 제거한다. y 는 Series 로 둔다.",
    ),
    (
        re.compile(r"^#\s*──\s*4\.\s*전처리"),
        "[설명] 수치형은 train 중앙값·범주형은 최빈값으로 채운 뒤 LabelEncoder 등 적용한다.",
    ),
    (
        re.compile(r"^#\s*──\s*5\.\s*3종\s*모델"),
        "[설명] 여러 모델을 5-fold CV 로 비교한다(분류는 accuracy 등 지시에 맞게).",
    ),
    (
        re.compile(r"^#\s*──\s*6\.\s*최적"),
        "[설명] CV 에서 고른 모델로 전체 train 을 다시 학습한다.",
    ),
    (
        re.compile(r"^#\s*──\s*7\.\s*특성\s*중요도"),
        "[설명] 트리 모델이면 feature_importances_ 상위 몇 개를 출력한다.",
    ),
    (
        re.compile(r"^#\s*──\s*8\.\s*예측"),
        "[설명] test 예측 후 submission.csv 를 문제 형식에 맞게 저장한다.",
    ),
    (
        re.compile(r"^#\s*-+\s*Step\s*1\s*:\s*import"),
        "[설명] statsmodels·scipy 등 문제에서 요구하는 import 만 모은다.",
    ),
    (
        re.compile(r"^#\s*-+\s*Step\s*2\s*:\s*BASE"),
        "[설명] BASE URL 변수를 두고 read_csv 경로를 만든다.",
    ),
]


def insert_descriptions(lines: list[str]) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        st = line.rstrip("\n")
        if i + 1 < len(lines) and lines[i + 1].strip().startswith("# [설명]"):
            i += 1
            continue
        for pat, desc in SECTIONS:
            if pat.match(st):
                out.append("# " + desc + "\n")
                break
        i += 1
    return out


def main() -> None:
    for n in range(1, 26):
        for path in sorted(ROOT.glob(f"{n:02d}_*.py")):
            raw = path.read_text(encoding="utf-8")
            if "[따라치기 방법]" not in raw:
                continue
            new_lines = insert_descriptions(raw.splitlines(keepends=True))
            path.write_text("".join(new_lines), encoding="utf-8")
            print(path.name)


if __name__ == "__main__":
    main()

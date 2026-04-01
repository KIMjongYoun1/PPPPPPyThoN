#!/usr/bin/env python3
"""02~25 연습 파일: 기존 정답은 유지하고 # 주석 처리 + 상단 따라치기 안내 삽입."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

LEARNING_BLOCK = """\
#
# [따라치기 방법]
# · 각 섹션의 **[설명]**(있는 경우)을 읽고, 그 아래 `#` 로만 적힌 **정답 코드 줄** 을 주석 없이 따라 친다.
# · 전부 입력한 뒤에는 코드 줄 맨 앞 `# ` 만 제거해도 되고, 빈 파일에 순서대로만 쳐도 된다.
# · 실행 검증: `python 이파일이름.py` (URL 로드 문제는 인터넷 연결)
#
# [시험 공통 포인트]
# · 결측·중앙값·최빈값·인코딩 기준은 **train 만** (test 로 통계 내지 않기).
# · 회귀에서 scoring 이 `neg_root_mean_squared_error` 이면 출력 시 부호 반전(-mean).
#
# ============================================================
"""


def first_code_line_index(lines: list[str]) -> int | None:
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            continue
        return i
    return None


def is_fully_commented(lines: list[str]) -> bool:
    idx = first_code_line_index(lines)
    return idx is None


def insert_learning_block(header: list[str]) -> list[str]:
    if "[따라치기 방법]" in "".join(header):
        return header
    pos = None
    for k in range(len(header) - 1, -1, -1):
        if header[k].strip() == "# ============================================================":
            pos = k
            break
    if pos is None:
        pos = 0
    ins = pos + 1
    while ins < len(header) and header[ins].strip() == "":
        ins += 1
    return header[:ins] + ["\n", LEARNING_BLOCK] + header[ins:]


def comment_body(body: list[str]) -> list[str]:
    out: list[str] = []
    for line in body:
        if not line.strip():
            out.append(line)
            continue
        if line.lstrip().startswith("#"):
            out.append(line)
            continue
        out.append("# " + line)
    return out


def process_file(path: Path) -> str:
    if path.name.startswith("01_") and "데이터_로드" in path.name:
        return "skip_01"

    raw = path.read_text(encoding="utf-8")
    if "[따라치기 방법]" in raw and is_fully_commented(raw.splitlines(keepends=True)):
        return "skip_done"

    lines = raw.splitlines(keepends=True)
    idx = first_code_line_index(lines)
    if idx is None:
        return "skip_no_code"

    if "[따라치기 방법]" in raw:
        # 이미 안내 있음 — 본문만 주석 처리 필요할 수 있음
        header = lines[:idx]
        body = lines[idx:]
        if all(
            not b.strip() or b.lstrip().startswith("#")
            for b in body
        ):
            return "skip_done"
        new_body = comment_body(body)
        path.write_text("".join(header + new_body), encoding="utf-8")
        return "comment_only"

    header = insert_learning_block(lines[:idx])
    body = comment_body(lines[idx:])
    path.write_text("".join(header + body), encoding="utf-8")
    return "ok"


def main() -> None:
    for n in range(2, 26):
        for path in sorted(ROOT.glob(f"{n:02d}_*.py")):
            r = process_file(path)
            print(path.name, r)


if __name__ == "__main__":
    main()

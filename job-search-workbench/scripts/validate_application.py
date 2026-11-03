#!/usr/bin/env python3
"""Validate stable structural rules for a tailored HTML resume and BOSS greeting."""

from __future__ import annotations

import argparse
from html import unescape
import re
import subprocess
import sys
from pathlib import Path


FORBIDDEN = ("墨刀", "岗位匹配成果", "面向岗位的经营框架")


def finish(errors: list[str], warnings: list[str]) -> int:
    for item in warnings:
        print(f"WARNING: {item}")
    for item in errors:
        print(f"ERROR: {item}")
    if errors:
        print("APPLICATION_INVALID")
        return 1
    print("NOTE: structural checks only; factual and JD review required")
    print("APPLICATION_OK")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("resume", type=Path)
    parser.add_argument("--greeting-file", type=Path)
    parser.add_argument("--pdf", type=Path)
    args = parser.parse_args()
    errors: list[str] = []
    warnings: list[str] = []

    if not args.resume.is_file():
        errors.append(f"resume missing: {args.resume}")
        return finish(errors, warnings)

    text = args.resume.read_text(encoding="utf-8")
    if re.search(r"\{\{[^{}]+\}\}", text):
        errors.append("resume contains unresolved template placeholders")
    sheet_pattern = r'<article\b[^>]*class=["\'][^"\']*\bsheet\b'
    if len(re.findall(sheet_pattern, text)) != 2:
        errors.append("resume must contain exactly two article.sheet elements")
    if "styles/resume.css" not in text:
        errors.append("resume must link to styles/resume.css")
    if not re.search(r"<h2>\s*工具\s*</h2>", text):
        errors.append("missing separate 工具 section")
    if not re.search(r"<h2>\s*教育\s*</h2>", text):
        errors.append("missing separate 教育 section")
    for term in FORBIDDEN:
        if term in text:
            errors.append(f"forbidden resume term: {term}")
    # Check rendered labels, not archive paths, comments or legitimate employers.
    display_text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    display_text = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", "", display_text, flags=re.S | re.I)
    display_text = unescape(re.sub(r"<[^>]+>", " ", display_text))
    compact_display = re.sub(r"\s+", "", display_text)
    for label in ("定制简历", "定制版", "主简历", "JD版", "制作说明"):
        if label in compact_display:
            errors.append(f"internal label in public resume: {label}")
    label_regions = re.findall(r"<title\b[^>]*>.*?</title>|<h[1-6]\b[^>]*>.*?</h[1-6]>|<header\b[^>]*>.*?</header>|<[^>]+class=[\"'][^\"']*\bfooter\b[^\"']*[\"'][^>]*>.*?</div>", text, flags=re.S | re.I)
    for region in label_regions:
        label_text = unescape(re.sub(r"<[^>]+>", " ", region))
        if re.search(r"(?<![A-Za-z0-9])v\s*\d+(?:\.\d+)*(?![A-Za-z0-9])|版本\s*[:：]?\s*\d|第\s*\d+\s*版|草稿", label_text, re.I):
            errors.append("internal version/draft label in resume title, heading, header or footer")
            break
    for risky in ("精通", "高度匹配", "全面掌握"):
        if risky in text:
            warnings.append(f"review potentially inflated wording: {risky}")

    css_path = args.resume.parent / "styles" / "resume.css"
    if not css_path.is_file():
        errors.append(f"independent CSS missing: {css_path}")

    if args.greeting_file:
        if not args.greeting_file.is_file():
            errors.append(f"greeting missing: {args.greeting_file}")
        else:
            greeting = args.greeting_file.read_text(encoding="utf-8").strip()
            count = len(re.sub(r"\s+", "", greeting))
            if count < 80 or count > 140:
                errors.append(f"greeting length must be 80-140 non-space characters, got {count}")
            sentence_count = len(re.findall(r"[。！？!?]", greeting))
            if sentence_count > 4:
                errors.append(f"greeting must contain at most 4 sentences, got {sentence_count}")
            for term in ("精通", "专家", "资深", "高度匹配", "全面掌握"):
                if term in greeting:
                    errors.append(f"forbidden greeting term: {term}")

    if args.pdf:
        if not args.pdf.is_file():
            errors.append(f"PDF missing: {args.pdf}")
        else:
            try:
                result = subprocess.run(
                    ["pdfinfo", str(args.pdf)],
                    check=True,
                    capture_output=True,
                    text=True,
                )
                pages_match = re.search(r"^Pages:\s+(\d+)", result.stdout, re.MULTILINE)
                size_match = re.search(
                    r"^Page size:\s+([0-9.]+) x ([0-9.]+) pts",
                    result.stdout,
                    re.MULTILINE,
                )
                if not pages_match or int(pages_match.group(1)) != 2:
                    got = pages_match.group(1) if pages_match else "unknown"
                    errors.append(f"PDF must contain exactly 2 pages, got {got}")
                if not size_match:
                    errors.append("could not determine PDF page size")
                else:
                    width, height = map(float, size_match.groups())
                    if abs(width - 595.28) > 3 or abs(height - 841.89) > 3:
                        errors.append(f"PDF must be A4, got {width:.2f} x {height:.2f} pts")
            except (OSError, subprocess.CalledProcessError) as exc:
                errors.append(f"pdfinfo failed: {exc}")

    return finish(errors, warnings)


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate the stage-aware structure of a saved job package."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ALLOWED = {"待判断", "准备投递", "已投递", "HR沟通", "面试中", "Offer", "未通过", "主动暂停"}
SUBMITTED_OR_LATER = {"已投递", "HR沟通", "面试中", "Offer", "未通过"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("job_folder", type=Path)
    args = parser.parse_args()
    root = args.job_folder
    errors: list[str] = []
    warnings: list[str] = []

    required = ("JD", "岗位记录.md", "岗位分析.md", "job-context.json", "简历", "简历/styles/resume.css", "沟通", "面试")
    for rel in required:
        if not (root / rel).exists():
            errors.append(f"missing required path: {rel}")

    jd_dir = root / "JD"
    if jd_dir.is_dir() and not any(p.is_file() for p in jd_dir.iterdir()):
        errors.append("JD directory contains no source image or document")

    context_path = root / "job-context.json"
    context = None
    if context_path.is_file():
        try:
            context = json.loads(context_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid job-context.json: {exc}")

    if context is not None:
        status = context.get("status")
        if status not in ALLOWED:
            errors.append(f"invalid status: {status!r}")
        artifacts = context.get("artifacts", {})
        timeline = context.get("timeline", [])
        if not isinstance(timeline, list) or not timeline:
            errors.append("timeline must contain at least one event")
        if status in SUBMITTED_OR_LATER:
            if not artifacts.get("submitted_greeting"):
                warnings.append("submitted status without frozen submitted_greeting")
            submitted_resume = artifacts.get("submitted_resume")
            if not submitted_resume:
                warnings.append("submitted status without frozen submitted_resume")
            elif not (root / submitted_resume).is_file():
                errors.append(f"submitted resume path does not exist: {submitted_resume}")
        if status == "面试中" and not artifacts.get("interview_pack"):
            warnings.append("interview status without interview_pack path")

        for rel in artifacts.get("jd_images", []):
            if not (root / rel).is_file():
                errors.append(f"JD artifact path does not exist: {rel}")
        drafts = artifacts.get("resume_drafts", [])
        if not drafts:
            errors.append("artifacts.resume_drafts must contain at least one draft")
        for rel in drafts:
            if not (root / rel).is_file():
                errors.append(f"resume draft path does not exist: {rel}")
        if status == "准备投递" and (artifacts.get("submitted_resume") or artifacts.get("submitted_greeting")):
            errors.append("draft status must not contain submitted artifacts")
        if status == "准备投递" and not artifacts.get("draft_greeting"):
            warnings.append("draft package does not yet contain a BOSS greeting")

        allowed_permissions = {"application-only", "application-and-interview", "public", "approved"}
        for index, mapping in enumerate(context.get("evidence_map", []), start=1):
            strength = mapping.get("strength")
            claim_ids = mapping.get("claim_ids", [])
            permission = mapping.get("permission")
            if strength == "Gap" and claim_ids:
                errors.append(f"evidence_map[{index}] Gap must not contain claim_ids")
            if strength in {"Strong", "Transferable"} and not (claim_ids or mapping.get("source_pointers")):
                warnings.append(f"evidence_map[{index}] has no claim or source pointer")
            if permission and permission not in allowed_permissions:
                errors.append(f"evidence_map[{index}] permission not allowed for application: {permission}")

        record_path = root / "岗位记录.md"
        if record_path.is_file():
            record = record_path.read_text(encoding="utf-8")
            match = re.search(r"当前状态[：:]\s*([^\n]+)", record)
            if match and match.group(1).strip() != status:
                errors.append(f"status mismatch: 岗位记录={match.group(1).strip()} job-context={status}")

    resumes = list((root / "简历").glob("*.html")) if (root / "简历").is_dir() else []
    if not resumes:
        errors.append("no HTML resume draft found in 简历/")

    for item in warnings:
        print(f"WARNING: {item}")
    for item in errors:
        print(f"ERROR: {item}")
    if errors:
        print("JOB_PACKAGE_INVALID")
        return 1
    print("JOB_PACKAGE_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

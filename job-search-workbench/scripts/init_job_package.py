#!/usr/bin/env python3
"""Create a new draft job package from the Skill's reusable assets."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import date, datetime
from pathlib import Path


def safe_component(value: str) -> str:
    cleaned = re.sub(r"[\\/:*?\"<>|]", "-", value.strip())
    cleaned = re.sub(r"\s+", "", cleaned)
    return cleaned or "unknown"


def fill_template(path: Path, values: dict[str, str]) -> str:
    text = path.read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--company", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--city", default="待确认")
    parser.add_argument("--salary", default="待确认")
    parser.add_argument("--experience", default="待确认")
    parser.add_argument("--education", default="待确认")
    parser.add_argument("--recruiter", default="待确认")
    parser.add_argument("--platform", default="BOSS直聘")
    parser.add_argument("--candidate-name", default="候选人")
    parser.add_argument("--jd", action="append", default=[], type=Path)
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parent.parent
    assets = skill_root / "assets"
    folder_name = f"{args.date}_{safe_component(args.company)}_{safe_component(args.role)}"
    target = args.root / folder_name
    if target.exists():
        print(f"ERROR: target already exists: {target}")
        return 1

    for rel in ("JD", "简历/styles", "沟通", "面试"):
        (target / rel).mkdir(parents=True, exist_ok=False if rel == "JD" else True)

    values = {
        "公司": args.company,
        "岗位": args.role,
        "地点": args.city,
        "薪资": args.salary,
        "经验": args.experience,
        "学历": args.education,
        "联系人": args.recruiter,
        "平台": args.platform,
        "建议": "待分析",
        "下一步": "完成岗位分析与申请材料",
        "日期时间": datetime.now().astimezone().isoformat(timespec="minutes"),
        "date": args.date,
        "company": safe_component(args.company),
        "role": safe_component(args.role),
        "datetime": datetime.now().astimezone().isoformat(timespec="minutes"),
    }
    (target / "岗位记录.md").write_text(fill_template(assets / "job-record-template.md", values), encoding="utf-8")
    (target / "岗位分析.md").write_text(fill_template(assets / "job-analysis-template.md", values), encoding="utf-8")
    (target / "沟通/HR沟通记录.md").write_text(fill_template(assets / "hr-log-template.md", values), encoding="utf-8")
    (target / "面试/说明.md").write_text(
        "# 面试准备入口\n\n确认面试后，以实际投递简历生成面试准备、快速复习卡和面试复盘。\n",
        encoding="utf-8",
    )

    resume_name = f"{safe_component(args.candidate_name)}-{safe_component(args.role)}-v1.html"
    resume_text = (assets / "resume-template.html").read_text(encoding="utf-8")
    resume_text = resume_text.replace("{{姓名}}", args.candidate_name).replace("{{目标岗位}}", args.role)
    (target / "简历" / resume_name).write_text(resume_text, encoding="utf-8")
    shutil.copy2(assets / "styles/resume.css", target / "简历/styles/resume.css")

    jd_paths: list[str] = []
    for index, source in enumerate(args.jd, start=1):
        if not source.is_file():
            print(f"ERROR: JD source missing: {source}")
            shutil.rmtree(target)
            return 1
        suffix = source.suffix.lower() or ".bin"
        destination = target / "JD" / f"{index:02d}-JD原始资料{suffix}"
        shutil.copy2(source, destination)
        jd_paths.append(str(destination.relative_to(target)))

    context = {
        "schema_version": "1.0",
        "job_id": f"{args.date}_{safe_component(args.company)}_{safe_component(args.role)}",
        "status": "准备投递",
        "job": {
            "company": args.company,
            "role": args.role,
            "city": args.city,
            "salary": args.salary,
            "experience": args.experience,
            "education": args.education,
            "recruiter": args.recruiter,
            "platform": args.platform,
            "captured_at": datetime.now().astimezone().isoformat(timespec="minutes"),
            "posted_at": None,
            "unresolved_fields": [],
        },
        "analysis": {
            "recommendation": "待分析",
            "hiring_problem": "",
            "must_haves": [],
            "preferred": [],
            "hidden_constraints": [],
            "positioning": "",
            "gaps": [],
            "questions": [],
        },
        "evidence_map": [],
        "artifacts": {
            "jd_images": jd_paths,
            "resume_drafts": [f"简历/{resume_name}"],
            "draft_greeting": "",
            "submitted_resume": None,
            "submitted_greeting": None,
            "interview_pack": None,
            "review": None,
        },
        "pending_facts": [],
        "timeline": [
            {
                "at": datetime.now().astimezone().isoformat(timespec="minutes"),
                "from": None,
                "to": "准备投递",
                "event": "draft_created",
                "reason": "用户要求准备投递材料",
                "next_action": "完成岗位分析、BOSS话术和定制简历",
            }
        ],
    }
    (target / "job-context.json").write_text(json.dumps(context, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(target)
    return 0


if __name__ == "__main__":
    sys.exit(main())

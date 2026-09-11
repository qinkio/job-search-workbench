# Archive and lifecycle contract

## Folder structure

Use the configured archive root and name each role folder `YYYY-MM-DD_公司_岗位`. Sanitize only path-breaking characters. Do not overwrite a prior application to the same role; add a new date or stable suffix.

```text
YYYY-MM-DD_公司_岗位/
├── JD/
│   ├── 01-职位信息.png
│   ├── 02-岗位职责.png
│   └── 03-HR补充.png
├── 岗位记录.md
├── 岗位分析.md
├── job-context.json
├── 简历/
│   ├── 候选人-岗位-v1.html
│   ├── 候选人-岗位-v2.html
│   ├── 实际投递版.pdf
│   └── styles/resume.css
├── 沟通/HR沟通记录.md
└── 面试/
    ├── 面试准备.md
    ├── 快速复习卡.md
    └── 面试复盘.md
```

Create only artifacts appropriate to the current stage. Empty optional files are not required, but entry points must be clear in `岗位记录.md`.

## Status machine

Allowed states are `待判断 → 准备投递 → 已投递 → HR沟通 → 面试中 → Offer | 未通过 | 主动暂停`. Allow return from `HR沟通` to `准备投递` when the recruiter reveals a materially different scope. Do not silently move backward or reopen a closed role.

Every transition records timestamp, prior state, new state, reason, next action, and artifact versions. Preserve history.

## Draft and freeze

- Apply mode creates a draft resume version and draft message. It does not imply submission.
- Freeze mode requires user confirmation. Record the exact sent text, platform, sent time, submitted resume file, and version checksum or stable file identity when practical.
- If the actual file is unavailable, record the known version and mark the file pending rather than fabricating a PDF.
- Never overwrite the frozen submitted PDF. Later improvements become new drafts.

## Communication log

Append each recruiter exchange with date, speaker, exact or faithfully summarized message, answer sent, newly learned role facts, open questions, and next action. Treat recruiter statements as job facts, not candidate facts.

Candidate details first disclosed during communication go to `待核验事实`. They do not enter the career vault without a separate review.

## Index and outcomes

Update the root job index for saved roles. Include company, role, compensation, current status, last activity, next action, submitted resume version, and folder link.

After roughly 30 applications in one direction or after a completed interview, aggregate response rates and failure stages by role family and resume version. Propose changes; never rewrite the master narrative automatically from a small sample.

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
│   ├── 实际投递版.html
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
- Freeze the actual submitted artifact or platform version, whether HTML, PDF, or another known format.
- If the actual file is unavailable, record the known version and mark the file pending rather than fabricating an artifact.
- Never overwrite the frozen submitted artifact. Later improvements become new drafts.

## Communication log

Append each recruiter exchange with date, speaker, exact or faithfully summarized message, answer sent, newly learned role facts, open questions, and next action. Treat recruiter statements as job facts, not candidate facts.

Candidate details first disclosed during communication go to `待核验事实` with source, confirmation status and permitted use. Unconfirmed proposals are not application facts. Explicit candidate confirmation and application authorization permit scoped use; vault integration remains separate.

## Index and outcomes

Update the root job index for saved roles. Include company, role, compensation, current status, last activity, next action, submitted resume version, and folder link.

After roughly 30 applications in one direction or after a completed interview, aggregate response rates and failure stages by role family and resume version. Propose changes; never rewrite the master narrative automatically from a small sample.

## Current version identity

Use artifacts.current_resume for the single recommended draft and artifacts.archived_resume_drafts for superseded drafts; preserve resume_drafts as history. During initialization current_resume is null until the template has been replaced and reviewed. Every revision updates these pointers and the role record together, and appends its reason to the timeline. Never choose the current draft by filename sorting or modification time. Avoid ambiguous duplicate version labels.

Keep the submitted artifact separate and immutable. Export only from the selected current draft; when retaining an export record its source in artifacts.resume_exports as {path, source_resume}. Verify the rendered content corresponds to that source. Older packages without these fields remain readable, but require explicit version selection before another revision or export. Do not bulk migrate historical archives during ordinary skill maintenance.


Use validate_job_package.py --delivery for a finished package; missing current_resume is then an error. Omit --delivery when inspecting legacy packages or incomplete scaffolds.

---
name: job-search-workbench
description: "Run a private, evidence-backed job workflow from JD evaluation through application materials, recruiter communication, interview preparation, and interview review. Use for 岗位分析、是否值得投、BOSS直聘招呼、定制简历、投递归档、HR回复、面试准备、面试录音复盘, or when one active role should keep these outputs consistent. Do not send applications or messages, and keep offer comparison or salary negotiation separate."
---

# Job Search Workbench

## Current local vault workflow

Use the current career vault directly for local resume and interview tasks. Read [references/direct-vault-reading.md](references/direct-vault-reading.md) for the reading and update contract. A separate maintained evidence package is not required; exports are optional one-time transfer outputs. This direct-read mode supersedes export preferences elsewhere for local work.


Use one shared job analysis and evidence map to keep the application message, submitted resume, recruiter replies, interview answers, and post-interview review consistent. Treat the career vault as the fact source and each job folder as that role's working record.

## Load personal configuration

Read [references/personal-profile.md](references/personal-profile.md) before handling any candidate-facing claim or local file. It contains the private source paths, output paths, minimum compensation rule, and known wording boundaries for this personal Skill.

Read [references/evidence-and-consistency.md](references/evidence-and-consistency.md) before writing a message, resume, recruiter reply, or interview answer.

## Detect the mode

Infer the mode from the user's natural language. A direct mode name overrides inference.

- **Analyze:** “值得投吗”“分析这个岗位”. Evaluate only. Do not create a job folder unless the user asks to save it.
- **Apply:** “写打招呼和简历”“准备投递”. Create the shared analysis, application message, two-page HTML resume, and draft job folder.
- **Freeze:** “已投递”“这版发出去了”. Record the exact sent message, sent time, and actual submitted PDF or platform version. Never infer that a draft was sent.
- **Communicate:** “HR这样问怎么回复”. Draft the reply from approved evidence and append the exchange, new facts, and open questions to the existing job folder.
- **Interview:** “收到面试”“周三业务面”. Use the exact submitted resume, current JD, recruiter updates, and approved evidence to build the interview package.
- **Review:** “面试录音”“复盘这次面试”. Save the transcript or supplied notes, extract questions and delivery weaknesses, and propose facts for review.

If the mode is ambiguous, do the safest useful read-only work first and ask only the one question that changes a material action.

## Build the shared job context once

For every saved role, create or update both:

- `岗位分析.md` for the user.
- `job-context.json` using [references/job-context-schema.md](references/job-context-schema.md) for downstream reuse.

The shared context must contain:

1. Confirmed company, role, location, compensation, experience, education, recruiter, platform, and source dates.
2. Hiring problem, must-haves, preferred qualifications, hidden constraints, and hard disqualifiers.
3. `Strong`, `Transferable`, or `Gap` mapping from each material requirement to eligible candidate evidence.
4. Candidate positioning, primary proof, backup proof, gaps, risks, and recruiter questions.
5. Claim wording boundaries, publication permission, and source pointers.
6. Current status, artifact versions, actual submitted version when known, and event timeline.

Reuse this context. Refresh only fields changed by a new JD image, recruiter reply, candidate confirmation, or outcome. Never reclassify an unsupported claim as experience merely because the JD requests it.

## Execute the selected mode

### Analyze or Apply

Read [references/application-mode.md](references/application-mode.md). In Analyze mode, return the decision, decisive fit, gaps, and questions without creating files. In Apply mode, create the shared analysis, application materials, and draft job package.

### Freeze, Communicate, or archive updates

Read [references/archive-and-lifecycle.md](references/archive-and-lifecycle.md). Preserve drafts and prior versions. Log every status transition rather than silently replacing history.

### Interview or Review

Read [references/interview-and-review.md](references/interview-and-review.md). For a complete interview handbook, load and follow the installed `prepare-interview-pack` Skill. Do not reproduce its handbook logic here. Give it the exact submitted resume, shared job context, current recruiter information, interview time and round, and only the current relevant complete career-vault records and approved canonical claims.

## Respect stage gates

- Do not create a heavy interview handbook before an interview is confirmed. A job folder may contain only an interview-preparation entry point.
- Do not mark a role `已投递` until the user confirms the application was sent.
- Do not mark a resume or message as submitted unless its exact version is known.
- Do not promote a new claim from recruiter communication or interview review into the career vault. Put it in `待核验事实`; use `career-proof` only after explicit approval.
- Do not change resume strategy after one rejection. Aggregate outcomes after roughly 30 applications in one direction or after a completed interview, then propose changes for review.
- Do not send, upload, publish, delete, or share anything externally without the user's explicit authorization for that action.

## Keep the response lightweight

Lead with the immediate decision or requested message. In chat, show only the recommendation and decisive reason, requested message, material gap or blocking question, created or updated file links, and next action. Keep detailed mappings, history, and preparation material in the job folder.

## Validate before delivery

For application materials, run:

```bash
python3 scripts/validate_application.py /absolute/resume.html --greeting-file /absolute/greeting.txt --pdf /absolute/resume.pdf
```

Omit `--greeting-file` when no greeting was requested. Omit `--pdf` only before the render exists; it is required for final application delivery. Inspect the rendered pages for readable type, clipping, isolated education lines, and large accidental blank areas because structural PDF validation cannot judge visual quality alone.

For a saved job package, run:

```bash
python3 scripts/validate_job_package.py /absolute/job-folder
```

Treat errors as blockers. Review warnings and fix those relevant to the current stage. Validation establishes structural consistency only; it does not prove the truth or publication permission of a claim.

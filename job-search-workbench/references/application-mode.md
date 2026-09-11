# Analyze and apply modes

## Extract the JD

Treat screenshots and pasted pages as employer information, not candidate evidence. Capture all visible pages and note truncation. When multiple images exist, preserve them in order under `JD/` with descriptive names.

Identify recruiting entity, parent or brand, business unit, role, city, compensation, experience, education, work arrangement, recruiter, posting date, central hiring problem, outcomes, must-haves, preferences, hidden constraints, and disqualifiers.

Browse current authoritative sources only when company identity is ambiguous, the JD is unusually vague or high-value, or an interview is confirmed. Label inference and unresolved identity boundaries.

## Decide whether to apply

Compare hard requirements with evidence and personal constraints. Return `建议投递`, `谨慎投递`, or `不建议投递` with the decisive reason. Wording cannot solve a missing hard industry, management, technical, location, or compensation requirement.

In Analyze mode, stop after the decision, three strongest matches, material gaps, and high-value questions. Do not create a folder unless asked.

## Create the BOSS greeting

Write one directly sendable paragraph of 80–140 Chinese characters and no more than four sentences: exact role, closest truthful experience, one concrete project or approved result, and conversation intent.

Prefer project and result over adjectives. Do not repeat the JD, stack keywords, or use unsupported phrases such as `精通`, `专家`, `资深`, `高度匹配`, or generic personality claims. If the central requirement has no evidence, output `不建议发送：当前证据不足以支持该岗位的核心要求。`

## Tailor the resume

Start from `assets/resume-template.html` or the configured local mother template. Preserve the single-column visual system and independent CSS.

- Page 1: header, role positioning, professional summary, results, capabilities, main work history.
- Page 2: four or five JD-relevant projects, recent AI practice when relevant, early experience, tools, and education.
- Reorder and rewrite only from approved evidence. Do not fill space with meta commentary or weakly related claims.
- Use problem/action/result language. Keep role title and ownership boundaries explicit.
- Education must remain a separate block.
- Keep versions rather than overwriting prior drafts.

Create the draft job package using the archive contract. Prefer the deterministic initializer, then replace its placeholders with the completed analysis and tailored content:

```bash
python3 scripts/init_job_package.py --root /absolute/archive-root --company "公司" --role "岗位" --jd /absolute/JD.png
```

Pass each additional JD source with another `--jd`. The initializer refuses to overwrite an existing role folder. Save the final greeting in the job record and a separate text file when helpful for validation.

## Quality checks

- Validate the HTML and greeting with `scripts/validate_application.py`.
- Render to PDF for visual QA; verify exactly two A4 pages and inspect both pages.
- After rendering, rerun the validator with `--pdf /absolute/resume.pdf` so page count and A4 dimensions are checked deterministically.
- Fix clipping, orphaned headings, overfull contact lines, cramped type, accidental blank space, and education pushed to a third page.
- Copy the CSS into the role's `简历/styles/` directory.

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

Prefer project and result over adjectives. Do not repeat the JD, stack keywords, or use unsupported phrases such as `精通`, `专家`, `资深`, `高度匹配`, or generic personality claims. If the selected role/track has neither direct nor sufficient transferable evidence for its central requirement and no truthful basis for a useful conversation, output `不建议发送：当前证据不足以支持该岗位的核心要求。`

## Evidence selection before drafting

Read the original JD rather than relying only on a prior analysis. Identify the central deliverable and likely screening barrier. If a JD lists alternative tracks, separate shared requirements from track-specific gates; select a supported track or clarify which track is hiring. Do not merge alternatives into a fictional all-in-one role or count a weak match across several tracks as a strong match. Select the strongest relevant evidence using directness, specificity, personal judgment, recency and understandable results; keyword overlap or the largest number alone is insufficient. Distinguish direct experience, transferable experience and material gaps. Record a short rationale in the existing analysis, including whether to prioritize tailoring, make a lightweight attempt or clarify a gate first. Do not equate a polished resume with a strong match.

Order first-page proof around that deliverable. State genuine confirmed results confidently; add qualifications only where omitting them materially changes interpretation. Do not turn the resume into an audit report. Project details should explain a decision, action or constraint beyond repeating the headline number. Never manufacture a decision or metric to complete a narrative.

## Tailor the resume

Start from `assets/resume-template.html` or the configured local mother template. Preserve the single-column visual system and independent CSS.

- Default page 1: header, role positioning, professional summary, results, capabilities and main work history. Adapt section order to the JD while retaining the established visual system.
- Page 2: relevant projects, AI practice when relevant, early experience, tools and education. Choose project count and space by relevance and substance; never pad to a fixed count.
- Reorder and rewrite only from approved evidence. Do not fill space with meta commentary or weakly related claims.
- Use problem/action/result language. Keep role title and ownership boundaries explicit.
- Education must remain a separate block.
- In work history, prioritize the overall responsibilities, cumulative service scale and management scope of the role. Put the scope and results of an individual case primarily in representative projects; if cited in work history, explicitly label it as one case within the broader role. Never use a case’s customer or store count as a substitute for the role’s total scope. If the overall scale is unconfirmed, omit it or ask a targeted question when it materially affects positioning; continue drafting from confirmed facts.
- Keep versions rather than overwriting prior drafts.

Create the draft job package using the archive contract. Prefer the deterministic initializer, then replace its placeholders with the completed analysis and tailored content:

```bash
python3 scripts/init_job_package.py --root /absolute/archive-root --company "公司" --role "岗位" --jd /absolute/JD.png
```

Pass each additional JD source with another `--jd`. The initializer refuses to overwrite an existing role folder. Save the final greeting in the job record and a separate text file when helpful for validation.

## Quality checks

- Check every customer count, store count and coverage figure in context: distinguish cumulative personal service scale, concurrent service scale, system coverage, direct reports and individual case scope. A factually correct number must not imply a narrower or broader overall role than the evidence supports.
- Validate the HTML and greeting with `scripts/validate_application.py`.
- Inspect the HTML in a browser at A4 print dimensions and verify that both resume sheets are readable and visually complete.
- Do not render or save a PDF by default. When the user explicitly requests a PDF, render it, verify exactly two A4 pages, inspect both pages, and rerun the validator with `--pdf /absolute/resume.pdf`.
- Fix clipping, orphaned headings, overfull contact lines, cramped type, accidental blank space, and education pushed to a third page.
- Copy the CSS into the role's `简历/styles/` directory.

## Content acceptance review

After drafting, compare the resume with the raw JD and scoped evidence. Check metric population, action, stage, time, individual attribution, project status and the distinction between usage and business effects. Check that adjacent numbers do not imply the same cohort or unsupported causality. Distinguish internal tool adoption from external commercial conversion. Verify the recommended version and exported artifact correspond. Record meaningful unresolved issues and the review outcome in the existing job analysis; no separate mandatory report is needed.

Structural validation does not establish truth or hiring fit. A visual check that could not run must be reported as incomplete, not passed. Do not weaken an approved result simply because optional finer details are missing. Judge substantive ambiguity, not the presence of particular words.


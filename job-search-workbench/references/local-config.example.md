# Local configuration example

Copy this file to `local-config.md` inside the installed Skill, then replace the placeholders. `local-config.md` is private and should never be committed.

## Local sources and outputs

- Career asset root: `/absolute/private/path/to/career-assets`
- Approved evidence export: `/absolute/private/path/to/application-evidence.json`
- Resume template: `/absolute/private/path/to/resume-template.html`
- Shared resume CSS: `/absolute/private/path/to/resume.css`
- Job archive root: `/absolute/private/path/to/job-archive`
- Job index: `/absolute/private/path/to/job-archive/00-index.md`

Preserve original JD screenshots, resumes, transcripts, and evidence. Job folders contain purpose-specific copies and derived material, not replacements for source files.

## Candidate boundaries

- Preferred location: `{{location}}`
- Compensation constraints: `{{private rule; never place in the resume unless explicitly requested}}`
- Formal role titles: `{{approved titles}}`
- Unsupported skills or titles that must not be claimed: `{{boundaries}}`
- Approved AI or portfolio practice wording: `{{boundary}}`
- Resume layout requirements: `{{for example: two A4 pages, single column, separate tools and education}}`

## Default language and artifacts

- Language: `Chinese`
- Application resume: `two-page, single-column, A4, ATS-friendly HTML with independent CSS`
- Recruiter greeting: `80-140 Chinese characters, no more than four sentences`

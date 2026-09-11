# job-context.json schema

Use UTF-8 JSON. Preserve unknown fields during updates.

```json
{
  "schema_version": "1.0",
  "job_id": "2026-09-11_company_role",
  "status": "准备投递",
  "job": {
    "company": "",
    "role": "",
    "city": "",
    "salary": "",
    "experience": "",
    "education": "",
    "recruiter": "",
    "platform": "",
    "captured_at": "",
    "posted_at": null,
    "unresolved_fields": []
  },
  "analysis": {
    "recommendation": "建议投递",
    "hiring_problem": "",
    "must_haves": [],
    "preferred": [],
    "hidden_constraints": [],
    "positioning": "",
    "gaps": [],
    "questions": []
  },
  "evidence_map": [
    {
      "requirement": "",
      "strength": "Strong",
      "claim_ids": [],
      "source_pointers": [],
      "ownership_boundary": "",
      "permission": "application-only"
    }
  ],
  "artifacts": {
    "jd_images": [],
    "resume_drafts": [],
    "draft_greeting": "",
    "submitted_resume": null,
    "submitted_greeting": null,
    "interview_pack": null,
    "review": null
  },
  "pending_facts": [],
  "timeline": [
    {
      "at": "",
      "from": null,
      "to": "准备投递",
      "event": "draft_created",
      "reason": "",
      "next_action": ""
    }
  ]
}
```

Allowed status values: `待判断`, `准备投递`, `已投递`, `HR沟通`, `面试中`, `Offer`, `未通过`, `主动暂停`.

Allowed evidence strengths: `Strong`, `Transferable`, `Gap`. A `Gap` item must not contain invented claim IDs. `submitted_resume` and `submitted_greeting` remain null until user-confirmed submission. Timeline entries are append-only.

`captured_at` is when the source was saved. `posted_at` is the employer's posting date and remains null when not visible. Put truncated title, missing company, unclear compensation, or similar uncertainties in `unresolved_fields`; never infer them from the capture date.

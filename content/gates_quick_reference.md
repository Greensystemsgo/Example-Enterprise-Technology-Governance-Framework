Gates Quick Reference
=====================

Purpose
-------
Use this sheet to establish at a glance which approvals and artifacts are expected at each gate. It supports the best-practice workflow described in `framework_overview.md` and can be linked directly from request forms or dashboards.

Gate Summary
------------
- Gate 0 - Business Need Intake
  - Focus: capture business justification, funding, and ownership commitment via the centralized request solution.
  - Artifacts: intake form, ownership acknowledgement, initial attachments.
  - Primary Owner: Service Desk.
  - Separation of duties: Service Desk cannot approve their own requests; independent validation required.
  - Business justification: Must articulate mission/outcome/value; "tech debt" alone is insufficient unless debt remediation is fully scoped and risk-ranked with clear outcomes.
  - Suggested SLA: Triage within 2 business days (requires CAB review if repeatedly missed).

- Gate 1 - Impact & Ownership Confirmation
  - Focus: confirm capacity, classify data, and ensure every asset has named owners.
  - Artifacts: ownership matrix, impact checklist, prerequisite tracker, asset type declaration (workstation/server/other), ownership model selection (Infrastructure-managed or Requestor-managed).
  - Notes: All directory object requests (create, modify, disable, delete) must flow through centralized intake so lifecycle reviews remain audit-ready. Workstation requests route through the Service Desk by default; server engagement is determined by the ownership model confirmed at Gate 1.
  - Primary Owners: Service Desk coordination with Infrastructure, AD, Network, Security reviewers.
  - Separation of duties: Teams cannot approve their own work without independent validation from another team.
  - CAB checkpoints: High-risk or high-impact requests require CAB review.
  - Cloud workloads: Shared-responsibility mapping required.
  - Vendor milestones: Vendor onboarding preparation required.
  - Suggested SLA: Impact assessment within 5 business days (requires CAB review if repeatedly missed).

- Gate 2 - Technical & Security Review
  - Focus: finalize architecture, security controls, and risk posture.
  - Artifacts: design packet, hardening checklist, security review, exception log.
  - Notes: Security highlights vulnerability management gaps; unresolved gaps require remediation or a formal exception.
  - Primary Owners: Infrastructure, Network, Security.
  - SIEM evidence: All technical designs must include logging and monitoring requirements with SIEM integration.
  - CAB checkpoints: Technical decisions requiring exception approval must be reviewed by CAB.
  - Cloud readiness: Cloud readiness validation required.
  - Suggested SLA: Technical review within 7 business days (requires CAB review if repeatedly missed).

- Gate 3 - Financial & Procurement Approval
  - Focus: validate spend, vendor assurances, and contract alignment.
  - Artifacts: bill of materials, quotes, funding authorization, vendor attestations.
  - Primary Owners: Procurement lead with Security for vendor risk input.
  - Vendor milestones: All vendor relationships must include security attestations and compliance documentation.
  - CAB checkpoints: Vendor contracts exceeding standard thresholds require CAB review.
  - Suggested SLA: Procurement review within 3 business days (requires CAB review if repeatedly missed).

- Gate 4 - Implementation Readiness
  - Focus: confirm build prerequisites, testing, change planning, and communications.
  - Artifacts: implementation checklist, test summary, change record, communication plan, confirmation that mandatory security tooling and SIEM logging are configured.
  - Primary Owners: Infrastructure with sign-offs from AD, Network, Security, Service Desk.
  - SIEM evidence: Monitoring handoffs and post-change validation requirements.
  - Cloud readiness: Cloud deployments must demonstrate proper configuration management and monitoring setup.
  - CAB checkpoints: Emergency implementations require CAB oversight.
  - Suggested SLA: Readiness confirmation within 2 business days (requires CAB review if repeatedly missed).

- Gate 5 - Post-Implementation Verification
  - Focus: validate outcomes, update inventories, and close outstanding work.
  - Artifacts: validation report, monitoring handoff, CMDB update, training confirmation, audit evidence uploaded.
  - Primary Owners: Service Owner with Infrastructure and Security verification.
  - SIEM evidence: Post-change validation and ongoing monitoring confirmation.
  - CAB checkpoints: Emergency changes must complete verification within two business days with CAB review.
  - Suggested SLA: Verification completion within 3 business days (requires CAB review if repeatedly missed).

Emergency & Standard Changes
----------------------------
- All changes require documentation, CAB oversight, and retro review within two business days for emergencies.
- Emergency changes move rapidly but must satisfy the same artifacts within two business days after implementation.
- Emergency changes require CAB review within two business days with complete evidence package and retroactive approval.

Escalation Notes
----------------
- Any gate can trigger escalation to the Change Advisory Board (CAB) when requirements cannot be met or risks require leadership acceptance.

Linking Guidance
----------------
Reference the gate-specific templates in `templates/gates/` when embedding links in forms or workflow tools.

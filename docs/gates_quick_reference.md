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

- Gate 1 - Impact & Ownership Confirmation
  - Focus: confirm capacity, classify data, and ensure every asset has named owners.
  - Artifacts: ownership matrix, impact checklist, prerequisite tracker, asset type declaration (workstation/server/other), ownership model selection (Infrastructure-managed or Requestor-managed).
  - Notes: All directory object requests (create, modify, disable, delete) must flow through centralized intake so lifecycle reviews remain audit-ready. Workstation requests route through the Service Desk by default; server engagement is determined by the ownership model confirmed at Gate 1.
  - Primary Owners: Service Desk coordination with Infrastructure, AD, Network, Security reviewers.

- Gate 2 - Technical & Security Review
  - Focus: finalize architecture, security controls, and risk posture.
  - Artifacts: design packet, hardening checklist, security review, exception log.
  - Notes: Security highlights vulnerability management gaps; unresolved gaps require remediation or a formal exception.
  - Primary Owners: Infrastructure, Network, Security.

- Gate 3 - Financial & Procurement Approval
  - Focus: validate spend, vendor assurances, and contract alignment.
  - Artifacts: bill of materials, quotes, funding authorization, vendor attestations.
  - Primary Owners: Procurement lead with Security for vendor risk input.

- Gate 4 - Implementation Readiness
  - Focus: confirm build prerequisites, testing, change planning, and communications.
  - Artifacts: implementation checklist, test summary, change record, communication plan, confirmation that mandatory security tooling and SIEM logging are configured.
  - Primary Owners: Infrastructure with sign-offs from AD, Network, Security, Service Desk.

- Gate 5 - Post-Implementation Verification
  - Focus: validate outcomes, update inventories, and close outstanding work.
  - Artifacts: validation report, monitoring handoff, CMDB update, training confirmation, audit evidence uploaded.
  - Primary Owners: Service Owner with Infrastructure and Security verification.

Escalation Notes
----------------
- Any gate can trigger escalation to the Governance Council when requirements cannot be met or risks require leadership acceptance.
- Emergency changes move rapidly but must satisfy the same artifacts within two business days after implementation.

Linking Guidance
----------------
Reference the gate-specific templates in `templates/gates/` when embedding links in forms or workflow tools.

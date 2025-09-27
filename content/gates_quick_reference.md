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
  - Business justification: Must articulate mission/outcome/value or risk reduction; "tech debt" only acceptable if fully scoped with risk impact assessment and clear remediation outcomes.
  - Change types: Normal, Major, Standard, Emergency changes all follow formal intake process.
  - Suggested SLA: Triage within 2 business days (requires CAB review if repeatedly missed).

- Gate 1 - Impact & Ownership Confirmation
  - Focus: confirm capacity, classify data, and ensure every asset has named owners.
  - Artifacts: ownership matrix, impact checklist, prerequisite tracker, asset type declaration (workstation/server/other), ownership model selection (Infrastructure-managed or Requestor-managed).
  - Notes: All directory object requests (create, modify, disable, delete) must flow through centralized intake so lifecycle reviews remain audit-ready. Workstation requests route through the Service Desk by default; server engagement is determined by the ownership model confirmed at Gate 1.
  - Primary Owners: Service Desk coordination with Infrastructure, AD, Network, Security reviewers.
  - Separation of duties: Teams cannot approve their own work without independent validation from another team.
  - CAB checkpoints: High-risk or high-impact requests require CAB review.
  - Data classification touchpoints: Reference Data Classification Matrix and include appropriate handling requirements.
  - Accessibility/privacy checks: WCAG 2.1 AA compliance validation and privacy impact assessment for citizen-facing systems.
  - Cloud workloads: Cloud shared-responsibility mapping required.
  - Vendor milestones: Vendor onboarding preparation required.
  - Suggested SLA: Impact assessment within 5 business days (requires CAB review if repeatedly missed).

- Gate 2 - Technical & Security Review
  - Focus: finalize architecture, security controls, and risk posture.
  - Artifacts: design packet, hardening checklist, security review, exception log.
  - Notes: Security highlights vulnerability management gaps; unresolved gaps require remediation or a formal exception.
  - Primary Owners: Infrastructure, Network, Security.
  - Data classification validation: Technical designs must align with data classification requirements and handling procedures.
  - Accessibility/privacy validation: WCAG 2.1 AA compliance verification and privacy impact assessment completion required.
  - SIEM evidence: All technical designs must include logging and monitoring requirements with minimum logging profile verification.
  - Risk scoring: Qualitative risk assessment using risk scoring method with CAB escalation thresholds.
  - CAB checkpoints: Technical decisions requiring exception approval must be reviewed by CAB.
  - Cloud readiness: Cloud readiness validation required.
  - Suggested SLA: Technical review within 7 business days (requires CAB review if repeatedly missed).

- Gate 3 - Financial & Procurement Approval
  - Focus: validate spend, vendor assurances, and contract alignment.
  - Artifacts: bill of materials, quotes, funding authorization, vendor attestations.
  - Primary Owners: Procurement lead with Security for vendor risk input.
  - Vendor due diligence: SOC 2 Type II or equivalent attestation, SIG-Lite questionnaire completion, breach notification SLA documentation, data location disclosure required.
  - Vendor milestones: All vendor relationships must include security attestations and compliance documentation using vendor due diligence checklist.
  - CAB checkpoints: Vendor contracts exceeding standard thresholds require CAB review.
  - Suggested SLA: Procurement review within 3 business days (requires CAB review if repeatedly missed).

- Gate 4 - Implementation Readiness
  - Focus: confirm build prerequisites, testing, change planning, and communications.
  - Artifacts: implementation checklist, test summary, change record, communication plan, confirmation that mandatory security tooling and SIEM logging are configured.
  - Primary Owners: Infrastructure with sign-offs from AD, Network, Security, Service Desk.
  - Logging profile verification: All systems must meet minimum logging profile requirements with retention and verification confirmation.
  - Service tiering checks: RTO/RPO validation, patch/vulnerability management SLA confirmation, backup and recovery testing completion.
  - SIEM evidence: Monitoring handoffs and post-change validation requirements.
  - Cloud readiness: Cloud deployments must demonstrate proper configuration management and monitoring setup.
  - CAB checkpoints: Emergency implementations require CAB oversight.
  - Suggested SLA: Readiness confirmation within 2 business days (requires CAB review if repeatedly missed).

- Gate 5 - Post-Implementation Verification
  - Focus: validate outcomes, update inventories, and close outstanding work.
  - Artifacts: validation report, monitoring handoff, CMDB update, training confirmation, audit evidence uploaded.
  - Primary Owners: Service Owner with Infrastructure and Security verification.
  - Risk register updates: All identified risks must be documented in risk register template with mitigation status and review dates.
  - Legal-hold confirmation: Data retention and legal-hold requirements must be documented and confirmed for applicable systems.
  - SIEM evidence: Post-change validation and ongoing monitoring confirmation.
  - CAB checkpoints: Emergency changes must complete verification within two business days with CAB review.
  - Suggested SLA: Verification completion within 3 business days (requires CAB review if repeatedly missed).

Emergency & Standard Changes
----------------------------
- All changes require documentation, CAB oversight, and retro review within two business days for emergencies.
- Emergency changes move rapidly but must satisfy the same artifacts within two business days after implementation.
- Emergency changes require CAB review within two business days with complete evidence package and retroactive approval.
- Standard change catalog requires annual review and CAB oversight for pre-approved activities.

Gate RACI Reference
-------------------
- For detailed responsibility and accountability matrices across all gates, see the Gate RACI Reference which outlines Responsible, Accountable, Consulted, and Informed roles for each gate artifact.

Escalation Notes
----------------
- Any gate can trigger escalation to the Change Advisory Board (CAB) when requirements cannot be met or risks require leadership acceptance.

Linking Guidance
----------------
Reference the gate-specific templates in `templates/gates/` when embedding links in forms or workflow tools.

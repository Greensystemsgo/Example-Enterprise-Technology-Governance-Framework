Enterprise Technology Governance Overview
=======================================

1. Purpose and Scope
--------------------
This overview captures recommended best practices for coordinating technology work in alignment with the Mayor's [Executive Directive No. 2 on cybersecurity](https://d3n8a8pro7vhmx.cloudfront.net/mayorofla/pages/17070/attachments/original/1426620047/ED2_with_signature_and_letterhead.pdf). A signed copy is stored in `executive_directive_2/executive_directive_2_signed_letterhead.pdf`. It defines standard approval gates and collaboration touchpoints every technology request should satisfy before funds are committed or enterprise assets are changed. It applies to all departments, business units, contractors, and vendors that interact with the City's technology environment. This document is guidance, not a formal policy, and nothing here should be viewed as new; it reflects long-standing industry standards (TSA, CIS, NIST) and City directives that everyone is expected to understand and follow.

2. Guiding Principles
---------------------
- Ownership is defined and documented for the full lifecycle of every asset, service, or process.
- No work proceeds without passing the prescribed gates; approvals are secured prior to purchase orders, provisioning, or deployment.
- Documentation and audit trails are mandatory. If it is not recorded, it is not considered complete.
- All requests, approvals, artifacts, and communications are captured in the centralized request solution. Ad-hoc channels (chat, email, hallway conversations) do not meet compliance requirements.
- Collaboration across core teams (Infrastructure, Active Directory, Service Desk, Network, Security) is the default operating model.
- Practices align with the City's cybersecurity mandates, including the Mayor's [Executive Directive No. 2 on cybersecurity](https://d3n8a8pro7vhmx.cloudfront.net/mayorofla/pages/17070/attachments/original/1426620047/ED2_with_signature_and_letterhead.pdf).
- Audit expectations mirror TSA, CIS, and NIST guidance: controls must be reviewable, repeatable, and evidenced through the centralized request process.

3. Governance Bodies and Roles
------------------------------
- Business Requestor: Initiates requests, provides business justification, funding source, and confirms operational ownership.
- Service Desk ([Service Desk Overview](teams/service_desk_overview.html)): Operates the intake queue, validates completeness, and logs requests in the official system of record. The Service Desk manages the workstation fleet lifecycle by default; its involvement in server workflows is coordinated with Infrastructure and the owning team based on organizational policy.
- Infrastructure Team ([Infrastructure Overview](teams/infrastructure_overview.html)): Reviews hosting, compute, storage, backup, and platform requirements; leads provisioning after all gates clear. Server ownership defaults to Infrastructure unless the requesting team formally accepts lifecycle responsibilities during Gate 1.
- Active Directory (AD) Team ([Active Directory Overview](teams/active_directory_overview.html)): Manages domain joins, account provisioning, and directory policy enforcement.
- Network Team ([Network Overview](teams/network_overview.html)): Ensures segmentation, addressing, firewall, and connectivity compliance.
- Security Team (including SOC) ([Security Overview](teams/security_overview.html)): Performs risk assessment, validates alignment with security baselines, identifies process gaps (e.g., vulnerability management, logging coverage), maintains the exception program, and may isolate or take assets offline to investigate anomalies.
- Governance Council (cross-team): Reviews escalated or high-risk items, resolves disputes, and signs off on exceptions.

4. Standard Request Lifecycle and Gates
---------------------------------------
Every technology request progresses through the following stages. Gate artifacts are stored with the request record and may not be bypassed. Use the quick-reference summary in [Gates Quick Reference](./gates_quick_reference.html) for a one-page view of gate expectations. Gate templates are organized in `templates/gates/`, with supporting team worksheets in the team-specific subfolders.

- Gate 0 - Business Need Intake
  - Required artifacts: intake form, business justification, funding source, target timeline, ownership acknowledgement.
  - Service Desk confirms completeness and assigns tracking ID in the centralized request solution. Informal channels do not satisfy intake requirements.

- Gate 1 - Impact & Ownership Confirmation
  - Infrastructure, AD, Network, and Security teams receive the request simultaneously.
  - Required artifacts: ownership matrix, asset classification, asset type declaration (workstation, server, other), data sensitivity statement, support runway plan, capacity estimate, ownership model selection (Infrastructure-managed or Requestor-managed).
  - All requests to create, modify, disable, or delete directory objects must be routed through the centralized request process so lifecycle actions remain auditable.
  - Owners confirm they can accept responsibilities; otherwise the request is paused until gaps are resolved.

- Gate 2 - Technical & Security Review
  - Infrastructure validates hosting strategy; Network confirms network design; Security issues the risk assessment.
  - Required artifacts: architecture diagram, configuration standards checklist, patching approach, security controls checklist, exception log (if applicable).
  - Security highlights risk gaps identified through vulnerability management or other monitoring efforts; teams must either remediate or file a formal exception.
  - Outputs: go/no-go decision, remediation tasks, or escalation to the Governance Council.

- Gate 3 - Financial & Procurement Approval
  - Purchasing authority verifies vendor compliance, warranty terms, maintenance coverage, and budget alignment.
  - Required artifacts: bill of materials, quotes, vendor security attestations, funding authorization signature.

- Gate 4 - Implementation Readiness
  - All teams confirm prerequisites are satisfied prior to implementation: naming conventions, asset tags, image approval, change window, rollback plan.
  - Required artifacts: implementation checklist, test results summary, change record, communication plan, confirmation that mandatory security tooling baselines are deployed and logging feeds are configured to the central SIEM.

- Gate 5 - Post-Implementation Verification
  - Requestor and core teams complete verification, store documentation, and confirm operational ownership.
  - Required artifacts: validation report, monitoring handoff, updated CMDB/asset registry entry, training materials (if applicable), confirmation that ongoing logging continues to the SIEM.

5. Ownership Expectations
-------------------------
The ownership matrix is the authoritative record of who is responsible for every asset, configuration item, and supporting process introduced by a request. It is created during Gate 0 and validated at Gate 1; requests without a complete matrix do not advance. The matrix stays attached to the request so auditors and responders can see exactly who owns day-to-day operations versus escalation and compliance tasks.

Minimum columns for the ownership matrix:

- Asset/Service Name
- Primary Owner (name, team, contact)
- Backup Owner (name, team, contact)
- Support Model (Infrastructure-managed or Requestor-managed)
- Core Responsibilities (patch cadence, monitoring, backups, DR, documentation)
- Escalation Path (24x7 on-call rotation or contractual contact)
- Runbook/Artifact Links (procedures, diagrams, CMDB entries)

Example ownership matrix entry:

| Asset/Service | Primary Owner | Backup Owner | Support Model | Core Responsibilities | Escalation Path | Runbook Links |
| --- | --- | --- | --- | --- | --- | --- |
| HR Records Platform | Jane Smith (HRIS) | Infrastructure Duty Manager | Infrastructure-managed | Quarterly patching, nightly backups, SIEM log review | Infrastructure On-Call (213-555-0100) | `\\city\runbooks\hris\operations.md` |

Usage expectations:

- Workstations default to the Service Desk support model (see [Service Desk Overview](teams/service_desk_overview.html)); servers default to the Infrastructure-managed model unless the requesting team formally accepts lifecycle ownership ([Infrastructure Overview](teams/infrastructure_overview.html)).
- Directory-integrated services must document their AD dependencies and matrix ownership in collaboration with the [Active Directory Overview](teams/active_directory_overview.html) practices.
- Network connectivity, segmentation, and firewall stewardship must align with the responsibilities documented in the [Network Overview](teams/network_overview.html).
- Security obligations (patching SLAs, logging, exception handling, incident response escalation) are documented in the matrix consistent with the [Security Overview](teams/security_overview.html).
- Requestors selecting the Requestor-managed model must document how they will fulfill Infrastructure and Security baseline tasks, including tooling requirements and evidence collection for audits.
- The matrix is reviewed at each gate to verify ownership remains accurate; changes after Gate 5 must be logged through the centralized request system so the matrix stays current.

6. Documentation, Audit, and Lifecycle Reviews
----------------------------------------------
- Gate artifacts, approvals, and communications are stored in the centralized request system with version control and retention per records policy.
- Audit evidence must demonstrate alignment with TSA, CIS, and NIST expectations, including periodic lifecycle reviews of Active Directory objects and associated access.
- Directory object lifecycle reviews validate join requests, disablements, deletions, and permission changes. All actions are initiated through the centralized request process to preserve traceability.
- Security maintains a formal exception process. Requests that cannot meet baseline requirements, including logging obligations, use this process to document compensating controls, expiration dates, and risk acceptance.

7. Cross-Team Standards
-----------------------
- Naming conventions for servers, workstations, network devices, and service accounts are published jointly and applied before Gate 4 approval.
- New hosts must deploy the mandatory security tooling stack, satisfy baseline hardening requirements, and forward logs to the central SIEM unless a documented security exception is approved.
- All technology assets?servers, workstations, network devices, appliances, applications, or specialty systems?must send security-relevant logs to the central SIEM.
- Asset inventory is updated at Gate 5; no asset operates in production without an assigned owner, maintenance plan, and lifecycle end date.
- Emergency changes follow the same gates retroactively within two business days and require Governance Council review.
- When team process requirements conflict, the stricter control prevails unless an exception is granted in writing by the Governance Council.

8. Continuous Improvement
-------------------------
- Core teams meet monthly to review failed gates, escalations, and audit findings.
- Lessons learned update standards, templates, and training materials for requestors.
- Matured processes are documented as playbooks and shared to reduce rework and accelerate compliant delivery.
- Security shares vulnerability management trends, SOC findings, and exception metrics so teams address root causes, not just individual incidents.



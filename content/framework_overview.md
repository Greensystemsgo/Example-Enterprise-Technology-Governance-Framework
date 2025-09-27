Enterprise Technology Governance Overview
=======================================

1. Purpose and Scope
--------------------
This overview captures recommended best practices for coordinating technology work in alignment with the Mayor's [Executive Directive No. 2 on cybersecurity](https://d3n8a8pro7vhmx.cloudfront.net/mayorofla/pages/17070/attachments/original/1426620047/ED2_with_signature_and_letterhead.pdf). A signed copy is stored in `executive_directive_2/executive_directive_2_signed_letterhead.pdf`. It defines standard approval gates and collaboration touchpoints every technology request should satisfy before funds are committed or enterprise assets are changed. This framework applies to the entire organization—all departments, business units, contractors, and vendors that interact with the City's technology environment. Organizations must maintain awareness of applicable laws and regulations including but not limited to CIS, NIST, TSA, CPRA, CJIS, and GDPR requirements. This framework remains tool-agnostic and focuses on governance outcomes rather than specific platform implementations. This document is guidance, not a formal policy, and nothing here should be viewed as new; it reflects long-standing industry standards and City directives that everyone is expected to understand and follow.

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
- Change Advisory Board (CAB): Reviews escalated or high-risk items, resolves disputes, and signs off on exceptions. The CAB serves as the governance authority for technology change management.

### Governance Council Operating as Change Advisory Board (CAB)

The Governance Council operates in a CAB capacity as the primary governance body for technology change oversight, with the following characteristics:

**Membership Example:**
- CIO (Chair)
- CISO
- Infrastructure Director
- Security Lead
- Legal/Procurement Liaison
- Rotating Business Owner (based on request domain)

**Quorum Rules:**
- Minimum three members present
- Must include Security or Finance representative for all decisions
- Business owner participation required for requests affecting their domain
- No single team can approve all steps; CAB validates that approvals span independent reviewers

**Decision Authority:**
- Pause work that fails to meet governance standards
- Demand remediation actions and evidence
- Accept residual risk with documented justification
- Escalate to executive leadership when necessary

**Escalation Triggers:**
- High-risk requests with incomplete evidence
- Emergency changes requiring retroactive review
- Exception requests exceeding standard thresholds
- Cross-departmental impact or resource conflicts
- Regulatory compliance concerns

### Centralized Request Solution Expectations

The centralized request solution serves as the single source of truth for all technology requests and must provide the following capabilities:

**Core Capabilities:**
- Role-based access control with appropriate segregation of duties
- Comprehensive audit logs with immutable retention
- Document retention aligned with records management policies
- API access for reporting and integration needs
- Offline contingency procedures for emergency situations

**Tool Examples (Optional Illustrations):**
Organizations may consider solutions such as ServiceNow, Jira, Cherwell, or similar platforms that provide these capabilities. These examples are provided for illustration only; the specific tool selection should align with organizational standards and integration requirements.

4. Standard Request Lifecycle and Gates
---------------------------------------
Every technology request progresses through the following stages. Gate artifacts are stored with the request record and may not be bypassed. Use the quick-reference summary in [Gates Quick Reference](./gates_quick_reference.html) for a one-page view of gate expectations. Gate templates are organized in `templates/gates/`, with supporting team worksheets in the team-specific subfolders.

- Gate 0 - Business Need Intake
  - Required artifacts: intake form, business justification, funding source, target timeline, ownership acknowledgement.
  - Service Desk confirms completeness and assigns tracking ID in the centralized request solution. Informal channels do not satisfy intake requirements.
  - Separation of duties: Service Desk cannot approve their own requests; independent validation required.
  - Business justification criteria: Must articulate mission/outcome/value; "tech debt" alone is insufficient unless debt remediation is fully scoped and risk-ranked with clear outcomes.
  - Documentation requirements: All business justification must include regulatory compliance considerations and data classification.
  - Emergency change handling: Emergency requests must still follow formal intake but may expedite subsequent gates with CAB oversight.
  - Suggested SLA: Triage within 2 business days (requires CAB review if repeatedly missed).

- Gate 1 - Impact & Ownership Confirmation
  - Infrastructure, AD, Network, and Security teams receive the request simultaneously.
  - Required artifacts: ownership matrix, asset classification, asset type declaration (workstation, server, other), data sensitivity statement, support runway plan, capacity estimate, ownership model selection (Infrastructure-managed or Requestor-managed).
  - All requests to create, modify, disable, or delete directory objects must be routed through the centralized request process so lifecycle actions remain auditable.
  - Owners confirm they can accept responsibilities; otherwise the request is paused until gaps are resolved.
  - Separation of duties: Teams cannot approve their own work without independent validation from another team.
  - Dual approvals: High-risk or high-impact requests require dual approval from both technical and business stakeholders.
  - Cloud workloads: Special consideration for shared responsibility model and cloud provider dependencies; shared-responsibility mapping required.
  - Vendor/contractor steps: Third-party involvement must be documented with clear ownership boundaries; vendor onboarding preparation required.
  - Suggested SLA: Impact assessment within 5 business days (requires CAB review if repeatedly missed).

- Gate 2 - Technical & Security Review
  - Infrastructure validates hosting strategy; Network confirms network design; Security issues the risk assessment.
  - Required artifacts: architecture diagram, configuration standards checklist, patching approach, security controls checklist, exception log (if applicable).
  - Security highlights risk gaps identified through vulnerability management or other monitoring efforts; teams must either remediate or file a formal exception.
  - Outputs: go/no-go decision, remediation tasks, or escalation to the CAB.
  - Separation of duties: Security team cannot approve their own infrastructure requests; independent technical review required.
  - SIEM evidence: All technical designs must include logging and monitoring requirements with SIEM integration.
  - Cloud readiness: Cloud workloads must demonstrate compliance with shared responsibility model; cloud readiness validation required.
  - Suggested SLA: Technical review within 7 business days (requires CAB review if repeatedly missed).

- Gate 3 - Financial & Procurement Approval
  - Purchasing authority verifies vendor compliance, warranty terms, maintenance coverage, and budget alignment.
  - Required artifacts: bill of materials, quotes, vendor security attestations, funding authorization signature.
  - Separation of duties: Procurement cannot approve their own department's requests; independent financial oversight required.
  - Vendor/contractor workflow: Risk assessment, contract clauses, onboarding requirements with CAB oversight.
  - Vendor checkpoints: All vendor relationships must include security attestations and compliance documentation.
  - Contract clauses: Vendor agreements must include cybersecurity requirements and audit rights.
  - Suggested SLA: Procurement review within 3 business days (requires CAB review if repeatedly missed).

- Gate 4 - Implementation Readiness
  - All teams confirm prerequisites are satisfied prior to implementation: naming conventions, asset tags, image approval, change window, rollback plan.
  - Required artifacts: implementation checklist, test results summary, change record, communication plan, confirmation that mandatory security tooling baselines are deployed and logging feeds are configured to the central SIEM.
  - SIEM/logging evidence: Monitoring handoffs and post-change validation requirements.
  - Cloud readiness: Cloud deployments must demonstrate proper configuration management and monitoring setup.
  - Emergency change handling: Emergency implementations require retroactive CAB review within two business days with complete evidence package.
  - Suggested SLA: Readiness confirmation within 2 business days (requires CAB review if repeatedly missed).

- Gate 5 - Post-Implementation Verification
  - Requestor and core teams complete verification, store documentation, and confirm operational ownership.
  - Required artifacts: validation report, monitoring handoff, updated CMDB/asset registry entry, training materials (if applicable), confirmation that ongoing logging continues to the SIEM.
  - SIEM/logging evidence: Post-change validation and ongoing monitoring confirmation.
  - Emergency change handling: Emergency changes must complete verification within two business days with CAB review.
  - Evidence requirements: All implementations must provide audit evidence of successful deployment and ongoing monitoring.
  - Suggested SLA: Verification completion within 3 business days (requires CAB review if repeatedly missed).

**Emergency and Standard Changes:**
Emergency and pre-approved standard changes still run through the same gates, with CAB post-review within two business days for emergency changes. All changes must maintain audit trail and evidence collection regardless of approval pathway.

### Vendor & Contractor Governance

All vendor and contractor relationships must follow a structured governance workflow with CAB oversight:

**Intake & Assessment:**
- All vendor engagements must originate through the centralized request process
- Initial assessment includes security posture, compliance capabilities, and risk profile
- Business justification must demonstrate vendor necessity and alternatives considered

**Contract Clauses:**
- Cybersecurity requirements and audit rights must be included in all agreements
- Data handling and privacy obligations must align with applicable regulations
- Incident response and breach notification procedures must be defined
- Termination and data return procedures must be specified

**Onboarding:**
- Vendor access provisioning follows the same gate process as internal requests
- Identity lifecycle management for vendor accounts must be documented
- Network access and segmentation requirements must be validated
- Security training and awareness requirements must be completed

**Ongoing Monitoring:**
- Regular security assessments and compliance reviews
- Performance metrics and SLA monitoring
- Access reviews and privilege management
- Incident response coordination and reporting

**Renewal & Offboarding:**
- Contract renewal requires updated security assessment and CAB review
- Offboarding must include complete data return and access revocation
- Knowledge transfer and documentation handover requirements
- Post-engagement security review and lessons learned

**Clear Owner Expectations:**
- Each vendor relationship must have a designated business owner
- Technical oversight responsibilities must be clearly defined
- Security monitoring and incident response roles must be assigned
- Regular CAB reporting on vendor performance and risk status
- Owners must maintain evidence throughout the lifecycle; Procurement, Security, and CAB share oversight responsibilities

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
- Evidence quality expectations: All documentation must be tool-independent and focus on business outcomes rather than specific platform implementations.
- Cloud alignment: Cloud workloads must clearly document which security controls are managed by the organization versus the cloud provider.
- Minimum annual review cadence: All technology assets and processes must undergo annual review with updated risk assessments and compliance validation.
- Team SOP development: Each team is expected to develop detailed standard operating procedures and policies based on this framework, tailored to their specific operational requirements.

7. Cross-Team Standards
-----------------------
- Naming conventions for servers, workstations, network devices, and service accounts are published jointly and applied before Gate 4 approval.
- New hosts must deploy the mandatory security tooling stack, satisfy baseline hardening requirements, and forward logs to the central SIEM unless a documented security exception is approved.
- All technology assets—servers, workstations, network devices, appliances, applications, or specialty systems—must send security-relevant logs to the central SIEM.
- Asset inventory is updated at Gate 5; no asset operates in production without an assigned owner, maintenance plan, and lifecycle end date.
- Emergency changes follow the same gates retroactively within two business days and require CAB review.
- When team process requirements conflict, the stricter control prevails unless an exception is granted in writing by the CAB.
- Separation of duties for approval and verification activities: No single team can approve all steps; independent validation required across teams.

### SIEM and Logging Standards

**Minimum Telemetry Categories:**
- Endpoint security events (authentication, privilege escalation, file access)
- Identity and access management (logins, permission changes, account modifications)
- Network traffic and security events (firewall logs, intrusion detection, VPN access)
- Cloud control plane activities (configuration changes, API calls, resource provisioning)

**Evidence Quality Checks:**
- Log completeness validation and gap analysis
- Timestamp accuracy and synchronization verification
- Data integrity and tamper detection
- Retention compliance and archival procedures

**CAB Acceptance Criteria:**
- All security-relevant events must be captured and retained per policy
- Log analysis capabilities must support incident investigation and compliance reporting
- Integration with security tools and incident response workflows
- Regular validation of logging effectiveness and coverage

**Standard Changes and Maintenance:**
- Standard changes, maintenance windows, and emergency changes all follow the same gates with CAB oversight
- Only pre-approved standard changes may shortcut timing but still require documentation and periodic review
- All changes must maintain audit trail and evidence collection regardless of approval pathway

8. Continuous Improvement
-------------------------
- Core teams meet monthly to review failed gates, escalations, and audit findings with CAB feedback integration.
- Lessons learned update standards, templates, and training materials for requestors.
- Matured processes are documented as playbooks and shared to reduce rework and accelerate compliant delivery.
- Security shares vulnerability management trends, SOC findings, and exception metrics so teams address root causes, not just individual incidents.
- Annual framework refresh incorporates CAB recommendations, regulatory updates, and industry best practices.



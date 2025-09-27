Active Directory Overview
========================

1. Mission
----------
Safeguard the City's identity services by governing domain membership, account provisioning, and directory policies that underpin secure access to enterprise resources. This overview presents recommended best practices aligned with the Mayor's Executive Directive on cybersecurity and is not a formal policy.

2. Core Outcomes
----------------
- Identity Assurance: Enforce standards for account lifecycle, privileged access, and group policy configuration.
- Domain Hygiene: Maintain accurate organizational units, group structures, and automated controls that reduce manual effort.
- Lifecycle Compliance: Execute TSA/CIS/NIST-aligned audit policies for directory objects, ensuring every change is reviewable and traceable.
- Logging Coverage: Confirm domain controllers and identity-integrated services send security-relevant events to the central SIEM.
- Operational Insight: Provide metrics on join requests, provisioning lead times, audit findings, and exception status to stakeholders.

3. Engagement in the Request Lifecycle
--------------------------------------
- Gate 0/1: Review ownership acknowledgements for account sponsorship, confirm directory prerequisites, and reject informal requests that bypass the centralized intake.
- Gate 2: Assess domain join requirements, group policy needs, and access design in collaboration with Infrastructure and Security.
- Gate 3: Validate licensing impacts for directory-integrated services and document recurring support considerations.
- Gate 4: Approve naming conventions, service accounts, and group assignments before implementation proceeds, verifying mandatory security tooling and SIEM logging requirements are met where applicable.
- Gate 5: Confirm directory updates were completed, CMDB attributes are refreshed, lifecycle reviews are scheduled, logging remains active, and ongoing maintenance is assigned.

4. Collaboration Touchpoints
----------------------------
- Service Desk: Provide provisioning guides and automated workflows for standardized account requests routed through the centralized system.
- Infrastructure: Align on image preparation, OU placement, service account management, and log forwarding requirements.
- Network Team: Coordinate on authentication dependencies such as site definitions, replication, network segmentation, and secure log transport.
- Security Team: Share audit results, privileged access reviews, exception requests, remediation actions, and SOC findings related to identity controls.

5. Key Checklists and Artifacts
-------------------------------
- [AD Account Provisioning Template](../templates/ad/ad_account_provisioning_template.html): captures justification, owner approval, access scope, and logging requirements for service accounts.
- [AD Domain Join Checklist](../templates/ad/ad_domain_join_checklist.html): covers naming, OU placement, policy linkage, and SIEM onboarding steps.
- [AD Group Policy Change Log](../templates/ad/ad_group_policy_change_log.html): summarizes updates, testing evidence, deployment timing, and logging implications.
- [AD Privileged Access Review Schedule](../templates/ad/ad_privileged_access_review_schedule.html): documents frequency, participants, reporting requirements, and centralized exception tracking.

6. Continuous Improvement
-------------------------
- Conduct regular policy reviews to incorporate updated cybersecurity directives, logging standards, and emerging threats.
- Automate repetitive provisioning steps and integrate approvals with the request system where feasible.
- Track service-level targets for account provisioning, domain join turnarounds, logging coverage, and report to the Governance Council.
- Host quarterly knowledge sessions with stakeholder teams to explain standards, changes, audit results, logging mandates, and lifecycle review findings.

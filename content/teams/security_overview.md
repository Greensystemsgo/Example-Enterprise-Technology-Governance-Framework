Security Overview
================

1. Mission
----------
Protect the City's information assets by enforcing cybersecurity directives, assessing risk, and partnering with teams to implement effective controls. This overview offers recommended best practices aligned with the Mayor's Executive Directive on cybersecurity and does not constitute formal policy.

2. Core Outcomes
----------------
- Risk Assessment: Evaluate technology requests against security baselines, identify gaps highlighted by vulnerability management, and ensure teams address both findings and underlying process issues.
- Control Validation: Confirm logging, monitoring, vulnerability management, and access controls meet minimum standards.
- Audit Governance: Maintain TSA/CIS/NIST-aligned audit policies, including directory lifecycle reviews and evidence capture within the centralized request system.
- SOC Operations: Investigate anomalies and alerts, isolate or take assets offline when required, and coordinate with owners to justify continued risk exposure through the formal exception process.
- Governance Reporting: Provide visibility into risk posture, exception trends, remediation progress, and systemic gaps for leadership.

3. Engagement in the Request Lifecycle
--------------------------------------
- Gate 0/1: Review data classification, regulatory obligations, and ownership commitments for security accountability, ensuring all requests follow the centralized intake path.
- Gate 2: Lead the security review, produce risk assessment summaries, prescribe required controls or compensating measures, and document any required exceptions.
- Gate 3: Validate that vendors comply with cybersecurity requirements and that procurement artifacts include necessary assurances.
- Gate 4: Confirm hardening, vulnerability scan results, logging configuration, mandatory security tooling deployment, and SIEM integration are in place.
- Gate 5: Verify residual risks are accepted by the appropriate authority, monitoring integrations are operational, audit evidence is stored, and recurring control reviews are scheduled.
- CAB participation: Security provides risk assessments and security recommendations to CAB for all high-risk or complex requests.
- Required SME sign-offs: Security provides recommendations and evidence for CAB decisions; teams may not self-approve every step.
- Separation of duties: Security cannot approve their own requests; independent validation required from other teams.

4. Collaboration Touchpoints
----------------------------
- Service Desk: Provide guidance on security requirements for intake checklists and user communications.
- Infrastructure: Partner on hardening standards, patch cadence, backup validation, mandatory tooling enforcement, and logging coverage.
- Active Directory Team: Align on authentication policies, privileged access reviews, lifecycle audits, and directory exception handling.
- Network Team: Coordinate on segmentation strategies, firewall standards, SIEM telemetry integrations, and response playbooks.
- Cloud services: Security ensures cloud telemetry parity, shared responsibility model compliance, and cloud security posture management.
- Vendor oversight: Security tracks risk assessments, compliance validation, and ongoing security monitoring for vendor relationships; role in vendor/contractor oversight as relevant.

5. Key Checklists and Artifacts
-------------------------------
- [Security Review Template](../templates/security/security_review_template.html): captures data classification, threats, controls, residual risk, and centralized evidence references.
- [Security Exception Register](../templates/security/security_exception_register.html): documents approvals, central request IDs, expiration dates, and required follow-up actions.
- [Security Vulnerability Dashboard](../templates/security/security_vulnerability_dashboard.html): summarizes scan coverage, remediation timelines, outstanding findings, and systemic issues.
- [Security Incident Readiness Checklist](../templates/security/security_incident_readiness_checklist.html): covers monitoring, alert routing, SOC escalation paths, and on-call contact validation.

6. Continuous Improvement
-------------------------
- Conduct tabletop exercises and incident simulations to validate readiness, documenting corrective actions within agreed timelines.
- Track remediation performance, risk trends, exception closure rates, audit observations, and SOC isolation events; report insights to the CAB.
- Update security baselines in response to new directives, threats, or technology platforms.
- Deliver periodic awareness sessions for core teams and requestors on evolving security expectations, exception processes, and logging mandates.
- Tie continuous improvement activities to CAB feedback, annual framework refresh, and metrics reporting to the Governance Council/CAB.

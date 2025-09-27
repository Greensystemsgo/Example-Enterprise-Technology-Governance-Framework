Infrastructure Team Overview
===========================

1. Mission
----------
Deliver stable, secure, and recoverable compute, storage, and platform services that enable City departments to operate reliably and in compliance with cybersecurity directives. This overview shares recommended best practices aligned with the Mayor's Executive Directive on cybersecurity and is not a formal policy.

2. Core Outcomes
----------------
- Provisioning: Coordinate build activities for on-premises and cloud workloads once governance gates are cleared.
- Platform Resilience: Maintain patching, backup, and recovery practices that meet agreed recovery objectives.
- Server Custodianship: Serve as the default owner for server platforms unless a requesting team formally accepts lifecycle responsibilities through Gate 1.
- Security Baseline: Ensure every new host deploys the mandatory security tooling stack, meets hardening requirements, and forwards logs to the central SIEM unless a documented exception is approved.
- Standards Stewardship: Publish and maintain golden images, configuration baselines, and lifecycle plans for shared platforms.
- Operational Insight: Keep infrastructure records, diagrams, and metrics current so stakeholders can make informed decisions.

3. Engagement in the Request Lifecycle
--------------------------------------
- Gate 0/1: Assess capacity impacts, validate ownership commitments, and highlight any prerequisite work submitted through the centralized request solution.
- Gate 2: Recommend hosting patterns, document infrastructure requirements, collaborate with Network and Security peers on the design package, and confirm logging/monitoring coverage.
- Gate 3: Confirm the bill of materials, licensing impacts, and support contracts before purchases proceed.
- Gate 4: Use the implementation checklist to verify naming conventions, image selection, backup enrollment, monitoring, mandatory security tooling deployment, SIEM integration, and change scheduling.
- Gate 5: Validate build outcomes, update inventories, deliver run notes, confirm logging flow, and confirm operational ownership.

4. Collaboration Touchpoints
----------------------------
- Service Desk: Share status updates, standard build offerings, and knowledge articles for recurring requests, focusing on workstation engagement while coordinating server workflows as organizational policy dictates.
- Active Directory Team: Align on domain joins, group policies, and service account requirements.
- Network Team: Agree on segmentation, addressing, firewall changes, load-balancing considerations, and SIEM feed validation.
- Security Team: Review hardening, vulnerability scan results, logging configurations, residual risk statements, and exception requests until resolved.

5. Key Checklists and Artifacts
-------------------------------
- [Infrastructure New Build Checklist](../templates/infrastructure/infrastructure_new_build_checklist.html): covers provisioning, configuration hardening, mandatory tooling deployment, SIEM logging, and monitoring handoff.
- [Infrastructure Image Release Log](../templates/infrastructure/infrastructure_image_release_log.html): outlines version history, validation evidence, and deployment guidance.
- [Infrastructure Maintenance Calendar](../templates/infrastructure/infrastructure_maintenance_calendar.html): shows planned patch windows, emergency windows, and blackout periods.
- [Infrastructure Backup Readiness Worksheet](../templates/infrastructure/infrastructure_backup_readiness_worksheet.html): captures RPO/RTO targets, test evidence, and escalation contacts.

6. Continuous Improvement
-------------------------
- Hold retrospectives after high-impact incidents or failed gates and record corrective actions within ten business days.
- Review control posture quarterly with Security and Internal Audit to confirm alignment with city directives.
- Track lead times, change success rate, backup compliance, logging coverage, and ownership coverage; share metrics with the Governance Council.
- Publish an annual modernization roadmap detailing priorities, resource needs, and risk-reduction initiatives.

Network Overview
===============

1. Mission
----------
Design, secure, and operate the City's network infrastructure to provide reliable connectivity, segmentation, telemetry, and performance for all approved services. This overview summarizes recommended best practices aligned with the Mayor's Executive Directive on cybersecurity and does not represent formal policy.

2. Core Outcomes
----------------
- Segmentation Control: Define and enforce network zones, VLANs, and firewall policies that align with security directives.
- Connectivity Assurance: Plan and implement routing, load balancing, remote access, and isolation capabilities with minimal disruption.
- Visibility and Monitoring: Maintain telemetry, logging to the central SIEM, and alerting that supports rapid incident response and capacity planning.
- Lifecycle Stewardship: Manage hardware refresh cycles, configuration baselines, and vendor support relationships.

3. Engagement in the Request Lifecycle
--------------------------------------
- Gate 0/1: Evaluate impact on network capacity, address allocation, segmentation requirements, and logging coverage.
- Gate 2: Review architecture diagrams, firewall rule requests, network security controls, and SIEM integration with Infrastructure and Security peers.
- Gate 3: Confirm hardware, licensing, and carrier costs; document long-term support implications.
- Gate 4: Approve cutover plans, change windows, rollback strategies, monitoring updates, and confirm logs will flow to the SIEM once live.
- Gate 5: Validate connectivity, update network documentation, verify logging, and ensure operational ownership is accepted.

4. Collaboration Touchpoints
----------------------------
- Service Desk: Share standard network service offerings, change communication templates, and centralized request requirements for network work.
- Infrastructure: Align on load balancer configurations, DNS updates, network dependencies for new workloads, and SIEM telemetry needs.
- Active Directory Team: Coordinate on site definitions, replication topology, secure channel requirements, and log routing.
- Security Team / SOC: Co-author firewall standards, review segmentation exceptions, integrate telemetry with SIEM and incident response playbooks, and coordinate isolation actions when needed.

5. Key Checklists and Artifacts
-------------------------------
- [Network Firewall Change Checklist](../templates/network/network_firewall_change_checklist.html): captures rule justification, expiration dates, validation evidence, and SIEM logging confirmation.
- [Network Design Template](../templates/network/network_design_template.html): details VLAN assignments, IP plans, dependency mapping, and logging requirements.
- [Network Cutover Playbook](../templates/network/network_cutover_playbook.html): outlines change steps, validation tests, communication contacts, and rollback criteria.
- [Network Capacity Dashboard](../templates/network/network_capacity_dashboard.html): shows utilization trends, incident hotspots, refresh priorities, and telemetry health.

6. Continuous Improvement
-------------------------
- Perform post-change reviews for major network events and document lessons learned within ten business days.
- Refresh segmentation models and logging coverage in response to audit findings, threat intelligence, or architectural updates.
- Benchmark performance, availability, and telemetry targets, sharing results with the Governance Council.
- Update standards and templates when new technologies or security directives require changes to baseline practices.

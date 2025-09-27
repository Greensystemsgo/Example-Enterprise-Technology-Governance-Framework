# Gate RACI Reference

## RACI Matrix Legend
- **R (Responsible):** Does the work
- **A (Accountable):** Accountable for the outcome
- **C (Consulted):** Provides input and expertise
- **I (Informed):** Kept informed of progress and outcomes

## Gate 0 - Business Need Intake

| Artifact | Service Desk | Business Owner | Infrastructure | AD | Network | Security | Procurement | CAB |
|----------|--------------|----------------|----------------|----|---------|----------|-------------|-----|
| Intake Form | R | A | I | I | I | I | I | I |
| Business Justification | C | R/A | I | I | I | I | I | I |
| Funding Source | C | R/A | I | I | I | I | C | I |
| Target Timeline | C | R/A | I | I | I | I | I | I |
| Ownership Acknowledgement | C | R/A | I | I | I | I | I | I |
| Data Classification | C | R/A | I | I | I | C | I | I |
| Accessibility/Privacy Check | C | R/A | I | I | I | C | I | I |

## Gate 1 - Impact & Ownership Confirmation

| Artifact | Service Desk | Business Owner | Infrastructure | AD | Network | Security | Procurement | CAB |
|----------|--------------|----------------|----------------|----|---------|----------|-------------|-----|
| Ownership Matrix | R | A | C | C | C | C | I | I |
| Asset Classification | C | A | R | C | C | C | I | I |
| Asset Type Declaration | C | A | R | C | C | C | I | I |
| Data Sensitivity Statement | C | A | C | C | C | R | I | I |
| Support Runway Plan | C | A | R | C | C | C | I | I |
| Capacity Estimate | C | A | R | C | C | C | I | I |
| Ownership Model Selection | C | A | R | C | C | C | I | I |
| Cloud Shared-Responsibility Mapping | C | A | R | C | C | R | I | I |
| Vendor Onboarding Preparation | C | A | C | C | C | C | R | I |

## Gate 2 - Technical & Security Review

| Artifact | Service Desk | Business Owner | Infrastructure | AD | Network | Security | Procurement | CAB |
|----------|--------------|----------------|----------------|----|---------|----------|-------------|-----|
| Architecture Diagram | I | A | R | C | C | C | I | I |
| Configuration Standards | I | A | R | C | C | C | I | I |
| Patching Approach | I | A | R | C | C | C | I | I |
| Security Controls Checklist | I | A | C | C | C | R | I | I |
| Exception Log | I | A | C | C | C | R | I | I |
| Data Classification Validation | I | A | C | C | C | R | I | I |
| Accessibility/Privacy Validation | I | A | C | C | C | R | I | I |
| SIEM Evidence | I | A | R | C | C | R | I | I |
| Cloud Readiness Validation | I | A | R | C | C | R | I | I |
| Risk Scoring | I | A | C | C | C | R | I | I |

## Gate 3 - Financial & Procurement Approval

| Artifact | Service Desk | Business Owner | Infrastructure | AD | Network | Security | Procurement | CAB |
|----------|--------------|----------------|----------------|----|---------|----------|-------------|-----|
| Bill of Materials | I | A | C | I | I | I | R | I |
| Quotes | I | A | C | I | I | I | R | I |
| Vendor Security Attestations | I | A | C | I | I | R | R | I |
| Funding Authorization | I | R/A | I | I | I | I | C | I |
| SOC 2 Type II Attestation | I | A | C | I | I | R | R | I |
| SIG-Lite Questionnaire | I | A | C | I | I | R | R | I |
| Breach Notification SLA | I | A | C | I | I | R | R | I |
| Data Location Disclosure | I | A | C | I | I | R | R | I |
| Vendor Due Diligence | I | A | C | I | I | R | R | I |

## Gate 4 - Implementation Readiness

| Artifact | Service Desk | Business Owner | Infrastructure | AD | Network | Security | Procurement | CAB |
|----------|--------------|----------------|----------------|----|---------|----------|-------------|-----|
| Implementation Checklist | R | A | R | C | C | C | I | I |
| Test Results Summary | C | A | R | C | C | C | I | I |
| Change Record | C | A | R | C | C | C | I | I |
| Communication Plan | R | A | C | C | C | C | I | I |
| Security Tooling Baseline | I | A | R | C | C | R | I | I |
| SIEM Integration | I | A | R | C | C | R | I | I |
| Logging Profile Verification | I | A | R | C | C | R | I | I |
| Service Tiering Checks | I | A | R | C | C | C | I | I |
| RTO/RPO Validation | I | A | R | C | C | C | I | I |
| Patch/Vuln SLA Confirmation | I | A | R | C | C | R | I | I |
| Backup/Recovery Testing | I | A | R | C | C | C | I | I |

## Gate 5 - Post-Implementation Verification

| Artifact | Service Desk | Business Owner | Infrastructure | AD | Network | Security | Procurement | CAB |
|----------|--------------|----------------|----------------|----|---------|----------|-------------|-----|
| Validation Report | R | A | R | C | C | C | I | I |
| Monitoring Handoff | C | A | R | C | C | R | I | I |
| CMDB Update | C | A | R | C | C | C | I | I |
| Training Materials | R | A | C | C | C | C | I | I |
| Audit Evidence | C | A | R | C | C | R | I | I |
| Risk Register Updates | I | A | C | C | C | R | I | I |
| Legal-Hold Confirmation | I | A | C | C | C | R | I | I |
| SIEM Evidence | I | A | R | C | C | R | I | I |
| Ongoing Monitoring | I | A | R | C | C | R | I | I |

## Cross-Gate Responsibilities

### Service Desk
- **Primary Role:** Intake coordination, communication, and user support
- **Key Responsibilities:** Request intake, user communication, training materials, metrics collection
- **Accountability:** Intake quality, user satisfaction, communication effectiveness

### Business Owner
- **Primary Role:** Business justification, funding, and ownership
- **Key Responsibilities:** Business justification, funding authorization, ownership commitment, requirements definition
- **Accountability:** Business value, funding approval, ownership acceptance

### Infrastructure Team
- **Primary Role:** Technical implementation and capacity management
- **Key Responsibilities:** Hosting strategy, capacity planning, implementation execution, technical validation
- **Accountability:** Technical feasibility, capacity availability, implementation success

### Active Directory Team
- **Primary Role:** Identity and access management
- **Key Responsibilities:** Identity provisioning, access controls, directory services, authentication
- **Accountability:** Identity security, access control effectiveness, directory integrity

### Network Team
- **Primary Role:** Network connectivity and security
- **Key Responsibilities:** Network design, connectivity, firewall rules, network security
- **Accountability:** Network availability, connectivity security, firewall effectiveness

### Security Team
- **Primary Role:** Security controls and risk management
- **Key Responsibilities:** Security review, risk assessment, control validation, compliance
- **Accountability:** Security posture, risk management, compliance validation

### Procurement Team
- **Primary Role:** Vendor management and financial approval
- **Key Responsibilities:** Vendor due diligence, contract management, financial approval, vendor oversight
- **Accountability:** Vendor compliance, financial approval, contract effectiveness

### Change Advisory Board (CAB)
- **Primary Role:** Governance oversight and decision making
- **Key Responsibilities:** Risk assessment, approval decisions, escalation management, governance oversight
- **Accountability:** Governance effectiveness, risk management, decision quality

## Escalation Procedures

### Standard Escalation
- **Gate 0:** Service Desk escalates incomplete or complex requests to CAB
- **Gate 1:** Teams escalate capacity or ownership issues to CAB
- **Gate 2:** Security escalates high-risk or complex technical issues to CAB
- **Gate 3:** Procurement escalates vendor or financial issues to CAB
- **Gate 4:** Infrastructure escalates implementation readiness issues to CAB
- **Gate 5:** Teams escalate verification or compliance issues to CAB

### Emergency Escalation
- **All Gates:** Emergency requests escalate directly to CAB with immediate notification
- **CAB Response:** CAB provides immediate response and approval for emergency requests
- **Documentation:** Emergency escalations require complete documentation and retroactive review

### Executive Escalation
- **High-Risk Requests:** CAB escalates high-risk requests to executive leadership
- **Resource Conflicts:** CAB escalates resource conflicts to executive leadership
- **Policy Exceptions:** CAB escalates policy exceptions to executive leadership
- **Compliance Issues:** CAB escalates compliance issues to executive leadership

## Integration with Governance Framework

### Gate Integration
- **RACI Alignment:** RACI matrix aligns with gate processes and responsibilities
- **Decision Authority:** RACI matrix defines decision authority and approval processes
- **Escalation Procedures:** RACI matrix defines escalation procedures and authority
- **Accountability:** RACI matrix ensures clear accountability and responsibility

### Risk Management
- **Risk Ownership:** RACI matrix defines risk ownership and management responsibilities
- **Risk Escalation:** RACI matrix defines risk escalation procedures and authority
- **Risk Mitigation:** RACI matrix defines risk mitigation responsibilities and accountability
- **Risk Reporting:** RACI matrix defines risk reporting responsibilities and accountability

### Compliance Management
- **Compliance Ownership:** RACI matrix defines compliance ownership and management responsibilities
- **Compliance Validation:** RACI matrix defines compliance validation responsibilities and accountability
- **Compliance Reporting:** RACI matrix defines compliance reporting responsibilities and accountability
- **Compliance Improvement:** RACI matrix defines compliance improvement responsibilities and accountability

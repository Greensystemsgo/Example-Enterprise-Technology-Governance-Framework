# Gate to NIST/CIS Matrix

## NIST Cybersecurity Framework 2.0 Mapping

### Gate 0 - Business Need Intake

| NIST CSF Function | NIST CSF Category | Gate 0 Artifacts | Implementation |
|-------------------|-------------------|------------------|----------------|
| **Govern (GV)** | GV.OC - Organizational Context | Business justification, funding source, ownership acknowledgement | Business context and requirements documented |
| **Govern (GV)** | GV.RM - Risk Management Strategy | Data classification, accessibility/privacy assessment | Risk management strategy aligned with business needs |
| **Identify (ID)** | ID.AM - Asset Management | Asset type declaration, ownership model | Asset management requirements identified |
| **Identify (ID)** | ID.BE - Business Environment | Business justification, target timeline | Business environment requirements documented |
| **Identify (ID)** | ID.GV - Governance | Ownership acknowledgement, data classification | Governance requirements established |

### Gate 1 - Impact & Ownership Confirmation

| NIST CSF Function | NIST CSF Category | Gate 1 Artifacts | Implementation |
|-------------------|-------------------|------------------|----------------|
| **Identify (ID)** | ID.AM - Asset Management | Asset classification, asset type declaration, ownership matrix | Asset management requirements confirmed |
| **Identify (ID)** | ID.RA - Risk Assessment | Data sensitivity statement, capacity estimate | Risk assessment requirements established |
| **Identify (ID)** | ID.SC - Supply Chain Risk Management | Vendor onboarding preparation, cloud shared-responsibility mapping | Supply chain risk management requirements established |
| **Protect (PR)** | PR.AC - Identity Management and Access Control | Ownership model selection, access control requirements | Identity and access control requirements established |
| **Protect (PR)** | PR.DS - Data Security | Data classification, data handling requirements | Data security requirements established |

### Gate 2 - Technical & Security Review

| NIST CSF Function | NIST CSF Category | Gate 2 Artifacts | Implementation |
|-------------------|-------------------|------------------|----------------|
| **Protect (PR)** | PR.AC - Identity Management and Access Control | Architecture diagram, security controls checklist | Identity and access control implementation |
| **Protect (PR)** | PR.DS - Data Security | Data classification validation, encryption requirements | Data security implementation |
| **Protect (PR)** | PR.IP - Information Protection Processes and Procedures | Configuration standards, patching approach | Information protection processes implementation |
| **Protect (PR)** | PR.MA - Maintenance | Patching approach, maintenance procedures | Maintenance procedures implementation |
| **Protect (PR)** | PR.PT - Protective Technology | Security controls checklist, SIEM evidence | Protective technology implementation |
| **Detect (DE)** | DE.AE - Anomalies and Events | SIEM evidence, logging requirements | Anomaly and event detection implementation |
| **Detect (DE)** | DE.CM - Security Continuous Monitoring | Minimum logging profile, monitoring requirements | Continuous monitoring implementation |
| **Respond (RS)** | RS.RP - Response Planning | Risk scoring, incident response requirements | Response planning implementation |

### Gate 3 - Financial & Procurement Approval

| NIST CSF Function | NIST CSF Category | Gate 3 Artifacts | Implementation |
|-------------------|-------------------|------------------|----------------|
| **Govern (GV)** | GV.RM - Risk Management Strategy | Vendor due diligence, risk assessment | Risk management strategy implementation |
| **Identify (ID)** | ID.SC - Supply Chain Risk Management | Vendor due diligence checklist, SOC 2 attestation | Supply chain risk management implementation |
| **Protect (PR)** | PR.IP - Information Protection Processes and Procedures | Vendor security attestations, compliance documentation | Information protection processes implementation |
| **Protect (PR)** | PR.DS - Data Security | Data location disclosure, breach notification SLA | Data security implementation |
| **Respond (RS)** | RS.CO - Communications | Breach notification SLA, communication procedures | Communications implementation |

### Gate 4 - Implementation Readiness

| NIST CSF Function | NIST CSF Category | Gate 4 Artifacts | Implementation |
|-------------------|-------------------|------------------|----------------|
| **Protect (PR)** | PR.AC - Identity Management and Access Control | Implementation checklist, access control validation | Identity and access control implementation |
| **Protect (PR)** | PR.DS - Data Security | Data security validation, encryption implementation | Data security implementation |
| **Protect (PR)** | PR.IP - Information Protection Processes and Procedures | Configuration validation, process implementation | Information protection processes implementation |
| **Protect (PR)** | PR.MA - Maintenance | Patch management, maintenance procedures | Maintenance procedures implementation |
| **Protect (PR)** | PR.PT - Protective Technology | Security tooling baseline, SIEM integration | Protective technology implementation |
| **Detect (DE)** | DE.AE - Anomalies and Events | Logging profile verification, monitoring setup | Anomaly and event detection implementation |
| **Detect (DE)** | DE.CM - Security Continuous Monitoring | Monitoring validation, continuous monitoring setup | Continuous monitoring implementation |
| **Respond (RS)** | RS.RP - Response Planning | Incident response validation, response procedures | Response planning implementation |

### Gate 5 - Post-Implementation Verification

| NIST CSF Function | NIST CSF Category | Gate 5 Artifacts | Implementation |
|-------------------|-------------------|------------------|----------------|
| **Protect (PR)** | PR.AC - Identity Management and Access Control | Access control validation, identity management verification | Identity and access control verification |
| **Protect (PR)** | PR.DS - Data Security | Data security verification, encryption validation | Data security verification |
| **Protect (PR)** | PR.IP - Information Protection Processes and Procedures | Process verification, procedure validation | Information protection processes verification |
| **Protect (PR)** | PR.MA - Maintenance | Maintenance verification, patch management validation | Maintenance procedures verification |
| **Protect (PR)** | PR.PT - Protective Technology | Security tooling verification, SIEM validation | Protective technology verification |
| **Detect (DE)** | DE.AE - Anomalies and Events | Logging verification, monitoring validation | Anomaly and event detection verification |
| **Detect (DE)** | DE.CM - Security Continuous Monitoring | Monitoring verification, continuous monitoring validation | Continuous monitoring verification |
| **Respond (RS)** | RS.RP - Response Planning | Incident response verification, response procedures validation | Response planning verification |
| **Recover (RC)** | RC.RP - Recovery Planning | Backup verification, recovery procedures validation | Recovery planning verification |

## CIS Controls v8 Mapping

### Gate 0 - Business Need Intake

| CIS Control | Control Description | Gate 0 Artifacts | Implementation |
|-------------|-------------------|------------------|----------------|
| **CIS Control 1** | Inventory and Control of Enterprise Assets | Asset type declaration, ownership model | Asset inventory requirements established |
| **CIS Control 2** | Inventory and Control of Software Assets | Software requirements, licensing considerations | Software inventory requirements established |
| **CIS Control 3** | Data Protection | Data classification, data handling requirements | Data protection requirements established |
| **CIS Control 4** | Secure Configuration of Enterprise Assets and Software | Configuration requirements, security baselines | Secure configuration requirements established |
| **CIS Control 5** | Account Management | Ownership acknowledgement, access requirements | Account management requirements established |

### Gate 1 - Impact & Ownership Confirmation

| CIS Control | Control Description | Gate 1 Artifacts | Implementation |
|-------------|-------------------|------------------|----------------|
| **CIS Control 1** | Inventory and Control of Enterprise Assets | Asset classification, asset type declaration | Asset inventory requirements confirmed |
| **CIS Control 2** | Inventory and Control of Software Assets | Software requirements, licensing validation | Software inventory requirements confirmed |
| **CIS Control 3** | Data Protection | Data sensitivity statement, data handling requirements | Data protection requirements confirmed |
| **CIS Control 4** | Secure Configuration of Enterprise Assets and Software | Configuration requirements, security baselines | Secure configuration requirements confirmed |
| **CIS Control 5** | Account Management | Ownership model selection, access control requirements | Account management requirements confirmed |
| **CIS Control 6** | Access Control Management | Access control requirements, authorization procedures | Access control management requirements confirmed |

### Gate 2 - Technical & Security Review

| CIS Control | Control Description | Gate 2 Artifacts | Implementation |
|-------------|-------------------|------------------|----------------|
| **CIS Control 4** | Secure Configuration of Enterprise Assets and Software | Configuration standards, security controls checklist | Secure configuration implementation |
| **CIS Control 5** | Account Management | Account management requirements, access controls | Account management implementation |
| **CIS Control 6** | Access Control Management | Access control implementation, authorization procedures | Access control management implementation |
| **CIS Control 7** | Continuous Vulnerability Management | Vulnerability management, patch management | Continuous vulnerability management implementation |
| **CIS Control 8** | Audit Log Management | SIEM evidence, logging requirements | Audit log management implementation |
| **CIS Control 9** | Email and Web Browser Protections | Web browser protections, email security | Email and web browser protections implementation |
| **CIS Control 10** | Malware Defenses | Malware protection, antivirus requirements | Malware defenses implementation |
| **CIS Control 11** | Data Recovery | Backup requirements, recovery procedures | Data recovery implementation |
| **CIS Control 12** | Network Infrastructure Management | Network security, firewall requirements | Network infrastructure management implementation |
| **CIS Control 13** | Data Protection | Data encryption, data handling procedures | Data protection implementation |
| **CIS Control 14** | Security Awareness and Skills Training | Security training requirements, awareness programs | Security awareness and skills training implementation |

### Gate 3 - Financial & Procurement Approval

| CIS Control | Control Description | Gate 3 Artifacts | Implementation |
|-------------|-------------------|------------------|----------------|
| **CIS Control 15** | Service Provider Management | Vendor due diligence, vendor security attestations | Service provider management implementation |
| **CIS Control 16** | Application Software Security | Application security requirements, secure development | Application software security implementation |
| **CIS Control 17** | Incident Response Management | Incident response procedures, breach notification | Incident response management implementation |
| **CIS Control 18** | Penetration Testing | Penetration testing requirements, security testing | Penetration testing implementation |

### Gate 4 - Implementation Readiness

| CIS Control | Control Description | Gate 4 Artifacts | Implementation |
|-------------|-------------------|------------------|----------------|
| **CIS Control 4** | Secure Configuration of Enterprise Assets and Software | Configuration validation, security baselines | Secure configuration implementation |
| **CIS Control 5** | Account Management | Account management validation, access controls | Account management implementation |
| **CIS Control 6** | Access Control Management | Access control validation, authorization procedures | Access control management implementation |
| **CIS Control 7** | Continuous Vulnerability Management | Vulnerability management validation, patch management | Continuous vulnerability management implementation |
| **CIS Control 8** | Audit Log Management | Logging profile verification, SIEM integration | Audit log management implementation |
| **CIS Control 9** | Email and Web Browser Protections | Web browser protections validation, email security | Email and web browser protections implementation |
| **CIS Control 10** | Malware Defenses | Malware protection validation, antivirus requirements | Malware defenses implementation |
| **CIS Control 11** | Data Recovery | Backup validation, recovery procedures | Data recovery implementation |
| **CIS Control 12** | Network Infrastructure Management | Network security validation, firewall requirements | Network infrastructure management implementation |
| **CIS Control 13** | Data Protection | Data encryption validation, data handling procedures | Data protection implementation |
| **CIS Control 14** | Security Awareness and Skills Training | Security training validation, awareness programs | Security awareness and skills training implementation |

### Gate 5 - Post-Implementation Verification

| CIS Control | Control Description | Gate 5 Artifacts | Implementation |
|-------------|-------------------|------------------|----------------|
| **CIS Control 4** | Secure Configuration of Enterprise Assets and Software | Configuration verification, security baselines | Secure configuration verification |
| **CIS Control 5** | Account Management | Account management verification, access controls | Account management verification |
| **CIS Control 6** | Access Control Management | Access control verification, authorization procedures | Access control management verification |
| **CIS Control 7** | Continuous Vulnerability Management | Vulnerability management verification, patch management | Continuous vulnerability management verification |
| **CIS Control 8** | Audit Log Management | Logging verification, SIEM validation | Audit log management verification |
| **CIS Control 9** | Email and Web Browser Protections | Web browser protections verification, email security | Email and web browser protections verification |
| **CIS Control 10** | Malware Defenses | Malware protection verification, antivirus requirements | Malware defenses verification |
| **CIS Control 11** | Data Recovery | Backup verification, recovery procedures | Data recovery verification |
| **CIS Control 12** | Network Infrastructure Management | Network security verification, firewall requirements | Network infrastructure management verification |
| **CIS Control 13** | Data Protection | Data encryption verification, data handling procedures | Data protection verification |
| **CIS Control 14** | Security Awareness and Skills Training | Security training verification, awareness programs | Security awareness and skills training verification |

## Compliance Mapping Summary

### NIST CSF 2.0 Coverage
- **Govern (GV):** Organizational context, risk management strategy
- **Identify (ID):** Asset management, business environment, governance, risk assessment, supply chain risk management
- **Protect (PR):** Identity management, data security, information protection processes, maintenance, protective technology
- **Detect (DE):** Anomalies and events, security continuous monitoring
- **Respond (RS):** Response planning, communications
- **Recover (RC):** Recovery planning

### CIS Controls v8 Coverage
- **Basic Controls (1-6):** Inventory, data protection, secure configuration, account management, access control
- **Foundational Controls (7-16):** Vulnerability management, audit logging, email/web protections, malware defenses, data recovery, network infrastructure, data protection, security awareness, service provider management, application security, incident response, penetration testing
- **Organizational Controls (17-18):** Incident response management, penetration testing

### Compliance Validation
- **Gate Integration:** All gates integrate with NIST CSF and CIS Controls
- **Artifact Alignment:** Gate artifacts align with NIST CSF categories and CIS Controls
- **Implementation Validation:** Implementation validates compliance with frameworks
- **Verification Requirements:** Verification confirms compliance with frameworks
- **Audit Support:** Framework mapping supports audit and compliance processes

## Integration with Governance Framework

### Gate Process Integration
- **NIST CSF Integration:** NIST CSF functions integrated into all gate processes
- **CIS Controls Integration:** CIS Controls integrated into all gate processes
- **Compliance Validation:** Compliance validation integrated into gate processes
- **Audit Support:** Framework mapping supports audit and compliance processes

### Risk Management Integration
- **Risk Assessment:** Framework mapping integrated into risk assessment
- **Risk Mitigation:** Framework mapping integrated into risk mitigation
- **Risk Monitoring:** Framework mapping integrated into risk monitoring
- **Risk Reporting:** Framework mapping integrated into risk reporting

### Continuous Improvement Integration
- **Framework Updates:** Framework mapping updated with framework changes
- **Compliance Monitoring:** Framework mapping supports compliance monitoring
- **Audit Preparation:** Framework mapping supports audit preparation
- **Training and Awareness:** Framework mapping supports training and awareness programs

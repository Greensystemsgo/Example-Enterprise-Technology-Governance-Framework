# Cloud Shared Responsibility Matrix

## Service Models and Responsibility Matrix

### Software as a Service (SaaS)

| Control Category | Customer Responsibility | Provider Responsibility | Shared Responsibility |
|------------------|------------------------|-------------------------|----------------------|
| **Identity & Access Management** | User provisioning, access policies, authentication configuration | Identity infrastructure, authentication services | Access control policies, user management |
| **Data Classification** | Data classification, handling procedures, retention policies | Data storage infrastructure, backup systems | Data protection, encryption implementation |
| **Logging & Monitoring** | Log analysis, alert configuration, incident response | Log collection, storage, basic monitoring | Log forwarding, monitoring integration |
| **Backup & Recovery** | Backup policies, recovery procedures, testing | Backup infrastructure, storage systems | Backup configuration, recovery planning |
| **Configuration Management** | Application configuration, user settings | Application infrastructure, platform services | Configuration policies, change management |
| **Legal & Compliance** | Compliance requirements, audit preparation | Compliance infrastructure, audit support | Compliance validation, audit coordination |

### Infrastructure as a Service (IaaS)

| Control Category | Customer Responsibility | Provider Responsibility | Shared Responsibility |
|------------------|------------------------|-------------------------|----------------------|
| **Identity & Access Management** | User provisioning, access policies, authentication configuration | Identity infrastructure, authentication services | Access control policies, user management |
| **Data Classification** | Data classification, handling procedures, retention policies | Physical infrastructure, data center security | Data protection, encryption implementation |
| **Logging & Monitoring** | Log analysis, alert configuration, incident response | Physical infrastructure, basic monitoring | Log forwarding, monitoring integration |
| **Backup & Recovery** | Backup policies, recovery procedures, testing | Physical infrastructure, storage systems | Backup configuration, recovery planning |
| **Configuration Management** | OS configuration, application deployment, patch management | Physical infrastructure, hypervisor management | Configuration policies, change management |
| **Legal & Compliance** | Compliance requirements, audit preparation | Physical infrastructure, compliance support | Compliance validation, audit coordination |

### Platform as a Service (PaaS)

| Control Category | Customer Responsibility | Provider Responsibility | Shared Responsibility |
|------------------|------------------------|-------------------------|----------------------|
| **Identity & Access Management** | User provisioning, access policies, authentication configuration | Identity infrastructure, authentication services | Access control policies, user management |
| **Data Classification** | Data classification, handling procedures, retention policies | Platform infrastructure, data services | Data protection, encryption implementation |
| **Logging & Monitoring** | Log analysis, alert configuration, incident response | Platform infrastructure, basic monitoring | Log forwarding, monitoring integration |
| **Backup & Recovery** | Backup policies, recovery procedures, testing | Platform infrastructure, storage systems | Backup configuration, recovery planning |
| **Configuration Management** | Application configuration, deployment policies | Platform infrastructure, runtime services | Configuration policies, change management |
| **Legal & Compliance** | Compliance requirements, audit preparation | Platform infrastructure, compliance support | Compliance validation, audit coordination |

## Control Implementation Guidelines

### Customer Responsibilities

#### Identity & Access Management
- **User Provisioning:** Implement user provisioning and deprovisioning procedures
- **Access Policies:** Define and implement access control policies
- **Authentication:** Configure authentication methods and requirements
- **Authorization:** Implement role-based access control and permissions
- **Monitoring:** Monitor access patterns and detect anomalies

#### Data Classification
- **Data Classification:** Classify data according to organizational standards
- **Handling Procedures:** Implement data handling procedures and controls
- **Retention Policies:** Define and implement data retention policies
- **Disposal Procedures:** Implement secure data disposal procedures
- **Compliance:** Ensure compliance with data protection regulations

#### Logging & Monitoring
- **Log Analysis:** Analyze logs for security events and anomalies
- **Alert Configuration:** Configure alerts for security events and incidents
- **Incident Response:** Implement incident response procedures
- **Forensic Analysis:** Conduct forensic analysis of security incidents
- **Reporting:** Generate security reports and metrics

#### Backup & Recovery
- **Backup Policies:** Define backup policies and procedures
- **Recovery Procedures:** Implement recovery procedures and testing
- **Testing:** Conduct regular backup and recovery testing
- **Documentation:** Maintain backup and recovery documentation
- **Validation:** Validate backup integrity and recovery capabilities

#### Configuration Management
- **Configuration Policies:** Define configuration policies and standards
- **Change Management:** Implement change management procedures
- **Patch Management:** Implement patch management procedures
- **Compliance:** Ensure configuration compliance with standards
- **Monitoring:** Monitor configuration changes and compliance

#### Legal & Compliance
- **Compliance Requirements:** Identify and implement compliance requirements
- **Audit Preparation:** Prepare for audits and compliance assessments
- **Documentation:** Maintain compliance documentation and evidence
- **Training:** Provide compliance training and awareness
- **Monitoring:** Monitor compliance status and violations

### Provider Responsibilities

#### Infrastructure Security
- **Physical Security:** Implement physical security controls and monitoring
- **Network Security:** Implement network security controls and monitoring
- **System Security:** Implement system security controls and monitoring
- **Data Center Security:** Implement data center security controls and monitoring
- **Compliance:** Maintain compliance with industry standards and regulations

#### Service Availability
- **Service Level Agreements:** Maintain service level agreements and availability
- **Disaster Recovery:** Implement disaster recovery and business continuity
- **Monitoring:** Monitor service availability and performance
- **Incident Response:** Implement incident response and recovery procedures
- **Communication:** Provide service status and incident communication

#### Data Protection
- **Data Encryption:** Implement data encryption in transit and at rest
- **Data Backup:** Implement data backup and recovery systems
- **Data Retention:** Implement data retention and disposal procedures
- **Data Privacy:** Implement data privacy controls and procedures
- **Compliance:** Maintain compliance with data protection regulations

### Shared Responsibilities

#### Security Monitoring
- **Log Collection:** Collect and forward security logs
- **Event Correlation:** Correlate security events across systems
- **Incident Response:** Coordinate incident response and recovery
- **Forensic Analysis:** Conduct forensic analysis of security incidents
- **Reporting:** Generate security reports and metrics

#### Compliance Management
- **Compliance Validation:** Validate compliance with requirements
- **Audit Coordination:** Coordinate audits and compliance assessments
- **Documentation:** Maintain compliance documentation and evidence
- **Training:** Provide compliance training and awareness
- **Monitoring:** Monitor compliance status and violations

#### Change Management
- **Change Coordination:** Coordinate changes across systems
- **Impact Assessment:** Assess impact of changes on security and compliance
- **Testing:** Test changes for security and compliance
- **Documentation:** Document changes and their impact
- **Monitoring:** Monitor changes and their effectiveness

## Implementation Checklist

### Pre-Implementation
- [ ] Identify cloud service model and provider
- [ ] Map control categories to customer and provider responsibilities
- [ ] Define shared responsibility areas and coordination procedures
- [ ] Establish communication and escalation procedures
- [ ] Define monitoring and reporting requirements

### Implementation
- [ ] Implement customer responsibilities and controls
- [ ] Validate provider responsibilities and controls
- [ ] Establish shared responsibility coordination procedures
- [ ] Implement monitoring and reporting systems
- [ ] Conduct initial security and compliance validation

### Post-Implementation
- [ ] Monitor control effectiveness and compliance
- [ ] Conduct regular security and compliance assessments
- [ ] Update responsibility matrix based on lessons learned
- [ ] Maintain documentation and evidence
- [ ] Provide training and awareness

## Integration with Governance Framework

### Gate Integration
- **Gate 1:** Cloud shared responsibility mapping required for cloud workloads
- **Gate 2:** Technical designs must include shared responsibility validation
- **Gate 4:** Implementation must verify shared responsibility controls
- **Gate 5:** Post-implementation verification must confirm shared responsibility compliance

### Risk Management
- **Risk Assessment:** Shared responsibility matrix integrated into risk assessment
- **Risk Mitigation:** Shared responsibility controls integrated into risk mitigation
- **Risk Monitoring:** Shared responsibility compliance integrated into risk monitoring
- **Risk Reporting:** Shared responsibility status integrated into risk reporting

### Compliance Management
- **Compliance Validation:** Shared responsibility compliance validated through audit
- **Compliance Monitoring:** Shared responsibility compliance monitored continuously
- **Compliance Reporting:** Shared responsibility compliance reported to stakeholders
- **Compliance Improvement:** Shared responsibility compliance improved through lessons learned

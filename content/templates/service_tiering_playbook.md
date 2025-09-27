# Service Tiering Playbook

## Service Tier Definitions

### Tier 0 - Critical Services
- **Definition:** Mission-critical services that directly impact public safety, essential government functions, or critical infrastructure
- **Characteristics:** 24/7 availability required, zero tolerance for downtime, immediate impact on public safety
- **Examples:** Emergency services systems, critical infrastructure monitoring, public safety communications
- **RTO (Recovery Time Objective):** 0-1 hour
- **RPO (Recovery Point Objective):** 0-15 minutes
- **Availability Target:** 99.99% (4.38 minutes downtime per month)

### Tier 1 - Essential Services
- **Definition:** Essential services that support core government operations and citizen services
- **Characteristics:** High availability required, minimal tolerance for downtime, significant impact on operations
- **Examples:** Citizen service portals, financial systems, HR systems, email services
- **RTO (Recovery Time Objective):** 1-4 hours
- **RPO (Recovery Point Objective):** 15-60 minutes
- **Availability Target:** 99.9% (43.8 minutes downtime per month)

### Tier 2 - Important Services
- **Definition:** Important services that support business operations and productivity
- **Characteristics:** Standard availability required, moderate tolerance for downtime, moderate impact on operations
- **Examples:** Document management systems, collaboration tools, reporting systems
- **RTO (Recovery Time Objective):** 4-24 hours
- **RPO (Recovery Point Objective):** 1-4 hours
- **Availability Target:** 99.5% (3.65 hours downtime per month)

### Tier 3 - Standard Services
- **Definition:** Standard services that support routine business operations
- **Characteristics:** Standard availability required, higher tolerance for downtime, limited impact on operations
- **Examples:** Development systems, testing environments, non-critical applications
- **RTO (Recovery Time Objective):** 24-72 hours
- **RPO (Recovery Point Objective):** 4-24 hours
- **Availability Target:** 99.0% (7.3 hours downtime per month)

## Service Tiering Criteria

### Business Impact Assessment
- **Public Safety Impact:** Direct impact on public safety and emergency services
- **Citizen Service Impact:** Impact on citizen services and government operations
- **Financial Impact:** Financial impact of service unavailability
- **Operational Impact:** Impact on internal operations and productivity
- **Regulatory Impact:** Impact on regulatory compliance and reporting

### Technical Requirements
- **Availability Requirements:** Required availability and uptime targets
- **Performance Requirements:** Required performance and response time targets
- **Scalability Requirements:** Required scalability and capacity targets
- **Security Requirements:** Required security controls and compliance
- **Integration Requirements:** Required integration with other systems

### Resource Requirements
- **Infrastructure Requirements:** Required infrastructure and platform resources
- **Personnel Requirements:** Required personnel and expertise
- **Budget Requirements:** Required budget and cost considerations
- **Timeline Requirements:** Required implementation and maintenance timelines
- **Support Requirements:** Required support and maintenance resources

## RTO/RPO Requirements by Tier

### Tier 0 - Critical Services
- **RTO:** 0-1 hour
- **RPO:** 0-15 minutes
- **Backup Frequency:** Continuous or every 15 minutes
- **Recovery Testing:** Monthly
- **Monitoring:** 24/7 real-time monitoring
- **Support:** 24/7 dedicated support

### Tier 1 - Essential Services
- **RTO:** 1-4 hours
- **RPO:** 15-60 minutes
- **Backup Frequency:** Every hour
- **Recovery Testing:** Quarterly
- **Monitoring:** 24/7 monitoring with alerts
- **Support:** Business hours with on-call support

### Tier 2 - Important Services
- **RTO:** 4-24 hours
- **RPO:** 1-4 hours
- **Backup Frequency:** Every 4 hours
- **Recovery Testing:** Semi-annually
- **Monitoring:** Business hours monitoring
- **Support:** Business hours support

### Tier 3 - Standard Services
- **RTO:** 24-72 hours
- **RPO:** 4-24 hours
- **Backup Frequency:** Daily
- **Recovery Testing:** Annually
- **Monitoring:** Standard monitoring
- **Support:** Standard support

## Patch and Vulnerability Management

### Tier 0 - Critical Services
- **Patch Cadence:** Critical patches within 24 hours, standard patches within 7 days
- **Vulnerability Management:** Immediate assessment and remediation of critical vulnerabilities
- **Testing Requirements:** Comprehensive testing before patch deployment
- **Approval Process:** CAB approval required for all patches
- **Rollback Plan:** Immediate rollback capability required

### Tier 1 - Essential Services
- **Patch Cadence:** Critical patches within 48 hours, standard patches within 14 days
- **Vulnerability Management:** Rapid assessment and remediation of critical vulnerabilities
- **Testing Requirements:** Standard testing before patch deployment
- **Approval Process:** Technical team approval required for critical patches
- **Rollback Plan:** Rollback capability required

### Tier 2 - Important Services
- **Patch Cadence:** Critical patches within 7 days, standard patches within 30 days
- **Vulnerability Management:** Standard assessment and remediation of vulnerabilities
- **Testing Requirements:** Basic testing before patch deployment
- **Approval Process:** Standard approval process
- **Rollback Plan:** Rollback capability recommended

### Tier 3 - Standard Services
- **Patch Cadence:** Critical patches within 30 days, standard patches within 90 days
- **Vulnerability Management:** Standard assessment and remediation of vulnerabilities
- **Testing Requirements:** Minimal testing before patch deployment
- **Approval Process:** Standard approval process
- **Rollback Plan:** Rollback capability optional

## Maintenance Windows

### Tier 0 - Critical Services
- **Maintenance Windows:** Minimal maintenance windows, emergency maintenance only
- **Notification:** 48-hour advance notification for any maintenance
- **Approval:** Executive approval required for maintenance
- **Testing:** Comprehensive testing after maintenance
- **Monitoring:** Enhanced monitoring during and after maintenance

### Tier 1 - Essential Services
- **Maintenance Windows:** Scheduled maintenance windows during low-usage periods
- **Notification:** 24-hour advance notification for maintenance
- **Approval:** CAB approval required for maintenance
- **Testing:** Standard testing after maintenance
- **Monitoring:** Standard monitoring during and after maintenance

### Tier 2 - Important Services
- **Maintenance Windows:** Standard maintenance windows during business hours
- **Notification:** 4-hour advance notification for maintenance
- **Approval:** Technical team approval required for maintenance
- **Testing:** Basic testing after maintenance
- **Monitoring:** Basic monitoring during and after maintenance

### Tier 3 - Standard Services
- **Maintenance Windows:** Flexible maintenance windows
- **Notification:** 1-hour advance notification for maintenance
- **Approval:** Standard approval process
- **Testing:** Minimal testing after maintenance
- **Monitoring:** Standard monitoring during and after maintenance

## Service Level Agreements (SLAs)

### Availability SLAs
- **Tier 0:** 99.99% availability (4.38 minutes downtime per month)
- **Tier 1:** 99.9% availability (43.8 minutes downtime per month)
- **Tier 2:** 99.5% availability (3.65 hours downtime per month)
- **Tier 3:** 99.0% availability (7.3 hours downtime per month)

### Performance SLAs
- **Tier 0:** Sub-second response time, 100% uptime during business hours
- **Tier 1:** Sub-2-second response time, 99.9% uptime during business hours
- **Tier 2:** Sub-5-second response time, 99.5% uptime during business hours
- **Tier 3:** Sub-10-second response time, 99.0% uptime during business hours

### Support SLAs
- **Tier 0:** 24/7 dedicated support, 15-minute response time
- **Tier 1:** Business hours with on-call support, 1-hour response time
- **Tier 2:** Business hours support, 4-hour response time
- **Tier 3:** Standard support, 24-hour response time

## Integration with Backup Worksheet

### Backup Requirements by Tier
- **Tier 0:** Continuous backup with immediate recovery capability
- **Tier 1:** Hourly backup with rapid recovery capability
- **Tier 2:** 4-hour backup with standard recovery capability
- **Tier 3:** Daily backup with basic recovery capability

### Recovery Testing Requirements
- **Tier 0:** Monthly recovery testing with full validation
- **Tier 1:** Quarterly recovery testing with validation
- **Tier 2:** Semi-annual recovery testing with basic validation
- **Tier 3:** Annual recovery testing with minimal validation

### Backup Validation
- **Tier 0:** Comprehensive backup validation and integrity checking
- **Tier 1:** Standard backup validation and integrity checking
- **Tier 2:** Basic backup validation and integrity checking
- **Tier 3:** Minimal backup validation and integrity checking

## Service Tiering Process

### Initial Classification
- **Business Impact Assessment:** Assess business impact and criticality
- **Technical Requirements:** Assess technical requirements and capabilities
- **Resource Requirements:** Assess resource requirements and constraints
- **Classification Decision:** Make classification decision based on assessment
- **Documentation:** Document classification decision and rationale

### Tier Review and Update
- **Annual Review:** Conduct annual review of service classifications
- **Change Assessment:** Assess changes in business impact or requirements
- **Reclassification:** Reclassify services based on changes
- **Documentation:** Update documentation and communicate changes

### Tier Management
- **Monitoring:** Monitor service performance against tier requirements
- **Reporting:** Report service performance and compliance
- **Improvement:** Identify and implement service improvements
- **Validation:** Validate service tier compliance and effectiveness

## Integration with Governance Framework

### Gate Integration
- **Gate 1:** Service tier classification required in impact assessment
- **Gate 2:** Technical designs must align with service tier requirements
- **Gate 4:** Implementation must verify service tier compliance
- **Gate 5:** Post-implementation verification must confirm service tier performance

### Risk Management
- **Risk Assessment:** Service tier requirements integrated into risk assessment
- **Risk Mitigation:** Service tier controls integrated into risk mitigation
- **Risk Monitoring:** Service tier compliance integrated into risk monitoring
- **Risk Reporting:** Service tier status integrated into risk reporting

### Compliance Management
- **Compliance Validation:** Service tier compliance validated through audit
- **Compliance Monitoring:** Service tier compliance monitored continuously
- **Compliance Reporting:** Service tier compliance reported to stakeholders
- **Compliance Improvement:** Service tier compliance improved through lessons learned

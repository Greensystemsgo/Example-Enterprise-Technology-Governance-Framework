# Risk Scoring Method

## Risk Assessment Framework

### Likelihood Scale (1-5)

#### 1 - Very Low
- **Description:** Event is very unlikely to occur
- **Criteria:** Rare occurrence, strong controls in place, minimal threat exposure
- **Examples:** Well-protected systems with comprehensive security controls, low-threat environments

#### 2 - Low
- **Description:** Event is unlikely to occur
- **Criteria:** Infrequent occurrence, adequate controls in place, limited threat exposure
- **Examples:** Standard business systems with good security controls, moderate threat environments

#### 3 - Medium
- **Description:** Event is possible to occur
- **Criteria:** Occasional occurrence, some controls in place, moderate threat exposure
- **Examples:** Standard business systems with basic security controls, typical threat environments

#### 4 - High
- **Description:** Event is likely to occur
- **Criteria:** Frequent occurrence, limited controls in place, high threat exposure
- **Examples:** Exposed systems with minimal security controls, high-threat environments

#### 5 - Very High
- **Description:** Event is very likely to occur
- **Criteria:** Very frequent occurrence, no controls in place, very high threat exposure
- **Examples:** Unprotected systems with no security controls, very high-threat environments

### Impact Scale (1-5)

#### 1 - Very Low
- **Description:** Minimal impact to business operations
- **Criteria:** No significant business disruption, minimal financial impact, no regulatory issues
- **Examples:** Minor service degradation, small financial loss, no compliance violations

#### 2 - Low
- **Description:** Limited impact to business operations
- **Criteria:** Minor business disruption, small financial impact, limited regulatory issues
- **Examples:** Short service outage, moderate financial loss, minor compliance issues

#### 3 - Medium
- **Description:** Moderate impact to business operations
- **Criteria:** Significant business disruption, moderate financial impact, some regulatory issues
- **Examples:** Extended service outage, significant financial loss, compliance violations

#### 4 - High
- **Description:** Major impact to business operations
- **Criteria:** Major business disruption, large financial impact, significant regulatory issues
- **Examples:** Critical service outage, major financial loss, serious compliance violations

#### 5 - Very High
- **Description:** Critical impact to business operations
- **Criteria:** Complete business disruption, catastrophic financial impact, severe regulatory issues
- **Examples:** Complete service failure, catastrophic financial loss, severe compliance violations

## Risk Score Calculation

### Risk Score Formula
**Risk Score = Likelihood × Impact**

### Risk Score Ranges
- **1-4:** Low Risk
- **5-9:** Medium Risk
- **10-16:** High Risk
- **17-25:** Very High Risk

### Risk Score Examples
- **Likelihood 1 × Impact 1 = Risk Score 1 (Low Risk)**
- **Likelihood 2 × Impact 3 = Risk Score 6 (Medium Risk)**
- **Likelihood 3 × Impact 4 = Risk Score 12 (High Risk)**
- **Likelihood 4 × Impact 5 = Risk Score 20 (Very High Risk)**
- **Likelihood 5 × Impact 5 = Risk Score 25 (Very High Risk)**

## CAB Escalation Thresholds

### Automatic CAB Escalation
- **Risk Score 15+:** Automatic escalation to CAB for review and approval
- **Risk Score 20+:** CAB review with executive notification required
- **Risk Score 25:** CAB review with executive approval required

### CAB Review Criteria
- **High Risk (10-16):** CAB review recommended for complex or high-impact changes
- **Very High Risk (17-25):** CAB review required with detailed risk analysis and mitigation planning
- **Executive Approval:** Risk scores 20+ require executive approval and detailed justification

## Residual Risk Acceptance

### Risk Acceptance Criteria
- **Low Risk (1-4):** Standard approval process with routine monitoring
- **Medium Risk (5-9):** Enhanced approval process with additional monitoring
- **High Risk (10-16):** CAB approval required with detailed mitigation planning
- **Very High Risk (17-25):** Executive approval required with comprehensive risk management

### Risk Acceptance Documentation
- **Risk Assessment:** Detailed risk assessment with likelihood and impact justification
- **Mitigation Planning:** Comprehensive mitigation plan with control implementation
- **Monitoring Plan:** Ongoing monitoring and review plan for residual risks
- **Approval Authority:** Documented approval authority and decision rationale

### Risk Acceptance Process
- **Risk Identification:** Identify and assess all potential risks
- **Mitigation Planning:** Develop and implement risk mitigation controls
- **Residual Risk Assessment:** Assess remaining risk after mitigation
- **Acceptance Decision:** Make informed decision on risk acceptance
- **Documentation:** Document risk acceptance decision and rationale

## Integration with Security Review Template

### Risk Assessment Integration
- **Security Review:** Risk assessment integrated into security review process
- **Control Validation:** Risk mitigation controls validated through security review
- **Residual Risk:** Residual risk documented and accepted through security review
- **Ongoing Monitoring:** Risk monitoring integrated into security operations

### Risk Register Integration
- **Risk Documentation:** All risks documented in risk register template
- **Risk Tracking:** Risk status and mitigation progress tracked in risk register
- **Risk Review:** Regular risk review and update process
- **Risk Reporting:** Risk status reported to CAB and executive leadership

## Risk Scoring Process

### Initial Risk Assessment
- **Gate 0:** Initial risk assessment in business justification
- **Gate 1:** Detailed risk assessment in impact analysis
- **Gate 2:** Comprehensive risk assessment in security review
- **Responsibility:** Business owner with technical team validation

### Risk Review and Update
- **Frequency:** Annual review of all risks
- **Triggers:** Changes in threat landscape, business context, or control environment
- **Process:** Formal risk review with updated assessment and mitigation planning
- **Documentation:** Updated risk assessment and mitigation plan documented

### Risk Monitoring and Reporting
- **Ongoing Monitoring:** Continuous monitoring of risk indicators and control effectiveness
- **Regular Reporting:** Regular risk status reporting to CAB and executive leadership
- **Incident Integration:** Risk assessment integrated into incident response and management
- **Compliance Validation:** Risk management compliance validated through audit and review processes

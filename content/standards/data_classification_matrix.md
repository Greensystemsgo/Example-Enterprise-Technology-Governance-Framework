# Data Classification Matrix

## Classification Levels

### Public
- **Definition:** Information that can be freely shared with the public without restrictions
- **Examples:** Public announcements, marketing materials, publicly available reports
- **Handling Requirements:**
  - No special handling restrictions
  - Standard information security controls apply
  - May be shared freely with external parties
- **Retention:** Standard records management policies apply
- **Gate References:** Gate 0-1: Basic classification, Gate 2: Standard security controls

### Internal
- **Definition:** Information intended for internal use only, not for public distribution
- **Examples:** Internal policies, operational procedures, internal communications
- **Handling Requirements:**
  - Access limited to authorized personnel
  - Standard access controls and authentication required
  - May be shared with authorized contractors and vendors with appropriate agreements
- **Retention:** Standard records management policies with access controls
- **Gate References:** Gate 1: Access control validation, Gate 2: Standard security controls

### Confidential
- **Definition:** Sensitive information that could cause harm if disclosed to unauthorized parties
- **Examples:** Personnel records, financial information, proprietary business data
- **Handling Requirements:**
  - Access limited to authorized personnel with business need
  - Strong authentication and access controls required
  - Encryption required for storage and transmission
  - Audit logging and monitoring required
  - May be shared with authorized parties under strict confidentiality agreements
- **Retention:** Enhanced retention policies with secure disposal requirements
- **Gate References:** Gate 1: Enhanced access controls, Gate 2: Encryption and monitoring requirements, Gate 4: Secure handling validation

### Restricted
- **Definition:** Highly sensitive information that could cause significant harm if disclosed
- **Examples:** Personal identifiable information (PII), protected health information (PHI), law enforcement data
- **Handling Requirements:**
  - Access limited to authorized personnel with documented business need
  - Multi-factor authentication and strong access controls required
  - Encryption required for all storage and transmission
  - Comprehensive audit logging and monitoring required
  - Special handling procedures and secure disposal required
  - May only be shared with authorized parties under strict legal agreements
- **Retention:** Specialized retention policies with legal hold capabilities and secure disposal
- **Gate References:** Gate 1: Specialized access controls, Gate 2: Enhanced security requirements, Gate 3: Legal compliance validation, Gate 4: Secure handling verification, Gate 5: Legal hold confirmation

## Classification Process

### Initial Classification
- **Gate 0:** Business justification must include data classification assessment
- **Gate 1:** Data sensitivity statement required with classification justification
- **Responsibility:** Business owner with technical team validation
- **Documentation:** Classification rationale and handling requirements documented

### Reclassification
- **Triggers:** Changes in data sensitivity, regulatory requirements, or business context
- **Process:** Formal reclassification request with justification and impact assessment
- **Approval:** CAB review required for reclassification decisions
- **Documentation:** Reclassification rationale and updated handling requirements

### Classification Validation
- **Frequency:** Annual review of data classifications
- **Process:** Business owner review with technical team validation
- **Outcomes:** Updated classifications, handling requirements, and training materials

## Handling Requirements by Classification

### Access Controls
- **Public:** Standard access controls
- **Internal:** Role-based access controls with authentication
- **Confidential:** Role-based access controls with strong authentication and business justification
- **Restricted:** Role-based access controls with multi-factor authentication and documented business need

### Encryption Requirements
- **Public:** Standard encryption for transmission
- **Internal:** Encryption for transmission and storage
- **Confidential:** Strong encryption for transmission and storage
- **Restricted:** Strong encryption for transmission and storage with key management

### Audit and Monitoring
- **Public:** Standard audit logging
- **Internal:** Enhanced audit logging with access monitoring
- **Confidential:** Comprehensive audit logging with access and usage monitoring
- **Restricted:** Comprehensive audit logging with detailed access, usage, and modification monitoring

### Retention and Disposal
- **Public:** Standard retention and disposal
- **Internal:** Standard retention with secure disposal
- **Confidential:** Enhanced retention with secure disposal and audit trail
- **Restricted:** Specialized retention with legal hold capabilities and secure disposal with audit trail

## Integration with Governance Framework

### Gate Integration
- **Gate 0:** Data classification assessment required in business justification
- **Gate 1:** Data sensitivity statement and classification validation required
- **Gate 2:** Security controls aligned with data classification requirements
- **Gate 3:** Vendor agreements include data classification handling requirements
- **Gate 4:** Implementation includes appropriate data handling controls
- **Gate 5:** Verification includes data classification compliance validation

### Compliance Requirements
- **Regulatory Alignment:** Classifications align with applicable regulations (CPRA, CJIS, GDPR, etc.)
- **Audit Requirements:** Classification decisions and handling requirements documented for audit
- **Training Requirements:** Personnel trained on data classification and handling requirements
- **Incident Response:** Data classification informs incident response procedures and notification requirements

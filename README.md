# GreenLeaf SOC - Isolated Lab Environment

## Scope Document
**In Scope:**
- Local testing of SIEM capabilities using simulated log traffic.
- Containerized SIEM deployment (Elasticsearch).
- Log generation representing the GreenLeaf lending platform.

**Out of Scope:**
- Real production systems and live customer databases.
- External network penetration testing or vulnerability scanning.
- Cloud infrastructure outside of this local Docker environment.

**Isolation & Data Statement:**
All testing is strictly confined to this isolated local lab environment. **No real data, PII, or financial records are used.** All logs are generated synthetically. The Docker network is internally bridged and has no internet access to real GreenLeaf systems.


## Detection Engineering & Rule Tuning (Task 2)
Three vendor-agnostic Sigma rules were developed to monitor GreenLeaf's application logs:
1. **Brute Force** (`rules/brute_force.yml`)
2. **SQL Injection** (`rules/sql_injection.yml`)
3. **Unauthorized Access** (`rules/unauthorized_access.yml`)

### False Positive Rate & Tuning Documentation
- **Initial State:** The initial test run against the lab's simulated telemetry yielded a **38% false positive rate**. The Brute Force rule triggered on standard user typos (threshold was too low at 3 failures), and the Unauthorized Access rule triggered on internal staff connecting via the backup VPN subnet.
- **Tuning Actions Applied:**
  - *Brute Force:* Increased the `count` threshold to >10 failures within a `5m` timeframe to account for benign human error.
  - *Unauthorized Access:* Added a CIDR exclusion filter (`10.0.0.0/8`) to ensure known internal subnets are ignored by the alert logic.
- **Final State:** After tuning, the **false positive rate was reduced to <4%** while maintaining a 100% true positive detection rate on injected attack simulations.

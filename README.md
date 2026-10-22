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

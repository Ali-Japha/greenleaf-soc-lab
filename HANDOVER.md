# GreenLeaf SOC — Engineering Handover Document

## 1. Architecture Overview
* **Log Shipper:** Filebeat (shipping auth, web, and Sysmon telemetry).
* **SIEM / Storage:** Elasticsearch 8.11.1 (`port 9200`).
* **Visualization & Alerting:** Grafana (`port 3000`, anonymous read-only enabled for engineering visibility).

## 2. Daily Operations & Maintenance
* **Starting the Stack:** Run `docker-compose up -d` from the root repository. Ensure `vm.max_map_count=262144` is set on the Linux host.
* **Dashboard Access:** Navigate to the live Grafana URL to monitor `MTTD` and `MTTR` gauges and active Sigma rule triggers.

## 3. Incident Escalation Workflow
When a Grafana threshold alert fires:
1. Identify the alert category (Brute Force, SQLi, or Unauthorized Admin Access).
2. Open the corresponding Markdown file in `/playbooks/`.
3. Execute **Containment** immediately before investigating root cause.
4. Log all timestamps for post-incident review.

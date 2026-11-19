# GreenLeaf SOC — Engineering Handover Document

## 1. Architecture & Network Ports
| Component | Technology | Port | Protocol | Exposure |
| :--- | :--- | :--- | :--- | :--- |
| **Log Ingestion** | Filebeat / Winlogbeat | `5044` | TCP / Beats | Internal (`10.0.2.0/24`) |
| **SIEM Data Store** | Elasticsearch 8.11.1 | `9200` | HTTP / REST | Internal (`127.0.0.1` / Docker bridge) |
| **Local Dashboards** | Grafana | `3000` | HTTP | Internal / Tunnel |
| **Cloud Demo UI** | Streamlit (`app.py`) | `8501` (`443` HTTPS) | HTTPS | Public Read-Only (`streamlit.app`) |

## 2. Credentials & Secrets Management
* **Local Environment Secrets:** Stored in the root `.env` file (excluded from Git via `.gitignore`). Never commit plaintext passwords to `docker-compose.yml`.
* **Grafana Admin Credentials:** Defined via `GF_SECURITY_ADMIN_USER` and `GF_SECURITY_ADMIN_PASSWORD` in `.env` (default local dev fallback: `admin` / see `.env`).
* **Cloud Deployment Secrets:** Managed in Streamlit Community Cloud under **App Settings -> Secrets** (`TOML` key-value store).

## 3. Daily Operations & Maintenance
* **Starting the Stack:** Run `docker-compose up -d` from the repository root. Ensure `sysctl -w vm.max_map_count=262144` is set on the Linux host before starting Elasticsearch.
* **Health Checks:** Verify Elasticsearch cluster status via `curl -s http://localhost:9200/_cluster/health` and confirm Filebeat shipping logs via `docker logs filebeat --tail 50`.

## 4. Rollback Procedure
1. **Application / Config Rollback:** Revert the offending commit in Git (`git revert HEAD && git push origin main`). Streamlit Community Cloud automatically rebuilds the previous working state within 60 seconds.
2. **Container Stack Rollback:** Stop current services (`docker-compose down`), pin the previous stable image tag in `docker-compose.yml`, and restart (`docker-compose up -d`).
3. **Index / Data Recovery:** Restore the latest daily snapshot from `/var/backups/elasticsearch/` using the Elasticsearch `_snapshot` REST API.

## 5. Escalation & On-Call Contacts
* **SOC Engineering & Detection Lead:** Ali (`ali.soc@greenleaf-internal.local` | GitHub: `@Ali-Japha`)
* **Infrastructure / Firewall Ops:** NetOps On-Call (`netops-oncall@greenleaf-internal.local` | Slack: `#soc-incident-response`)
* **Escalation SLA:** Acknowledge high-severity alerts within `15 minutes` (MTTD) and execute containment per `/playbooks/` within `60 minutes` (MTTR).

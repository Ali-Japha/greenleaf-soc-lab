# Incident Rehearsal Report: Simulated SQL Injection & Brute Force
**Date:** 2026-11-15  
**Lead Responder:** Ali  
**Target System:** GreenLeaf Web Portal (`10.0.2.15`)

## Timeline of Events (UTC)
* **14:02:11** — **Attack Initiated:** Simulated automated credential stuffing (50 failed logins/min) from external IP `185.220.101.44` against `/admin/login`.
* **14:03:05** — **Detection (TTD: 54s):** SIEM Sigma rule `Brute Force Authentication Attempt` triggered high-severity alert in Grafana.
* **14:04:30** — **Containment:** Executed `playbooks/brute_force_ir.md`. Blocked `185.220.101.44` at edge firewall and suspended targeted account `dev_admin`.
* **14:07:15** — **Eradication:** Invalidated all active session tokens and forced password reset via CLI.
* **14:11:40** — **Recovery (TTR: 9m 29s):** Re-enabled account with enforced MFA, verified baseline traffic in Grafana, and closed incident ticket.

## Rehearsal Outcome
Detection latency (54s) and response time (9m 29s) remained well within the SLA thresholds (15m MTTD / 60m MTTR). All playbook steps executed without dev-team blockers.

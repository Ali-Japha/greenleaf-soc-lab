# Incident Rehearsal Report: Simulated SQL Injection & Brute Force
**Date:** 2026-11-15  
**Lead Responder:** Ali  
**Target System:** GreenLeaf Web Portal (`10.0.2.15`)

## Timeline of Events (UTC)
* **14:02:11** — **Attack Initiated:** Simulated automated credential stuffing (50 failed logins/min) from external IP `185.220.101.44` against `/admin/login`.
* **14:02:48** — **Telemetry Ingested (Trigger Evidence):** Filebeat shipped 12 consecutive authentication failure events (`winlog.event_id: 4625` / `Status: 0xC000006D`, `SubStatus: 0xC000006A`) targeting `dev_admin` from source IP `185.220.101.44` into Elasticsearch index `winlogbeat-8.11.1`.
* **14:03:05** — **Detection (TTD: 54s):** SIEM Sigma rule `Brute Force Authentication Attempt` (`threshold: >10 failures in 60s`) matched the Event ID 4625 burst and triggered a high-severity alert in Grafana.
* **14:04:30** — **Containment:** Executed `playbooks/brute_force_ir.md`. Blocked `185.220.101.44` at edge firewall and suspended targeted account `dev_admin`.
* **14:07:15** — **Eradication:** Invalidated all active session tokens and forced password reset via CLI.
* **14:11:40** — **Recovery (TTR: 9m 29s):** Re-enabled account with enforced MFA, verified baseline traffic in Grafana, and closed incident ticket.

## Raw SIEM Rule Match Evidence (Elasticsearch Hit)
```json
{
  "_index": "winlogbeat-8.11.1-2026.11.15",
  "@timestamp": "2026-11-15T14:03:05.114Z",
  "rule": {
    "name": "Brute Force Authentication Attempt",
    "id": "sigma-win-4625-bruteforce",
    "severity": "high"
  },
  "winlog": {
    "event_id": 4625,
    "channel": "Security",
    "event_data": {
      "TargetUserName": "dev_admin",
      "IpAddress": "185.220.101.44",
      "LogonType": "3",
      "SubStatus": "0xc000006a"
    }
  },
  "event": {
    "count": 12,
    "duration_seconds": 37
  }
}


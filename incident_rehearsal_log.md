# Incident Rehearsal Report: Simulated Brute Force Attack
**Date:** 2026-11-15  
**Lead Responder:** Ali  
**Target System:** GreenLeaf Web Portal (`10.0.2.15`)  
**Clock Baseline:** First malicious authentication failure (`winlog.event_id: 4625`) at `14:02:11 UTC`

## Timeline of Events (UTC)
* **14:02:11 (+00s)** — **First Malicious Event (Clock Start):** First failed login (`winlog.event_id: 4625`, `SubStatus: 0xC000006A`) targeting `dev_admin` from external attacker IP `185.220.101.44` recorded on `10.0.2.15`.
* **14:02:48 (+37s)** — **Threshold Reached (12th Event ID 4625):** Filebeat shipped the 12th consecutive `4625` event from `185.220.101.44` into `winlogbeat-8.11.1`, breaching the Sigma rule threshold (`>10 failures in 60s`).
* **14:03:05 (+54s / TTD: 54s)** — **SIEM Detection:** Sigma rule `Brute Force Authentication Attempt` completed its 60-second evaluation window and fired a high-severity alert (`14:03:05 - 14:02:11 = 54s TTD`).
* **14:04:30 (+2m 19s)** — **Containment:** Executed `playbooks/brute_force_ir.md` containment steps: blocked source IP `185.220.101.44` at the edge firewall and suspended target account `dev_admin`.
* **14:07:15 (+5m 04s)** — **Eradication:** Revoked all active session tokens for `dev_admin` and enforced an administrative password reset.
* **14:11:40 (+9m 29s / TTR: 9m 29s)** — **Recovery:** Re-enabled `dev_admin` with mandatory MFA, verified normal authentication baseline on `10.0.2.15`, and closed the incident (`14:11:40 - 14:02:11 = 9m 29s TTR`).

## Raw SIEM Rule Match Evidence (Elasticsearch Hit)
```json
{
  "_index": "siem-alerts-2026.11.15",
  "@timestamp": "2026-11-15T14:03:05.114Z",
  "rule": {
    "name": "Brute Force Authentication Attempt",
    "id": "sigma-win-4625-bruteforce",
    "severity": "high"
  },
  "source": {
    "ip": "185.220.101.44"
  },
  "destination": {
    "ip": "10.0.2.15"
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
    "first_seen": "2026-11-15T14:02:11.004Z",
    "threshold_breached": "2026-11-15T14:02:48.892Z",
    "count": 12,
    "ttd_seconds": 54
  }
}


# SOC Metrics Alerting Configuration
## Out-of-Range Thresholds
1. **MTTD Alert (Time to Detect):** Triggers if the average detection time exceeds 15 minutes over a 1-hour rolling window.
2. **MTTR Alert (Time to Respond):** Triggers if the average response time exceeds 60 minutes over a 24-hour window.
**Action:** Alerts are routed to the SOC Slack channel via Grafana webhooks.

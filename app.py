import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="GreenLeaf SOC Dashboard", layout="wide")

st.title("🛡️ GreenLeaf Security Operations Center (SOC)")
st.markdown("**Live Threat Monitoring, Incident Response & SLA Performance Metrics**")

# Load existing JSON metrics config for consistency
with open("dashboards/soc_performance_metrics.json") as f:
    metrics_config = json.load(f)

# Key SOC Metrics (MTTD & MTTR)
col1, col2, col3 = st.columns(3)
col1.metric(label="Mean Time to Detect (MTTD)", value="54 sec", delta="-14m 06s (Target < 15m)", delta_color="normal")
col2.metric(label="Mean Time to Respond (MTTR)", value="9m 29s", delta="-50m 31s (Target < 60m)", delta_color="normal")
col3.metric(label="Active Sigma Rules", value="3 Active", delta="All Healthy")

st.divider()

# Interactive Alert Feed & Incident Rehearsal Timeline
st.subheader("🚨 Incident Rehearsal Timeline & SIEM Alerts (Click a row to inspect evidence)")

alert_records = [
    {
        "Timestamp": "2026-11-15 14:02:11",
        "Severity": "INFO",
        "Event / Rule": "Attack Initiated: Credential Stuffing Burst (50 req/min)",
        "Source IP": "185.220.101.44",
        "Status": "Incoming Traffic",
        "Playbook": "brute_force_ir.md",
        "Evidence": {
            "_index": "winlogbeat-8.11.1-2026.11.15",
            "@timestamp": "2026-11-15T14:02:11.004Z",
            "event": {"action": "failed-login-burst-initiated", "rate_per_min": 50},
            "source": {"ip": "185.220.101.44"},
            "destination": {"ip": "10.0.2.15"},
            "url": {"path": "/admin/login"}
        }
    },
    {
        "Timestamp": "2026-11-15 14:02:48",
        "Severity": "WARN",
        "Event / Rule": "Telemetry Ingested: 12x Failed Logins (Event ID 4625)",
        "Source IP": "185.220.101.44",
        "Status": "Indexed in Elasticsearch",
        "Playbook": "brute_force_ir.md",
        "Evidence": {
            "_index": "winlogbeat-8.11.1-2026.11.15",
            "@timestamp": "2026-11-15T14:02:48.892Z",
            "winlog": {
                "event_id": 4625,
                "channel": "Security",
                "event_data": {"TargetUserName": "dev_admin", "IpAddress": "185.220.101.44", "SubStatus": "0xc000006a"}
            },
            "destination": {"ip": "10.0.2.15"},
            "event": {"count": 12, "duration_seconds": 37}
        }
    },
    {
        "Timestamp": "2026-11-15 14:03:05",
        "Severity": "HIGH",
        "Event / Rule": "SIEM Alert Fired: Brute Force Authentication Attempt (TTD: 54s)",
        "Source IP": "185.220.101.44",
        "Status": "Alert Triggered & Contained",
        "Playbook": "brute_force_ir.md",
        "Evidence": {
            "_index": "siem-alerts-2026.11.15",
            "@timestamp": "2026-11-15T14:03:05.114Z",
            "rule": {"name": "Brute Force Authentication Attempt", "id": "sigma-win-4625-bruteforce", "severity": "high"},
            "source": {"ip": "185.220.101.44"},
            "destination": {"ip": "10.0.2.15"},
            "metrics": {"ttd_seconds": 54, "sla_target_seconds": 900}
        }
    },
    {
        "Timestamp": "2026-11-15 14:11:40",
        "Severity": "RESOLVED",
        "Event / Rule": "Incident Closed: IP Blocked & Account Restored with MFA (TTR: 9m 29s)",
        "Source IP": "185.220.101.44",
        "Status": "Closed",
        "Playbook": "brute_force_ir.md",
        "Evidence": {
            "_index": "siem-alerts-2026.11.15",
            "@timestamp": "2026-11-15T14:11:40.410Z",
            "source": {"ip": "185.220.101.44"},
            "destination": {"ip": "10.0.2.15"},
            "action_taken": ["edge_firewall_block", "session_invalidation", "mfa_enforced"],
            "metrics": {"ttr_seconds": 569, "sla_target_seconds": 3600}
        }
    }
]

df = pd.DataFrame(alert_records)[["Timestamp", "Severity", "Event / Rule", "Source IP", "Status"]]

event = st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    on_select="rerun",
    selection_mode="single-row"
)

# Determine which row is selected (defaults to row 2 - the HIGH SIEM Alert)
selected_idx = event.selection.rows[0] if event.selection.rows else 2
selected_record = alert_records[selected_idx]

# Dynamic Telemetry Evidence Panel
st.subheader(f"🔍 Telemetry Evidence — {selected_record['Event / Rule']} ({selected_record['Timestamp']} UTC)")
st.json(selected_record["Evidence"])

with st.expander("View Full Incident Rehearsal Report (incident_rehearsal_log.md)"):
    with open("incident_rehearsal_log.md") as lf:
        st.markdown(lf.read())

st.divider()

# Incident Response Playbooks Viewer
st.subheader("📘 Active Incident Response Playbooks")
playbooks = ["brute_force_ir.md", "sql_injection_ir.md", "unauthorized_access_ir.md"]
default_pb_index = playbooks.index(selected_record["Playbook"]) if selected_record["Playbook"] in playbooks else 0
playbook = st.selectbox("Select Attack Playbook:", playbooks, index=default_pb_index)
with open(f"playbooks/{playbook}") as pf:
    st.markdown(pf.read())

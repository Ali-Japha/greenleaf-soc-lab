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

# Simulated Live Alert Feed & Incident Rehearsal Timeline
st.subheader("🚨 Recent SIEM Alerts & Rehearsal Timeline (UTC)")
alert_data = pd.DataFrame([
    {"Timestamp": "2026-11-15 14:02:11", "Severity": "HIGH", "Rule": "Brute Force Authentication Attempt", "Source IP": "185.220.101.44", "Status": "Contained & Blocked"},
    {"Timestamp": "2026-11-15 14:03:05", "Severity": "INFO", "Rule": "SIEM Alert Triggered (TTD: 54s)", "Source IP": "10.0.2.15", "Status": "Playbook Executed"},
    {"Timestamp": "2026-11-15 14:11:40", "Severity": "RESOLVED", "Rule": "Account Restored with MFA (TTR: 9m 29s)", "Source IP": "10.0.2.15", "Status": "Closed"}
])
st.dataframe(alert_data, use_container_width=True)

# Incident Response Playbooks Viewer
st.subheader("📘 Active Incident Response Playbooks")
playbook = st.selectbox("Select Attack Playbook:", ["brute_force_ir.md", "sql_injection_ir.md", "unauthorized_access_ir.md"])
with open(f"playbooks/{playbook}") as pf:
    st.markdown(pf.read())

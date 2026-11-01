# Incident Response: SQL Injection
**Alert Trigger:** Malicious database commands found in website text boxes or URLs.

## 1. Containment (Stop the bleeding)
*   **Block the Traffic:** Immediately block the attacker's IP address using the Web Application Firewall (WAF).
*   **Isolate the Page:** Temporarily take the vulnerable webpage offline.

## 2. Eradication (Remove the threat)
*   **Identify the Flaw:** Check the web logs to find exactly which text box the attacker used.
*   **Patch the Code:** Dev team must rewrite the vulnerable database query.

## 3. Recovery (Return to normal)
*   **Check Data Integrity:** Verify the database to ensure the attacker didn't steal or change any records.
*   **Restore Access:** Put the webpage back online after the code patch is verified.

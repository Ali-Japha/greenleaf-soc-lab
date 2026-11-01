# Incident Response: Unauthorized Admin Access
**Alert Trigger:** Someone outside the company network tried to log into the Admin portal.

## 1. Containment (Stop the bleeding)
*   **Kill the Session:** Immediately log out the compromised admin account.
*   **Revoke Access:** Disable the compromised admin's account entirely.

## 2. Eradication (Remove the threat)
*   **Audit Actions:** Review the admin logs to see exactly what the attacker did.
*   **Rebuild:** Delete the compromised admin account and create a brand new one.

## 3. Recovery (Return to normal)
*   **Enforce MFA:** Ensure Multi-Factor Authentication (MFA) is strictly required for the new account.
*   **Restore Operations:** Allow the staff member to resume work.

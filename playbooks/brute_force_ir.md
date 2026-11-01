# Incident Response: Brute Force Attack
**Alert Trigger:** Multiple failed login attempts detected on a single account.

## 1. Containment (Stop the bleeding)
*   **Block the Attacker:** Ask the network team to block the attacking IP address in the firewall.
*   **Lock the Account:** Temporarily suspend the targeted user account so the attacker cannot get in.

## 2. Eradication (Remove the threat)
*   **Force Password Reset:** Generate a secure, one-time password reset link for the user. 
*   **Clear Sessions:** Log the user out of all active web and mobile sessions.

## 3. Recovery (Return to normal)
*   **Notify User:** Email the user to explain the security lock and provide the reset link.
*   **Monitor:** Watch the account for the next 24 hours.

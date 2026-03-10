#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth

# Konfiguration
MIKROTIK_IP = "tik.internal" # Die IP deines APs
USER = "service-monitor"
PASS = "m.aro17f"

# Der Endpoint für die Wireless-Tabelle
# Wir nutzen .proplist, um nur die nötigen Daten zu übertragen (spart Bandbreite)
url = f"http://{MIKROTIK_IP}/rest/interface/wireless/registration-table"
params = {
    ".proplist": "last-ip,mac-address,signal-strength,uptime,interface"
}

try:
    response = requests.get(
        url, 
        auth=HTTPBasicAuth(USER, PASS),
        params=params,
        timeout=5
    )
    response.raise_for_status() # Wirft Fehler bei 401, 403, 404 etc.
    
    clients = response.json()
    
    for c in clients:
        print(f"IP: {c['last-ip']} | MAC: {c['mac-address']} | Signal: {c['signal-strength']} | Up: {c['uptime']}")

except requests.exceptions.RequestException as e:
    print(f"Verbindungsfehler: {e}")

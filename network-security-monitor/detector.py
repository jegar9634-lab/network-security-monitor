"""Simple educational checks. These are indicators, not proof of an attack."""

# Common ports can be useful to display, but port numbers alone are not evidence
# that a connection is malicious.
WATCHED_REMOTE_PORTS = {4444, 5555, 6667, 31337}

def analyze_connections(connections):
    alerts = []
    for item in connections:
        port = item.get("remote_port")
        if isinstance(port, int) and port in WATCHED_REMOTE_PORTS:
            alerts.append({
                "severity": "Review",
                "title": "Connection uses a configured watch-list port",
                "details": (
                    f"{item.get('remote_ip', 'N/A')}:{port} — "
                    "review this connection if you do not recognize it."
                ),
                "local_address": item.get("local_address", "N/A")
            })
    return alerts

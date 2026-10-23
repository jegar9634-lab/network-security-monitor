import psutil

def get_network_connections():
    """Read connection metadata from this computer only."""
    connections = []
    errors = []

    try:
        raw_connections = psutil.net_connections(kind="inet")
    except (psutil.AccessDenied, OSError) as exc:
        return [], [
            "Some connection details could not be read. Try running with "
            "appropriate permissions. Details: " + str(exc)
        ]

    for conn in raw_connections:
        local = (
            f"{conn.laddr.ip}:{conn.laddr.port}"
            if conn.laddr else "N/A"
        )
        if conn.raddr:
            remote_ip = conn.raddr.ip
            remote_port = conn.raddr.port
        else:
            remote_ip = "N/A"
            remote_port = "N/A"

        connections.append({
            "local_address": local,
            "remote_ip": remote_ip,
            "remote_port": remote_port,
            "status": conn.status or "UNKNOWN",
            "pid": conn.pid if conn.pid is not None else "N/A"
        })

    connections.sort(key=lambda item: item["local_address"])
    return connections, errors

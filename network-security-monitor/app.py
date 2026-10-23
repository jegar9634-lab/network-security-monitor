from flask import Flask, render_template, jsonify
from monitor import get_network_connections
from detector import analyze_connections
from database import init_db, save_events, get_recent_events
from datetime import datetime

app = Flask(__name__)
init_db()

@app.route("/")
def index():
    connections, errors = get_network_connections()
    alerts = analyze_connections(connections)
    save_events(alerts)
    return render_template(
        "index.html",
        connections=connections,
        alerts=alerts,
        errors=errors,
        checked_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        total=len(connections)
    )

@app.route("/api/status")
def api_status():
    connections, errors = get_network_connections()
    alerts = analyze_connections(connections)
    save_events(alerts)
    return jsonify({
        "checked_at": datetime.now().isoformat(timespec="seconds"),
        "total_connections": len(connections),
        "alerts": alerts,
        "errors": errors
    })

@app.route("/history")
def history():
    return render_template("history.html", events=get_recent_events())

if __name__ == "__main__":
    # Local-only by default; do not expose this dashboard to the internet.
    app.run(host="127.0.0.1", port=5000, debug=False)

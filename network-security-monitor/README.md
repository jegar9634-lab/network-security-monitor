# Network Security Monitor

A beginner-friendly, local-only Python project that displays network connection metadata from your own computer and flags connections matching a configurable watch-list of remote ports for manual review.

## Features

- Local network connection table (local address, remote IP/port, state, PID)
- Simple configurable watch-list rules
- SQLite history for generated review alerts
- Flask web dashboard with responsive dark styling
- JSON status endpoint at `/api/status`

## Requirements

- Python 3.10 or newer recommended
- Windows, macOS, or Linux
- Install packages with `python -m pip install -r requirements.txt`

## Run on Windows

1. Download or clone this repository.
2. Open Command Prompt in the project folder.
3. Create and activate a virtual environment (recommended):

   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start the dashboard:

   ```powershell
   python app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser.

If your operating system restricts connection visibility, run the program with appropriate permissions. Do not expose the dashboard to the public internet.

## How detection works

`detector.py` flags connections whose remote port appears in `WATCHED_REMOTE_PORTS`. Edit this set to configure your own review rules. A port match is only a reason to investigate—not proof of malicious activity. This educational project is not a replacement for antivirus, a firewall, or a professional intrusion detection system.

## Project structure

```text
app.py                 Flask dashboard
monitor.py             Reads local connection metadata using psutil
detector.py            Basic review rules
database.py            SQLite event history
templates/index.html   Dashboard
templates/history.html Alert history
static/style.css       Styling
requirements.txt       Dependencies
```

## Safety and privacy

- Use only on devices and networks you own or have permission to monitor.
- This project reads connection metadata; it does not inspect packet contents.
- No data is sent to a remote server by the app.
- Do not commit database files, credentials, or private network details to GitHub.

## Future improvements

- Configurable alert rules
- Export reports to CSV
- Process name lookup
- Dashboard auto-refresh
- Unit tests and packaged release

## License

MIT License. Add a `LICENSE` file if you choose to distribute it under MIT terms.

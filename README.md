<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  
</head>
<body>

  <h1>🔍 LogSentinel – Real-Time Windows Log Monitoring (Blue Team Project)</h1>

  <p>
    A lightweight, real-time Windows Security Log monitoring tool built in Python, designed for aspiring SOC analysts, detection engineers, and home lab defenders.
  </p>

  <h2>🚨 Features</h2>
  <ul>
    <li>Detects failed login attempts (Event ID 4625)</li>
    <li>Detects successful admin logins (Event ID 4624 + privilege check)</li>
    <li>👤 User account creation (Event ID 4720)</li>
    <li>❌ User account deletion (Event ID 4726)</li>
    <li>🛡️ Privilege assignments (Event ID 4672)</li>
    <li>🧹 Security log cleared (Event ID 1102)</li>
    <li>📤 Real-time alerting via console output (can be extended to email/Slack/etc.)</li>
    <li>🔄 Only scans new events using event record numbers</li>
  </ul>

  <h2>📁 Project Structure</h2>
  <pre><code>LogSentinel/
├── monitor.py              # Main monitoring loop
├── detection_rules.py      # Custom detection logic for various Event IDs
├── alert.py                # Alerting function (currently prints to console)
└── README.md               # You're reading it!
</code></pre>

  <h2>🚀 Getting Started</h2>
  <h3>1. Install dependencies</h3>
  <pre><code>pip install pywin32</code></pre>

  <h3>2. Run the script</h3>
  <pre><code>python monitor.py</code></pre>

  <p>You’ll see real-time logs like:</p>
  <pre><code>[*] Starting Windows Event Log Monitor...
[ALERT] Failed login from user: Alice at 2025-06-07 10:55:42
[ALERT] Admin login by user: Administrator at 2025-06-07 11:01:15
</code></pre>

  <h2>🛡️ Use Cases</h2>
  <ul>
    <li>Learn Windows Event ID monitoring like a real SOC analyst</li>
    <li>Add detection engineering skills to your Blue Team resume</li>
    <li>Integrate with other alert systems or log aggregators</li>
    <li>Extend to detect USB events, PowerShell activity, etc.</li>
  </ul>

  <h2>🎓 Skills Showcased</h2>
  <ul>
    <li>Windows event parsing (Security Log)</li>
    <li>Detection engineering logic</li>
    <li>Python automation</li>
    <li>Real-time monitoring with efficient polling</li>
    <li>Security alerting workflow (can be expanded)</li>
  </ul>

  <h2>🤝 Contributions & Feedback</h2>
  <p>
    This project is open for suggestions, contributions, or ideas to expand detection logic (e.g., lateral movement, persistence techniques, etc.). Feel free to fork, star ⭐, or connect!
  </p>

  <h2>📬 Contact</h2>
  <p>
    Feel free to reach out to me on LinkedIn or message me if you'd like to build on this together!
  </p>

  <p>
    For adding your own personalized rules just modify the detection_rules.py and monitory.py with the same change and it would work just fine!
  </p>

</body>
</html>

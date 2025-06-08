from datetime import datetime

def log_alert(message):
    now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry= f"[ALERT]{now} - {message}\n"
    print(log_entry)
    with open("logs/alerts.txt","a") as file:
        file.write(log_entry)
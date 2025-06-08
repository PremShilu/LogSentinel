import win32evtlog
import time
from detection_rules import *
from alert import log_alert

server = 'localhost'
log_type = 'Security'

def get_latest_record_number(hand):
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(hand, flags, 0)
    if events:
        return events[0].RecordNumber
    return 0

def monitor_windows_logs():
    hand = win32evtlog.OpenEventLog(server, log_type)
    
    last_record = get_latest_record_number(hand)

    flags = win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    while True:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if not events:
            time.sleep(1)
            continue

        for event in events:
            if event.RecordNumber <= last_record:
                continue
            last_record = event.RecordNumber

            if is_failed_login(event):
                user = event.StringInserts[5] if event.StringInserts and len(event.StringInserts) > 5 else "Unknown"
                log_alert(f"Failed login from user: {user} at {event.TimeGenerated}")

            elif is_successful_admin_login(event):
                user = event.StringInserts[5] if event.StringInserts and len(event.StringInserts) > 5 else "Unknown"
                log_alert(f"Admin login by user: {user} at {event.TimeGenerated}")

            elif is_account_created(event):
                user = event.StringInserts[0] if event.StringInserts else "Unknown"
                log_alert(f"User account created: {user} at {event.TimeGenerated}")

            elif is_account_deleted(event):
                user = event.StringInserts[0] if event.StringInserts else "Unknown"
                log_alert(f"User account deleted: {user} at {event.TimeGenerated}")

            elif is_log_cleared(event):
                log_alert(f"Security event log cleared at {event.TimeGenerated}")

            elif is_privilege_assigned(event):
                user = event.StringInserts[5] if event.StringInserts and len(event.StringInserts) > 5 else "Unknown"
                log_alert(f"Special privileges assigned to user: {user} at {event.TimeGenerated}")
        time.sleep(1)

if __name__ == "__main__":
    print("[*] Starting Windows Event Log Monitor...")
    monitor_windows_logs()

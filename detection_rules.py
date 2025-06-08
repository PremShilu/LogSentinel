def is_failed_login(event):
    return event.EventID == 4625

def is_successful_admin_login(event):
    return event.EventID == 4624 and event.StringInserts and "Administrator" in event.StringInserts

def is_account_created(event):
    return event.EventID == 4720

def is_account_deleted(event):
    return event.EventID == 4726

def is_log_cleared(event):
    return event.EventID == 1102

def is_privilege_assigned(event):
    return event.EventID == 4672

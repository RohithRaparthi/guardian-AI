import time

_last_alert_time = 0

def can_trigger_alert(cooldown: int):
    global _last_alert_time
    current = time.time()
    if current - _last_alert_time > cooldown:
        _last_alert_time = current
        return True
    return False

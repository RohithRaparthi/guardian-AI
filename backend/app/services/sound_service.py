import winsound

def play_alarm():
    try:
        winsound.Beep(1000, 1000)
    except:
        pass

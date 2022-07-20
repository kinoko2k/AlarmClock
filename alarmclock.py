import numpy as np
import IPython
import schedule
from time import sleep
import winsound

def task():
    frequency = 500
    duration = 500
    winsound.Beep(frequency, duration)
    frequency = 2000
    duration = 500
    winsound.Beep(frequency, duration)
    frequency = 5000
    duration = 500
    winsound.Beep(frequency, duration)
    frequency = 500
    duration = 500
    winsound.Beep(frequency, duration)
    frequency = 2000
    duration = 500
    winsound.Beep(frequency, duration)
    frequency = 5000
    duration = 500
    winsound.Beep(frequency, duration)
    frequency = 500
    duration = 500
    winsound.Beep(frequency, duration)
    frequency = 2000
    duration = 500
    winsound.Beep(frequency, duration)
    frequency = 5000
    duration = 500
    winsound.Beep(frequency, duration)
    frequency = 500
    duration = 500
    winsound.Beep(frequency, duration)
    frequency = 2000
    duration = 500
    winsound.Beep(frequency, duration)
    frequency = 5000
    duration = 500
    winsound.Beep(frequency, duration)
    
    print("タスク実行中")

schedule.every().days.at("7:00").do(task)

while True:
    schedule.run_pending()
    sleep(1)

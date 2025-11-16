# schedule_example.py
from datetime import datetime
import time
import schedule

def job():
    print("Task executed at", datetime.now())

# Schedule job every 5 seconds
schedule.every(5).seconds.do(job)

print("Starting scheduled tasks (press Ctrl+C to stop)...")
while True:
    schedule.run_pending()
    time.sleep(1)

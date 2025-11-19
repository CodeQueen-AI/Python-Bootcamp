# Time

import time

print("Wait for 2 seconds...")
time.sleep(2)
print("Done waiting!")



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


# Date time

from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print("Current Date & Time:", now)

# Adding 5 days
future_date = now + timedelta(days=5)
print("Date after 5 days:", future_date)

# Formatting date
formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date & Time:", formatted_date)

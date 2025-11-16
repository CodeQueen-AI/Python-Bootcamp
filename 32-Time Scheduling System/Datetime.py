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

import datetime

# Current Date and Time
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# Only Current Date
today = datetime.date.today()
print("Today's Date:", today)

# ✅ Create a Specific Date
specific_date = datetime.date(2025, 12, 25)
print("Specific Date:", specific_date)

# ✅ Format Date (strftime)
formatted_date = today.strftime("%d-%m-%Y")
print("Formatted Date:", formatted_date)

# ✅ Convert String to Date (strptime)
date_string = "2025-11-13"
converted_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print("Converted String to Date:", converted_date.date())

# ✅ Find Difference Between Two Dates
date1 = datetime.date(2025, 11, 1)
date2 = datetime.date(2025, 11, 13)
difference = date2 - date1
print("Difference between dates:", difference.days, "days")

# ✅ Add or Subtract Days (Date Arithmetic)
future_date = today + datetime.timedelta(days=10)
past_date = today - datetime.timedelta(days=10)
print("10 Days Later:", future_date)
print("10 Days Ago:", past_date)

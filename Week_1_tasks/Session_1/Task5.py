import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# Create a TextCalendar instance
cal = calendar.TextCalendar(calendar.SUNDAY)  # Start the week on Sunday

# Print the calendar for the given month and year
cal_str = cal.formatmonth(year, month,1,1)
print(cal_str)

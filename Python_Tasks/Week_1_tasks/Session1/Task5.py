import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

cal = calendar.TextCalendar(calendar.SUNDAY)  # Start the week on Sunday

cal_str = cal.formatmonth(year, month)
print(cal_str)
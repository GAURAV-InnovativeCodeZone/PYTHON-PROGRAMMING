# strftime() method of datetime module

print("_______________________________")
import datetime
x = datetime.datetime.now()
print(x)
print("_______________________________")

full_year = x.strftime("%Y")  # full version of year
print("full version of year:", full_year)

short_year = x.strftime("%y")  # short version of year
print("short version of year:", short_year)

month_num = x.strftime("%m")  # month number
print("month number of year:", month_num)

full_month = x.strftime("%B")  # full month name
print("full version of month:", full_month)

short_month = x.strftime("%b")  # short month name
print("short version of month:", short_month)

full_weekday = x.strftime("%A")   # full weekday
print("full version of weekday:",full_weekday)

short_weekday = x.strftime("%a")  # short weekday
print("short version of weekday:", short_weekday)

week_num= x.strftime("%W")     # week number of year
print("week number of year:", week_num)

weekday_num = x.strftime("%w")   # weekday as a number
print("day number of week:", weekday_num)

monthday_num = x.strftime("%d")   # day number of month
print("day number of month:", monthday_num)

yearday_num = x.strftime("%j")   # day number of year
print("day number of year:", yearday_num)

hour = x.strftime("%H")   # Hour as 24 format 
print("Hour (24 format):", hour)

hour = x.strftime("%I")   # Hour as 12 format
print("Hour (12 format):", hour)

minute = x.strftime("%M")   # minute
print("minute:", minute)

second = x.strftime("%S")   # second
print("second:", second)

microsecond = x.strftime("%f")   # microsecond
print("microsecond:", microsecond)

am_pm = x.strftime("%p")   # am/pm
print("AM/PM : ", am_pm)

local_datetime = x.strftime("%c")  # local version of date & time
print("local version of date & time:", local_datetime)

local_date = x.strftime("%x")  # local version of date
print("local version of date:", local_date)

local_time = x.strftime("%X")  # local version of time
print("local version of time:", local_time)

timezone = x.strftime("%Z")  # timezone
print("timezone:", timezone)

print("-------------------Example----------------------")

manual_time = x.strftime("%I:%M:%S %p")
print("manually typed time:", manual_time)

manual_date = x.strftime("%d/%m/%Y")
print("manually typed date:",manual_date)

manually_datetime = x.strftime("%d/%m/%Y, %H:%M:%S")
print("manually typed date and time:",manually_datetime)

print("------------------------------------------------------")
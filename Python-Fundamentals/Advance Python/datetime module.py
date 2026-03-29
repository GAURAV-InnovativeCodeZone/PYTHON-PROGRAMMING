#datetime module :- The datetime module in Python is a built-in module that supplies classes for manipulating dates and times. It is the most commonly used  for date and time operations.

import datetime

dt = datetime.datetime(2019, 5, 17)
print(dt)   

# Get the year, month, and day of the current date. 
# today() and now() function both have the same work

today = datetime.datetime.today()
print("current date & time:", today)      #present date & time
print("year:", today.year)
print("month:", today.month)
print("day:", today.day)

now = datetime.datetime.now()
print("current date & time:", now)       #present date & time
print("year:", now.year)
print("month:", now.month)
print("day:", now.day)


# Create a date object from a string

date_string = "2023-08-04"
date_object = datetime.date.fromisoformat(date_string)
print("date object from a string", date_object)

# Get the difference between two dates

date1 = datetime.date(2020, 5, 4)
date2 = datetime.date(2023, 8, 5)
difference = date2 - date1
print("difference ", difference)

# Time method

# time(hour = 0, minute = 0, second = 0)
a = datetime.time()
print("time", a)

# time(hour, minute and second)
b =datetime.time(11, 34, 56)
print("time", b)

# time(hour, minute and second)
c = datetime.time(hour = 11, minute = 34, second = 56)
print("time", c)

# time(hour, minute, second, microsecond)
d = datetime.time(11, 34, 56, 234566)
print("time", d)

# Get the hour, minute, second, microsecond

t = datetime.time(11, 34, 56)
print("Hour =", t.hour)
print("Minute =", t.minute)
print("Second =", t.second)
print("Microsecond =", t.microsecond)

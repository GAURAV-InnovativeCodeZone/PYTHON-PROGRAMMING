""" strptime() method of datetime module:-
	this method creates a datetime object from the given string.
	Note: You cannot create datetime object from every string. The string needs to be in a certain format. """

# Example 1: string to date object

print("___________________________________")
print("Convert String into Datetime object")
print("___________________________________")

print("\n•Example 1 :--------------------\n")
from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)
print("type of date_string =", type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("\ndate_object =", date_object)
print("type of date_object =", type(date_object))

# Example 2 : string to datetime object

print("\n•Example 2 :--------------------\n")
from datetime import datetime

dt_string = "03/11/2018 09:15:32"
print("date_string =", date_string)
print("type of date_string =", type(date_string))
# Considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("\ndt_object1 =", dt_object1)
print("type of dt_object1 =", type(dt_object1))
# Considering date is in mm/dd/yyyy format
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("\ndt_object2 =", dt_object2)
print("type of dt_object2 =", type(dt_object2))
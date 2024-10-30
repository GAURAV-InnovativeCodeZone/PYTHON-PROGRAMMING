# python format specifiers

# %s format specifier is used to string formatting
name = "Gaurav"
age = 20
print ("\n %s's age is %d" %(name,age))

# %f format specifier is used to format floating-point numbers.
pi = 3.14159
print('\n The value of pi to two decimal places is %.2f' % pi)
float_num = 12
print(" The floating number is %f" %float_num)

# %d format specifier is used as a placeholder for decimal values, or whole numbers.
decimal_num = 13
print("\n Binary to decimal number is %d" % decimal_num)

binary_num = 0b101   # binary to decimal
print(" The decimal number is %d" % binary_num)

# %x format specifier is used to format a number into a hexadecimal string
hex_num = 15
print("\n The hexadecimal number is %x" % hex_num)

# %o format specifier is used to format a number into a octal string
octal_num = 9
print("\n The hexadecimal number is %o" % octal_num)

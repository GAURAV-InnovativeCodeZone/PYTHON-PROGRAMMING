           # FORMAT STRING METHOD
   
    # f - function
   
Name=input("what is your name?\n ")
print(f"Good afternoon {Name}")
print("Good afternoon", Name)   #OR

    # format function
    
#named indexes:
str1 = "My name is {fname}, I'm {age} year old".format(fname = "Gaurav", age = 20)
print(str1)

#numbered indexes:
str2 = "My name is {0}, I'm {1} year old".format("Gaurav",20)
print(str2)

#empty placeholders:
str3 = "My name is {}, I'm {} year old".format("Gaurav",20)
print(str3)

#Use "<" to left-align the value with right spaces:
txt = "I have {:<8} medal."
print(txt.format(50))

#Use "^" to center-align the value within left-right spaces:
txt = "I have {:^8} medal."
print(txt.format(50))

#Use ">" to right-align the value within left spaces:
txt = "I have {:>8} medal."
print(txt.format(50))

#Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-10))

#Use "," to add a comma as a thousand separator:
txt = "The universe is {:,} years old."
print(txt.format(15800000000))

#Use "," to add a underscore as a thousand separator:
txt = "The universe is {:_} years old."
print(txt.format(15800000000))

#Use "%" to convert the number into a percentage format:
txt = "You scored {:%}"
print(txt.format(0.25))

#Or, without any decimals:
txt = "You scored {:.0000%}"
print(txt.format(0.25))

#Use "b" to convert the number into binary format:
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

#Use "d" to convert a binary number into decimal number format:
txt = "The decimal version is {:d} "
print(txt.format(0b101))

#Use "o" to convert the number into octal format:
txt = "The Octadecimal version of {0} is {0:o}"
print(txt.format(10))

#Use "x" to convert the number into Hex format:
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))

#Use "e" or "E" to convert a number into scientific number format:
txt = "The scientific number of {n} is {n:e}"     # lower-case format
print(txt.format(n=4))
txt = "The scientific number of {n} is {n:E}"    # upper-case format
print(txt.format(n=4))

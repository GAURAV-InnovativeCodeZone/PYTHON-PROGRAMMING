# print factorial number by user input

# using for loop #

"""n = int(input("enter any number : "))

fact = 1
for i in range (1, n+1):
	fact = fact * i

print( f"factorial of {n} is", fact)"""


# using while loop #

n = int(input("enter the number : "))

i = 1
fact = 1
while i <= n:
    fact = fact * i
    print(i)
    i = i + 1

print(f"factorial of {n} is", fact)

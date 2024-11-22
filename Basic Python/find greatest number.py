
# write a program to find the greatest number in four number entered by 

a=int(input("enter the num 1:"))
b=int(input("enter the num 2:"))
c=int(input("enter the num 3:"))
d=int(input("enter the num 4:"))

if(a>=b and a>=c and a>=d):
	print(a, "is greater than b,c,d")
	
elif(b>=c and b>=d and b>=a):
	print(b, "is greater than a,c,d")
	
elif(c>=d and c>=a and c>=b):
	print(c, "is greater than a,b,d")
	
else:
	print(d, "is greater than a,b,c")
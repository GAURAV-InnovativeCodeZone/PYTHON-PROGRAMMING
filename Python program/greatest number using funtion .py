
 # greatest number using by def() funtion

def greatest_number():
	
	a=int(input("enter the num1 :"))
	b=int(input("enter the num2 :"))
	c=int(input("enter the num3 :"))
	
	if (a>b) and (a>c):
		print(a, "is greatest number")
	elif (b>c) and (b>a):
		print(b, "is greatest number")
	else:
		print(c, "is greatest number")
		
greatest_number()
		
	


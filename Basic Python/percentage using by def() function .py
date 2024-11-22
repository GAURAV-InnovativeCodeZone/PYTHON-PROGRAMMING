
 # percentage using by def() function

def per():
	
	math=int(input(" enter the marks in math : "))
	eng=int(input(" enter the marks in english : "))
	bio=int(input(" enter the marks in biology : "))
	
	print("Your percentage is", ((math+eng+bio)/300)*100)

per()

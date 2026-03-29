
 # multiplication table of n using by recursion

n=int(input("enter the number : "))
def table(n, i=1):
	if (i>10):
		return
	print(f"{n}*{i} = {n*i}")
	table(n, i+1)
	
table(n)
		
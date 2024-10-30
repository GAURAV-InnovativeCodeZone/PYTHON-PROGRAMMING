
 # sum of number using by recursion

n=int(input("enter the number : "))
def sum(n):
	if n==0 or n==1:
		return 1
	return n + sum(n-1)
print(sum(n))
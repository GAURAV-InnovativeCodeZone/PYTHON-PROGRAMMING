
  # multiplication table of any number by using while loop
  
n=int(input("enter any number:"))
print()
print(f"multiplication table of {n}")
i=1
while i<11:
	#print(n, "*", i, "=", n*i)
	print(f"\t {n}*{i}={n*i}")
	i+=1     

#multiplication of table with limitation of n

n1 = int(input("starting limit : "))
n2 = int(input("ending limit   : "))
print()

print(f"multiplication table from {n1} to {n2}")

for a in range(n1,n2):
	print("\n")
	for b in range(1,11):
		print(f"\t {a}*{b}={a*b}")
		#print(a, "*", b, "=", a*b)
 
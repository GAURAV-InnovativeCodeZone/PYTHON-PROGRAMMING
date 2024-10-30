# multiplication table of any number by using for loop

n = int(input("Enter any number:"))
print()
print(f"multiplication table of {n}")
for i in range(1, 11):
    # print(n, "*", i, "=", i*n)
    print(f"\t {n} x {i} = {n*i}")

x=int(input("enter a number : "))
for i in range(x):
    for j in range(x-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print()    
for i in range(x-1):
    for j in range(i+1):
        print(" ",end="")
    for k in range(x-i-1):
        print("* ",end="")
    print()           
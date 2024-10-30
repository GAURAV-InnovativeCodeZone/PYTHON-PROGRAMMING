# Method 1 (using third variable)
a = 5
b = 7
print("\nBefore Swapping--")
print("a =",a, "b =",b)
temp = a   #temp=5
a = b      #a=7
b = temp   #b=5
print("After Swapping--")
print("a =",a, "b =",b)

# Method 2 (using comma operator/without using third variable)
c = 10
d = 20
print("\nBefore Swapping--")
print("c =",c, "d =",d)

c,d = d,c
print("After Swapping--")
print("c =",c, "d =",d)

# Method 3 (using arithmetic addition and subtraction operators)
p = 11
q = 22
print("\nBefore Swapping--")
print("p =",p, "q =",q)
p = p+q    # p=11+22=33
q = p-q    # q=33-22=11
p = p-q    # p=33-11=22
print("After Swapping--")
print("p =",p, "q =",q)

# Method 4 (using arithmetic multiplication and division operators)
p = 8
q = 4
print("\nBefore Swapping--")
print("p =",p, "q =",q)
p = p*q    # p=8*4=32
q = p/q    # q=32/4=8
p = p/q    # p=32/8=4
print("After Swapping--")
print("p =",p, "q =",q)

# Method 5 (using bitwise XOR operator)

A = 75  #75=1001011
B = 65  #65=1000001
print("\nBefore Swapping--")
print("A =",A, "B =",B)
A = A^B   # A=1001011^1000001=0001010
B = A^B   # B=0001010^1000001=1001011
A = A^B   # A=0001010^1001011=1000001
print("After Swapping--")
print("A =",A, "B =",B)

# Method 6 (using bitwise addition and subtraction operator)

x = 2    #2=0010
y = 6    #6=0110
print("\nBefore Swapping--")
print("x =",x, "y =",y)
x = (x&y)+(x|y)   # x = (0010 & 0110)+(0010 | 0110) = 1000
y = x+(~y)+1      # y = [1000 + (~0110)+ 1] = [1000 + (-0111) + 1] = 0010
x = x+(~y)+1      # x = [1000 + (~0010)+ 1] = [1000 + (-0011) + 1] = 0110
print("After Swapping--")
print("x =",x, "y =",y)

# note : The bitwise NOT of a positive integer n gives -(n+1) that means (~n)=-(n+1)
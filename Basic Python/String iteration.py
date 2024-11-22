# String iteration

str = "Gaurav Singh Panwar"
print(str)
x = len(str)
print("length of str ", x)
for n in range(x):
	print(str[n])
	
# Reverse string iteration - way 1

str2 = "Gaurav Singh Panwar"
print(str2)
y = len(str2)
print("length of str2", y)
for n in range(y-1, -1, -1):
	print(str2[n])
	
# Reverse string iteration - way 2

str3 = "Gaurav Singh Panwar"
print(str2)
str3 = str3[-1 :: -1]  #store reverse string
print(str3)
z = len(str3)
print("length of str3", z)
for n in range(z):
	print(str3[n])
	
# String iteration without using length

txt = "Gaurav Panwar"
print(txt)
for n in txt:
	print(n)
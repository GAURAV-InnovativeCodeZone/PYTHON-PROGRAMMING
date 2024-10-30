# List iteration

list1 = [5, 10, 15, 20, 25]
print(list1)
x = len(list1)
print("length of list1 ", x)
for n in range(x):
	print(list1[n])
	
# Reverse string iteration - way 1

list2 = [5, 10, 15, 20, 25]
print(list2)
y = len(list2)
print("length of list2 ", y)
for n in range(y-1, -1, -1):
	print(list2[n])
	
# Reverse string iteration - way 2

list3 = [5, 10, 15, 20, 25]
print(list3)
list3 = list3[-1 :: -1]  #store reverse list
print(list3)
z = len(list3)
print("length of list3 ", z)
for n in range(z):
	print(list3[n])
	
# String iteration without using length

txt = [10, 20, 30, 40, 50,]
print(txt)
for n in txt:
	print(n)
# zip() function : iterate over multiple iterables(list, set, tuple, dictionary) at the same time.
# Syntax : zip(iterable1, iterable2, ...)

# way-1 : using zip()

list1 = [2,4,6,8,10]
list2 = [5,10,15,20,25]
for x,y in zip(list1,list2):
  print(x,y)

# way-2 : without using zip()

list1 = [1,3,5,7,9]
list2 = [4,8,12,16,20]
t = len(list1)
for i in range(t):
  print(list1[i], list2[i])


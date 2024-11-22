""" Comprehension Method : it's an elegant and concise way to define and create a new 
list, set or dictionary based on an existing iterable object. """

# using comprehension

a = [b for b in range(1,21)]
print(a)

# using comprehension with filter/condition

n = [m for m in range(1,21) if m%2==0]
print(n)

# without using comprehension

list = []
for i in range(1,21):
  list.append(i)
print(list)

# exmaple : convert string into list using comprehension

string = ("GAURAV")
print("string:", string)
list = [s for s in string]
print("list:", list)
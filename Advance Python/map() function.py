' ' ' map() function :- It works as an iterator to transform each element of iterables and returns a new iterable with the results. It takes two arguments: a function and an iterable. ' ' '
# syntax : map(function, iterable)

# Example 1

print("\n-----Example 1-----\n")
def add_one(x):
  return x + 1
items1 = [10, 20, 30, 40]
print("old iterables list:", items1)

result = map(add_one, items1)
print("new iterables list:", list(result))



# It is often used with lambda functions, which are anonymous functions

# Example 2

print("\n-----Example 2-----\n")
items2= [1, 2, 3, 4]
print("old iterables list:", items2)

result = map(lambda x: x * x, items2)
print("new iterables list:", list(result))


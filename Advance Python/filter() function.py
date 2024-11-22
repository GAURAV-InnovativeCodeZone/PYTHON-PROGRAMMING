' ' ' filter() function :- It works as an iterator to filter each element of iterables and returns a new iterable that the element is true. It can be used to clean up data, remove unwanted elements. It takes two arguments: a function and an iterable.' ' '
# syntax : filter(function, iterable)

# Example 1

print("\n-----Example 1-----\n")
def even(x):
  return x % 2 == 0

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("old iterable list:", items)

even_num = filter(even, items)

print("new iterable list only even number:", list(even_num))



# Example 2

print("\n-----Example 2-----\n")

ages = [5, 12, 17, 18, 24, 32]
print("old iterable list of all ages:", ages)

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)
print("new iterable list which is adults:", next(adults))
  
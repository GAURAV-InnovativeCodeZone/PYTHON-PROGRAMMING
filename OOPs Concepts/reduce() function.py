''' reduce() function :- It works by applying the function to the first two elements of the iterable and the result is then applied to the third element of the iterable, and so on. '''
# syntax : reduce(function, iterable,[ initializer])

# sum of elememt of the sequence
from functools import reduce

def add(a, b):
  return a + b

numbers = [1, 2, 3, 4, 5]

sum = reduce(add, numbers)
print("sum of elememt of the sequence:", sum)

# concatenate the strings into a single string
str_list = ['G', 'a', 'u', 'r', 'a', 'v']

add_string = reduce(lambda x, y: x + y, str_list)

print("concatenate the strings into a single string:", add_string)
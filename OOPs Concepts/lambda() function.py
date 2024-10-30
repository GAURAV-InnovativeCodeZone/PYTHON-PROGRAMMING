  # Example 1
print("\n-----Example 1-----\n")

def incrementor(n):
    return lambda x: x + n

increment_by_one = incrementor(1)
increment_by_ten = incrementor(10)

print(increment_by_one(5))
print(increment_by_ten(5)) 


 # Example 2
print("\n-----Example 2-----\n")

def my_map(func, iterable):
    result = []
    for item in iterable:
    	result.append(func(item))
        return result

a = (my_map(lambda x: x + 5, [1,2,3]))
print(a)

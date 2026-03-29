' ' ' sorted() function :- It is a built-in function that returns a new sorted list from an iterable. It takes three arguments, there is two optional arguments: key and reverse. ' ' ' 
# syntax : sorted(iterable, key=None, reverse=False)

# Sort a list of numbers in ascending order

num = [5, 3, 2, 1, 4]
print("list of numbers:", num)

sorted_num = sorted(num)
print("sorted numbers list in ascending order:", sorted_num)

# Sort a list of strings in descending order

names = ["Alice", "Bob", "Carol", "Dave"]
print("\nlist of names:", names)

sorted_names = sorted(names, reverse=True)
print("sorted list in descending order:", sorted_names)

# Sort a list of dictionaries by the value of a key
my_list = [{'name': 'Alice', 'age': 25}, 
                  {'name': 'Bob', 'age': 30}, 
                  {'name': 'Carol', 'age': 27}]
sorted_list = sorted(my_list, key=lambda x: x['age'])
print("\nsorted list:", sorted_list)
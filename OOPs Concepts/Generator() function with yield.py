' ' ' generator() function :- A generator function is a function that returns an iterator. When you call a generator function, it does not return a single value, instead it returns an iterator object with a sequence of values. ' ' '

' ' ' yield keyword :- it allows you to create functions that generate sequences of values without having to store all of the values in memory at once. This can be very useful for working with large datasets or for generating sequences of values on demand. ' ' '

  # Example 1
print("\n-----Example 1-----\n")

def generator():
   yield "Welcome"
   yield "to"
   yield "coding"

gen_object = generator()
print(type(gen_object))

print(next(gen_object))
print(next(gen_object))

for i in gen_object:
	print(list(i))


# Example  2	
print("\n-----Example 2-----\n")
			
def simple_generator():
	yield "Welcome to Python Programming"

gen_obj = simple_generator()
print(next(gen_obj))


# Example 3
print("\n-----Example 3-----\n")

def squares(num):
  for i in range(num):
    yield i * i
    
for x in squares(6):
  print(x)    # square of element of the sequence
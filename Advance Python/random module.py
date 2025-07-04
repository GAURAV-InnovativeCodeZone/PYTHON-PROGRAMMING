''' random module :- its define a series of functions for generating or manipulating random integers.
'''

import random

# randint() method returns an integer number in range(start, stop)

n1 = random.randint(1, 10)
print("\n randint random number:", n1)

# randrange() method returns an integer number in range(start, stop-1)

n2 = random.randrange(1, 10)
print("\n randrange random number:", n2)

# choice() method returns a random element from sequence

list1 = ["mango", "strawberry", "apple", "banana", "cherry"]
print("\n random element from sequence:", random.choice(list1))

# choices() and sample() method returns a list with the specified number of randomly selected element from sequence

# syntax: random.choices(sequence, weights=None, cum_weights=None, k=1)
list2 = ["apple", "banana", "cherry"]
print("\n list with random selected element:\n", random.choices(list2, weights = [8, 1, 1], k = 6))

# syntax: random.sample(sequence, k)
list3 = ["raddish", "tomato", "potato", "spinach"]
print("\n list of randomly selected elements:", random.sample(list3, k=2))

# shuffle() method change the order of element

list4 = [10,20,30,40,50,60]
random.shuffle(list4)
print("\n sequence after shuffle:", list4)

# random() method returns a random floating number between 0 and 1

random = random.random()
print("\n random float number between 0 and 1:", random)

# uniform() method returns a random floating number between the two specified numbers (both included)

n3 = random.uniform(5, 10)
print("\n Random float number between specified number:", n3)

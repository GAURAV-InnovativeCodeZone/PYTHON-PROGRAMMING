""" Key Differences between function and method """

# Scope: Functions are independent and define outside the class, while methods are associated (define inside the class) with a class and operate on its objects.
# Calling: Functions are called by their name directly (e.g., function_name()), while methods are called on an object using dot notation (e.g., object.method_name()).
# self parameter: Methods have a mandatory self parameter, while functions do not.


'''Function'''


# This is a function that takes two parameters x and y
def add_numbers(x, y):
    return x + y  # return their sum

# calling the `add_numbers` function with arguments 5 and 7
result = add_numbers(5, 7)
print("The sum of two numbers :", result)  # output : 12


'''Method'''


# This is a class named Dog
class Dog:
    # This is a method named bark
    def bark(self):
        print("The dog is barking...!")

# creating an instance of the `Dog` class.
my_dog = Dog()
# calling the `bark` method of the `Dog` class on the `my_dog` instance.
my_dog.bark()  # output : The dog is barking...!

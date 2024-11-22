'''
★ Multiple Inheritance ★
The Child class inherits the attributes and method from all parents class.
It has one child class and multiple parent classes.
'''

# Base class 1
class division:
    def __init__(self, num1, num2):
        self.n = num1
        self.m = num2

    def divide(self):
        return self.n / self.m


# Base class 2
class modulus:
    def __init__(self, num1, num2):
        self.n = num1
        self.m = num2

    def mod(self):
        return self.n % self.m


# Derived class
class Display(division, modulus):
    def __init__(self, num1, num2):
        self.n = num1
        self.m = num2

    def div_and_mod(self):
        divval = division.divide(self)
        modval = modulus.mod(self)
        return (divval, modval)


# Main execution
if __name__ == "__main__":
   num1 = int(input("Enter the first number: "))
   num2 = int(input("Enter the second number: "))

# Instance of derived class
x = Display(num1, num2)
print("Division:", x.divide())
print("Modulus:", x.mod())
print("DivMod:", x.div_and_mod())

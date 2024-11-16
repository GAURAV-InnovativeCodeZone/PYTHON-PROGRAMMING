"""
Public:
Definition: Public members are accessible from anywhere, both inside and outside the class.
Convention: No special naming convention is used and No underscore prefix.

Private:
Definition: Private members are intended to be accessed only within the class itself.
Convention: Single underscore prefix (_): A double leading underscore (__) is used to indicate a private member. Python performs name mangling on these members to make them less accessible from outside the class.

Protected:
Definition: Protected members are intended to be accessed only within the class itself and its subclasses.
Convention: Double underscore prefix (__): A single leading underscore (_) is used to indicate a protected member.
"""


class Access_Specifiers:
    def __init__(self):
        self.public_var = 10  # public modifier
        self._protected_var = 20  # protected modifier
        self.__private_var = 30  # private modifier


    def public_method(self):
        print("\nPublic Method called...")   
        print("Acccessible public variable", self.public_var)
        print("Acccessible protected variable", self._protected_var)
        print("Acccessible private variable", self.__private_var, "using public method")
        self.__private_method()
        
        
    def _protected_method(self):
        print("\nProtected Method called...")
        print("Acccessible protected variable", self._protected_var)
        print("Acccessible public variable", self.public_var)
        print("Acccessible private variable", self.__private_var, "using protected method")
        
        
    def __private_method(self):
        print("\nPrivate method called...")
        print("Acccessed private method","within public method")
        

# Create an instance of the class
obj = Access_Specifiers()

# Accessing the protected variable and method
obj._protected_method()

# Accessing the public variable and method
obj.public_method()

# Trying to access the private method directly then it will be raise error
# obj.__private_method()  # AttributeError: 'MyClass' object has no attribute '__private_method'
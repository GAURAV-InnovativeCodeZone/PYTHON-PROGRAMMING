'''
A class method receives the class(cls) as implicit first argument, just like an instance method receives the instance(self).
To declare a class method, use @classmethod
It can be called either on the class (e.g. C.f()) or on an instance
(e.g. C().f()). The instance is ignored except for its class.
'''

class MyClass:
    class_var = 0
    
    def __init__(self, value):
        self.instance_var = value
    
    @classmethod
    def increament_class_var(cls):
        cls.class_var += 1
        print(f"class variable increamented to: {cls.class_var}")
    
    @classmethod
    #example of an alternative constructor
    def create_from_string(cls, data_string):
        value = int(data_string.split(":")[1])
        return cls(value)

#calling a class method directly on the class
MyClass.increament_class_var()

#using an alternative constructor
instance1 = MyClass.create_from_string("data :10")
print(f"Instance 1 value: {instance1.instance_var}")
        
        
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Hello! My name is {self.name} and Iam {self.age} years old.")
obj = person("Gaurav",23)
print(obj.name)
obj.say_hello()
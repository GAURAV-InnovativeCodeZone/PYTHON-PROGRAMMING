'''
Demontrating abstraction in Python using a simple Car class.
Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object.
'''

class Car:
    def __init__(self):
        self.accelerate = True
        self.brake = True
        self.clutch = True
        
    def start(self):
        self.clutch = True
        self.accelerate = True
        print('Car started with clutch engaged and accelerate pressed.')

    def stop(self):
        self.accelerate = False
        self.brake = True
        print('Car stopped with brake applied.')

car = Car()
car.start()
print('Internal state after starting:', car.__dict__)
car.stop()
print('Internal state after stopping:', car.__dict__)

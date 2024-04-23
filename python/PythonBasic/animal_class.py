
class animal(object):
    def __init__(self, name):
        self.name = name

    def move(self):
        print("move~")

    def speak(self):
        print("speak~")

class Dog(animal):
    def speak(self):
        print('woof-woof')

class Duck(animal):
    def speak(self):
        print('quack-quack')
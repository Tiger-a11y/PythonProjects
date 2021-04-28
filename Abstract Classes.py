# ______ Abstract Classes _______#
# from abc import ABC, abstractmethod
# class Computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass
#
# class Laptop(Computer):
#     def process(self):
#         print("running")
#
# com = Computer()
# com.process()
# com1 = Laptop()
# com1.process()

# from abc import ABC, abstractmethod
class Animal():
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("i can run and walk")

class Snake:
    def move(self):
        print("i can crawl")

class Dog:
    def move(self):
        print("i can bark")
class Lion:
    def move(self):
        print("i can Roar")

# Drivers Code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
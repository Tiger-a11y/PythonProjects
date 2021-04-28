from threading import *
from time import sleep
class A(Thread):
    def run(self):
        for i in range(5):
            print('Hello')
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(1)

obj1 = A()
obj2 = B()

obj1.start()
sleep(0.2)
obj2.start()

obj1.join()
obj2.join()
print('bye')
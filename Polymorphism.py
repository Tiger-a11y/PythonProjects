#
# #  *****---- Duck Typing  ----*****
#
# class My_editor:
#     def execute(self):
#         print('Spell check')
#         print('convention check')
#         print('compiling')
#         print('running')
#
#
# class Pycharm:
#     def execute(self):
#         print('Compiling ')
#         print('Running')
#
#
# class Laptop:
#     def code(self,ide):
#         ide.execute()
#
# ide = Pycharm()
# # ide2= My_editor()
#
# A1 = Laptop()
# A1.code(ide)


# # *****---- Operator Overloading ----*****
#
# class student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#
#     def __gt__(self, other):
#         r1 = self.m1 + self.m2
#         r2 = other.m1 + other.m2
#         if r1>r2:
#             return True
#         else:
#             return False
#     # def __str__(self):
#     #     return '{ } { }'.format(self)
#
#
# s1 = student(54,65)
# s2 = student(48,59)
#
# s3 = s1 +s2
#
# if s1>s2:
#     print('s1 Wins')
#
# else:
#     print('s2 Wins')
#
# a = 8
# print(a)
#
# print(s1.m2 )

# # *** --- Method overriding ----****
#
#
# class Student:
#        def __init__(self,m1,m2):
#            self.m1 = m1
#            self.m2 = m2
#
#        def show(self):
#            return self.m1 ,self.m2
#
#        def sum(self,a=None,b=None,c=None):
#            s=0
#            if a!=None and b!=None and c!=None:
#                s=a+b+c
#            elif a!=None and b!=None:
#                s = a+b
#            else:
#                s=a
#            return s
#
#
# A = Student(45,56)
# print(A.show())
# print(A.sum(5,56,2))

# *****----Method Overriding ---*****

# class A:
#     def show(self):
#         print('in A show')
# class B(A):                         #___Works on Inheritance___#
#     # print('in B show')
#     pass
# a1 = B()
# a1.show()


#  __Another Example__

class Parent():
 # Constructor
  def __init__(self):
      self.value = "Inside Parent"

        # Parent's show method
  def show(self):
      print(self.value)


# Defining child class
class Child(Parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)


# Driver's code
obj1 = Parent()
obj2 = Child()
obj2.show()
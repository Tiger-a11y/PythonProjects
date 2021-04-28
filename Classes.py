#  ----Class Constructor ------
# class computer:
#     def __init__(self,cpu,ram):             # constructor
#         self.cpu = cpu
#         self.ram = ram
#
#     def config(self):
#         print('config is:',self.cpu,self.ram)
#
#
# com1 = computer('i5',16)
# com2 = computer('rysen',12)
#
# com1.config()
# com2.config()

# ----- Constructor, Self And Compairing ------

# class computer:
#     def __init__(self):
#         self.name="Akash"
#         self.age=27
#
#     def update(self):
#         self.age = 30
#
#     def compare(self,other):
#         if self.age == other.age:
#             print("they are same")
#
#
# c1 = computer()
# c2 = computer()
#
# c1.name = 'Rashi'
# c1.age = 16
#
# if c1.compare(c2):
#     print('they are same')
# else:
#     print('they are differant')
#
# # c2.update()
#
# print(c1.name,c1.age)
# print(c2.name,c2.age)

# --- Types of Methods ---

# class student:
#     school = 'N.E.S'
#     def __init__(self,m1,m2,m3):
#         self.sub1 = m1
#         self.sub2 = m2
#         self.sub3 = m3
#
#     def avg(self):
#         return (self.sub1+self.sub2+self.sub3)/3
#
#     @classmethod
#     def getschool(cls):
#         return cls.school
#
#     @staticmethod
#     def info():
#         print("This is Student class.. in abc module")
#
#     # def  get_m1(self):
#     #     return self.sub1
#     # def set_m1(self,value):
#     #     self.sub1 = value
#
# s1 = student(12,56,32)
# s2 = student(32,24,36)
#
# print(s1.avg())
# print(student.getschool())
#
# student.info()

#  --- Inner Cass --

# class student:
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.Laptop()
#
#     def show(self):
#         print(self.name,self.rollno)
#
#
#     class Laptop:
#         def __init__(self):
#             self.brand = 'hp'
#             self.cpu = 'i5'
#             self.ram = 8
#
#         def show(self):
#             print(self.brand,self.cpu,self.ram)
#
# s1=student('Avi',21)
# s2=student('gaurav',32)
#
# s1.show()
# # s2.show()
#
# lap1 = student.Laptop()
# # lap2 = student.Laptop()
# # lap1 = s1.lap
# # lap2 = s2.lap
#
# lap1.show()
# # lap2.show()
#
# # print(id(lap1))
# # print(id(lap2))

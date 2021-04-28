# Health Management System
# 3 clients - Harry, Rohan and Hammad

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

# Health Management System
# 3 clients - Harry, Rohan and Hammad
#
# def getdate():
#     import datetime
#     return datetime.datetime.now()


# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


# bhai ye rha program
import datetime


def gettime():
    return datetime.datetime.now()


def take(b):
    if b == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("harry-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (b == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (b == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")


def retrieve(b):
    if b == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (b == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (b == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    take(b)
else:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    retrieve(b)


# def getdate():
#     import datetime
#     return datetime.datetime.now()
# def client_name():
#     n = int(input("Which client do you want to access\n"
#                   "1.Harry\n2.Rohan\n3.Gaurav\n"))
#
#     def take (a):
#         a=str(int(input("1. update exercise \n 2.update diet ")))
#         if a==1:
#             with open("Ex.txt") as f:
#                 print()
#     print("What do you want to update")
#     value = int(input("What do you wanna update\n"
#                       "1.Exercise\n2.Diet\n"))
#     if n != 1:
#         return
# client_name()
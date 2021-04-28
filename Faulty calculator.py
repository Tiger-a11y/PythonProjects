# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
# Made by Avinash Wagh
print("Enter 1st Number")
val1 = int(input())
print('Enter 2nd Number')
val2 = int(input())
print('so What you Want?'+'+,-,/,%,*')
operator = input()

if val1 == 45 and val2 == 3 and operator == '*' or val1 == 3 and val2 == 45 and operator == '*':
    print("555")
elif val1 == 56 and val2 == 9 and operator == '+' or val1 == 9 and val2 == 56 and operator == '+':
    print("77")
elif val1 == 56 and val2 == 6 and operator == '/' or val1 == 6 and val2 == 56 and operator == '/':
    print("4")
elif operator == '*':
    mult = val1*val2
    print(mult)
elif operator == '+':
    plus = val2+val1
    print(plus)
elif operator == '/':
    Div = val2/val1
    print(Div)
elif operator == '-':
    Div = val2-val1
    print(Div)
elif operator == '%':
    percent = val2 % val1
    print(percent)
else:
    print("Error! Please check your input")

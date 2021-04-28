print("enter no 1\n ")
num1 = input()
print("enter no 2 \n")
num2 = input()
try:
    print("the sum of the two no is:",
          int(num1)+int(num2))
except Exception as error:
    print(error)

print("this is the important line")
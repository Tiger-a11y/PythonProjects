# !!!!!  Astrologer Star Pattern !!!!!
try:
    print("Enter your desired rows")
    n1 = int(input())
    print("Enter 1 or 0")
    n2 = bool(int(input()))
    if n2 == True:
        for i in range(1, n1 + 1):
            for j in range(1, i + 1):
                print("*", end="")
            print()
    elif n2 == False:
        for i in reversed(range(1, n1 + 1)):
            for j in range(1, i + 1):
                print("*", end="")
            print()
except Exception as e:
    print("invalid input")
# number=int(input('enter the number:\n'))
# bol=bool(int(input('enter 1 is true 0 is Flase:\n')))
# if bol==1:
#     for i in range(1,number+1) :
#         print('*'*i)
#
# if bol==0:
#     for i in range(number+1,0,-1) :
#         print('*'*int(i))

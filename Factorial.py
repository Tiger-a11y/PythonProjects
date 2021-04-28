# # try bHere's my approach towards the assignment. I hope you like it.
# def fib():
#  a = []
#  n = int(input("enter the value of n  : "))
#  a.append(0)
#  a.append(1)
#  for i in range(2,n):
#       a.append(a[i-1] + a[i-2])
#       if a[i] >= n:
#           a.pop(i)
#           break
#  print(a)
# fib()

# Factorial by iterable method

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f = f*i
#         print(f)
#     return f
# n=int(input('enter the no of factorial you want :-\n'))
# print('the factorial of :{} is :{}'.format(n,fact(n)))

#Factorial by Reccursive method

# def fact(n):
#     if n==0:
#         return 1
#
#     return n*fact(n-1)
#
# result = fact(5)
# print(result)



# def wellness(list):
#     '''this function prints stirng which you enters'''
#     list = [1,2,3,4]
#     print("list inside", list)
#     return
# list = [10,20,30]
# wellness(list)
# print("list out side", list)
# print(wellness.__doc__ )

# Keyword ,positioning example

# def person(name, **data):
#     print(name)
#     for i,j in data.items():
#         print(i,'-',j)
#
#
# person('navin', age=28, city='mumbai', mo=54691278)

# Even Odd count

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
# how to get input from user to list

lst = []
n = int(input('enter the no of elements : \n'))

for i in range(0,n):
    ele=int(input('neter the value :-'))
    lst.append(ele)
print(lst)

even, odd = count(lst)

print("even : {} and Odd : {}".format(even,odd))
print(even)
print(odd
      )
list1 = [["harry",1],  ["Larry",2], ["Avi",4], ["Gaurav",7] ]
dict1 = dict(list1)
print(dict1)
for item, lollipop in dict1.items():
    print(item, "have lollypop ",lollipop)
for x,y in list1:
    print (x,"lolly pop",y)

    #Quizz

list2 = ["nana",67,"llaj",5,8,4,"kaka"]
for item in list2:
    if str(item).isdigit():
       print(item)

list3 = ["aj","ak","kj"]
for m in list3:

    if m == "ak":
        break
    print(m)

#for x in range(0,14,2):
#    print(x)
for x in range(6):
    print(x)
    if x == 3:
      break
else:
    print("you are at end   ")



# prime no code
num = 10
for i in range(2,num):
    if num % i == 0:
        print(num, "is not a prime no")
        break
else :
        print(num, " it is a prime no")
#    i = i+1

#  Quizz

while (1):
    x = int(input("enter the no\n"))
    if x>100:
        print("congrats you entered greater value than 100\n")
        break
    else:
        print("Try again\n")

# WHILE LOOP AND NESTED LOOP
i = 1                                   #INITIAIZATION
while(i<=4):                            #CONDITION
    print("Avinash"," ",end="")
    j = 3                               #INITIALISATION
    while(j>=1):                        #CONDITION
        print("Rocks","!!! ",end="")
        j = j - 1                       #INCREAMENT/DECREAMENT
    i=i+1                               ##INCREAMENT/DECREAMENT
    print()

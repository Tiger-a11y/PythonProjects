pos = -1
def search(list,n):
    # i=0
    # while i<len(list):
    #     if list[i] == n:
    #         globals()['pos'] = i
    #         return True
    #     i = i + 1
    # return False
    for i in range (len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False

list = [2,6,8,1,9,4,3]
n = 4

if search(list,n):
    print('Found at ',pos+1)

else:
    print('Not found')
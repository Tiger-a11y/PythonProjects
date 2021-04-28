f= open("avi.txt")
# print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(14)
print(f.readline())
# print(f.tell())
f.close()


# to delete the file :-
# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")
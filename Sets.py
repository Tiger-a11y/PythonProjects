s1 = set((1,2,3,4))
s2 = {1, 5, 7, 9, 3}
'''print(s1)
print(type(s1))
print(s2)'''
for x in s1:
    print(x)
Fruits = { "mango", "carrot","onion","grapes"}
print("onion" in Fruits)
Fruits.add("orange")
print(Fruits)
Tropical = {"mango","apple", "banana", "cherry"}
All = Fruits.union(Tropical)
print(All)
Fruits.remove("onion")
print(Fruits)
u1 = {1,2,3,4}
u2 = {5,8,6,7}
u3 = u1.isdisjoint(u2)
print(u3)
# dictionary is nothing but key value pairs
d1 = ()
#print(type(d1))
d2 = {"Harry": "Burger",
      "Rohan":"Fish", "Chetan":"Roti",
      "Shubham":{"B":"maggie", "L": "Roti","D": "Chicken" }}
print(d2["Shubham"])
print(d2["Harry"])
print(d2["Shubham"]["L"])
# Add items
d2["Ankit"]= "junk food"
print(d2)
d2["420"] = "Kababs"
print(d2)
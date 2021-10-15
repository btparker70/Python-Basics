# dictionaries are collections of key-values pairs
# like a phone book name -> contact
# string as key integer as value
# we can only use immutable types for keys
point = {"x":1, "y": 2}
# dict function to create dictionaries
# takes keyword arguments like x=1
point = dict(x=1, y=2)
point["x"]
# since dictionaries are key-value pairs we cannot
# access it with a numeric index like point[0]
print(point["x"])
point["x"] = 10
point["z"] = 20
print(point["x"])
# print(point["a"])
# this gives us an error
if "a" in point:
      print(point["a"])
# this doesnt give an error

point = {"x":1, "y": 2}
print(point.get("a"))
# this gives us a return of 'none"
# you can have it return something if it cant find
print(point.get("a", "cant"))

# to delete
del point["x"]

for key in point:
    print(key, point[key])
# y 2

for key, value in point.items():
    print(key, value)
# y 2
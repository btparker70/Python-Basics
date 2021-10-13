# tuples are read only lists
# contains sequence of objects

# you dont have to use paranthesis
point = (1, 2)
point = 1, 2
print(type(point))

point = (1, 2) * 3
print(point)
# (1, 2, 1, 2, 1, 2)

# convert list to tuple
point = tuple([1, 2])
string = tuple("Hello World")

# returns a tuple with only those items
print(point[0:2])

x, y, z = point
if 10 in point:
    print("exists")

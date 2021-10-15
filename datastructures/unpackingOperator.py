numbers = [1, 2, 3]
print(numbers)
# how do we print individual numbers
# the unpacking operator is *
# it is exactly the same as the spread ... from js
print(*numbers)

# instead of calling the list function we can unpack
values = list(range(5))
print(values)
# instead of calling the list function we can unpack
# using the unpacking operator
values = [*range(5)]
print(values)

# multiple unpacking
values = [*range(5), *"Hello"]
print(values)
# this is a great way to combine lists and add stuff
first = [1, 2]
second = [3]
combined = [*first, "a", *second, *"Hello"]
print(combined)
# [1, 2, 'a', 3, 'H', 'e', 'l', 'l', 'o']


# we can unpack dictionary with **
first = {"x": 1}
second = {"x": 10, "y":2}
# this takes out all the key value pairs from first
# and upbacks second
combined = {**first, **second, "z": 1}
print(combined)
# {'x': 10, 'y': 2, 'z': 1}
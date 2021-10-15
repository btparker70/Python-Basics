values = []
for x in range(5):
    values.append(x * 2)

# this is exactly the same
values = [x * 2 for x in range(5)]

# we can do it as a set instead of a list
valuesSet = {x * 2 for x in range(5)}
print(valuesSet)
# {0, 2, 4, 6, 8}

{1: "a", 2: "b"}
valuesSet = {x: x * 2 for x in range(5)}
print(valuesSet)
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
# now we have a dictionary with these key pairs

# for tuples
valuesSet = (x * 2 for x in range(5))
print(valuesSet)
# returns a generator object
# <generator object <genexpr> at 0x0000020195282110>
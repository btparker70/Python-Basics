letters = ["a", "b", "c"]

# this returns an enumerable object which is iterable
# a tuple
# tuples are like lists but they are read only
for letter in enumerate(letters):
    print(letter)
# (0, 'a')
# (1, 'b')
# (2, 'c')


letters = ["a", "b", "c"]
# items = (0, "a")
# index, letters = items
for index, letter in enumerate(letters):
    print(index, letter)

# 0 a
# 1 b
# 2 c
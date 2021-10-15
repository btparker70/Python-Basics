# list comprehension expression
values = [x * 2 for x in range(10)]
for x in values:
    print(x)

# this is memory inefficient if the list is long
# it stores the values in the memory
# it's more efficient to use a generator object
# generator objects are iterable like lsits
# each iteration gives a new value

from sys import getsizeof

values = (x * 2 for x in range(1000))
print("gen:", getsizeof(values))
# gen 104
# takes 104 bytes of memory
# doesnt change on size

# you cant find the length of a generator because it has no length
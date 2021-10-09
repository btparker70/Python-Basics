# we have 2 types of loops in python
# for
# while

# for x in "Python":
#   print(x)

# for x in ['a', 'b', 'c', 'd']:
#   print(x)

# things prints 0-4
# for x in range(5):
#   print(x)

# this prints 2 3 4
# for x in range(2, 5):
#   print(x)

# this prints 0, 2, 4, 6, 8 even numbers with step '2'
# for x in range(0, 10, 2):
#   print(x)

# ranges dont return a list
# it returns a range object
print(type(range(5)))
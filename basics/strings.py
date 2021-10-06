course = "Python Programming"
# this prints the length of the string
print(len(course))

# this prints the char at index 0 "P"
print(course[0])

# this returns the first char from the end of the string
print(course[-1])

# this will slice a string "Pyt"
print(course[0:3])

# this is exactly the same we can just excluding writing it
print(course[:3])

# this will return the entire string starting from 0
print(course[0:])

# this will return the entire string because there are no bounds
print(course[:])

# strings are immutable, so when we change
#  them it's stored as a new variable at a new location in memory

print(id(course))
print(id(course[0]))


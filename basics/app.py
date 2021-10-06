# variable
students_count = 1000
# float
rating = 4.99
# boolean
is_published = True
# string
course_name = "Python"
#  you can do triple quotes if your string has multiple lines
course_name_2 = """
Python
Course
"""

# you can initailize multiple variables on the same line
x = 1
y = 2
x, y = 1, 2

# we can set multiple variables to the same value
x = y = 1

# we can run this to print the type of variable students_count is
students_count = 1000
print(type(students_count))
# returns <class 'int'>
print(type(1.1))
print(type(True))
print(type("hello"))

age = 20
age = "Python"
print(age)

x = 1
id(x)
print(id(x))
# this returns the address of the memory location where we've stored x
x = x + 1
print(id(x))

# this is a list
x = [ 1, 2, 3]
print(id(x))

# lists are mutable, so the address doesn't change
x.append(4)
print(id(x))
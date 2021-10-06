course = " Python Programming "

# uppercase
print(course.upper())

# lowercase
print(course.lower())

# title makes the 1st char each sentance capitalized
print(course.title())

# this trims white space before or after string
print(course.strip())

# this trims white space before string
print(course.lstrip())

# this trims white space after string
print(course.rstrip())

# find the index of a char
print(course.find("Pro"))

# if the char doesnt exist it will return -1
print(course.find("pro"))

# replace char with a different one  -ython -rogramming
print(course.replace("P", "-"))

# check if this string is in the variable course boolean!
print("Programming" in course)
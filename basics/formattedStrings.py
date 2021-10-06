first = "Brian"
last = "Parker"

# we can do this to concat strings
full = first + " " + last
print(full)

# this is a better way called formatted strings
# what we have between curly braces will be replaced at run time
full = f"{first} {last}"
print(full)

# you can put any valid espressions between {}

full = f"{len(first)} {2 + 2}"
print(full)
numbers = [1, 2, 3]

first = numbers[0]
second = numbers[1]
third = numbers[2]

# this is called list unpacking
# same result
nunbers = [1, 2, 3]
first, second, third = numbers

# the number of items on the left of the = must be
# equal to the length of the list

numbers = [1, 2, 3, 4, 4, 4, 4, 4, 9]
first, second, *other, last = numbers

print(first)
print(other)
print(last)

# this is called an arbitrary argument
# the *other in numbers is an arbitrary list

# lists are a sequence of objects
# can be strings, etc...defined

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
# matrix is a 2 dimensional list
# list of 100 0's
zeros = [0] * 100
# you can concat lists
combine = zeros + letters

# [0, 1, 2, 3...]
# we dont have to write this out there is a method
# goes up to 19
numbers = list(range(20))

#  prints each char out as an item in the list
chars = list("Hello World")

# 11
print(len(chars))

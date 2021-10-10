letters = ["a", "b", "c", "d"]

# returns a
print(letters[0])

# returns d
print(letters[-1])
letters[0] = "A"
print(letters)

# this returns a new list with the first
# 3 items in the list
print(letters[0:3])

numbers = list(range(20))
# this returns every other item
# 0, 2, 4...
print(numbers[::2])

# 19, 18, 17, 16...
print(numbers[::-1])
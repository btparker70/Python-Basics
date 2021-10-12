numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)
# [2, 3, 6, 8, 51]

# sort backwards? descending
numbers = [3, 51, 2, 8, 6]
# sort method takes 2 parameters: key and reverse
numbers.sort(reverse=True)
print(numbers)
# [51, 8, 6, 3, 2]

numbers = [3, 51, 2, 8, 6]
# sorted function takes an iterable, key and reverse

print(sorted(numbers))
# print(sorted(numbers, reverse=True))

# sort METHOD modifies the original list
# sorted FUNCTION does not modify the list

# sorting lists of complex objects
items = [
  ("Product1", 11),
  ("Product2", 12),
  ("Product3", 10)
]

# takes item and returns price
def sorted_item(item):
    return item[1]

# we are passing a reference to the function. not calling it
items.sort(key=sorted_item)
print(items)

# lambda functions are 1 line functions we can pass
# to other functions
# lambdas are anonymous functions

items = [
  ("Product1", 11),
  ("Product2", 12),
  ("Product3", 10)
]

def sorted_item(item):
    return item[1]

# we are passing a reference to the function. not calling it
# lambdas take arguments:and an expression
items.sort(key=lambda item: item[1])
print(items)
# this is a shorter and cleaner way to write functions that are only
# used once
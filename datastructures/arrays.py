# in python arrays are better for large lists
# better for high efficiency
# 90% of the time use lists

from array import array

# array takes typecode. that determins what the array contains
# i is for type signed integer
numbers = array("i", [1, 2, 3])

numbers.append(4)
numbers.insert(2, 5)
print(numbers)
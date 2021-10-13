list1 = [1, 2, 3]
list2 = [10, 20, 30]

# combine into a single list of tuples
# [(1, 10), (2, 20), (3, 30)]
# use zip function to combine lsits

print(list(zip(list1, list2)))
# do list to conver it to a list

# you can pass more iterables
print(list(zip("abc", list1, list2)))
# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
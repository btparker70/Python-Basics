# sets are collections with no duplicates
numbers = [1, 1, 2, 2, 3, 4]
uniques = set(numbers)
print(uniques)
# {1, 2, 3, 4}

second = {1, 4}
second.add(5)
second.remove(5)
len(second)
print(second)

numbers = [1, 1, 2, 2, 3, 4]
first = set(numbers)
second = {1, 5}
# this returns a new set that includes all the items
# that are either in 1st or second set
print(first | second)
# {1, 2, 3, 4, 5}
print(first & second)
# {1}
# prints only what is in both
print(first - second)
{2, 3, 4}
# prints what is only in the first
print(first ^ second)
# returns what are in either set but not both
# {2, 3, 4, 5}

if 1 in first:
    print("yes")
# in python everything is an object

letters = ["a", "b", "c"]

# how to add new items to a list or remove existing items
# add:
# append adds to the end of the list
# functions of objects are methods
letters.append("d")
print(letters)
# ['a', 'b', 'c', 'd']

# if you want to add an item at any position, use insert method

letters.insert(0, "-")
print(letters)
# ['-', 'a', 'b', 'c', 'd']

# remove
# remove from end of list: pop method
letters.pop()
print(letters)
# you can add values to pop to remove at any index
letters.pop(0)

# when you dont know the index you can use remove method
letters.remove("b")
# removes first occurance

# delete method removes a range of items
del letters[0]
del letters[0:3]

# remove all the objects on the list
letters.clear()
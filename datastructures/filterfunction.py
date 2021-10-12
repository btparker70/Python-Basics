items = [
  ("Product1", 11),
  ("Product2", 12),
  ("Product3", 10)
]

# we want to filter and only get items with prices >10

# the result is a boolean value
# if it's true, it's added to the list
x = filter(lambda item: item[1] >= 10, items)
print(x)
# gives us a filter object

filtered = list(filter(lambda item: item[1] > 10, items))
print(filtered)
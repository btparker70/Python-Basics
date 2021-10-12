#  each item in this list is a tuple of 2 items

items = [
  ("Product1", 11),
  ("Product2", 12),
  ("Product3", 10)
]

prices = []
for item in items:
    prices.append(item[1])


print(prices)
# [11, 12, 10]


# or use map function
x = map(lambda item: item[1], items)
print(x)
# this map function will iterate over the 2nd arg, items
# and call the lambda function on each item of the iterable
# it returns a map object, which is iterable
for item in x:
    print(item)

# 11
# 12
# 10

# or you can just make a list
prices = list(map(lambda item: item[1], items))
print(prices)
# [11, 12, 10]
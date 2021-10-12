
items = [
  ("Product1", 11),
  ("Product2", 12),
  ("Product3", 10)
]

prices = list(map(lambda item: item[1], items))
# [expression for item in items]
prices = [item[1] for item in items]
# these produce the same result

filtered = list(filter(lambda item: item[1] > 10, items))
#  the cleanest way to use map and filter
# is with list comprehensions
# [expression for item in items]
filtered = [item for item in items if item[1] > 10]
letters = ["a", "b", "c"]

# find the index of a given object in a list


print(letters.index("a"))
# returns 0


# if we want to check if a value is in a list
letters = ["a", "b", "c"]
if "d" in letters:
  print(letters.index("d"))


# count
letters.count("d")
# returns number of occurrances of a given item in a list

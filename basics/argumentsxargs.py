
# what if we want to add more parameters to a function?
def multiply1(a, b):
  return a * b


multiply1(2, 3)

# we can turn the arguments into a list
def multiply2(*list):
  print(list)


multiply2(2, 3, 4, 5)
# when we add a * before a parameter like on line 10
# python seeds it as a tuple and can package inputs into a tuple
# tuple is good because we can iterate through it

def multiply3(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply2(2, 3, 4, 5))
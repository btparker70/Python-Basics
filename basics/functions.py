# lists are like numbers = [1, 2, 3]
# a tuple is numer = (1, 2, 3)

def increment(number, by):
  return( number, number + by)


print(increment(2, 3))

# we can assign default values to parameters
# we can set type with the : int here
# we can add the return type after as well with ->
def increment(number: int, by: int=1) -> tuple:
  return( number, number + by)


print(increment(2, by=3))
# this is a keyword argument


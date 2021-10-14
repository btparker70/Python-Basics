from timeit import timeit
# timeit can calculate execution time of code

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
# raise is to raise a type of exception
"""
print("first code ", timeit(code1, number=10000))

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("second code ", timeit(code2, number=10000))
# runs 10000 times and gives execution time
# raising exceptions for small apps is okay
# it is really slow for large user base
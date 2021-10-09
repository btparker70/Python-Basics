def fizz_buzz(input):
    string = ""

    if input % 3 == 0:
        string += "Fizz"
    if input % 5 == 0:
        string += "Buzz"
  
    if string == "":
        return input
    # instead of an else:
    return string


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
print(fizz_buzz(7))
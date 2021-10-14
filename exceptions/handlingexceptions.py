# to handle the value error 
# put in try block
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No excceptions were thrown")
print("Execution continues")

# when you make a try block
# python will run anything 
# if it throws an exception it does the except claus
# if you dont handle exceptions properly
# app crashes

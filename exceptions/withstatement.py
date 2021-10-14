try:
    with open("cleanup.py") as file:
        print("file opened")
    age = int(input("Age: "))
    xfactor = 10 / age   
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No excceptions were thrown")

# when we use the with statement
# python will close the file without a finally statement
# the with statement is used to automatically release external resources

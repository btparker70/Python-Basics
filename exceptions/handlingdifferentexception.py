try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("You didn't enter a valid age.")

else:
    print("No excceptions were thrown")

# if any statements in the try block execute, it closes the block
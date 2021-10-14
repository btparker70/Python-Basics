try:
    file = open("cleanup.py")
    age = int(input("Age: "))
    xfactor = 10 / age
    
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No excceptions were thrown")
finally:
    file.close()

# finally clause is always executed even if there's no exception
# great place to close files, network connections etc
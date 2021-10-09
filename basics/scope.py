def greet():
    if True:
        message = "a"
    print(message)

greet()
# message is a local variable while greet is global
# local variables arent block level
# this means they can be accessed globally

message = "a"

def greet():
    message = "b"
    # this variable becomes a local variable!
    # it wont modify the global fariable
    # this will print "a"
    

greet()
print(message)


message = "a"

def greet():
    global message
    message = "b"
    # if we run this we will get 'b'
    # because we are modifying the global variable message
    

greet()
print(message)
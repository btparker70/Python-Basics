def save_user(**user):
    print(user)

# these are keyword arguments
save_user(id=1, name="admid")
# returns {'id': 1, 'name': 'admid'}
# this return is called a dictionary
# it's like an object in javascript

def save_user(**user):
    print(user["id"])

# these are keyword arguments
save_user(id=1, name="admid")
# this returns 1, the value of id
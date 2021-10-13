browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
# [1, 2, 3]

browsing_session.pop()
print(browsing_session)
print("redirect", browsing_session[-1])
# redirect 2
# get the item at the top of the stack

# find if stack is empty
if not browsing_session:
    print("disable")
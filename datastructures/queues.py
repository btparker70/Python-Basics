# stacks have lifo behavior
# queues have fifo first in first out
# queue removes from the beginning
# [1, 2, 3] -> [2, 3]
# this is bad for large lists
# deque is a class
from collections import deque
# declaring deque list variable
# empty list as argument
queue = deque([])
# has similar methods to list objects
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
# if it's empty it's falsey
if not queue:
    print("empty")
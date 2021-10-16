class Point:
    def draw(self):
        print("draw")


point = Point()
# if we want to know if an object is a instance 
# of a given class
print(isinstance(point, Point))
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point({self.x}, {self.y})")
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

x = int(input())
y = int(input())

x2 = int(input())
y2 = int(input())

p1 = Point(x, y)
p2 = Point(x2, y2)

p1.show()
p2.show()
print(f"Distance between points: {p1.dist(p2)}")

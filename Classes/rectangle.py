class Shape:
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

a = int(input())
b = int(input())
rectangle = Rectangle(a, b)
print(f"Area of rectangle: {rectangle.area()}")

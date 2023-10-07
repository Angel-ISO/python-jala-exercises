class GeometricShape:
    def calculate_area(self):
        pass

class Square(GeometricShape):
    def __init__(self, side, color):
        self.side = side
        self.color = color

    def calculate_area(self):
        return self.side * self.side
    
    def calculate_perimeter(self):
          return 4 * self.side


square = Square(5, "red")


print(f"here u have Square Area: {square.calculate_area()}")
print(f"here u have Square Perimeter: {square.calculate_perimeter()}")
print(f"here u have Square Perimeter: {square.color}")

class Circle:

    def calculate_area(self):
        print(3.14*self.radius**2)
        
    def calculate_perimeter(self):
        print(2*3.14*self.radius)

    def __init__(self,radius):
        self.radius = radius

circle1 = Circle(3)
circle1.calculate_area()
circle1.calculate_perimeter()

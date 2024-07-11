class Triangle:

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def calculate_area(self):
        print((self.base * self.height) / 2)

    def calculate_perimeter(self):
        print(self.base * 3)

triangle1 = Triangle(2,3)
triangle1.calculate_area()
triangle1.calculate_perimeter()
class Shape: #Shape(Parent Class)
    def __init__(self):
        pass

    def getPerimeter():
        return perimeter
    
    def getArea():
        return area

class Rectangle(Shape): #Rectangle(Child Class of Shape)
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.perimeter = 0

    def getPerimeter(self): #method for getting Perimeter
        length = self.length
        width = self.width
        perimeter = (length + width) * 2
        self.perimeter = perimeter

class Circle(Shape): #Circle(Child Class of Shape)
    def __init__(self, radius):
        self.radius = radius

    def getArea(self): #method for getting Area
        radius = self.radius
        pi = 3.14
        area = pi * (radius * radius)
        self.area = area

    
rec = Rectangle(10,20) #Rectangle Object
rec.getPerimeter()
print("Retangle perimeter is", rec.perimeter, ".")

cir = Circle(10) #Circle Object
cir.getArea()
print("Circle area is", cir.area, ".")
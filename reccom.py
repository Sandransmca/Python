class Rectangle:#creating a class
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def display(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)

    def area(self):
        return self.length * self.breadth #equation of the area of a rectangle

    def perimeter(self):
        return 2 * (self.length + self.breadth) #equation of the perimeter of a rectangle
     #compare the areas of two rectangles
    def compare(self, other):
        if self.area() == other.area():
            print("Area is equal")
        elif self.area() < other.area():
            print("First area is less")
        else:
            print("Second area is greater")


# Input for first rectangle
l1 = int(input("Enter first length: "))
b1 = int(input("Enter the first breadth: "))
r1 = Rectangle(l1, b1)
print("First rectangle:")
r1.display()
print("Area of first rectangle:", r1.area())
print("Perimeter of first rectangle:", r1.perimeter())

# Input for second rectangle
l2 = int(input("Enter second length: "))
b2 = int(input("Enter the second breadth: "))
r2 = Rectangle(l2, b2)
print("Second rectangle:")
r2.display()
print("Area of second rectangle:", r2.area())
print("Perimeter of second rectangle:", r2.perimeter())

# Comparing the two rectangles
r1.compare(r2)

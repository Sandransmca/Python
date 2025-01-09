class rectangle:
    area = 0
    perimeter = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length + self.width)
length1 = int(input("Enter length of the rectangle 1 : "))
width1 = int(input("Enter width of the rectangle  1 : "))
length2 = int(input("Enter length of the rectangle  2  : "))
width2 = int(input("Enter width of the rectangle  2 : "))
rect1= rectangle(length1, width1)
rect2= rectangle(length2, width2)
print("Area of 1st rectangle  :",rect1.calc_area())
print("Perimeter of 1st rectangle  :",rect1.perimeter())
print("Area of 2nd rectangle  :",rect2.calc_area())
print("Perimeter of 2nd rectangle  :",rect2.perimeter())
def compare():
    r1 = rect1.calc_area()
    r2 = rect2.calc_area()
    if r1 > r2:
        print("Rectangle 1st is large")
    elif r1 == r2:
        print("these 2 are equal")
    else:
        print("Rectangle 2nd is large")
compare()
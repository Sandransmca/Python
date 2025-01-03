class Rectangle:
     def __init__(self,length,breadth):
         self.length=length
         self.breadth=breadth
     def area(self):
         return self.length*self.breadth
     def perimeter(self):
         return 2*(self.length+self.breadth)
l1=int(input("enter the length"))
b1=int(input("enter the breadth"))
r1=Rectangle(l1,b1)
print("area of first rectangle is",r1.area())
print("perimeter of first rectangle is",r1.perimeter())
l2=int(input("enter the length"))
b2=int(input("enter the breadth"))
r2=Rectangle(l2,b2)
print("area of second rectangle is",r2.area())
print("perimeter of second rectangle is",r2.perimeter())
a1=r1.area()
a2=r2.area()
if a1>a2:
    print("area of first rectangle is high")
else:
    print("area is high in second rectangle ")
if a1==a2:
    print("both rectangles have same area")

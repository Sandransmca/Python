a=int(input("enter sides of square:"))
s_area=lambda a:a*a
print("area of square",s_area(a))

l=int(input("enter lenght of rectangle:"))
b=int(input("enter breadth of rectangle:"))
r_area=lambda l,b:l*b
print("area of rectangle",r_area(l,b))

b=int(input("enter base of triangle:"))
h=int(input("enter height of triangle:"))
t_area=lambda b,h:.5*b*h
print("area of triangle",t_area(b, h))
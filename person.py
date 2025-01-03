


class Person:
  def __init__(self,name,age):
      self.name=name
      self.age=age
  def display(self):
      print(self.name)
      print(self.age)
  def compare(self, other):
     if self.age == other.age:  # Compare the age attribute of both objects
        print("Both are same") # Return True if ages are the same
     elif self.age>other.age:
        print("p1 is elader")
     else:
         print("p2 is elader")

n1=input("Enter the name of person 1: ")
n2=input("Enter the name of person 2: ")
a1=input("Enter the age of person 1: ")
a2=input("Enter the age of person 2: ")
p1=Person(n1,a1)
p2=Person(n2,a2)
(p1.compare(p2))
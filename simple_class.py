class Car:
    wheels = 4  # class-level attribute

    def __init__(self, m, c):
        self.m = m  # instance attribute for model
        self.c = c  # instance attribute for car brand

    def display(self):
        print(self.m)  # prints the model
        print(self.c)  # prints the car brand


# Creating an instance of the Car class
c1 = Car(19, "BMW")

# Calling the display method on the instance
c1.display()

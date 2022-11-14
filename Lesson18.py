# exercise 1:
# 1.Create a Python class Person with attributes: name and age of type string.
# 2.Create a display() method that displays the name and age of an object created via the Person class.
# 3.Create a child class Student which inherits from the Person class and which also has
# a section attribute.
# 4.Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# 5.Create a student object via an instantiation on the Student class and then test the displayStudent method.
'''
class Person:
    attr1 = 'Name'
    attr2 = 'Age'

    def display(self):
        self.attr1 = 'Sokrat'
        self.attr2 = '30'


class Student(Person):
    def display(self):
        print(self.attr1, self.attr2)


Sokrat = Student()
Sokrat.display()

'''


# Exercise 2:
# 1.Write a Rectangle class in Python language, allowing you to build a rectangle
# with length and width attributes.
# 2.Create a Perimeter() method to calculate the perimeter of the rectangle and a
# Area() method to calculate the area of the rectangle.
# 3.Create a method display() that display the length, width, perimeter and
# area of an object created using an instantiation on rectangle class.
# 4.Create a Parallelepiped child class inheriting from the Rectangle class and with
# a height attribute and another Volume() method to calculate the volume of the Parallelepiped

'''
class Rectangle:
    length = 7
    width = 5

    def count_perimeter(self):
        return 2 * (self.length + self.width)

    def count_area(self):
        return self.length * self.width

    def display(self):
        print("The length:\t", self.length)
        print("The width:\t", self.width)
        print("The width:\t", self.count_perimeter())
        print("The width:\t", self.count_area())


class Parallelepiped(Rectangle):
    height = 8

    def volume(self):
        return self.height * self.count_area()


rect_1 = Parallelepiped()
rect_1.volume()
'''

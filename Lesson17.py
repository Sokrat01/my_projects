'''
# Exercise 1  Write a Python program to create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def show(self):
        print(f'The max speed of the car is {self.max_speed}:\t')
        print(f'\nThe max speed of the car in mileage is {self.mileage}:')


Audi = Vehicle(160, 260)
Audi.show()
'''

'''
# Exercise 1 second version: 
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


BMW = Vehicle(260, 160)
print(f'\nThe max speed of the car is{BMW.max_speed}')
print(f'The max speed of the car in mileage is{BMW.mileage}')
'''

'''
# Exercise2 Restyling by me: Write a Python class named Student with two attributes student_name, marks. Modify the attribute
# values of the said class and print the original and modified values of the said attributes:
class Student:

    def __init__(self, st_num, marks):
        self.st_num = st_num
        self.marks = marks

    def show(self):
        print(f"The name of the student is: {self.st_num}")
        print(f"the mark of the student is: {self.marks}")


stud1 = Student("Sokrat", "10")
stud1.show()

'''

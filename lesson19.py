'''
# Exercise2: Create a base class Car and child classes (BMW, Ferrari) and get max_speed method from base class and
# also child classes should have custom method.
class car:
    def __init__(self, max_speed):
        self.max_speed = max_speed

        def speed_1(self):
            return '\nThe speed:\t'

        def fact(self):
            return '\nits the max speed of the car:\t'

        def __str__(self):
            return self.max_speed


class bmw(car):
    def __init__(self, low_speed):
        super().__init__('bmw')
        self.low_speed = low_speed

    def speed_1(self):
        return self.low_speed

    def fact(self):
        return '\nThis is the low speed of the car:\t'


class ferrari(car):
    def __init__(self, mid_speed):
        super().__init__('Ferrari')
        self.mid_speed = mid_speed

    def speed_1(self):
        return self.mid_speed

    def fact(self):
        return '\n these are the legal low speeds of the cars'


car1 = bmw(40)
car2 = ferrari(60)
print(car2)
print(car2.fact())
print(car1.fact())
print(car2.speed_1())
print(car1.speed_1())
'''

'''
# exercise1 from lesson 15:

import random

x = random.randint(1, 10)


def my_numb():
    y = int(input('Guess the number:\t'))
    if x == y:
        print(f'its true, random num is {y}:')
    else:
        print(f'its false, random num is: {x}')


print(my_numb())
'''

'''
import random

a = random.randint(1, 10)
d = int(input("input number from 1 to 10:\t"))    

if a == d:
    print(f"True, random number is {d}")

else:
    print(f"False, random number is {a}")
'''

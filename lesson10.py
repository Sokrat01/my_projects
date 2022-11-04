'''
def perimeter_of_rect(length, width):
    return 2 * (length + width)


length = int(input('The length of rectangle is:\t'))  # Arajadranq1
width = int(input('The width of rectangle is:\t'))

a = perimeter_of_rect(length, width)
print('Perimeter of rectangle is:', a)

'''

'''
def perimeter_of_square(_):
    return 4 * width


width = int(input('The perimeter_of square is:\t'))             # Arajadranq2
x = perimeter_of_square(width)
print(x)
'''

'''
def area_of_rectangle(length, width):
    return length * width


length = int(input('The length of rectangle is:\t'))       # Arajadranq3
width = int(input('the width of rectangle is:\t'))
x = area_of_rectangle(length, width)
print(x)
'''

'''
def area_of_square(_):
    return side_length * side_length


side_length = int(input('The area of square is:'))    # Arajadranq4
a = area_of_square(side_length)
print(a)
'''

'''
def myfunction(s):
    e = {'upper': 0, 'lower': 0}
    for c in s:
        if c.isupper():
            e['upper'] += 1
        elif c.islower():                                           #Arajadranq5
            e['lower'] += 1
        else:
            pass
    print('upper:', e['upper'])
    print('lower:', e['lower'])


myfunction('The quick Brown Fox')



'''

'''
def lista(numbers):
    d = []
    for i in numbers:
        if i not in d:                           #Arajadranq6
            d.append(i)
    return d


print(lista([1, 2, 3, 3, 3, 5, 6, 15, 201]))
'''


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


x = int(input('The Number:\t', ))
print('The number is prime:\t', is_prime(x))

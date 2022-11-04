# lesson1
'''
a = 150
b = 16.67
print(a + b)  # Arajadranq1
z = bool(166.67)

print(z)
print(a > b) and (z > a) or (b > z)
print(a, b, z, sep='"_"')
print(a, b, z, end='Me')


'''
from itertools import count

'''
k = 35
my_bool = (k)                   #Arajadranq2
my_int = int(my_bool + 3)
print(my_int)

'''

'''
str1 = 'Sokrat\t'
str2 = 'Gevorgyan'
print('str1+str2 = ', str1 + str2)              #Arajadranq3

'''

# lesson1

'''
x = int(input("number"))
if x % 2 == 0 and x % 3 == 0:                           #Arahjadranq2
    print("the number is even")
elif x % 3 == 0:
    print("the number is odd")
else:
    print("its not true")
'''

'''
x = 15
y = 20                                              #Arahjadranq3
z = int(input("the number: "))
print = ("greather", max(x, y, z))
'''

'''
d = 30
k = 20
if d == k:                                           #Arahjadranq4
    print(d)
elif d > k:
    print('d is bigger than k')
elif k < d:
    print('k is bigger than d')
else:
    print('the function dont works well')

'''

'''
a = 15
b = 97

if a == b:
    print(a)
elif a > b:                                     #Arahjadranq5
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("happy new year")

'''
# Lesson2
'''
for x in range(11, 99):
    if x % 4 == 1:                  #Arajadranq2
        print(x)
'''
'''
t = int(input('Temperature:\t'))
if t <= 18:
    print('its cold:\t')
elif 18 < t < 24:
    print('its pleasant:\t')
else:
    t >= 24
    print('its hot')
'''

'''
for i in range(7, 30):                            #Arahjadranq4
    if i % 2 == 0:
        print(i)
'''
'''
while a < 40:
    a = a +4
    print(a)

'''
'''
for a in range(100, 600):                             #Arajadranq5
    if a % 3 == 0 and a % 11 == 0 and a % 7 != 0:
        print(a)
'''
'''
for i in range(1, 100):
    if i % 7 == 0:
        print('The number divides by:\t', i)
'''

'''
for x in range(1, 100):
    if x % 7 == 0:
        print('the number divides by:\t', x)
'''

# lesson3
'''
str = str(input('The word:\t'))
if str == str[::-1]:
    print('The string is palindrome')        #Arajadranq1
else:
    print('String is not palindrome')
'''

'''
x = str(input('word:\t'))
length = len(x)
if len(x) < 10:
    print('Short word')
elif len(x) > 10:
    print('Long word')
else:
    print('Too long world')
'''

'''
str1 = input('The string:\t')
for i in str1:
    if i == 'a':
        print(str1.count(i))
        break
'''
'''
list_of_numbers = [1, 12, 3, 14, 5, 16]
for i in list_of_numbers:
    print(sum(list_of_numbers))
    break
'''
# lesson4
'''
list_of_numbers = [-5, 2, 9, -3, -255, 55, 60, 70, 98, -101]            #Arajadranq1
max(list_of_numbers)
print('The largest number in the list:\t', max(list_of_numbers))
'''

'''
my_list = [1, 50, 20, 60, 70, 20, 30, 40, 50, 60, 80, 99, -1]
for val in my_list:
    if val == 20:
        val = 200
        break
print(val)
'''

'''
list_of_numbers = [1, 7, 8]                 #Arajadranq 3
y = 0
if i in list_of_numbers:
    y = y * i
    print(y)
'''
'''
k = [1, 5, 8, 9,  11, -20, -2]
x = 0                                   #Arajadranq4
while x < len(k):
    if k[x] < 0:
        k.remove(k[x])
        x = 0
    else:
        x = x + 1
    print(k)
'''
'''
e = [11, 22, 51, 54, 12, 36, 48, 66, 73, 25, 31, 7, 9, ]        #Arajadranq5
for x in e:
    if x % 2 == 0:
        print(x)
'''
# lessson5
'''
import random

e = []
b = []
length = int(input('The list of numbers:\t'))
length = int(input('The list of numbers:\t'))  # 1
for _ in range(length):
    e.append(random.randint(0, 50))
    b.append(random.randint(0, 50))
print(e)
print(b)

e = set(e)  # 1.1
print(e)
b = set(b)
print(b)

if e == b:  # 1.2
    print('The number is true:\t')
else:
    print('The number is false:\t')

i = e.union(b)  # 1.3
print(i)

i = e.intersection(b)  # 1.4
print(i)

i = e.difference(b)  # 1.5
print(i)
'''
# lesson6
'''
k = '*'
for i in range(1, 5, 1):
    for e in range(1, i + 1):
        print(k, end=' ')
    print(' ')
for i in range(5, -1, -1):
    for e in range(-1, i - 1):
        print(k, end=' ')
    print(' ')
'''

'''
new_dict = {}
my_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
length = len(my_dict.values())
for i in my_dict.values():
    new_dict[1] = len(i)
    print(new_dict)
'''
'''
x = 75869
y = 0
while x:
    x //= 10
    y = y + 1
print('The number digit is:\t')
print(y)

'''
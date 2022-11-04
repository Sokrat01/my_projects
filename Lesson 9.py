'''
n = '*'
for i in range(1, 5, 1):
    for a in range(1, i + 1):
        print(n, end=' ')
    print(' ')
for i in range(5, -1, -1):
    for a in range(-1, i - 1):
        print(n, end=' ')
    print(' ')

'''

'''
num = 75869
x = 0
while num:                                              #Arajadranq 3
    num //= 10
    x = x + 1
print("The number digits is: ")
print(x)
'''

'''
a = [23, 65, 19, 90]                             #Arajadranq 10
temp = a[2]
a[2] = a[0]
a[0] = temp
print(a)

'''


'''
import random
y = int(input('Enter the number:\t'))
k = []
a = 0
b = 0
for i in range(y):
    k.append(random.randint(-2000, 2000))      #Arajadranq 9
    if k[i] < 0:
        a = a + 1
    if k[i] > 0:
        b = b + 1
print(k)
print('Enter the positive numbers: ', a)
print('Enter the negative numbers: ', b)
'''

'''
z = {}
y = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}  #6 Arajadranq 
length = len(y.values())
for i in y.values():
    z[1] = len(i)
    print(z)
'''
x = 60
y = 10
z = x / y
print(z)
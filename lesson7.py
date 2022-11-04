'''
import random

a = []
b = []
length = int(input('numbers of elements in list:\t'))   #'Arajadranq'1
for _ in range(length):
    a.append(random.randint(0, 20))
    b.append(random.randint(0, 20))

print(a)
print(b)

a = set(a)
print(a)
b = set(b)
print(b)  # 'Arajadranq'1.1

if a == b:
    print('it is true')  # 'Arajadranq'1.2
else:
    print('it is false')

c = a.union(b)  # 'Arajadranq'1.3
print(c)

c = a.intersection(b)  # 'Arajadranq'1.4
print(c)

c = a.difference(b)  # 'Arajadranq'1.5
print(c)

'''

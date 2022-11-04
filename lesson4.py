'''
num = int(input("enter a number:\t "))
factorial = 1
if num < 0:
    print("factorial not exist for negative numbers\t")       #Arajadranq 1
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
        print("the factorial of", num, "is", factorial)
'''

'''
x = 4
for i in range(10, 100):             #Arajadranq 2
    if i % x == 1:
        print(i)
'''

'''
t = int(input("temperature: "))
if t <= 18:
    print("it is cold")
elif 18 < t < 24:
    print("it is pleasant")                   #Arajadranq 3
else:
    t >= 24
    print("it is hot")
'''

'''
for x in range(100, 600):
    if x % 3 == 0 and x % 11 == 0 and x % 7 != 0:
        print(x)
'''

'''
while x < 40:                    #Arajadranq 4.1
     x += 4
     print(x)
'''

'''
for i in range(7, 30):              #Arajadranq 4.2
   if i % 2 == 0:
        print(i)
'''

'''
for i in range(100, 600):                #Arajadranq5
    if i % 3 == 0 and i % 11 == 0:
        print(i)
else:
    if i % 7 != 0:
        print("the number:  is not dividable 7")
'''



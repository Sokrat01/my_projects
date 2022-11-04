# exercise1 Write a Python program to calculate the sum of a list of numbers using recursion

'''
def list_of_num(num):
    if len(num) == 1:
        return num[0]
    else:
        return num[0] + list_of_num(num[1:])


a = [1, 7, 8, 12]
print(list_of_num(a))
'''

'''
#Write a Python program to get the factorial of a non-negative integer using recursion.
def fac_of_num(x):                                  
    if x == 1:
        return 1
    else:
        return x * fac_of_num(x - 1)


a = 5
print(fac_of_num(a))
'''

'''
#Write a Python program to calculate the harmonic sum of n-1.
#Note: The harmonic sum is the sum of reciprocals of the positive integers.
#Example.
def harmonic_sum(num):
    if num == 0:
        return print('cant divide')
    if num == 1:
        return num
    else:
        return 1/num + harmonic_sum(num-1)


number = int(input("Write number and count harmonic sum:"))
print(harmonic_sum(number))
'''

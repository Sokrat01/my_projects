'''
str = (input("enter the name: "))
if(str == str[::-1]):
    print("string is palindrome")               #Arajadranq 1
else:
    print("string is not palindrome")
'''

'''
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':                 #5 dasi 2 arajadranq sxalmab arel em erord arajadrani tuganq
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('abc'))
print(add_string('string'))
'''

'''
x = input("the word you want")                      #2 Arajadranq
length = len(x)
if length < 10:
    print("short word")                          
else:                                          
    if length > 10:
        print("long word")
'''

'''
def sum(numbers):
    total = 0
    for x in numbers:
        total += x                       #4 arajadranq
    return total
print(sum((1,12,3,14,5,16)))

'''

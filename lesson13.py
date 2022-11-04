# 1Write a Python function to read the content from a text file "poem.txt" line by line and display the
# same on screen.
'''
file = open('poem.txt', 'r', encoding='utf-8')
print(file.read())
'''

'''
#3Write a Python program to add text to a file and display the text in python.txt file.
with open('python.txt', 'a') as file:
    x = input('Enter what you want to append:\t')
    for i in x:
        file.write('we are together\n')
    print(i)
'''

# 4Write a Python function display_words() to read lines from a text file "story.txt", and display those
# words, which are less than 4 characters.
'''
def display_words():
    with open('story.txt', 'r', encoding='utf-8') as file:
        d = file.read()
        k = d.split()
        for i in k:
            if len(i) < 4:
                print('The words with 4 characters is:\n', i)
            else:
                print('Cant find the word we need:\n', i)


display_words()
'''
'''
# 5 Write a python program to read a file, a.txt line by line and write it to another b.txt file.
z = input("Text ")
with open('a.txt', 'r') as a:
    a.read()

    with open('b.txt', 'w') as b:
            b.write(a)
'''

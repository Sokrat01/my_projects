# Perfect coding

def str_1():
    str_inp = (input('Enter the string:\t')).upper()
    if str_inp == str_inp[::-1]:
        print(f'String is palindrome:\t {str_inp}')
    else:
        print(f'String is not palindrome:\t {str_inp}')
        return


str_1()

# 1- import string module
# 2- store all characters in lists (upper/lower case, digits, punctuations)
# 3- take number of characters from user
# 4- make sure the number of characters is 8 or more
# 5- shuffle all lists
# 6- calculate 30% and 20% of number of characters
# 7- create password 60% letters 40% digits and punctuations

import string
import random

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_strong_password():
    
    length = int(input('Enter password Length: '))

    if length < 8:
        print('A strong password should be at least 8 Characters! ')
        length = int(input('\nEnter password Length again: '))

    alphabets_count = int(input('Enter alphabets count: '))
    digits_count = int(input('Enter digits count: '))
    special_characters_count = int(input('Enter special characters count: '))

    characters_count = alphabets_count + digits_count + special_characters_count


    if characters_count > length:
        print('Characters count can not be greater then the password length.')
        return(generate_strong_password())

    password = []


    for i in range(alphabets_count):
        password.append(random.choice(alphabets)) 

    for i in range(digits_count):
        password.append(random.choice(digits))

    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    
    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    
    random.shuffle(password)

    print("".join(password),'\nEnjoy your Strong Password ^-^')

generate_strong_password()

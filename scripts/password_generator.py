#!/usr/local/bin/python3

import random

# The script uses these characters to generate your password(s)
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*().,?'

number = input('Amount of passwords of generate: ')
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nHere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
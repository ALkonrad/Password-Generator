import random

symbols = 'abcdefghijklmnopqrstuvwxyz'
symbols += symbols.upper()
symbols += '0123456789'

password = ''

for full_password in range(3):
    for password_chunk in range(5):
        password += symbols[random.randint(0, len(symbols) - 1)]
    password += '-'

password = password.rstrip('-')
print(password)

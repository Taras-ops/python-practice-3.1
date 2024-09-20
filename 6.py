password = input('Enter a password to validate: ')

numbers = '0123456789'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '$#@'

flag1 = False
flag2 = False
flag3 = False
flag4 = False

for i in password:
    if i in lowercase:
        flag1 = True
    elif i in uppercase:
        flag2 = True
    elif i in numbers:
        flag3 = True
    elif i in symbols:
        flag4 = True

if not flag1:
    print('At least 1 letter between [a-z].')
if not flag2:
    print('At least 1 letter between [A-Z].')
if not flag3:
    print('At least 1 number between [0-9].')
if not flag4:
    print('At least 1 character from [$#@].')
if len(password) < 6:
    print('Minimum length 6 characters.')
if len(password) > 16:
    print('Maximum length 16 characters.')

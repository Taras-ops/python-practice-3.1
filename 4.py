data = input('Enter a string: ')

digit_count = 0
letter_count = 0

numbers = '0123456789'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in data:
    if i in numbers:
        digit_count += 1
    elif i in lowercase or i in uppercase:
        letter_count += 1

print('Letters: ' + str(letter_count))
print('Digits: ' + str(digit_count))

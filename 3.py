numbers = input('Enter numbers with comma between them: ')

arr = numbers.split(',')

even_count = 0
odd_count = 0

for i in arr:
    if int(i) % 2 == 0:
        odd_count += 1
    else:
        even_count += 1

print('Number of even numbers: ' + str(even_count))
print('Number of odd numbers: ' + str(odd_count))
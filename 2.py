word = input('Enter a word: ')

res = ''
i = len(word) - 1

while i >= 0:
    res += word[i]
    i -= 1

print('The result: ' + res)

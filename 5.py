i = 0
res = ''

while i < 6:
    if i == 3:
        i += 1
        continue

    res += str(i) + ' '
    i += 1

print(res)

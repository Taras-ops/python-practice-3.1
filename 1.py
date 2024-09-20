i = 9
j = 1

while i > 0:
    res = ''

    for _ in range(j):
        res += '* '

    if i < 6:
        j -= 1
    else:
        j += 1

    i -= 1
    print(res)

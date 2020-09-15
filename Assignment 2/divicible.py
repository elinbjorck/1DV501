n = 0

def conditions_met(n, i):
    print(i, end=' ')
    n += 1
    if n % 10 == 0:
        print('')
    return n

for i in range(100,201):
    if i % 4 == 0:
        if i % 5 != 0:
            n = conditions_met(n,i)
    elif i % 5 == 0:
        n = conditions_met(n,i)



try:
    integer = int(input('skriv in ett possitivt heltal: '))
    if integer <= 0:
        print('Not possitive')
        exit(0)

except: print('Not an integer'), exit(0)

sigma = 0
k = 2

while sigma < integer:
    sigma += k
    k += 2
# rätt k är det sista där summan är under gränsen. När detta är nått plussar den på 2 på k.
# summan är fortfarande mindre så while loopen 
k -= 4
print(f'Largest k = {k}')
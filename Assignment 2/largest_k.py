try:
    integer = int(input('skriv in ett possitivt heltal: '))
except: print('Inte ett heltal.'), exit(0)

if integer <= 0:
    print('Inte possitivt')
    exit(0)

sigma = 0
k = 2

while sigma < integer:
    sigma += k
    k += 2
# rätt k är det sista där summan är under gränsen. När detta är nått plussar den på 2 på k.
# summan är fortfarande mindre så while loopen 
k -= 4
print(f'Largest k = {k}')
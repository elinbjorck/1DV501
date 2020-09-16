try:
    print('Hi')
    number = int(input('Ge mig ett udda heltal som är possitivt: '))
except: print('Följ instruktionerna ditt as.'), exit(0)

if number < 0:
    print(f'{number} är inte possitivt.')
    exit(0)
if number % 2 == 0:
    print(f'{number} är ett jamnt tal')
    exit(0)

print('wow, du är bra på att göra som du blir tillsagd')
try:
    number = int(input('Ge mig ett udda heltal som är possitivt: '))
except: print('Följ instruktionerna ditt as.'), exit(0)

if number < 0:
    print(f'{number} är inte possitivt.')
    exit(0)
if number % 2 == 0:
    print(f'{number} är ett jamnt tal')
    exit(0)

print('wow, du är bra på att göra som du blir tillsagd')
#allt ovan testar talet som användaren skriver in

for i in range(number):
    print(' '*i+'*'*(number-i))

for i in range (1,number+1,2):
    space = (number-i)//2
    print(' '*space + '*'*i + ' '*space)

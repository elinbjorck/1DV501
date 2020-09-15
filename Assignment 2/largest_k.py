try:
    original = float(input('skriv in ett possitivt heltal: ')) #sparar som float först så att jag kan kolla så de inte skrev in ett decimaltal
    integer = int( original )
    if integer <= 0 or original != integer: exit()

except: print('Please follow the instructions'), exit(0)

sigma = 0
k = 2

while sigma < integer:
    sigma += k
    k += 2
# rätt k är det sista där summan är under gränsen. När detta är nått plussar den på 2 på k.
# summan är fortfarande mindre så while loopen 
k -= 4
print(f'Largest k = {k}')
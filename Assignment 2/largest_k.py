try:
    original = float(input('skriv in ett possitivt heltal: ')) #sparar som float först så att jag kan kolla så de inte skrev in ett decimaltal
    integer = int( original )
    if integer <= 0 or original != integer: exit()

    sigma = 0
    k = 2

    while sigma < integer:
        sigma += k
        k += 2

    k -= 4 # while loopen avbryts när summan blir större än integer. det skedde när k var två stärre än största-k, efter det plussas det på ytterligare 2 på k. 
    print(f'Largest k = {k}')

except: print('Please follow the instructions')
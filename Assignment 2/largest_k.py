integer = int(input('skriv in ett possitivt heltal: '))

sigma = 0
k = 2

while sigma < integer:
    sigma += k
    k += 2

k -= 4 # while loopen avbryts när summan blir större än integer. det skedde när k var två stärre än största k, efter det plussas det på ytterligare 2 på k. 
print(f'Largest k = {k}')
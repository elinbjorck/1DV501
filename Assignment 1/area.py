import math
while True:
    radious = input('Ge mig en radie(cm): ')
    try:
        radious = float(radious)
        break
    except ValueError as error:
        print(f'{error} är inte ett tal')

#area = pi*r^2

area = round(math.pi*radious**2, 1)

print(f'Motsvarande area är: {area}cm^2')
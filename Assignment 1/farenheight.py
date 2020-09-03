f = float(input('Skriv temperaturen i farenheight så att vi kan konvertera den till en vettigare enhet: '))

# F = (9 / 5) * C + 32 => C = (F - 32) * (5 / 9)

c = round((f-32) * (5/9), 1)
print(f'Den vettiga temperaturen är: {c} celcius')
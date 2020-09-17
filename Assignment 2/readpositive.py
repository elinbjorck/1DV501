def is_positive_and_odd(integer):
    return integer>0 and integer % 2 != 0

for i in range(1,6):
    try:
        raw = input(f'Skriv in ett possitivt udda heltal, försök {i}: ')
        tal = int(raw)
    except:
        print(f'{raw} är inte ens ett heltal.')
        continue
    if is_positive_and_odd(tal):
        print(f'wow! {tal} är ett possitivt udda heltal. Efter bara {i} försök... Du är begåvad.')
        exit(0)
    print('Instruktionerna följdes inte.')

print('Jag trodde inte detta skulle vara så svårt')
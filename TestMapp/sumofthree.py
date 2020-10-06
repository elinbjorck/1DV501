while True:
    number = input('skriv ett tresiffrigt tal: ')
    try:
        number = int(number)
        if number < 100 or number > 999:
            print('måste vara ett tresiffrigt tal')
            continue
        break
    except ValueError:
        print('måste vara ett heltal')

digit1 = number//100
digit2 = (number%100)//10
digit3 = number%10

print(f'Sum of digits: {digit1+digit2+digit3}')
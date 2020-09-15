try:
    original = float( input( 'enter a possitive integer: ' ))
    integer = int( original )
    if integer <= 0 or original != integer:
        exit()

    sigma = 0
    k = 1

    while sigma < integer:
        sigma += k
        k+=2
    k -= 2 #den plussar på en till på slutet av varje iteration, så; för att få rätt måste vi ta bort den för att få rött ressultat.
    print(f'smallest k is: {k}')

except ValueError as not_a_number:
    print('Please input a number')

except SystemExit as not_possitive:
    print('Follow instructions and input a possitive integer')


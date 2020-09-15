try:
    integer = int( input( 'Enter a possitive integer: ' ))

    if integer <= 0:
        print('Your input value is not possitive')
        exit(0)

except ValueError as not_a_number:
    print('Please input an integer')
    exit(0)

sigma = 0
k = 1

while sigma < integer:
    sigma += k
    k+=2
k -= 2 #den plussar på en till på slutet av varje iteration, så; för att få rätt måste vi ta bort den för att få rött ressultat.
print(f'smallest k is: {k}')


import sys

try:
    integer = int( input( 'enter a possitive integer: ' ))
    if integer <= 0: 
        sys.exit('please follow the instructions')
except ValueError as not_a_number:
    print('please input a number')
except SystemExit as not_possitive:
    print('follow instructions and input a possitive integer')

sigma = 0
k = 1

while sigma < integer:
    sigma += k
    k+=1
k -= 1 #den plussar på en till på slutet av varje iteration, så; för att få rätt måste vi ta bort den för att få rött ressultat.
print(f'smallest k is: {k}')
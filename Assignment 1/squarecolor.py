identyfyer = input('Enter a chess square identifyer (from a1 to h8)')
letter = identyfyer[0]
number = int(identyfyer[1])

distance_from_a = ord(letter)-ord(a)+1 # Will find the letters distance from a, will give numbers from 0 to 7, then we ad 1 to get numbers from 1 to 8

if distance_from_a % 2 == number % 2:
    prin

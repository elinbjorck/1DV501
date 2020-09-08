from random import randint
current_number = 0
number_of_numbers = 5   # vad är detta för namn?!
sum = 0

print('five random numbers:', end = '    ') #avslutar med ' ' så att den inte ska byta rad
for i in range(number_of_numbers):
    current_number = randint(1,100)
    sum = sum + current_number
    print(current_number, end = '   ')  #avslutar med ' ' så att den inte ska byta rad. gör att jag måste börja printen efter loopen med radbryte

print( f'\nThe sum is: {sum}')
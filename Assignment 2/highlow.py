from random import randint
random_number = randint(1,101)
guess = int(input("I'm thinking of a number between 1 and 100, guess: "))
number_of_guesses = 1

while guess != random_number:
    if guess > random_number: print('To high')
    else: print('To low')
    guess=int(input('Guess again: '))
    number_of_guesses += 1

print(f'You got it right after {number_of_guesses} guesses! Well donne.')
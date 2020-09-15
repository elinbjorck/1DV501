from random import randint
random_number = randint(1,101)
print("I'm thinking of a number between 1 and 100, take a guess!")

for number_of_guesses in range(1,11):
    guess=int(input(f'Guess {number_of_guesses}: '))
    if guess > random_number: print('To high')
    elif guess < random_number: print('To low')
    else: print(f'You got it right after {number_of_guesses} guesses! Well donne.'), exit(0)

print('Over 10 guesses just give up')
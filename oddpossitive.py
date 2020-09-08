from random import randint
number = randint(-10,10)

print(f'The generated number is {number}')

if number % 2 == 0:
    print(f'{number} is even', end = ' ')
else:
    print(f'{number} is odd', end = ' ')


if number < 0:
    print('and negative')
else:
    print('and possitive')
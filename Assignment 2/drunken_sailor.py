from random import randint

def ask_for_possitive_integer(instructions):
    while True:
        try:
            possitive_integer = int(input(instructions))
        except:
            print('Your entery is not an integer')
            continue
        if possitive_integer > 0: break
        print(f'{possitive_integer} is not possitive.')
    return possitive_integer

coordinates = [0, 0]

print('Every number you enter should be a possitive integer.')

size = ask_for_possitive_integer('Enter the size: ')
steps = ask_for_possitive_integer('Enter the number of steps: ')
sailors = ask_for_possitive_integer('Enter the number of sailors: ')

direction = 0
unlucky_bastards = 0

for i in range(sailors):
    for _ in range(steps):
        direction = randint(0,1)
        coordinates[direction] += (-1)**randint(1,2)
        if -size <= coordinates[direction] <= size:
            continue
        unlucky_bastards += 1
        break
    coordinates = [0, 0]

print(f'Out of {sailors} sailors {unlucky_bastards} ({round(100*unlucky_bastards/sailors,2)}%) fell in the water.')





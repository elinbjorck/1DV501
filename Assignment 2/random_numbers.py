from random import randint

def min(list_of_numbers):
    min=list_of_numbers[0]
    for i in list_of_numbers:
        if i<min: min = i
    return min

def max(list_of_numbers):
    max = list_of_numbers[0]
    for i in list_of_numbers:
        if i>max: max = i
    return max

def avrage(list_of_numbers):
    s = 0
    avrg = 0
    for i in list_of_numbers:
        s += i
    avrg = s/len(list_of_numbers)
    avrg = round(avrg,2)
    return avrg

def ask_for_possitive_integer(instructions):
    while True:
        try:
            possitive_integer = int(input(instructions))
        except:
            print('Det du angav var inte ett heltal')
            continue
        if possitive_integer > 0: break
        print(f'{possitive_integer} är inte possitivt.')
    return possitive_integer

def random_list(length):
    randlist = []
    for i in range(length):
        randlist.append(randint(1,100))
    return randlist

amount = ask_for_possitive_integer('Skriv in det antal slumpmässiga nummer som du vill ha: ')

numbers = random_list(amount)

print(f'genererade tal är: {numbers}')
print(f'medeltal, min och max är: {avrage(numbers), min(numbers), max(numbers)}')
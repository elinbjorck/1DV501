def ask_for_integer(message):
    while True:
        try:
            return int(input(message))
        except:
            print('I was exprcting an integer. ')


numbers = []
i = 1

ask_for_integer('Give me an integer: ')

while True:
    number = ask_for_integer(f'Integer {i}: ')
    i += 1
    if number < 0:
        break
    else:
        numbers.insert(0, number)


print(numbers)


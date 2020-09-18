def ask_for_integer(message):
    while True:
        try:
            return int(input(message))
        except:
            print('I was exprcting an integer. ')


numbers = []
i = 1

while True:
    number = ask_for_integer(f'Integer {i}: ')
    if number < 0:
        break
    else:
        numbers.insert(0, number)
    i += 1

print(f'Number of integers: {i-14}')
print(f'In reverse: {numbers}')


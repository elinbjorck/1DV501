try:
    int_string = input('Enter a large possitive integer(at least 4 digits): ')
    length = len(int_string)
    if int(int_string) < 0:
        print('Your number is not possitive')
        exit(0)
    if length < 4:
        print("Your number does'nt have enough digits")
        exit(0)

except ValueError as letter_or_decimal:
    print('Not an integer')
    exit(0)

current_number = 0

odd = 0
even = 0
zero = 0

for i in range(0,length):
    current_number = int(int_string[i])
    if current_number == 0: zero += 1
    elif current_number % 2 == 0: even += 1
    else: odd += 1
print(f'Zeros: {zero}\nOdd: {odd}\nEven: {even}')


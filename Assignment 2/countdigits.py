try:
    integer = input('Enter a large possitive integer(at least 4 digits): ')
    length = len(integer)
    if 0 > int(integer) or int(integer) != float( integer ) or length < 4: exit()
   
except: print('Please follow the instructions'), exit(0)

current_number = 0

odd = 0
even = 0
zero = 0

for i in range(0,length):
    current_number = int(integer[i])
    if current_number == 0: zero += 1
    elif current_number % 2 == 0: even += 1
    else: odd += 1
print(f'Zeros: {zero}\nOdd: {odd}\nEven: {even}')


first_name = input('First name: ')
last_name = input('Last name: ')

short_name = f'{first_name[0]}. '

if len(last_name) < 4:

    short_name = short_name + last_name
else:
    short_name = short_name + last_name[0:4]

print(f'Short name: {short_name}')
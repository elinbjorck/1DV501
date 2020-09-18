import list_functions as lf

random = lf.random_list(10)

print(random)

avrg = lf.average(random)

print(f'the average of our list is: {avrg}')

odd_ball = lf.only_odd(random)

print(f'here are the odd elements in our list: {odd_ball}')

stringy_boi = lf.to_string(odd_ball)

print(f'gere it is as a string: {stringy_boi}')

big_random = lf.random_list(20)
has_1_then_2 = lf.contains(big_random,1,2)

print(f'The list: {big_random}')

if has_1_then_2:
    print('has the numbers 1 and 2 in sequence')
else:
    print('does not have the numbers 1 and 2 in sequence')

definetly_has_1_and_2 = [1,2]

has_1_then_2 = lf.contains(definetly_has_1_and_2,1,2)

print(f'The list: {definetly_has_1_and_2}')

if has_1_then_2:
    print('has the numbers 1 and 2 in sequence')
else:
    print('does not have the numbers 1 and 2 in sequence')

duplicates = lf.has_duplicates(big_random)

print(f'The list: {big_random}')

if duplicates:
    print('Has duplicates')
else:
    print('Does not have duplicates')

definetley_has_duplicates = [1,1]
duplicates = lf.has_duplicates(definetley_has_duplicates)

if duplicates:
    print(f'The list {definetley_has_duplicates} has duplicates.')
else:
    print(f'The list {definetley_has_duplicates} does not have duplicates.')

no_duplicates = [1, 2, 3, 4]
duplicates = lf.has_duplicates(no_duplicates)

if duplicates:
    print(f'The list {no_duplicates} has duplicates.')
else:
    print(f'The list {no_duplicates} does not have duplicates.')
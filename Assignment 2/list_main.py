import list_functions as lf

random = lf.random_list(10)

print(random)

avrg = lf.average(random)

print(f'the average of our list is: {avrg}')

odd_ball = lf.only_odd(random)

print(odd_ball)

stringy_boi = lf.to_string(odd_ball)

print(stringy_boi)

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

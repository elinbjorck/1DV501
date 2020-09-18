import stringfunctions as sf

s = 'hello world'

print(sf.concat(s, 3))
print(sf.count(s, 'l'))
print(sf.reverse(s))
print(f'The first and last letter in {s} is: {sf.first_last(s)}')
if sf.has_two_X(s):
    print(f'{s} has two X')
if sf.has_duplicates(s):
    print(f'{s} has duplicates')

deffinetly_2X = 'XX'
more_than_2X = 'XXX'

if sf.has_two_X(deffinetly_2X):
    print(f'{deffinetly_2X} has two X')
if sf.has_two_X(more_than_2X):
    print(f'{more_than_2X} has two X')
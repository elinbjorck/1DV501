integers = [0, 0, 0]
letters = ['A', 'B', 'C'] #kommer spara i listor ocxh iterera över dem. kanske är onödigt när det är så få, men går jag så här kan jag lätt lägga till fler. 
largest = 0

print('Please input 3 integers A, B, C')

for i, letter in enumerate(letters):
    integers[i] = int( input(f'Enter {letter}: '))

for i, number in enumerate(integers):
    if number > largest:
        largest = number

print(f'Largest number is:  {largest}')

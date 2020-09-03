savings = int(input('skriv in dina pengar (som ett heltal): '))
interest = int(input('Ge mig din renta (som ett heltal): '))
p = 1 + interest/100        # förändringsfaktor
y = 5       # years

# värde efter y år: S * P^5y

savings = round( savings * p**y )
print( f'efter {y} år har du sparat: {savings}')
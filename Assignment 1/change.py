price = float(input('Vad kostar det du betalar för?: '))
pay = int(input('Hur mycket pengar lämnade du fram?: '))
amount = 0 # the amount of bills needed of the current type
bills =[1000, 500, 200, 100, 50, 20, 10, 5, 1] 
change = pay-price

for i, bill in enumerate(bills):
    amount = int(change//bill)
    change = change%bill
    if amount == 1: #lite if satser för att printa rätt ord så att meningarna låter bra. behövs inte egentligen.
        if bill > 10:
            print(f'{amount} {bill}-lapp.')
        else:
            print(f'{amount} {bill}-krona.')
    else:
        if bill > 10:
            print(f'{amount} {bill}-lappar.')
        else:
            print(f'{amount} {bill}-kronor.')

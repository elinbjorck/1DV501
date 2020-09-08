price = 0
pay = 0 #what the person payed with
amount = 0 # the amount of bills needed of the current type
bills =[1000, 500, 200, 100, 50, 20, 10, 5, 1]
change = price-pay
for i, bill in enumerate(bills):
    amount = change//bill
    change = change%bill
    if bill>10:
        print(f'{amount} stycken {bill}lapp.')
    else:
        print(f'{amount} stycken {bill}krona.')

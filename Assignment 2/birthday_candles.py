candles_left = 0
total_amount_of_boxes = 0
buy = 0
candles_in_box = 24

for age in range(1,101):
    while True:
        if candles_left < age:
            buy += 1
            candles_left += candles_in_box
        else:
            break
    total_amount_of_boxes += buy

    candles_left -= age

    if buy != 0:
        print(f'köp {buy} lådor, innan du fyller {age}')
    buy =0

print(f'Totalt antal lådor: {total_amount_of_boxes}, ljus kvar: {candles_left}, vila i frid.')


from random import randint

def contains(list, value):
    """returns true if 'list' contains 'value'"""
    for thing in list:
        if thing == value:
            return True
    return False
start = 1
stop = 35
lottery_numbers = [randint(start,stop)]
current = 0

for i in range(6):
    current = randint(start,stop)
    while contains(lottery_numbers, current):
        current = randint(start,stop)
    lottery_numbers.append(current)

print(lottery_numbers)
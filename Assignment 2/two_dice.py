
from random import randint

def throwdice():
    return randint(1,6)

ressult = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10000):
    dice_sum = throwdice()+throwdice()
    ressult[dice_sum-2] += 1

current = 2
for i in ressult:
    print(f'{current}: {i}')
    current += 1

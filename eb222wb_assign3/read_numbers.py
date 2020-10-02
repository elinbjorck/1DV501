from math import sqrt
import os

def mean(lst):
    _sum = 0
    for i in lst:
        _sum += i

    return _sum/len(lst)

def std(lst):
    mean_value = mean(lst)
    _sum = 0
    for i in lst:
        _sum += (i-mean_value)**2
    return sqrt(_sum/len(lst))


test_list = [1,6,5,7,4,3,9]
print(mean(test_list))
print(std(test_list))

path = os.getcwd()
print(path)
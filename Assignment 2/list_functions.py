from random import randint

def random_list(n):
    lst = []
    for i in range(n):
        lst.append(randint(1,100))
    return lst
def average(lst):
    sum_ = 0
    for n in lst:
        sum_ += n
    return round(sum_/len(lst))

def only_odd(lst):
    odd_list = []
    for n in lst:
        if n % 2 == 1:
            odd_list.append(n)
    return odd_list

def to_string(lst):
    str_ = ''
    for n in lst:
        str_ += f'{str(n)}, '
    return str_
def contains(lst, a, b):
def has_duplicates(lst):
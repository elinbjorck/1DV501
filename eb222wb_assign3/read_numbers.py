from math import sqrt
import os

PATH_FILE_A = os.getcwd()+'/eb222wb_assign3/10000_integers/file_10000integers_A.txt'
PATH_FILE_B = os.getcwd()+'/eb222wb_assign3/10000_integers/file_10000integers_B.txt'

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

def file_to_int_list(path, separator):
    int_list = []
    with open(path, 'r') as file_:
        for line in file_:
            for i in line.split(separator):
                int_list.append(int(i))
    return int_list

A_list = file_to_int_list(PATH_FILE_A,',')
B_List = file_to_int_list(PATH_FILE_B,':')
print(mean(A_list))
print(std(A_list))
print(mean(B_List))
print(std(B_List))
path = os.getcwd()
print(path)
import os

PATH_FILE_A = os.getcwd()+'/eb222wb_assign3/10000_integers/file_10000integers_A.txt'
PATH_FILE_B = os.getcwd()+'/eb222wb_assign3/10000_integers/file_10000integers_B.txt'

def file_to_int_list(path, separator):
    int_list = []
    with open(path, 'r') as file_:
        for line in file_:
            for i in line.split(separator):
                int_list.append(int(i))
    return int_list

def count_different(lst):
    number_set = set(lst)
    print(len(number_set))

def count_ocurances(lst):
    ocurances = {}
    for number in lst:
        ocurances[str(number)] = 0
    for number in lst:
        ocurances[str(number)] += 1
    print(ocurances)


test_list = [1, 3 , 6, 6, 7, 8, 4, 4]

count_different(test_list)
count_ocurances(test_list)
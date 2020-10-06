import os

PATH_FILE_A = os.getcwd()+'/10000_integers/file_10000integers_A.txt'
PATH_FILE_B = os.getcwd()+'/10000_integers/file_10000integers_B.txt'

def file_to_int_list(path, separator):
    """reads a file and turnes it in to a list of integers. The file needs to contain only integers separated by a 'separator'"""
    int_list = []
    try:
        with open(path, 'r') as file_:
            for line in file_:
                for i in line.split(separator):
                    int_list.append(int(i))
        return int_list
    except FileNotFoundError as error:
        print('The file can not be found', error)
        exit(0)
    except TypeError as error:
        print(error, 'the file contained something other than integers and separators.' )
        exit(0)

def count_different(lst):
    number_set = set(lst)
    print(len(number_set))

def count_ocurances(lst):
    ocurances = {}
    for number in lst:
        ocurances[str(number)] = ocurances.get(str(number), 0)+1
    print(ocurances)

a_list = file_to_int_list(PATH_FILE_A, ',')

count_different(a_list)
count_ocurances(a_list)
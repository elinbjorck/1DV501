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
    pass

def count_ocurances(lst):
    pass

test_list[1, 3 , 6, 6, 7, 8, 4, 4]
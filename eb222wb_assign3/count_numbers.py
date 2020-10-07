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
    except ValueError as error:
        print(f'The file contained something other than integers and separators: {error}' )
        exit(0)

def count_different(lst):
    number_set = set(lst)
    return len(number_set)

def count_ocurances(lst):
    ocurances = {}
    for number in lst:
        ocurances[str(number)] = ocurances.get(str(number), 0)+1
    return ocurances

def most_common(dict):
    '''returns a list [key,value] with the element in the dictionary with the highest value. '''
    largest = [0,'']
    for key, value in dict.items():
        if value > largest[0]:
            if len(largest) > 2:
                largest = [value,key]

            largest[0] = value
            largest[1] = key

        elif value == largest[0]:
            largest.append(key)

    return largest



a_list = file_to_int_list(PATH_FILE_A, ',')
common_a = most_common(count_ocurances(a_list))
b_list = file_to_int_list(PATH_FILE_B, ':')
common_b = most_common(count_ocurances(b_list))

print(f'The amount of different numbers in file A: {count_different(a_list)}')
print(f'The most common number in A is: {common_a[1:]} with {common_a[0]} ocurances')

print(f'The amount of different numbers in file B: {count_different(b_list)}')
print(f'The most common number in B is: {common_b[1:]} with {common_b[0]} ocurances')

test_list = [2,1,5,5,5,6,6,6,7,8,8] #testar om most_common kan spara ner flera värden ifall det finns dubletter.
largest_test = most_common(count_ocurances(test_list))[1:]
print(largest_test)
from list_functions import average

def median(list_):
    list_.sort()
    length = len(list_)
    if length%2 == 0:
        return average([list_[length//2-1], list_[length//2]])
    else:
        return list_[length//2]
def gap(list_):
    list_.sort()
    length = len(list_)
    return list_[length-1]-list_[0]

salaries = input('Enter salaries sepparated with a space: ')
salaries = salaries.split(' ')
salarie_list=[]
for salarie in salaries:
    try:
        salarie_list.append(int(salarie))
    except:
        continue

print(f'Median: {median(salarie_list)}')
print(f'Average: {average(salarie_list)}')
print(f'Gap: {gap(salarie_list)}')
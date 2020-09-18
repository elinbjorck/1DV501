from list_functions import average

def mean(list_):
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

test = [1,8,9,3,2,7]

print(test)
print(average(test))
print(mean(test))
print(gap(test))
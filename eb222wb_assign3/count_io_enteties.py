import os

def count_directories(dir_path):
    enteries = os.scandir(dir_path) #skapar en lista med allt som finns i mappen
    total = 0
    for _ in enteries: #går igenom allt som finns i listan
        total += 1  #räknar varje element
    return total

def count_py_files(dir_path):
    enteries = os.scandir(dir_path)
    total = 0
    for entery in enteries:
        if entery.name.endswith('py'): # kollar om namnet slutar på py -----> pytonfil
            total += 1  #räknar varje pythonfil
    return total
    
path = 'C:\\Users\\elinb\Documents\\TestMapp'          # Path pointing to directory containing other directories
print("Dir Count:", count_directories(path))
     
print("Py-file Count:", count_py_files(path))
import os
PATH = os.getcwd() + '/testMapp'

def count_directories(dir_path):

    try:
        enteries = os.scandir(dir_path) #skapar en lista med allt som finns i mappen
        total = 0
        for entery in enteries: #går igenom allt som finns i listan
            if entery.is_dir():
                total += 1  #räknar varje element
        return total
    except FileNotFoundError:
        print(f'Mappen "{PATH}" du försöker öppna finns inte.')
        exit(0)

def count_py_files(dir_path):
    try:
        enteries = os.scandir(dir_path)
        total = 0
        for entery in enteries:
            if entery.name.endswith('py'): # kollar om namnet slutar på py -----> pytonfil
                total += 1  #räknar varje pythonfil
        return total
    except FileNotFoundError:
        print(f'Mappen "{PATH}" du försöker öppna finns inte.')
        exit(0)

print("Dir Count:", count_directories(PATH))
     
print("Py-file Count:", count_py_files(PATH))
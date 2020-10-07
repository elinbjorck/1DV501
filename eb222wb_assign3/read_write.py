import os
def read_file(file_path):
    try:
        _file = open(file_path, 'r')
        lines = []
        for line in _file:
            lines.append(line)
        _file.close()
    except FileNotFoundError:
        print('the file did not exist')
    return lines 

def write_file(lines, file_path):
    
    _file = open(file_path, 'w')
    _file.writelines(lines)
    _file.close

_path = os.getcwd() + '/TestMapp/testTextFil.txt'

read = read_file(_path)

write_file(read, _path.replace('.','1.'))


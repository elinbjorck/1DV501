import os
def read_file(file_path):
    _file = open(file_path, 'r')
    lines = []
    for line in _file:
        lines.append(line)
    _file.close()
    return lines 

def write_file(lines, file_path):
    _file = open(file_path, 'w')
    _file.writelines(lines)
    _file.close

_path = 'C:\\Users\\elinb\\Documents\\TestMapp\\testTextFil.txt'

read = read_file(_path)

write_file(read, _path.replace('.','1.'))


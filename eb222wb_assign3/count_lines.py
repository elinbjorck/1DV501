import os

dir_path = os.getcwd()

def count_lines(file_path):
    lines = 0
    with open(file_path,'r',encoding='utf8') as python_file:
        for line in python_file:
            if line.strip():
                lines += 1
    return lines

def count_py_lines(path):
    directory_content = os.scandir(path)
    total_lines = 0
    for content in directory_content:
        if content.name.startswith('.'):
            continue
        elif content.is_dir():
            total_lines += count_py_lines(content.path)
        elif content.name.endswith('.py'):
            total_lines += count_lines(content.path)
    return total_lines

print(count_py_lines(dir_path))

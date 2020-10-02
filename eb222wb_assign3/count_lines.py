import os

path_current = os.getcwd()

print(path_current)

itterator_thing = os.scandir(path_current)
path_list =[]
for thing in itterator_thing:
    print(thing)
    if thing.is_dir():
        path_list.append(thing.path)
print(path_list)

def dir_digger(path):
    directory_content = os.scandir(path)
    for content in directory_content:
        if content.is_dir:
            dir_digger(content.path)
        elif content.name.endswith('.py'):
            print(content.name)

dir_digger(path_current)

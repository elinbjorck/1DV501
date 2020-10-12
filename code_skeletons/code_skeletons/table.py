# A binary search based dictionary imlementation 
# only using list of length 4.

# Each node is a list of length four where positions
# 0 = key, 1 = value, 2 = left-child, 3 = right-child


# Creates and returns the root to a new empty table.
# The complete function is given and should not be changed.
def new_empty_root():
    return [None,None,None,None]

# Add a new key-value pair to table if the key doean't already exist.
# Update value if already key exists in the table.
def add(root,key,value):
    if root[0] == None:
        root[0] = key
        root[1] = value
    elif key < root[0]:
        if root[2] == None:
            root[2] = new_empty_root()
        add(root[2], key, value)
    elif key > root[0]:
        if root[3] == None:
            root[3] = new_empty_root()
        add(root[3], key, value)
    else:
        root[1] = value



# Returns a string representation of the table content.
# That is, all key-value pairs
def to_string(node):
    dict_string = ''
    if node[2] != None: 
        dict_string += to_string(node[2])
    dict_string += f', {node[0]} : {node[1]}'
    if node[3] != None:
        dict_string += to_string(node[3])
    return dict_string


# Returns the value for the given key. Returns None if key doesn't exists.
def get(node,key):
    if key < node[0]: 
        if node[2] == None:
            return None
        return get(node[2],key)
    if key > node[0]:
        if node[3] == None:
            return None
        return get(node[3],key)
    else:
        return node[1]

# Returns the maximum depth (an integer) of the tree.
# That is, the length of longest root-to-leaf path.
def max_depth(node):
    pass

# Returns the number og key-value pairs currently stored in the table
def count(node):
    return len(get_all_pairs(node)) # slött att använda gap. gör om. 

# Returns a list of all key-value pairs as tuples 
# sorted as left-to-right, in-order
def get_all_pairs(root):
    dict_list = [] # ändra till loop, denna gör en ny lista för varje gång den går in ett steg i funktionen
    if root[2] != None:
        dict_list += get_all_pairs(root[2])
    dict_list.append((root[0], root[1]))
    if root[3] != None:
        dict_list += get_all_pairs(root[3])
    return dict_list

root = new_empty_root()

add(root,4,2)
add(root, 6,8)
add(root,2,9)
add(root,8,6)
add(root,3,9)
print(root)
print(to_string(root))
print(get(root,6))
print(get_all_pairs(root))
print(count(root))
#hej
# A list based hash table implementation for strings.
# Initial bucket size is 10, we the double the bucket size
# when nElements = bucketSize.

size = 0      # global variable, current number of elements

# Returns a new empty set
# The complete function is given and should not be changed.
def new_empty_set():
    global size
    size = 0
    buckets = []
    for i in range(10):
        buckets.append([])
    return buckets


# Adds word to word set if not already added
def add(word_set, word):
    pass

# Returns current number of elements in set
def count(word_set):
    pass

# Returns current size of bucket list
def bucket_list_size(word_set):
    pass

# Returns a string representation of the set content
def to_string(word_set):
    pass

# Returns True if word in set, otherwise False    
def contains(word_set, word):
    pass

# Removes word from set if there, does nothing 
# if word not in set
def remove(word_set, word):
    pass

# Returns the size of the bucket with most elements
def max_bucket_size(word_set):
    pass




    



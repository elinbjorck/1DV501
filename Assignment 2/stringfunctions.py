def concat(s, n):
    return s*n

def count(s,x):
    x_count = 0
    for character in s:
        if character == x:
            x_count += 1
    return x_count

def reverse(s):
    rev = ''
    for character in s:
        rev = character + rev
    return rev

def first_last(s):
    first = s[1]
    last = s[len(s)-1]
    return first, last
def has_two_X(s):
    s=s
def has_duplicates(s):
    s=s

s = 'hello world'

print(concat(s, 3))
print(count(s, 'l'))
print(reverse(s))
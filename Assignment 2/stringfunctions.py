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
    first = s[0]
    last = s[len(s)-1]
    return first, last

def has_two(s,x):
    return count(s,x) == 2

def has_two_X(s):
    return has_two(s,'X')

def has_duplicates(s):
    for character in s:
        if has_two(s,character):
            return True
    return False

s = 'hello world'

print(concat(s, 3))
print(count(s, 'l'))
print(reverse(s))
print(first_last(s))
print(has_two_X(s))
print(has_duplicates(s))
print(has_two_X('XXi'))
print(has_two_X('XXX'))
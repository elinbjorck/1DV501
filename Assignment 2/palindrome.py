def remove_all_but_small(string_):
    for i in range(32, 97):
        string_ = string_.replace(chr(i), '')
    for i in range(123, 127):
        string_=string_.replace(chr(i), '')
    return string_

def is_palindrome(string_):
    string_ = string_.lower()
    string_ = remove_all_but_small(string_)
    length = len(string_)
    stop = length//2
    for i  in range(stop):
        is_same = string_[i] == string_[length-(i+1)]
        if is_same: continue
        return False
    return True

palindrome = 'A nut for a jar of tuna.'

if is_palindrome(palindrome):
    print(f'{palindrome} is a palindrome')

not_palindrome='Elin björck'

if not is_palindrome(not_palindrome):
    print(f'{not_palindrome} is not a palindrome')

test_string = '1 råtta är bättre än 7!?<>][jesus'

print(test_string)
print(remove_all_but_small(test_string))
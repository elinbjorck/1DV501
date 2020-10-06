import os
import time

PATH_NEWS = os.getcwd()+'/large_texts.txt/eng_news_100k-sentences.txt'
PATH_GRAIL = os.getcwd()+ '/large_texts.txt/holy_grail..txt'
PATH_TEST = os.getcwd()+'/testMapp/testTextFil.txt'

#instead of leting each star represent a number of occurances I set the size I want for 
# the histogram(histogram_size) and then create a scaling factor that makes the largest column conform to that size
histogram_size = 50

def largest(dict):
    '''compares the values in a dictionary and returns the largest. 
    here we use it to make a scaling factor when we print the histogram'''
    largest = 0
    for i in dict.values():
        if i > largest:
            largest = i
    return largest

def print_histogram(dict):
    '''prints a histogram based on a dictionary'''
    largest_occurance =largest(dict)
    scaling_factor = histogram_size/largest_occurance
    for key, occurance in dict.items():
        print(f'{key} | {"*" * round(occurance*scaling_factor)}') 
    print(f'Largest column represent {largest_occurance} letters')

def count_letters(path):
    '''reads from a file and counts the letters. The method 'dict.get(key,default)' that will return 
    default if the keydoes not exist, is used so we are safe in the cases were the letter has not been added yet'''

    letters = {}
    if not os.path.exists(path):
        print(f'The path: {path} does not exist')
        exit(0)
    with open(path, 'r', encoding='utf8') as file:
        for line in file:
            for character in line.lower():
                if ord('a') <= ord(character) <= ord('z'):

                    #The method 'dict.get(key,default)' that will return 
                    #default if the key does not exist, is used so we are 
                    #safe in the cases were the letter has not been added yet
                    letters[character] = letters.get(character,0) + 1 

    return letters

def count_letters1(path):
    '''same as count letters, but I thought that this might be faster. 
    instead of using 'dict.get(key,default)' that checks if the key exist everytime we use it,
    we initie a dictionary with all the letters before, that way we can just 
    add to the existing key:value pairs. this way it is also sorted from the start. With limited testing 
    the time difference seamed very small'''
    letters = {}

    for i in range(ord('a'), ord('z')+1): #initiating a dictionary with all letters paired with the value 0
        letters[chr(i)] = 0

    if not os.path.exists(path):
            print(f'The path: {path} does not exist')
            exit(0)
    with open(path, 'r', encoding='utf8') as file:
        for line in file:
            for character in line.lower():
                if ord('a') <= ord(character) <= ord('z'):
                    letters[character] += 1

    return letters
                
letters_news = count_letters1(PATH_NEWS)
letters_python = count_letters(PATH_GRAIL)

print('Letter count in the news:')
print_histogram(letters_news)
print('Letter count in the holy grail:')
print_histogram(letters_python)




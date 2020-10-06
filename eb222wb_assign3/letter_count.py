import os

PATH_NEWS = os.getcwd()+'/large_texts.txt/eng_news_100k-sentences.txt'
PATH_GRAIL = os.getcwd()+ '/large_texts.txt/holy_grail.txt'
PATH_TEST = os.getcwd()+'/testMapp/testTextFil.txt'
X = 10000
STAR = '*'
def print_histogram(dict):
    for key, occurance in dict.items():
        print(f'{key} | {STAR * (occurance//X)}')

def count_letters(path):
    for i in range()
    letters = {}
    with open(path, 'r', encoding='utf8') as file:
        for line in file:
            for character in line.lower():
                if ord('a') <= ord(character) <= ord('z'):
                    letters[character] = letters.get(character,0) + 1
    return letters
                
letters = count_letters(PATH_NEWS)
print_histogram(letters)


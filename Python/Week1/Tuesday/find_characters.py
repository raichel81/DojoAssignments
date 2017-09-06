'''Assignment: Find Characters
Write a program that takes a list of strings 
and a string containing a single character, 
and prints a new list of all the strings containing 
that character.'''

word_list = ['hello','world','my','name','is','Anna']
char = 'o'


def find_characters(word_list,char):
    new_list = []
    for string in word_list:
        if char in string:
            new_list.append(string)
        else:
            continue
    print new_list

find_characters(word_list,char)


'''Assignment: Compare Lists
Write a program that compares two lists and prints a message 
depending on if the inputs are identical or not.

Your program should be able to accept and compare two lists:
list_one and list_two. If both lists are identical 
print "The lists are the same". If they are not identical 
print "The lists are not the same." Try the following test 
cases for lists one and two:

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
'''
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

def compare_lists(list_one,list_two):
    if list_one == list_two:
        print "The lists are the same"
    else:
        print "The lists are not the same"
        
compare_lists(list_one,list_two)

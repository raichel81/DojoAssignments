'''Assignment: Type List
Write a program that takes a list and prints a message for 
each element in the list, based on that element's data type.


Your program input will always be a list. For each item 
in the list, test its data type. If the item is a string, 
concatenate it onto a new string. If it is a number, 
add it to a running sum. At the end of your program 
print the string, the number and an analysis of what the 
list contains. If it contains only one type, print that type,
otherwise, print 'mixed'.'''

def type_list(list):
    int_list = []
    str_list = []
    for element in list:
        if isinstance(element,int):
            int_list.append(element)
        else:
            str_list.append(element)
    if len(int_list) <= 0:
        print "The list you entered is of string type"
        print "String: ", ' '.join(str_list) 
    elif len(str_list) <= 0:
        print "The list you entered is of integer type"
        print "Sum: " , sum(int_list)
    else:
        print "The list you entered is of mixed type"
        print "Sum: " , sum(int_list)
        print "String: ", ' '.join(str_list) 

type_list([34, 1, "apple", 2,"dog"])
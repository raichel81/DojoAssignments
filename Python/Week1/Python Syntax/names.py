'''Assignment: Names
Write the following function.

Part I
Given the following list:
'''
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
'''
Create a program that outputs:

Michael Jordan
John Rosales
Mark Guillen
KB Tonel
'''
def prints_names(list):
    for value in list:
        print value['first_name'] + " " + value['last_name']

prints_names(students)
'''
Part II
Now, given the following dictionary:
'''
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
'''
Create a program that prints the following format 
(including number of characters in each combined name):
'''
def name_count(dict):
    for key, list in dict.items():
        print key
        for i, value in enumerate(list, start=1):
            print i, "-", value['first_name'].upper(), value['last_name'].upper(), "-", len(value['first_name']+value['last_name']) 
name_count(users)

'''
Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13

Note: The majority of data we will manipulate as 
web developers will be hashed in a dictionary using 
key-value pairs. Repeat this assignment a few times to 
really get the hang of unpacking dictionaries, as it's a 
very common requirement of any web application.'''
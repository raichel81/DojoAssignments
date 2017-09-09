'''Assignment: Checkerboard
Write a program that prints a 'checkerboard' 
pattern to the console.

Your program should require no input and 
produce console output that looks like so:'''

'''* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *'''
import sys

for i in range(0, 8):
    if(i % 2):
        sys.stdout.write(' ')
    print('* * * *')


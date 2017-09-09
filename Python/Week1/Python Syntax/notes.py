
The following is a list of commonly used string methods:

string.count(substring): returns number of occurrences of substring in string.

string.endswith(substring): returns a boolean based upon whether the last characters 
of string match substring.

string.find(substring): returns the index of the start of the first occurrence of substring 
within string.

string.isalnum(): returns boolean depending on whether the string's length is > 0 
and all characters are alphanumeric (letters and numbers only). 
Strings that include spaces and punctuation will return False for this method. 
Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. 
All return booleans.

string.join(list): returns a string that is all strings within our set (in this case a list) 
concatenated.

string.split(): returns a list of values where string is split at the given character. 
Without a parameter the default split is at every space.

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

x = "Hello World"
print x.upper()
# output:
"HELLO WORLD"

x = [1,2,3,4,5]
x.append(99)
print x
#the output would be [1,2,3,4,5,99]

enumerate(sequence) used in a for loop context to return two-item-tuple for each item 
in the list indicating the index followed by the value at that index.

map(function, sequence) applies the function to every item in the sequence you pass in. 
Returns a list of the results.

.min(sequence) returns the lowest value in a sequence.

sorted(sequence) returns a sorted sequence

list.extend(list2) adds all values from a second sequence to the end of the original sequence.

list.pop(index) remove a value at given position. if no parameter is passed, 
defaults to final value in the list.

list.index(value) returns the index position in a list for the given parameter.

if age >= 18:
  print 'Legal age'
elif age == 17:
  print 'You are seventeen.'
else:
  print 'You are so young!'

  my_list = [4,'dog',99,['list','inside','another'],'hello world!']
  for element in my_list:
      print element

.replace()

.min()

.max()

.sort()

.len()
my_list = [1, 'Zen', 'hi']
print len(my_list)
# output
3


#Regular expression in python


import re
pattern=r"Python"
text='''Regular expressions are a powerful tool 
for working with strings and text data in Python.
Whether you're matching patterns, replacing text, 
or extracting information, regular expressions 
make it easy to perform complex string operations 
with just a few lines of code. With a little bit 
of practice, you'll be able to use regular 
expressions to solve all sorts of string-related 
problems in Python.
'''
match=re.search(pattern,text)
print(match)

import re
# Define a regular expression pattern
pattern = r"expression"

# Match the pattern against a string
text = r"Hello, world!"

match = re.search(pattern, text)

if match:
    print("Match found!")
else:
    print("Match not found.")
    
import re
pattern = r"cat"
text = "The cat is in the hat."
matches = re.findall(pattern, text)
print(matches)

import re
pattern = r"[a-z]+at"
text = "The cat is in the hat."

matches = re.findall(pattern, text)

print(matches)
# Output: ['cat', 'hat']

new_text = re.sub(pattern, "dog", text)

print(new_text)



import re
pattern=r"[A-Z]+ython"
text='''Regular expressions are a powerful tool 
for working with strings and text data in Python.
Whether you're matching patterns, replacing text, 
or extracting information, regular expressions 
make it easy to perform complex string operations 
with just a few lines of code. With a little bit 
of practice, you'll be able to use regular 
expressions to solve all sorts of string-related 
problems in Python and Cython.
'''
# match=re.search(pattern,text)
# print(match)

matches=re.finditer(pattern,text)
for match in matches:
   print(match) 
   print(match.span())
   print(text[match.span()[0]:match.span()[1]])



import re

text = "The email address is example@example.com."

pattern = r"\w+@\w+\.\w+"

match = re.search(pattern, text)

if match:
    email = match.group()
    print(email)


#Find out all information about google

# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE 
#     to match.
# ()  Enclose a group of REs

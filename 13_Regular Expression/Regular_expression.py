"""
Regular Expression is a tool for matching patterns in text.
 With the help of regular expression we can find,
 match and replace text in string.
"""

import re

str='Data Science with python'
print(re.findall('[a-z]+',str))

s=re.compile('[a-t]')
print(s.findall("Hello"))    

s='Data Science with python'
print(re.findall(r"\b\w{6}\b",s))


print(re.findall(r"\b\w{1,4}\b",s))



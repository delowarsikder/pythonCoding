# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 23:17:40 2020

@author: DelowaR
"""
text='Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'
text='Text is a common form of data, and Python comes with many helpful string methods to process the text stored in string values. You will make use of indexing, slicing, and string methods in almost every Python program you write'
import pyperclip
#text = pyperclip.paste()
pyperclip.copy(text)
t=pyperclip.paste()
lines = t.split('\n')
print('lines :\n')
print(lines)
print('adding bullet point :\n')
for i in range(len(lines)):
    lines[i]='*'+lines[i]
t='\n'.join(lines)
print(t)    
    
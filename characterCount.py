# -*- coding: utf-8 -*-
#explanation https://stackoverflow.com/questions/46506629/how-does-dict-setdefault-count-the-number-of-characters
"""
Created on Mon Feb 17 19:58:45 2020

@author: DelowaR
"""
'''
spam = {'name': 'Pooka', 'age': 5}

#if 'color' not in spam:
#    spam['color'] = 'black'
spam['color']='red'
spam['color']='black'#replace value but i want to check the color value exit or not in dictionary
spam.setdefault('color','white') #just like to if condition

print(spam)
'''

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for charecter in message:
    count.setdefault(charecter,0)
    count[charecter]+=1
#    print(count[charecter])
#print(count) 
print('use pprint to print')
pprint.pprint(count)

print('use pformat to print')
print(pprint.pformat(count))
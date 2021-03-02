# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:15:00 2020

@author: DelowaR
"""
'''
li=['cat','rat','dog','bats']
print('convert string to list:')
print(str(li))
st='_'.join(li)
print(st)

name='kuet,cse,2k16'
name=name.split(',')
print(name)'''

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''

print('Before spliting :\n',spam)
spam=spam.split('\n')
print('After spliting :\n',spam)
# spling is a method which can convert string to list

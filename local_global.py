# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 23:52:43 2020

@author: DelowaR
"""
'''def spam():
    eggs = 'spam' # this is the global
def bacon():
    eggs = 'bacon' # this is a localFunctions 71
def ham():
    print(eggs) # this is the global
eggs = 42 # this is the global
spam()
print(eggs)'''
def spam():
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)
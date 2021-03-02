# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 01:25:51 2020

@author: DelowaR
"""
'''
def spam(number):
    try:
        return 21/number
    except:
        print('Error : Invalid argument')
        
print(spam(3))
print(spam(0))
print(spam(7))'''        

#another process
def spam(number):
    return 21/number

try:
    print(spam(3))
    print(spam(0))
    print(spam(7))
except ZeroDivisionError:
    print('Error :Invalid argument')        
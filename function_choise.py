# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:41:24 2020

@author: DelowaR
"""

#import random

def check_number(n):
    if n==1:
        print('you pressed one')
    elif n==2:
        print('you pressed two')
    elif n==3:
        print('you pressed three')
    elif n<1:
        print('your input below one')
    elif n>3:
        print ('your input above three')
    else:
        print('invalid input')

#r =random.randint(1,3);
while True:
    print('pressed your choise  between 1 and 3 ')        
    s=int(input())
    check_number(s)

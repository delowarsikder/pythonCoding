# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:25:40 2020

@author: DelowaR
"""
import sys
true=True
while(true):
    print('Enter your valid number:')
    number=int(input())
    print('Your Obtain grade is:')
    if number>80 and number<=100:
        print('A+')
    elif number>=70 and number<=79:
        print('A')
    elif number>=60 and number<=69:
        print('A-')
    elif number>=50 and number<=59:
        print('B')
    elif number>=40 and number<=49:
        print('C')
    elif number>=33 and number<=39:
        print('D')
    elif number>=0 and number<=32:
        print('F')
    else:
        print('invalid input')
    print('do you want do search again ?')
    print('please input y for yes or n for not')
    y=input()
    if y=='y':
      true=True
    else:
        sys.exit()
     

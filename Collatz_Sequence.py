# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 01:45:21 2020

@author: DelowaR
"""

def collatz(number):
        if number%2==0:
            print(number//2)
        elif number%2!=0:
            print(number*3+1)
        
        
print('Enter number:')
while True:
    try:
        i=int(input())
        if(i==2):
            collatz(i)
            break
        collatz(i)
    except:
        print('Error: Invalid input')
        
  
        
        

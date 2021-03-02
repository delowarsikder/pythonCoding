# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 01:27:20 2020

@author: DelowaR
"""
import random
#import sys
secret_number=random.randint(1,20)
print('I am thinking a number between 1 and 20.')
#while True:
#Ask the player to guess 6 time
for guessTaken in range(1,7):
    print('Take a guess .')
    i = int(input())
    if secret_number==i:
        print('Good job! You guessed my number in'+str(i) +'guess')
#        sys.exit()
        break
    elif secret_number<i:
        print('Your Guess is too low')
    elif secret_number>i:
        print('Your Guess is too high')
    
if guessTaken == secret_number:
    print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secret_number))

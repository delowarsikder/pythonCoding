# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 23:16:58 2020

@author: DelowaR
"""
theBoard={'top-L' : ' ','top-M' : ' ','top-R' : ' ',
          'mid-L' : ' ','mid-M' : ' ','mid-R' : ' ',
          'low-L' : ' ','low-M' : ' ','low-R' : ' '}
    
def printBoard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])
    
turn='x'

for i in range(9):
    print(theBoard)
    print('turn for '+turn+' . move on which space ?')
    move=input()
    theBoard[move]=turn
    if turn == 'x':
        turn='o'
    else:
        turn='x'
    printBoard(theBoard)    

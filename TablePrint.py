# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 00:02:31 2020

@author: DelowaR
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    maxLen=-1
    for i in range(len(data)):
        for j in range(len(data[i])):
            if(len(data[i][j])>maxLen):
                maxLen=len(data[i][j])
    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].rjust(maxLen),end=' ')
        print(end='\n')    
#    print(len(data[0]))
        
printTable(tableData)        

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:36:17 2020

@author: DelowaR
"""
picnicItem={'apple':5,'egg':2,'milk':1}

print('I am bringing '+ str(picnicItem.get('bergur',0))+' liters')
#print('I am bringing '+ str(picnicItem['bergur'])+' liters')
print('I am bringing '+ str(picnicItem.get('milk',0))+' liters')
print('I am bringing '+ str(picnicItem.get('mango',0))+' liters')
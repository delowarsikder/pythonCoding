# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 23:41:15 2020

@author: DelowaR
"""

def eggs(someThing):
    someThing.append('world')
    
li=['a',1,'hello']
print(type(li))
eggs(li)
print(li)
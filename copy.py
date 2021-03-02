# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 01:17:57 2020
@author: DelowaR
"""

import copy
spam=['a','b','c','d']

cheese=copy.copy(spam) #second list

print('print spam :',spam)
print ('print copy cheese :',cheese)

cheese[0]='kuet'
print ('print cheese again : ',cheese)
print('print spam with changing cheese :',spam)

print('id of spam ' ,id(spam))
print('id of cheese ',id(cheese))

#li=copy.deepcopy(cheese)
#li=spam
#li.append('new')
#print(li)
#print(spam)

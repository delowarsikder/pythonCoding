# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 19:36:23 2020

@author: DelowaR
"""

def codeComma(S):
    new_str=""
    for i in range(len(S)):
        if(i!=len(S)-1):
            new_str+=old_li[i]+', '
        else:
            new_str+='and '+old_li[i]
    return new_str    


old_li=['apples', 'bananas', 'tofu', 'cats']
s=codeComma(old_li)
print('\''+s+'\'')      
   
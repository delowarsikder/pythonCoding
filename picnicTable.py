# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:37:42 2020

@author: DelowaR
"""
def printPicnic(picnicItems,leftWide,rightWide):
    print('PINIC ITEM'.center(leftWide+rightWide,'-'))
    for k,v in picnicItems.items():
        print(k.ljust(leftWide,'.'),str(v).rjust(rightWide))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

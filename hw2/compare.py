# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 04:30:27 2014

@author: Nitya Dhanushkodi
Software Design Homework 2
"""

def compare(x,y):
    if (x>y):
        return 1
    if (x==y):
        return 0
    if (x<y):
        return -1

x = compare(2,1)
print x
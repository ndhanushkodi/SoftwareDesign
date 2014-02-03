# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 04:09:18 2014

@author: Nitya Dhanushkodi
Software Design Homework 2
"""
def check_fermat(a,b,c,n):
    if(n>2 and ((a**n + b**n) == c**n)):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work"
        
check_fermat(3,4,5,3)
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
import math


def build_random_function(min_depth, max_depth):
    # your doc string goes here
    """ This is an extremely cool function that outputs a random function. I am very smart.
    """
    # your code goes here

    if max_depth == 1:
        rand_func = randint(0,1) 
        if rand_func == 0: 
            return ["x"]
        elif rand_func == 1:
            return ["y"]
        
                
    a = build_random_function(min_depth-1, max_depth-1)
    b = build_random_function(min_depth-1, max_depth-1)
        
    functions = [["prod", a, b], ["sin_pi", a], ["cos_pi",a], ["x"], ["y"]]
    
    rand_func = functions[randint(0,4)]
    
    if min_depth > 1:
        rand_func = functions[randint(0,2)]
    
    if max_depth == 1:
        rand_func = functions[randint(3,4)] 
    
    return rand_func

    

def evaluate_random_function(f, x, y):
    # your doc string goes here
    """Nitya does it again, smarter than ever.
    """

    # your code goes here
#    print 'f', f
#    print 'x', x
#    print 'y', y
    if f[0] == 'prod':
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    if f[0] == 'cos_pi':
        return math.cos(math.pi*evaluate_random_function(f[1], x, y))
    if f[0] == 'sin_pi':
        return math.sin(math.pi*evaluate_random_function(f[1], x, y))
    if f[0] == 'x':
        return x
    if f[0] == 'y':
        return y
        

"""Running this code will make the beautiful art which is sometimes ugly but not very often
This function builds random functions to represent the red, green, and blue values of pixels. 
"""
    
def make_art():
    red = build_random_function(5,8)
    green = build_random_function(5,9)
    blue = build_random_function(5,10)
    im = Image.new("RGB",(350,350))
    pixels = im.load()
    
    for x in range(0,349):
        for y in range(0,349):
            xscale = x/(349/2.0)-1
            yscale = y/(349/2.0)-1
            r = evaluate_random_function(red,xscale,yscale)
            g = evaluate_random_function(blue,xscale,yscale)
            b = evaluate_random_function(green,xscale,yscale)
            rrescale = (r+1)*255/2.0
            grescale = (g+1)*255/2.0
            brescale = (b+1)*255/2.0
            r = int(rrescale)
            g = int(grescale)
            b = int(brescale)
            pixels[x, y] = (r,g,b)
            #pixels.putpixel(x,y,)
    
    im.save("pic2.png")
    im.show()
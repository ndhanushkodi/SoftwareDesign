# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: Nitya Dhanushkodi
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
import math


## SS: Nice doc strings and comments, and great work overall! Functionality is very sound :) 

def build_random_function(min_depth, max_depth):
    """ This function outputs a random function using recursion. The arguments of the functions themselves can be functions
    which is where the recursion comes in. The function takes in a min_depth and a max_depth to specify how 'deep' the functions
    can be nested. 
    """

    if max_depth == 1: #in the base case, we don't want any more nesting- so I want to output x or y randomly
        rand_func = randint(0,1) 
        if rand_func == 0: 
            return ["x"]
        elif rand_func == 1:
            return ["y"]
        
                
    a = build_random_function(min_depth-1, max_depth-1) #this is the recursion- the arguments that are put in are random functions themselves
    b = build_random_function(min_depth-1, max_depth-1)
        
    functions = [["prod", a, b], ["sin_pi", a], ["cos_pi",a],["squared", a], ["cubed", a], ["x"], ["y"]]
    
    rand_func = functions[randint(0,4)]
    
    if min_depth > 1: #if I need more nesting, I don't want to just return x or y
        rand_func = functions[randint(0,4)]
    
    if max_depth == 1: #if the max depth is 1, I don't want more nesting so I need to return x or y
        rand_func = functions[randint(5,6)] 
    
    return rand_func

    
## SS: Passes my tests :) 
## SS: for this function, you might make use of 'elif' statements, even though the functionailty
##     is the same, stylistically, it's preferable
def evaluate_random_function(f, x, y):
    """This function evaluates the random function that I input, given values for x and y. It looks at the first element
    of each list, sees what operation to do, and outputs that operation for its arguments, which can be functions themselves. 
    """

    if f[0] == 'prod': #looking at the first element in the list with f[0], and evaluating, depending on the function
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)#this has two arguments
    if f[0] == 'cos_pi':
        return math.cos(math.pi*evaluate_random_function(f[1], x, y))
    if f[0] == 'sin_pi':
        return math.sin(math.pi*evaluate_random_function(f[1], x, y))
    if f[0] == 'squared':
        return evaluate_random_function(f[1], x, y)**2
    if f[0] == 'cubed':
        return evaluate_random_function(f[1], x, y)**3
    if f[0] == 'x':
        return x
    if f[0] == 'y':
        return y
        

## SS: Love the doc string :) 
def make_art():  
    """Running this code will make the beautiful art which is sometimes ugly but not very often
    This function builds random functions to represent the red, green, and blue values of pixels. It then loops through the pixels, 
    using the x and y values of the pixels as inputs to the function. It also rescales appropriately. 
    """
    #make random functions to represent rgb values
    red = build_random_function(4,12)
    green = build_random_function(5,12)
    blue = build_random_function(7,10)
    #create the blank image 
    im = Image.new("RGB",(350,350))
    #get the pixels to be able to change them
    pixels = im.load()
    
    for x in range(0,349): 
        for y in range(0,349): #loop through all the pixels
            #scale the pixel values from [-1,1] to input in the function
            xscale = x/(349/2.0)-1 
            yscale = y/(349/2.0)-1
            #evaluate the rgb values for the scaled pixel values
            r = evaluate_random_function(red,xscale,yscale)
            g = evaluate_random_function(blue,xscale,yscale)
            b = evaluate_random_function(green,xscale,yscale)
            #rescale the rgb values to be in the range of 0-255 because that is what they need to be for pixels
            rrescale = (r+1)*255/2.0
            grescale = (g+1)*255/2.0
            brescale = (b+1)*255/2.0
            r = int(rrescale)
            g = int(grescale)
            b = int(brescale)
            #changing the pixels to cool colors
            pixels[x, y] = (r,g,b)
          
    
    im.save("pic3.png")
    im.show()

make_art()
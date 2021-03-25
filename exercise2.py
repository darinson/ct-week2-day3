from math import pi


def square_footage(length, width):
    '''
    square_footage(int or float length of house, int or float width of house)
    
    Function calculates area of house (Length X Width = Area). Assumes that the inputs are in feet.
    
    Function returns int or float.
    '''
    area = length*width
    return(area)


def circumference(radius):
    '''
    circumference(int or float radius of circle)
    
    Function calculates circumference of a circle (2 x pi x r = circumference). Uses pi from math module.
    
    Function returns float.
    '''
    c = 2 * pi * radius
    return(c)
# add sub mul div , sqrt 
import math

def add(a , b):
    return a + b 

def sub(a , b):
    return a - b 

def mul(a , b):
    return a * b 

def div(a , b):
    return  a / b 

def square_root(a):
    if a < 0: 
        return None
    return math.sqrt(a)     
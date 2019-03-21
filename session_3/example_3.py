""" 
This is the header of the python file
company name: pythoncourse
"""
import random

def get_rand():
    return random.getrandbits(1)

var = 2
while get_rand():
    var **= var
    print(var)

print("end of iteration!")

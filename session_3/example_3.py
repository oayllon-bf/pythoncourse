""" 
This is the header of the python file
company name: pythoncourse
"""
import random

def get_rand():
    return random.getrandbits(1)

var = 8
while get_rand():
    var **= 3
    print(var)

print("end of iteration!")

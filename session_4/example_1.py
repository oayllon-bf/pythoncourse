""" 
This is the header of the python file
company name: pythoncourse
"""

# iterable files example

file = open("test.txt")
print(type(file))
print(next(file))
print(next(file))
print(next(file))
file.close()

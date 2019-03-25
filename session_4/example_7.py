""" 
This is the header of the python file
company name: pythoncourse
"""
# another example with map


def myfunc(a, b, c):
    return a + b + "_" + str(c)

x = map(myfunc, ('foot', 'hammer', 'pine'), ('ball', 'jack', 'apple'),(1,2,3))

print(list(x))
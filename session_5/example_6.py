""" 
This is the header of the python file
company name: pythoncourse
"""


class Add:
    def sum(self, a: int, b: int=None)-> int:
        # if isinstance(b, str):
        #     return b
        if b is not None:
            return a + b
        else:
            return a + 10

add = Add()
print(add.sum(2,3))
print(add.sum(2))
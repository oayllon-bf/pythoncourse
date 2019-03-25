""" 
This is the header of the python file
company name: pythoncourse
"""

# Its good practice to create a new object each time the function is called,
# by using a default arg to signal that no argument was provided
# (None is often a good choice).


def add_items(new_items, base_items=None):
    if base_items is None:
        base_items = []
    for item in new_items:
        base_items.append(item)
    return base_items

print(add_items([1, 2, 3]))
print(add_items([1, 2, 3]))
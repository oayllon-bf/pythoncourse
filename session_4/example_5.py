""" 
This is the header of the python file
company name: pythoncourse
"""

# call by reference with mutable objects, attempt to default list


def add_items(new_items, base_items=list()):
    for item in new_items:
        base_items.append(item)
    return base_items

print(add_items([1, 2, 3]))
print(add_items([1, 2, 3]))
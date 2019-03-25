""" 
This is the header of the python file
company name: pythoncourse
"""

# Calling by reference vs calling by value


def changeme(var_list):
    var_list.append([40,50])
    #var_list=[1,2]
    print("List inside the function: ", var_list, "position", id(var_list))
    return

mylist = [10,20,30]
print(f"list before function: {mylist}, position {id(mylist)}")
changeme(mylist)
print(f"list after function: {mylist}, position {id(mylist)}")
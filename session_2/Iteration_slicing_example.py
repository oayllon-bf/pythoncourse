"""
This is the header of the python file
company name: pythoncourse
"""

def perm(string):
    # Compute the list of all permutations of string
    if len(string) <= 1:
        return [string]
    r = []
    for i in range(len(string)):
        s = string[:i] + string[i+1:]
        p = perm(s)
        for x in p:
            r.append(string[i:i+1] + x)
    return r

if __name__=='__main__':
    result = perm("yomsadsa")
    print(result)
    print("end")





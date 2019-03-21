""" 
This is the header of the python file
company name: pythoncourse
"""
import random
import string


def generate_random_list(len=15):
    rand_list = []
    characters = list(string.ascii_lowercase)
    numbers = list(range(1,11))
    for i in range(len):
        opt = random.getrandbits(1)
        rand_list.append(random.choice(characters)) if opt else \
            rand_list.append(random.choice(numbers))
    return rand_list


def check_num(char):
    if isinstance(char, str):
        pass
    elif char % 2 == 0:
        print("Found an even number:", char)
        return char
    else:
        print("Found an odd number:", char)
        return char

my_list = generate_random_list()

print("**Welcome to the number evaluator**")
print("-"*35)
print(f"The randomly generated string is: {''.join(str(x) for x in my_list)}")
for element in my_list:
    print(f"Evaluating character: {element}...")
    if not check_num(element):
        print("Failed Evaluation!!")

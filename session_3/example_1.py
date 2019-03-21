"""
This is the header of the python file
company name: pythoncourse
"""

# Import the modules
import sys
import random

ans = True

while ans:
    question = input("Ask the seer a question: \n-> ")

    answers = random.randint(1, 8)

    if question == "":
        sys.exit()

    elif answers == 1:
        print("It is certain")

    elif answers == 3:
        print("You may rely on it")

    elif answers == 7:
        print("My answer is maybe")

    elif answers == 8:
        print("My sources say no")
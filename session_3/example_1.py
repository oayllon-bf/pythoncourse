"""
This is the header of the python file
company name: pythoncourse
"""

import sys
import random

ans = True

while ans:
    question = input("Ask the seer a question: \n-> ")

    answers = random.randint(1, 4)

    if question == "":
        ans = False
        print("Game ended!")
        #sys.exit()

    elif answers == 1:
        print("It is certain\n", "-"*20)

    elif answers == 2:
        print("You may rely on it\n", "-"*20)

    elif answers == 3:
        print("My answer is maybe\n", "-"*20)

    elif answers == 4:
        print("My sources say no\n", "-"*20)
""" 
This is the header of the python file
company name: pythoncourse
"""
# Other ways of iteration


def print_square_values(item):
    print(item**2)


def print_fibonacci_seq(item):
    a, b = 0, 1
    while b < item:
        print(b),
        a, b = b, a + b
    print("-"*5)


def custom_for_loop(iterable, action_to_do):
    iterator = iter(iterable)
    done_looping = False
    while not done_looping:
        try:
            item = next(iterator)
        except StopIteration:
            done_looping = True
        else:
            action_to_do(item)

custom_for_loop([8, 10, 20], print_fibonacci_seq)

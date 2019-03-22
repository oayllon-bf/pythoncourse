def one():
    return "one"

def two():
    return "two"

def three():
    return "three"


switcher = {
    1: one,
    2: two,
    3: three
}


def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()


if __name__=='__main__':
    var = 0
    while var <= 0 or var >= 4:
        try:
            var = int(input("Enter a number: "))
            if var not in (1, 2, 3):
                print("Invalid entry!")
        except ValueError:
            print("Invalid entry!")
            var = 0
    result = numbers_to_strings(var)
    print(f"The result is: {result}")
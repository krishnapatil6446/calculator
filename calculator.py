#calc.py

def add(a,b):                    #adding the two variables
    return a+b


# The subtract function was incorrectly implemented as b - a,
# but by convention subtract(a, b) should return a - b.
def subtract(a, b):               #subtracting the given variables
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("the operation is not possible.")

    return a / b

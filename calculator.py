#calc.py

def add(a,b):                    #adding the two variables
    return a+b

# fix subtract implementation
#def subtract(a, b):               #subtracting the given variables
#    return b - a

def subtract(a, b):               #subtracting the given variables
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("the operation is not possible.")

    return a / b

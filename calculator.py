def multiply(a, b):
    """This function multiplies two numbers."""
    return a * b

def subtract(a, b):
    """This function subtracts two numbers."""
    return a - b

def add(a, b):
    """This function adds two numbers."""
    return a + b

def power(a,b):
    """This function calculates the exponent of a number."""
    return a ** b

if __name__ == "__main__":
    print("Welcome to the simple calculator!")
    result = add(2, 3)
    print(f"2 + 3 = {result}")
    result2 = power(2, 3)
    print(result2)

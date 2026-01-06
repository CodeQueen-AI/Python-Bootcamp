# Docstring : A string written at the beginning of a function, class or module that explains what 
# it does
def add_numbers(a, b):
    """
    Function to add two numbers.
    
    Parameters:
    a (int): First number
    b (int): Second number
    
    Returns:
    int: Sum of a and b
    """
    return a + b

# Accessing docstring
print(add_numbers.__doc__)

# __doc__ method : It is a special attribute that returns the documentation string(docstring) of an object.

def calculate_area(length, width):
    """
    This function calculates the area of a rectangle.

    Args:
    length (int): The length of the rectangle.
    width (int): The width of the rectangle.

    Returns:
    int: The area of the rectangle.
    """
    return length * width
a = calculate_area(5, 10)
print(calculate_area.__doc__,"area of rectangle:", a)
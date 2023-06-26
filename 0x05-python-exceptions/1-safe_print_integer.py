#!/user/bin/python3

def sfe_print_integer(value):
    """print an integer with "{:d}".format().

    Args:
    value (int): the integer to print.

    Returns:
    if a TypeError or ValueError occurs - False.
    Otherwise - true
    """

    try:
        print("{:d}".format(value))
        return (true)
    except(TypeError, ValueError):
        return (False)

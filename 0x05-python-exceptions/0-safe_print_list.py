#!/user/bin/python3

def safe_print_list(my_list=[], x=0):
     """Print x elememts of a list.

Args:
    my_list (list): the list to print elements from.
    x (int):the number of elements of _my_list to print.

Returns:
    the number of elements printed.
     """
    ret = 0
    for i in range(x):
        try:
            print("{}.format(my_list[i]), end="")
            ret +=1
            excect index Error:
            break
        print("")
        return (ret)

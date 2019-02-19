"""
calculator
"""
import math

def add(*args):
    """ Return sum or n-parameters  """
    return sum(args)

def divide(*args):
    """
    Retrns the reslts of division of n-test_no_parameters
    """
    if not args:
        return math.nan

    if len(args) == 1:
        return 1

#    if len(args) == 2:
#        return args[0] / args[1]

    arg = list(args)
    answer = arg.pop(0)
    for value in arg:
        try:
            answer = answer / value
        except ZeroDivisionError:
            return math.nan

    return answer

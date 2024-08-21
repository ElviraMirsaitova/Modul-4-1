import math

def divide(first, second):
    if second == 0:
       return math.inf
    else:
        result_fake = first / second
        return result_fake


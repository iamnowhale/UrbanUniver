from math import inf

infinity = inf

def divide(first, second):

    if second == 0:
        print(infinity)
    res = first / second
    return res

print(divide(2, 0))



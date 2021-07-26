import math
def is_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    i = 1
    while i < n:
        m = i * i
        if m == n:
            return True
        elif m > n:
            return False
        i += 1
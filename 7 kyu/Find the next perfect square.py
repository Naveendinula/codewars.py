import math
def find_next_square(sq):
    n = int(sq ** 0.5)
    if sq == n * n:
        return (n+1) * (n+1)
    else:
        return -1
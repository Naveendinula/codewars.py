def square_digits(num):
    l = []
    for i in str(num):
        l.append(str(int(i)**2))
    return int("".join(l))
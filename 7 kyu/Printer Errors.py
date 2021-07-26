def printer_error(s):
    x = len(s)
    count = 0
    for i in s:
        if i in "nopqrstuvwxyz":
            count += 1
    return str(count) + '/' + str(x)    
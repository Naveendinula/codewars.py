def filter_list(l):
    new_list = []
    for item in l:
        if type(item) == int:
            new_list.append(item)
    return new_list
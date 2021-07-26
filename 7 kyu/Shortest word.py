def find_short(s):
    new_str = s.split(" ");
    new_str.sort(key=len)
    return len(new_str[0])
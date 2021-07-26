def get_middle(s):
    result = ""   
    middle = len(s) // 2
    if len(s) % 2 == 0: # even number
        result = s[middle-1], s[middle]
        return ''.join(result)
    
    if len(s) % 2 == 1:
        return (s[middle])
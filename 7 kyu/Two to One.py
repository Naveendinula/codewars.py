def longest(a1, a2):
    z = a1 + a2     #combining both strings.
    new_str = []    #creating a list
    for i in z:     #function that removes duplicates
        if i not in new_str:
            new_str.append(i)   #adding the individual characters to the list
    new_str.sort()              #arranging in alphabetical order
    return "".join(new_str)     #turning the list into a string(merging)
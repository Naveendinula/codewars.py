def duplicate_count(text):
    found = []
    lowertext = text.lower()
    for char in lowertext:
        if lowertext.count == 0:
            return 0
        elif (not(char in found) and lowertext.count(char) > 1):
            found.append(char)  
    return len(found)
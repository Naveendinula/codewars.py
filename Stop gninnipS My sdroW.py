def spin_words(sentence):
    w = sentence.split()
    l = []
    for i in w:
        if len(i) >= 5:
            l.append(i[::-1])
        else:
            l.append(i)
    new_string = " ".join(l)
    return new_string
def pig_it(text):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    new_text = text.split(" ")
    result = []
    for i in new_text:
        if not i in punc:
            result.append(i[1:] + i[0] + "ay")

    for i in new_text:
        if i in punc:
            result.append(i)
    return (" ".join(result))





    
def get_count(input_str):
    num_vowels = 0
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    for i in input_str:
        if i in vowels:
            num_vowels += 1
    return num_vowels
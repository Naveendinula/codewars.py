def binary_array_to_number(arr):
    binary = int(''.join(str(x) for x in arr)) 
    decimal, i , n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2,i)
        binary = binary // 10
        i += 1
    return decimal
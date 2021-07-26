def positive_sum(arr):
    s = 0 
    for x in arr:
       if x > 0:
           s = s + x
    return s
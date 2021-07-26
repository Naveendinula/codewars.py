# Codewars Python


---
## Sum of positive
You get an array of numbers, return the sum of all of the positives ones.

---

Example `[1,-4,7,12]` => `1 + 7 + 12 = 20`

**Note: if there is nothing to sum, the sum is default to 0.**

### Solution
```python
def positive_sum(arr):
    s = 0 
    for x in arr:
       if x > 0:
           s = s + x
    return s
```

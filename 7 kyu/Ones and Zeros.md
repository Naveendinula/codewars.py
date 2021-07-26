# Codewars Python


---
## Ones and Zeros

Given an array of ones and zeroes, convert the equivalent binary value to an integer.

---
### Given Examples

Eg: `[0, 0, 0, 1]` is treated as `0001` which is the binary representation of 1.`

```
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
```
---

### Solution

```python
def binary_array_to_number(arr):
    binary = int(''.join(str(x) for x in arr)) 
    decimal, i , n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2,i)
        binary = binary // 10
        i += 1
    return decimal
```
---


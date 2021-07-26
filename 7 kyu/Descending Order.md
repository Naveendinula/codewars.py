# Codewars Python


---
## Descending Order
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

---
### Given Examples
```
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
```
---

### Solution

```python
def descending_order(num):
                
    return int("".join(map(str, sorted([i for i in str(num)], reverse=True))))
```
---



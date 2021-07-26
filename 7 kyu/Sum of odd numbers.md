# Codewars Python


---
## Sum of odd numbers
Given the triangle of consecutive odd numbers:
```
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
```

---

### Given Examples

Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.:

```python
row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
```
---

### Solutions

```python
def row_sum_odd_numbers(n):
    row_sum = n ** 3
    return row_sum
```


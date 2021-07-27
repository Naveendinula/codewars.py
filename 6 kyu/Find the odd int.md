# Codewars Python


---
## Find the odd int
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

---
### Sample tests

```python
test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1); 
test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
test.assert_equals(find_it([10]), 10);
test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);
```
---

### Solutions

```python
def find_it(seq):
    seq_size = len(seq)
    for i in range (0, seq_size):
        count = 0
        for j in range (0, seq_size):
            if seq[i] == seq[j]:
                count += 1
        if count % 2 != 0:
            return seq[i]
```
---

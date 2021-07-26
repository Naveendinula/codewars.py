# Codewars Python


---
## Shortest word
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

---

## Solution

```python
def find_short(s):
    new_str = s.split(" ");
    new_str.sort(key=len)
    return len(new_str[0])
```
---

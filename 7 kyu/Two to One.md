# Codewars Python


---
## Two to One
Take 2 strings `s1` and `s2` including only letters from `a` to `z`. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from `s1` or `s2`.


---
### Given Examples

```python
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
```
---

### Solution

```python
def longest(a1, a2):
    z = a1 + a2     #combining both strings.
    new_str = []    #creating a list
    for i in z:     #function that removes duplicates
        if i not in new_str:
            new_str.append(i)   #adding the individual characters to the list
    new_str.sort()              #arranging in alphabetical order
    return "".join(new_str)     #turning the list into a string(merging)
```
---


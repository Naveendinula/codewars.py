# Codewars Python


---
## Get the Middle Character
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

### Input
A word (string) of length `0 < str < 1000` (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

### Output
The middle character(s) of the word represented as a string.

---
### Given Examples

```python
Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
```
---

### Solution

```python
def get_middle(s):
    result = ""   
    middle = len(s) // 2
    if len(s) % 2 == 0: # even number
        result = s[middle-1], s[middle]
        return ''.join(result)
    
    if len(s) % 2 == 1:
        return (s[middle])
```
---

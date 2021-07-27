# Codewars Python


---
## Cpunting Duplicates
Write a function that will return the count of **distinct case-insensitive** alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

---

### Given examples

```
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
```

### Solutions

```python
def duplicate_count(text):
    found = []
    lowertext = text.lower()
    for char in lowertext:
        if lowertext.count == 0:
            return 0
        elif (not(char in found) and lowertext.count(char) > 1):
            found.append(char)  
    return len(found)
```
---

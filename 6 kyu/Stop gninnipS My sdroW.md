# Codewars Python


---
## Stop gninnipS My sdroW
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (like the name of this kata).

+ Strings passed in will consist of only letters and spaces.
+ Spaces will be included only when more than one word is present.

---
### Given Examples

```python
spinWords("Hey fellow warriors") => "Hey wollef sroirraw" 
spinWords("This is a test") => "This is a test" 
spinWords("This is another test") => "This is rehtona test"
```
---

### Solutions

```python
def spin_words(sentence):
    w = sentence.split()
    l = []
    for i in w:
        if len(i) >= 5:
            l.append(i[::-1])
        else:
            l.append(i)
    new_string = " ".join(l)
    return new_string
```
---

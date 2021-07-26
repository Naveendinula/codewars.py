# Codewars Python


---
## Simple Pig Latin
Move the first letter of each word to the end of it, then add `"ay"` to the end of the word. Leave punctuation marks untouched.

---
### Given Examples

```python
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
```
---

### Solutions

```python
def pig_it(text):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    new_text = text.split(" ")
    result = []
    for i in new_text:
        if not i in punc:
            result.append(i[1:] + i[0] + "ay")

    for i in new_text:
        if i in punc:
            result.append(i)
            
    return (" ".join(result))
```
---

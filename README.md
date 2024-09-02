# PRG1-pair-programming-RegEx-PY

## Some sample Regular expressions to have a play with

```python
import re

valid_whole_number_regex = r"^[0-9]+$"
valid_positive_whole_decimal_number = r"^(?:0|[1-9]\d*)(?:\.\d+)?$"
valid_floating_point_2dp = r"^[0-9]+\.[0-9][0-9]$"
valid_alphabetic_string = r"^[A-Za-z]+$"

# Use the match method to check whether something matches the rules. 
if re.match(valid_whole_number_regex, "456"):
  print("Match found!") 
else:
  print("No match.")
```

## Create three functions that check specific pieces of data.

* e.g. 1. A name; 2. An age; 3. A height.

```python
person_name = "123abc"   # should return False
person_age = 15.5  # should this be allowed? - Depends on requirements, but generally, age is a whole number
person_height = "blah blah blah"  # should this be allowed? - No, height should be numeric

# Other regex methods do exist such as search() (which looks for matching
# characters) and sub() (which replaces characters), but match is 
# probably the most commonly used and the one you should use here.
```


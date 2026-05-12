




Question 1: Write a Python script using regular expressions to check whether a string contains only digits. The script should print whether the input is valid or invalid. Use re.fullmatch().

```python
import re

# Input string
text = "123456"

# Regex Explanation:
# ^ and $ are not needed because fullmatch() already checks the entire string
# \d  -> matches one digit
# +   -> one or more digits
pattern = r"\d+"

# fullmatch() checks whether the ENTIRE string satisfies the regex
result = re.fullmatch(pattern, text)

if result:
    print("Valid numeric string")
else:
    print("Invalid string")

# Example error case
# text = "123abc"
# This fails because letters are not digits

```
Question 2: Write a script to extract all email addresses from a paragraph using re.findall().

```python
import re

text = """
Contact us at admin@test.com or support123@company.org
"""

# Regex Explanation:
# [a-zA-Z0-9._%+-]+  -> username part
# @                  -> literal @ symbol
# [a-zA-Z0-9.-]+     -> domain name
# \.                 -> literal dot
# [a-zA-Z]{2,}       -> extension like com, org, edu

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)

print(emails)

# Output:
# ['admin@test.com', 'support123@company.org']

```
Question 3: Write a script to find all words beginning with a capital letter.

```python
import re

text = "Ravi studies at Delhi University with Amit"

# Regex Explanation:
# \b       -> word boundary
# [A-Z]    -> one uppercase letter
# [a-z]+   -> one or more lowercase letters

pattern = r"\b[A-Z][a-z]+"

matches = re.findall(pattern, text)

print(matches)

# Output:
# ['Ravi', 'Delhi', 'University', 'Amit']

```
Question 4: Write a script to validate a PIN code containing exactly 6 digits.

```python
import re

pin = "834001"

# Regex Explanation:
# \d{6} -> exactly 6 digits

pattern = r"\d{6}"

if re.fullmatch(pattern, pin):
    print("Valid PIN")
else:
    print("Invalid PIN")

# Example invalid PINs
# "12345"      -> too short
# "1234567"    -> too long
# "12A456"     -> contains letter

```
Question 5: Write a script to split a sentence wherever multiple spaces occur. Use re.split().

```python
import re

text = "Python    is   very     useful"

# Regex Explanation:
# \s+ -> one or more whitespace characters

pattern = r"\s+"

parts = re.split(pattern, text)

print(parts)

# Output:
# ['Python', 'is', 'very', 'useful']

```
Question 6: Write a script to replace all digits in a string with the symbol #. Use re.sub().

```python
import re

text = "Order 123 was shipped on 2025-05-10"

# Regex Explanation:
# \d -> matches one digit

pattern = r"\d"

result = re.sub(pattern, "#", text)

print(result)

# Output:
# Order ### was shipped on ####-##-##

```
Question 7: Write a script to extract all years from a text using capturing groups.

```python
import re

text = "India won in 1983 and again in 2011"

# Regex Explanation:
# (      ) -> capturing group
# \d{4}   -> exactly 4 digits

pattern = r"(\d{4})"

matches = re.findall(pattern, text)

print(matches)

# Output:
# ['1983', '2011']

```
Question 8: Write a script to find repeated words such as 'the the' using backreferences.

```python
import re

text = "This is is a test test sentence"

# Regex Explanation:
# (\w+)   -> capture a word
# \s+     -> one or more spaces
# \1      -> same word as captured in group 1

pattern = r"(\w+)\s+\1"

matches = re.findall(pattern, text)

print(matches)

# Output:
# ['is', 'test']

```
Question 9: Write a script to demonstrate greedy matching and non-greedy matching.

```python
import re

text = "<h1>Hello</h1><p>World</p>"

# Greedy matching
# .* consumes as much as possible
greedy = re.search(r"<.*>", text)

print("Greedy:")
print(greedy.group())

# Non-greedy matching
# .*? consumes as little as possible
lazy = re.search(r"<.*?>", text)

print("\nNon-Greedy:")
print(lazy.group())

# Output:
# Greedy      -> <h1>Hello</h1><p>World</p>
# Non-Greedy  -> <h1>

```
Question 10: Write a script to validate whether a password contains at least one uppercase letter and one digit.

```python
import re

password = "GoodPass1"

# Regex Explanation:
# (?=.*[A-Z]) -> positive lookahead for uppercase
# (?=.*\d)    -> positive lookahead for digit
# .{8,}       -> minimum 8 characters

pattern = r"(?=.*[A-Z])(?=.*\d).{8,}"

if re.fullmatch(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")

# Lookahead Explanation:
# (?=...) checks a condition without consuming text

```
Question 11: Write a script to extract hashtags from a social media post.

```python
import re

text = "Learning #Python and #DataScience is fun"

# Regex Explanation:
# #      -> literal hash
# \w+    -> one or more word characters

pattern = r"#\w+"

hashtags = re.findall(pattern, text)

print(hashtags)

# Output:
# ['#Python', '#DataScience']

```
Question 12: Write a script to remove duplicate spaces from a paragraph.

```python
import re

text = "Python     is     powerful"

# Regex Explanation:
# \s+ -> one or more spaces

result = re.sub(r"\s+", " ", text)

print(result)

# Output:
# Python is powerful

```
Question 13: Write a script to extract file extensions from filenames.

```python
import re

text = "report.pdf image.png notes.docx"

# Regex Explanation:
# \w+     -> filename
# \.      -> literal dot
# (\w+)   -> capture extension

pattern = r"\w+\.(\w+)"

extensions = re.findall(pattern, text)

print(extensions)

# Output:
# ['pdf', 'png', 'docx']

```
Question 14: Write a script using non-capturing groups to match titles such as Mr, Ms, and Dr.

```python
import re

text = "Dr. Sharma met Mr. Verma"

# Regex Explanation:
# (?:...) -> non-capturing group
# Used for grouping without storing match

pattern = r"(?:Mr|Ms|Dr)\."

matches = re.findall(pattern, text)

print(matches)

# Output:
# ['Dr.', 'Mr.']

```
Question 15: Write a script to check whether a string starts with 'Python'.

```python
import re

text = "Python is easy"

# Regex Explanation:
# ^ -> start anchor

pattern = r"^Python"

if re.search(pattern, text):
    print("Starts with Python")
else:
    print("Does not start with Python")

```
Question 16: Write a script to check whether a string ends with '.com'.

```python
import re

website = "example.com"

# Regex Explanation:
# \.com$ -> ends with .com

pattern = r"\.com$"

if re.search(pattern, website):
    print("Valid .com domain")
else:
    print("Invalid domain")

```
Question 17: Write a script to extract all floating-point numbers from text.

```python
import re

text = "Prices are 45.67 and 89.5 dollars"

# Regex Explanation:
# \d+    -> digits before decimal
# \.     -> decimal point
# \d+    -> digits after decimal

pattern = r"\d+\.\d+"

numbers = re.findall(pattern, text)

print(numbers)

# Output:
# ['45.67', '89.5']
________________________________________
```
Question 18: Write a script to validate Indian mobile numbers starting with 6, 7, 8, or 9.

```python
import re

mobile = "9876543210"

# Regex Explanation:
# [6789] -> first digit
# \d{9}  -> remaining 9 digits

pattern = r"[6789]\d{9}"

if re.fullmatch(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

```
Question 19: Write a script to extract dates in DD-MM-YYYY format.

```python
import re

text = "Exam dates are 12-05-2025 and 15-08-2026"

# Regex Explanation:
# \d{2} -> day
# -     -> separator
# \d{2} -> month
# -     -> separator
# \d{4} -> year

pattern = r"\d{2}-\d{2}-\d{4}"

dates = re.findall(pattern, text)

print(dates)

```
Question 20: Write a script using re.finditer() to display all numbers and their positions in a string.

```python
import re

text = "abc 123 def 456"

pattern = r"\d+"

matches = re.finditer(pattern, text)

for m in matches:

    print("Match:", m.group())
    print("Start:", m.start())
    print("End:", m.end())
    print("Span:", m.span())

# group() -> matched text
# start() -> starting index
# end()   -> ending index
# span()  -> tuple of start and end





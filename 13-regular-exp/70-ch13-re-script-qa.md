
Part A: Questions Based Mainly on the Chapter Topics
1. Write a Python script using re.findall() to extract all digit sequences from a string. The script should show the difference between \d and \d+.
```python
import re
# Sample string containing isolated and grouped digits
text = "My marks are 7, 89, and 1234."
# \d matches ONE digit at a time
single_digits = re.findall(r"\d", text)  # Finds each digit separately
print("Using \\d:", single_digits)  # Using \d: ['7', '8', '9', '1', '2', '3', '4']
# \d+ matches one or more consecutive digits
number_groups = re.findall(r"\d+", text)  # Finds groups of digits as whole numbers
print("Using \\d+:", number_groups)  # Using \d+: ['7', '89', '1234']
# Explanation:
# \d finds every individual digit separately.
# \d+ combines consecutive digits into a single match.
```

________________________________________
2. Write a script that checks whether a string starts with the word Python using the ^ anchor.
```python
import re
# Input string
text = "Python is powerful"
# ^ means start of string
result = re.search(r"^Python", text)  # Checks if string starts with "Python"
# Check whether match succeeded
if result:
    print("String starts with Python")
else:
    print("String does not start with Python")
# Explanation:
# The caret ^ checks the beginning position.
# It does not consume characters itself.
```
________________________________________
3. Write a script that checks whether a string ends with .com using the $ anchor.
```python
import re
# Sample domain name
text = "example.com"
# $ checks end of string
result = re.search(r"\.com$", text)  # Checks if string ends with ".com"
if result:
    print("Valid .com domain")
else:
    print("Does not end with .com")
# Explanation:
# \. matches a literal dot.
# $ ensures that .com appears at the end.
```
________________________________________
4. Write a script that extracts all lowercase letters from a string using the character class [a-z].
```python
import re
text = "PyThOn123abcXYZ"
# Find all lowercase letters
lowercase_letters = re.findall(r"[a-z]", text)  # Character class for lowercase letters
print(lowercase_letters)  # ['y', 'h', 'n', 'a', 'b', 'c']
# Explanation:
# [a-z] represents any lowercase English letter.
# Each matching character is returned individually.
```
________________________________________
5. Write a script that extracts all non-digit characters from a string using \D.
```python
import re
text = "Room45A7"
# \D matches anything that is NOT a digit
result = re.findall(r"\D", text)  # Finds all non-digit characters. Digits are ignored.
print(result)  # ['R', 'o', 'o', 'm', 'A']
# Explanation:
# Digits are ignored.
# Letters and symbols are matched instead.
```
________________________________________
6. Write a script that replaces all whitespace characters in a string with a single dash (-). Use re.sub().
```python
import re
text = "Python   is\tvery\nuseful"
# Replace one or more whitespace characters
cleaned = re.sub(r"\s+", "-", text)  # Replaces sequences of whitespace with a single dash
print(cleaned) # Python-is-very-useful
# Explanation:
# \s matches spaces, tabs, and newlines.
# + combines consecutive whitespace into one match.

```
________________________________________
7. Write a script that validates whether a PIN code contains exactly six digits.
```python
import re
pin = "834001"
# Fullmatch ensures ENTIRE string follows pattern
result = re.fullmatch(r"\d{6}", pin)
if result:
print("Valid PIN")
else:
print("Invalid PIN")
# Explanation:
# \d{6} means exactly six digits.
# re.fullmatch() prevents partial matching.
```
________________________________________
8. Write a script that demonstrates the difference between re.match() and re.search().
```python
import re
text = "Welcome to Python programming"
# match() checks only at beginning
m1 = re.match(r"Python", text)  # This will fail because "Python" is not at the start of the string.
# search() checks anywhere
m2 = re.search(r"Python", text)  # This will succeed because "Python" is found within the string.
print("re.match():", m1)  # Output: None, because the pattern "Python" does not match the start of the string.
print("re.search():", m2)  # Output: <re.Match object; span=(11, 17), match='Python'>, because the pattern "Python" is found starting at index 11 and ending at index 17 in the string.
# Explanation:
# match() fails because Python is not at start.
# search() succeeds because it scans entire string.
```
________________________________________
9. Write a script that uses alternation (|) to search for either cat or dog in a sentence.
```python
import re
text = "I have a dog at home"
# Alternation means OR
result = re.search(r"cat|dog", text)  # Checks for "cat" OR "dog" in the text
if result:
    print("Animal found:", result.group())  # Output: Animal found: dog, because "dog" is present in the text and is the first successful match found by the regex engine.
else:
    print("No animal found")  # Explanation:
# The regex engine tries "cat" first, which fails, then tries "dog", which succeeds, so "dog" is returned as the match.
# Explanation:
# Regex tries both alternatives.
# The first successful alternative is returned.
```

________________________________________
10. Write a script that uses grouping to repeat the word abc one or more times.
```python
import re
text = "abcabcabc"
# Group repeated using +
result = re.fullmatch(r"(abc)+", text)  # Checks if the entire string is one or more repetitions of "abc"
print(result)  # Output: <re.Match object; span=(0, 9), match='abcabcabc'>, because the entire string "abcabcabc" is made up of three repetitions of the substring "abc", which matches the pattern defined by the regex.
# Explanation:
# Parentheses treat abc as one unit.
# + repeats the entire group.
```

________________________________________
11. Write a script that extracts both username and domain name from an email address using capturing groups.
```python
import re
email = "student@gmail.com"
# Two capturing groups
match = re.search(r"(\w+)@(\w+\.\w+)", email)  # Captures username and domain parts of the email
if match:
    print("Username:", match.group(1))  # Output: Username: student, because the first capturing group (\w+) matches the username part of the email before the "@" symbol.
    print("Domain:", match.group(2))  # Output: Domain: gmail.com, because the second capturing group (\w+\.\w+) matches the domain part of the email after the "@" symbol, which consists of a word followed by a dot and another word.
# Explanation:
# Group 1 captures username.
# Group 2 captures domain portion.
```

________________________________________
12. Write a script that demonstrates the use of group(), start(), end(), and span() methods.
```python
import re
text = "Order number is 5678"
match = re.search(r"\d+", text)  # Finds the first sequence of digits in the text
if match:
    print("Matched text:", match.group())  # Output: Matched text: 5678, because the first sequence of digits found in the text is "5678".
    print("Start index:", match.start())  # Output: Start index: 16, because the sequence "5678" starts at index 16 in the text.
    print("End index:", match.end())  # Output: End index: 20, because the sequence "5678" ends at index 20 in the text.
    print("Span:", match.span())  # Output: Span: (16, 20), because the span of the matched sequence "5678" is from index 16 to 20.
# Explanation:
# group() returns matched text.
# start() and end() return positions.
# span() combines both indices.
```

________________________________________
13. Write a script that demonstrates partial consumption using re.match(r"\\d+", text).
```python
import re
text = "123 abc"
match = re.match(r"\d+", text)
if match:
print("Matched:", match.group())
print("Consumed span:", match.span())
print("Remaining text:", text[match.end():])
# Explanation:
# Only digits are consumed.
# Remaining characters are untouched.
```

________________________________________
14. Write a script that demonstrates full consumption of a string using .*.
```python
import re
text = "123 abc"
# Consume everything after digits
match = re.match(r"\d+.*", text)
if match:
print("Entire consumed text:", match.group())
print("Span:", match.span())
# Explanation:
# .* consumes remaining characters.
# Entire string becomes part of match.
```

________________________________________
15. Write a script that extracts all words from a sentence using \w+.
```python
import re
text = "Python is fun!"
words = re.findall(r"\w+", text)
print(words)
# Explanation:
# \w matches letters, digits, and underscore.
# + groups consecutive word characters.
```

________________________________________
16. Write a script that splits a sentence into words using re.split().
```python
import re
text = "Apple,Orange;Banana Grape"
# Split using comma, semicolon, or whitespace
parts = re.split(r"[,;\s]+", text)
print(parts)
# Explanation:
# Character class contains separators.
# + combines consecutive separators.
```

________________________________________
17. Write a script that demonstrates the difference between greedy and non-greedy matching.
```python
import re
text = "<b>Python</b><b>Java</b>"
# Greedy match
greedy = re.findall(r"<b>.*</b>", text)
print("Greedy:", greedy)
# Non-greedy match
nongreedy = re.findall(r"<b>.*?</b>", text)
print("Non-greedy:", nongreedy)
# Explanation:
# .* grabs maximum possible text.
# .*? grabs minimum possible text.
```

________________________________________
18. Write a script that counts how many replacements were made using re.subn().
```python
import re
text = "Marks: 45, 67, 89"
# Replace numbers with #
result = re.subn(r"\d+", "#", text)
print(result)
# Explanation:
# subn() returns tuple.
# First item = modified string.
# Second item = number of replacements.
```

________________________________________
19. Write a script that uses named groups to extract a date in the format DD-MM-YYYY.
```python
import re
text = "Today's date is 08-05-2026"
pattern = r"(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})"
match = re.search(pattern, text)
if match:
print(match.groupdict())
# Explanation:
# Named groups create dictionary-like access.
# Keys become group names.
________________________________________
20. Write a script that uses re.escape() to safely search for the literal text a+b.
```python
import re
text = "a+b"
# Escape special regex symbols
safe_pattern = re.escape("a+b")
result = re.fullmatch(safe_pattern, text)
print(result)
# Explanation:
# + normally means repetition.
# re.escape() removes special meaning.
```

________________________________________
21. Write a script that demonstrates the use of a compiled Pattern object.
```python
import re
# Compile pattern once
pattern = re.compile(r"\d+")
text1 = "123"
text2 = "456"
print(pattern.match(text1))
print(pattern.match(text2))
# Explanation:
# Compiled patterns are reusable.
# Useful for repeated matching.
```

________________________________________
22. Write a script that prints the attributes pattern, groups, and groupindex of a compiled Pattern object.
```python
import re
pattern = re.compile(r"(?P<word>\w+)-(\d+)")
print("Pattern:", pattern.pattern)
print("Groups:", pattern.groups)
print("Named groups:", pattern.groupindex)
# Explanation:
# pattern stores regex text.
# groups stores total capturing groups.
# groupindex maps names to numbers.
```

________________________________________
23. Write a script that validates whether a password contains at least one digit and one uppercase letter.
```python
import re
password = "Python123"
# Positive lookaheads used for validation
pattern = r"(?=.*[A-Z])(?=.*\d).{8,}"
result = re.fullmatch(pattern, password)
if result:
print("Strong password")
else:
print("Weak password")
# Explanation:
# (?=.*[A-Z]) checks uppercase letter.
# (?=.*\d) checks digit.
# .{8,} ensures minimum length.
```

________________________________________
24. Write a script that extracts all words beginning with a capital letter.
```python
import re
text = "Python and Java are Programming Languages"
result = re.findall(r"\b[A-Z]\w*", text)
print(result)
# Explanation:
# \b ensures word boundary.
# [A-Z] checks first letter uppercase.
```

________________________________________
25. Write a script that finds all repeated vowels in a string using quantifiers.
```python
import re
text = "cooool beeaautiful"
# Find repeated vowels
result = re.findall(r"[aeiou]{2,}", text)
print(result)
# Explanation:
# {2,} means two or more repetitions.
# Character class limits search to vowels.
```

________________________________________
26. Write a script that extracts all hexadecimal numbers from a string.
```python
import re
text = "Colors: #FFAA00 and #12BC9A"
result = re.findall(r"#[A-Fa-f0-9]{6}", text)
print(result)
# Explanation:
# Hexadecimal digits include 0-9 and A-F.
# {6} ensures exactly six digits.
________________________________________
27. Write a script that checks whether a string contains only alphabets and spaces.
```python
import re
text = "Python Programming"
result = re.fullmatch(r"[A-Za-z ]+", text)
if result:
print("Valid text")
else:
print("Contains invalid characters")
# Explanation:
# Character class includes letters and spaces.
# + ensures one or more characters.
```

________________________________________
28. Write a script that extracts all hashtags from a social media post.
```python
import re
text = "Learning #Python and #Regex is fun"
hashtags = re.findall(r"#\w+", text)
print(hashtags)
# Explanation:
# # matches literal hashtag symbol.
# \w+ captures hashtag text.
```

________________________________________
29. Write a script that demonstrates re.finditer() by printing all matches and their positions.
```python
import re
text = "cat bat rat"
# finditer() returns iterator of Match objects
for match in re.finditer(r"\w+", text):
print("Word:", match.group())
print("Position:", match.start(), match.end())
# Explanation:
# Each iteration produces one Match object.
# Position information is available.
```

________________________________________
30. Write a script that extracts only the file extensions from filenames.
```python
import re
text = "report.pdf image.png notes.txt"
extensions = re.findall(r"\.([A-Za-z0-9]+)", text)
print(extensions)
# Explanation:
# \. matches literal dot.
# Parentheses capture extension only.
```

________________________________________
Part B: Advanced and Extension Questions
31. Write a script that validates IPv4 addresses using Regular Expressions.
```python
import re
ip = "192.168.1.1"
# Simplified IPv4 regex
pattern = r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$"
result = re.fullmatch(pattern, ip)
if result:
    print("Valid IP")
else:
    print("Invalid IP")
# Explanation:
# Each number must be between 0 and 255.
# Dot-separated structure enforced.
________________________________________
32. Write a script that masks credit card numbers except the last four digits.
```python
import re
text = "My card number is 1234567812345678"
# Replace first 12 digits
masked = re.sub(r"\d(?=\d{4})", "*", text)
print(masked)
# Explanation:
# Positive lookahead keeps last 4 digits visible.
# Earlier digits are replaced.
```

________________________________________
33. Write a script that removes duplicate consecutive words from a sentence.
```python
import re
text = "This is is a test test sentence"
# Backreference used
cleaned = re.sub(r"\b(\w+)\s+\1\b", r"\1", text)
print(cleaned)
# Explanation:
# (\w+) captures a word.
# \1 refers back to same word.
```

________________________________________
34. Write a script that extracts all HTML tag names from a string.
```python
import re
html = "<html><body><h1>Title</h1></body></html>"
# Capture tag names
result = re.findall(r"<\/?([a-zA-Z0-9]+)", html)
print(result)
# Explanation:
# \/? optionally matches closing slash.
# Capturing group extracts tag names.
```

________________________________________
35. Write a script that converts dates from DD/MM/YYYY format to YYYY-MM-DD format using re.sub().
```python
import re
text = "Today's date is 08/05/2026"
# Rearrange captured groups
new_text = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", text)
print(new_text)
# Explanation:
# Groups capture day, month, year.
# Replacement string rearranges them.
```

________________________________________
36. Write a script that tokenizes a sentence into words and punctuation marks separately.
```python
import re
text = "Hello, world! How are you?"
# Match words OR punctuation
tokens = re.findall(r"\w+|[^\w\s]", text)
print(tokens)
# Explanation:
# Alternation separates words and punctuation.
# Useful in Natural Language Processing.
```

________________________________________
37. Write a script that identifies repeated whitespace in a text file and compresses it into single spaces.
```python
import re
text = "Python is\t\tvery\n\nuseful"
# Replace repeated whitespace
cleaned = re.sub(r"\s+", " ", text)
print(cleaned)
# Explanation:
# \s+ captures all repeated whitespace.
# Single space normalizes formatting.
```

________________________________________
38. Write a script that extracts URLs beginning with either http or https.
```python
import re
text = "Visit https://python.org and http://example.com"
urls = re.findall(r"https?://\S+", text)
print(urls)
# Explanation:
# s? makes 's' optional.
# \S+ captures remaining non-space characters.
```

________________________________________
39. Write a script that demonstrates catastrophic backtracking using a badly designed regex and explain why it is dangerous.
```python
import re
import time
# Poorly designed regex
pattern = r"(a+)+$"
# Long failing string
text = "a" * 25 + "X"
start = time.time()
result = re.match(pattern, text)
end = time.time()
print("Match:", result)
print("Time taken:", end - start)
# Explanation:
# Nested quantifiers can trigger excessive backtracking.
# Regex engine tries many combinations before failing.
# Dangerous in performance-sensitive systems.
```

________________________________________
40. Write a script that builds a mini regex tester where the user enters a pattern and a test string, and the script reports whether a match exists.
```python
import re
# User inputs
pattern = input("Enter regex pattern: ")
text = input("Enter test string: ")
try:
    # Try searching pattern
    result = re.search(pattern, text)
        if result:
            print("Match found:", result.group())
            print("Span:", result.span())
        else:
            print("No match found")
except re.error as e:
    print("Invalid regex pattern:", e)

# Explanation:
# Allows experimentation with regex.
# try-except handles invalid patterns safely.
# Useful educational mini-project.
```




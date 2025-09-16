import re

text = "Hi! my name is krishna manohar and my pin no:1714"

# Meta characters and quantifiers
print(re.findall("[h]", text))         # Matches all occurrences of 'h'
print(re.findall("^my", text))         # Matches 'my' only if it's at the beginning of the string
print(re.findall("is$", text))         # Matches 'is' only if it's at the end of the string
print(re.findall("k......", text))     # Matches 'k' followed by any 6 characters (e.g., 'krishna')
print(re.findall("an*", text))         # Matches 'a' followed by zero or more 'n's (e.g., 'a', 'an', 'annn')
print(re.findall("kr+", text))         # Matches 'k' followed by one or more 'r's (e.g., 'kr', 'krrr')
print(re.findall("i{1}", text))        # Matches exactly one 'i'

# Special sequences
print(re.findall(r"\s", text))         # Matches all whitespace characters (spaces, tabs, newlines)
print(re.findall(r"\S", text))         # Matches all non-whitespace characters
print(re.findall(r"\d", text))         # Matches all digit characters (0-9)
print(re.findall(r"\D", text))         # Matches all non-digit characters
print(re.findall(r"\w", text))         # Matches all alphanumeric characters (letters & digits) and underscores
print(re.findall(r"\W", text))         # Matches all non-alphanumeric characters
print(re.findall(r"1714\Z", text))     # Matches '1714' only if it's at the end of the string

# Sets / Character classes
print(re.findall("[kris]", text))      # Matches any occurrence of 'k', 'r', 'i', or 's'
print(re.findall("[123]", text))       # Matches any occurrence of '1', '2', or '3'
print(re.findall("[0-9]", text))       # Matches any digit (0-9)
print(re.findall("[a-z]", text))       # Matches any lowercase letter
print(re.findall("[0-9][0-9][0-9][0-9]", text))  # Matches any sequence of 4 consecutive digits


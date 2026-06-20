
# escape sequence characters in python

# In Python, escape sequence characters are special character combinations that start with a backslash \ and represent characters that are difficult or impossible to type directly in a string.

# They are mainly used inside string literals.

# Common Escape Sequences in Python
# Escape Sequence	Meaning	Example
# \n	New line	"Hello\nWorld"
# \t	Tab (horizontal tab space)	"Hello\tWorld"
# \\	Backslash	"C:\\Users\\Name"
# \'	Single quote	'It\'s Python'
# \"	Double quote	"He said \"Hi\""
# \r	Carriage return	"Hello\rWorld"
# \b	Backspace	"Hello\bWorld"
# \f	Form feed	Rarely used
# \ooo	Octal value	"\101" → A
# \xhh	Hexadecimal value	"\x41" → A
# Examples
# 1. New Line
# print("Hello\nWorld")
# Output:

# Hello
# World
# 2. Tab Space
# print("Name:\tJohn")
# Output:

# Name:   John
# 3. Quotes Inside String
# print("He said \"Hello\"")
# Output:

# He said "Hello"
# 4. Printing a Backslash
# print("C:\\Users\\Admin")
# Output:

# C:\Users\Admin
# Raw Strings (Avoid Escape Sequences)
# If you don’t want Python to treat \ as escape characters, use raw strings.

# print(r"C:\Users\John")
# Output:

# C:\Users\John
# ✅ Short Definition:
# Escape sequences are special characters preceded by \ used to represent characters like newlines, tabs, quotes, or backslashes inside strings.

# If you want, I can also show:

# 10 important escape sequence programs for exams, or

# Tricky Python escape sequence interview questions.
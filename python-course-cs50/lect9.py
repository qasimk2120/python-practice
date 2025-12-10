##validating user email address is an email address
##broken code/not the best practice
# email = input("What's your email address? ").strip().lower()

# #check if email contains @ and .

# if '@' in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")
# email = input("What's your email address? ").strip()
# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")


##best practices using python library re which is for regular expressions(a pattern)  re.search(pattern, string, flags=0)
## flags allow us to configure the regular expression differently
## . any character expect a newline
## * zero or more occurrences
## + one or more occurrences
## ? zero or one occurrences
## {n} exactly n occurrences
##{m, n} exactly n occurrences
## ^ matches the start of a string
## $ matches the end of a string or just before the newline at the end of the string
## []set of characters
## [^] complementing the set(cannot match the set of characters passed after  ^ inside the brackets)
##\w a word character(aswell as numbers and _) ##\W non word character ## \d decimal digit 
# ##\s whitespace character ##\S non-whitespace character ##\D non-decimal digit 
## A|B either A or B
##(...) a group
##(?:...) This is a non-capturing group in regular expressions.
##re.IGNORECASE -- Perform case-insensitive matching;
#3re.MULTILINE -- When specified, the pattern character '^' matches at 
#       the beginning of the string and at the beginning of each line (immediately following each newline); 
#       and the pattern character '$' matches at the end of 
#          the string and at the end of each line (immediately preceding each newline).
##re.DOTALL -- any character  +  new line

# import re
# email = input("What's your email address? ").strip()

# # r is for raw string, it allows us to use backslashes without escaping them, similar to f for strings where we want special formatting
# if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, flags=re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid")


##try to use a popular library to solve the problem, e.g. validating the email address


##formatting data , e.g. user's name bad practice in case of names such as Malan,Davif  , or Malan, David, Jr
# name = input("What's your name? ").strip()
# if ", " in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"

# print(f"hello, {name}")
## better way for formatting using regular expressions re
##  := walrus operator, cobinging assign a value and ask a if question
# import re
# name = input("What's your name? ").strip()

# if matches := re.search(r"^(.+), *(.+)$", name):
#     name = matches.group(2) + " " + matches.group(1)

# print(f"hello, {name}")
##re.sub substitute a pattern with another pattern
## extracting information to answer a question
##re.sub(pattern, repl, string, count=0, flags=0)  
# pattern is regular expression we are looking for, 
# epl is the replacement string, string is the string we are looking in, 
# count is the number of times we want to replace the pattern,
#  flags are the flags we want to use
import re
url = input("URL: ").strip()
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url) or below solution
# if matches  := re.search(r'^https?://?(www\.)?twitter\.com/(.+)$', url, re.IGNORECASE): #or below solution
if matches  := re.search(r'^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)', url, re.IGNORECASE):
    print(matches.group(1))
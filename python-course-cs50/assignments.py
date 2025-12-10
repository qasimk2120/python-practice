import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AN|PM)$"
    match  = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid format")
    
    hours1, minutes1, meridian1,hours2, minutes2, meridian2 = match.groups()   
    hours1, hours2 = int(hours1), int(hours2)
    minutes1, minutes2 = int(minutes1 or 0), int(minutes2 or 0)

    if not (0 <= minutes1 < 60 and 0 <= minutes2 < 60):
        raise ValueError("Invalid minutes")
    if not (1 <= hours1 <=12 and 1<=hours2 <=12):
        raise ValueError("Invalid hours")

    h1 = (h1 % 12) + (12 if meridian1 == "PM" else 0)   
    h2 = (h2 % 12) + (12 if meridian2 == "PM" else 0)

    return f"{h1:02}:{minutes1:02} to {h2:02}:{minutes2:02}"

if __name__ == "__main__":
    main()
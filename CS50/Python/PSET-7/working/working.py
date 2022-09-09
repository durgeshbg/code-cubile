import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if hours := re.search(r"([\d]*):?([\d]*)? (AM|PM) to ([\d]*):?([\d]*)? (AM|PM)", s):
            h1 = int(hours.group(1)) if hours.group(3) == 'AM' else int(hours.group(1)) + 12
            m1 = 0 if hours.group(2) == "" else int(hours.group(2))
            h2 = int(hours.group(4)) if hours.group(6) == 'AM' else int(hours.group(4)) + 12
            m2 = 0 if hours.group(5) == "" else int(hours.group(5))
            if m1 >= 60 or m2 >= 60 or h1 >= 24 or h2 >= 24: raise ValueError
            return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip):
        if byte1(matches.group(1)) and byte2(matches.group(2)) and byte3(matches.group(3)) and byte4(matches.group(4)):
            return True
        return False
    else:
        return False

if __name__ == "__main__":
    main()

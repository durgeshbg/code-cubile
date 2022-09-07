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

def byte1(b1):
    if int(b1) > 255:
        return False
    return True

def byte2(b2):
    if int(b2) > 255:
        return False
    return True

def byte3(b3):
    if int(b3) > 255:
        return False
    return True

def byte4(b4):
    if int(b4) > 255:
        return False
    return True

if __name__ == "__main__":
    main()

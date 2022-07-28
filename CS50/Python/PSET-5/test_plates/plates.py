def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def num_check(s):
    digits = ''
    for c in s:
        if c.isdigit():
            digits += c
            if digits[0] == '0':
                return False
        else:
            if not digits == '':
                return False
    return True

def is_valid(s):
    if len(s) <= 6 and len(s) >= 2 and s[0].isalpha() and s[1].isalpha() and s.isalnum():
        if num_check(s):
            return True
    return False

if __name__ == '__main__':
    main()


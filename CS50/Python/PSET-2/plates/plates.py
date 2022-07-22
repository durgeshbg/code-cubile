def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')




def is_valid(s):
    if s[0:2].isalpha() and len(s) <= 6 and len(s) >= 2:
        if num_check(s[2:]):
            if not (s.punctuation):
                return True
    return False
main()


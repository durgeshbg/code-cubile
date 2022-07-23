import random

def get_valid_int(s):
    while True:
        try:
            number = int(input(s))
            if number <= 0:
                continue
            return number
        except ValueError:
            continue

def main():
    level = get_valid_int('Level: ')
    number = random.randint(1, level)
    while True:
        guess = get_valid_int('Guess: ')
        if guess > number:
            print('Too large!')
        elif guess < number:
            print('Too small!')
        else:
            print('Just Right!')
            break

if __name__ == '__main__':
    main()
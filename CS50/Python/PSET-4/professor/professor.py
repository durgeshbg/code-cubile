import random


def main():
    level = get_level('Level: ')


def get_level(s):
    while True:
        try:
            l = int(input(s))
        except ValueError:
            continue
        if l in [1,2,3]:
            return l


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
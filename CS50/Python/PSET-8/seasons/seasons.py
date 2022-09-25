from datetime import date


def main():
    ...


def leapyear(y):
    return ((True if (y % 400 == 0) else False) if (y % 100 == 0) else True) if (y % 4 == 0) else False

if __name__ == "__main__":
    main()


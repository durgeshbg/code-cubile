from datetime import date
from sys import exit
import inflect
p = inflect.engine()

def main():
    try:
        y,m,d = map(int, input("Date of Birth: ").split("-"))
    except:
        exit("Invalid date")
    minutes = convert(y, m, d)
    words = p.number_to_words(minutes,andword='')
    print(words.capitalize()+" minutes.")


def convert(y, m, d):
    dob = date(y,m,d)
    d = date.today() - dob
    print(d.days * 24 * 60)
    return (d.days * 24 * 60)


if __name__ == "__main__":
    main()


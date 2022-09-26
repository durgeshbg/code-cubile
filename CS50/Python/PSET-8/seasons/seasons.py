from datetime import date
from sys import exit
import inflect
p = inflect.engine()

def main():
    s = input("Date of Birth: ")
    y,m,d = inputdate(s)
    minutes = convert(y, m, d)
    words = p.number_to_words(minutes,andword='')
    print(words.capitalize()+" minutes.")

def inputdate(s):
    try:
        y,m,d = map(int, s.split("-"))
        return y,m,d
    except:
        exit("Invalid date")

def convert(y, m, d):
    dob = date(y,m,d)
    d = date.today() - dob
    return (d.days * 24 * 60)


if __name__ == "__main__":
    main()


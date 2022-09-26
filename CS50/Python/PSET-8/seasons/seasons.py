from datetime import date
from sys import exit
import inflect
p = inflect.engine()

def main():
    try:
        y,m,d = map(int, input("Date of Birth: ").split("-"))
    except:
        exit("Invalid date")
    dob = date(y,m,d)
    d = date.today() - dob
    minutes = d.days * 24 * 60
    words = p.number_to_words(minutes,andword='')
    print(words.capitalize()+" minutes.")
if __name__ == "__main__":
    main()


def main():
    fraction = input('Fraction: ')
    p = convert(fraction)
    percentage = gauge(p)
    print(percentage)

def convert(f):
    fraction = f.split('/')
    numerator = int(fraction[0])
    denominator = int(fraction[1])
    
    if denominator == 0:
        raise ZeroDivisionError

    if numerator > denominator:
        raise ValueError

    else:
        p = round((numerator/denominator) * 100)
        return p

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
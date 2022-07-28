def main():
    fraction = input('Fraction: ').split('/')
    p = convert(fraction)
    if p:
        percentage = gauge(p)
        print(percentage)

def convert(fraction):
    try:
        numerator = int(fraction[0])
        denominator = int(fraction[1])
        
        if numerator > denominator:
            raise ValueError
        else:
            p = round((numerator/denominator) * 100)
            return p

    except (ValueError,ZeroDivisionError):
        pass

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
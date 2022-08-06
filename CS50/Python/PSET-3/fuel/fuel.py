while True:
    try:
        fraction = input("Fraction: ").split("/")
        numerator = int(fraction[0])
        denominator = int(fraction[1])

        if numerator > denominator:
            continue

        percentage = round((numerator / denominator) * 100)
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")
        break

    except (ValueError, ZeroDivisionError):
        continue

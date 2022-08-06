def main():
    time_str = input("What time is it? ").split(":")
    time = convert(time_str)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    return round(float(time[0]) + (float(time[1]) / 60), 2)


if __name__ == "__main__":
    main()

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
    # Support for 12 hour format
    time[1] = time[1].split(" ")
    if time[1][1].lower() == "p.m.":
        time[0] = int(time[0]) + 12

    return round(float(time[0]) + (float(time[1][0]) / 60), 2)


if __name__ == "__main__":
    main()

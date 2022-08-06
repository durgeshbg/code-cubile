def main():
    greet = input("Greeting: ")
    money = value(greet)
    print(f"${money}")


def value(greet):
    greeting = greet.strip().lower().split(" ")
    first_word = greeting[0]
    if first_word == "hello" or first_word == "hello,":
        return 0
    elif "h" == first_word[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

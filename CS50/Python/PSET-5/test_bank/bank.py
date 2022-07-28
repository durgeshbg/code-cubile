def main():
    greet = input("Greeting: ").strip().lower().split(" ")
    money = value(greet)
    print(f'${money}')


def value(greeting):
    first_word = greeting[0]
    if first_word == 'hello' or first_word == 'hello,':
        return 0
    elif 'h' == first_word[0] :
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
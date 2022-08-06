def main():
    twttr = input("Input: ")
    output = shorten(twttr)
    print(f"Output: {output}")


def shorten(word):
    twt_str = ""
    for c in word:
        if c.lower() in ["a", "e", "i", "o", "u"]:
            continue
        else:
            twt_str += c
    return twt_str


if __name__ == "__main__":
    main()

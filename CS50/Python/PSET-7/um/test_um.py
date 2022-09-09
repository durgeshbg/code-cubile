from um import count

def test_lowercase():
    assert count("hello, um, world") == 1
    assert count("um...") == 1
    assert count("um..um?") == 2


if __name__ == "__main__":
    main()
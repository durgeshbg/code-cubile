ask = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)
if ask == "42" or ask.lower() == "forty two" or ask.lower() == "forty-two":
    print("Yes")
else:
    print("No")

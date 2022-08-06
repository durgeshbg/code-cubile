names = []
while True:
    try:
        name = input("Name: ")
        if name != "":
            names.append(name)
    except EOFError:
        break
print()
print(f"Adieu, adieu, to ", end="")
for n in range(len(names)):
    if len(names) == 1:
        print(names[n])
    elif n == len(names) - 2:
        print(f"{names[n]} and {names[-1]}")
        break
    else:
        print(f"{names[n]}, ", end="")

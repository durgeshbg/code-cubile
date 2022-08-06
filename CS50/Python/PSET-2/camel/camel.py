camelCase = input("camelCase: ")
snake_case = ""

for i in camelCase:
    if i.isupper():
        i = "_" + i.lower()
    snake_case += i

print(f"snake_case: {snake_case}")

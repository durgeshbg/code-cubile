expression = input("Expression: ").split(' ')
x = float(expression[0])
y = expression[1]
z = float(expression[2])

match y:
    case '+':
        result = x + z
        print(f"{result:.1f}")
    case '-':
        result = x - z
        print(f"{result:.1f}")
    case '*':
        result = x * z
        print(f"{result:.1f}")
    case '/':
        result = x / z
        print(f"{result:.1f}")

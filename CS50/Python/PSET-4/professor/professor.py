import random

def main():
    level = get_level('Level: ')
    score = 0
    for i in range(10):
        trail = 0
        x, y, result = generate_integer(level)

        while True:
            try:
                print(f'{x} + {y} = ',end='')
                res = int(input())
            except ValueError:
                print('EEE')
                trail += 1
                if trail == 3:
                    print(f'{x} + {y} = {result}')
                    break
                continue
            if result == res:
                score +=1
                break
            else:
                print('EEE')
                trail += 1
                if trail == 3:
                    print(f'{x} + {y} = {result}')
                    break

    print(f'Score: {score}')

def get_level(s):
    while True:
        try:
            level = int(input(s))
        except ValueError:
            continue
        if level in [1,2,3]:
            return level


def generate_integer(level):
    a = pow(10, level - 1)
    b = pow(10, level) - 1
    x = random.randint(a, b)
    y = random.randint(a, b)
    return x, y, x + y


if __name__ == "__main__":
    main()
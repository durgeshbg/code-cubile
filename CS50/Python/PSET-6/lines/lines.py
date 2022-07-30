from sys import argv,exit

lc = 0

if len(argv) < 2:
    exit('Too few command-line arguments')
elif len(argv) > 2:
    exit('Too many command-line arguments')
elif '.py' not in argv[1]:
    exit('Not a python file')

try:
    with open(argv[1]) as file:
        for line in file:
            line = line.lstrip()
            if not line.startswith('#') and line != '':
                lc += 1

except FileNotFoundError:
    exit('File does not exist')

print(lc)
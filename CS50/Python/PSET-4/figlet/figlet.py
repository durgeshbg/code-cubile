import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
        if f not in fonts:
            sys.exit("Invalid usage")
        figlet.setFont(font=f)
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 0:
    f = random.choice(fonts)
    figlet.setFont(font=f)
else:
    sys.exit("Invalid usage")

s = input("Input: ")
print("Output: ")
print(figlet.renderText(s))

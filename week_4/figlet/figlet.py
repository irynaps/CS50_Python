from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)

elif len(sys.argv) == 3:
    if not sys.argv[1] == "-f" or sys.argv[1] == "--font":
        sys.exit("Invalid usage")
    elif not sys.argv[2] in fonts:
        sys.exit("Invalid usage")
    f = sys.argv[2]

else:
    sys.exit("Invalid usage")

str = input("Intput: ")
set_font = figlet.setFont(font=f)
print(figlet.renderText(str))

#submit50 cs50/problems/2022/python/figlet

from pyfiglet import Figlet
import random
import sys
figlet = Figlet()

if len(sys.argv)==1:
    random_font = random.choice(figlet.getFonts())
    figlet.setFont(font=random_font)
    text= input("Input: ")
    print(figlet.renderText(text))


elif len(sys.argv) == 3 and sys.argv[1] in["-f","--font"]:
    font = sys.argv[2]
    if font in figlet.getFonts():
        figlet.setFont(font=font)
        text = input("Enter text to render: ")
        print(fglet.renderText(text))
else:
    sys.exit(1)

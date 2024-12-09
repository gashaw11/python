submit50 cs50/problems/2022/python/figlet

from pyfiglet import Figlet
import random
import sys
figlet = Figlet()
text= input("Input: ")
if len(sys.argv)==1:
    print(figlet.renderText(text))
elif len(sys.argv) == 2:
    font = sys.argv[1]
    if font in figlet.getFonts():
        figlet.setFont(font=font)
        print(fglet.renderText(text))
else:
    random_font = random.choice(figlet.getFonts())
    figlet.setFont(font=random_font)
    print(figlet.renderText(text))

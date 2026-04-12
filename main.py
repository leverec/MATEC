__ver__ = "0.3.2"
from system.syntax.dispatcher import dispatch
from system.syntax.parser import parse
from utils.colors import colorize
import os

def run():
    running = True
    while running:
        signal = parse(input("$ "))
        if signal["command"] in ("clear", "cls") : os.system('cls' if os.name == 'nt' else 'clear')
        if signal["command"] in ("exit", "q")  : running = False
        result = dispatch(signal)

if __name__ == "__main__":
    print(colorize("TEXT_CYAN", "Type exit or q for stopping the script and make sure you've read Syntax.md for better understanding of the syntax!"))
    print(colorize("TEXT_PURPLE", "\033[4mhttps://github.com/leverec/MATEC/blob/main/Syntax.md"))
    run()
__ver__ = "0.2.1"
from system.syntax.dispatcher import dispatch
from system.syntax.parser import parse

def run():
    running = True
    while running:
        signal = parse(input("$ "))
        if signal["type"] == "system" and signal["command"] == "exit":
            running = False
        dispatch(signal)

if __name__ == "__main__":
    print("Type exit for stopping the script and make sure you've read Syntax.md for better understanding of the syntax!")
    print("https://github.com/leverec/MATEC/blob/main/Syntax.md")
    run()
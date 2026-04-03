__ver__ = "0.1.0"
from system.syntax.dispatcher import dispatch
from system.syntax.parser import parse


def main():
    running = True
    while running:
        signal = parse(input("$ "))
        if signal["type"] == "system" and signal["command"] == "exit":
            running = False
        dispatch(signal)

if __name__ == "__main__":
    print("Type exit for stopping the script and make sure you've read Syntax.md for better understanding of the syntax!")
    print("https://github.com/leverec/MATEC/Syntax.md")
    main()

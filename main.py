import random
import os
import sys

items = []

def cls():
    if sys.platform() == "win32":
        os.system("cls")
    else:
        os.system("clear")

def add():
    global items
    cls()
    sheesh = input("\n\t Enter item: ")
    items.append(sheesh)

def select_screen():
    cls()
    print("\n\t[1] Enter new item")
    print("\n\t[2] Pick from current items")
    input = input("\n\t[?] Select: ")
    return input

def main():
    while True:
        if select_screen() == "1":
            add()
        elif select_screen() == "2":
            item = random.choice(items)
            print(f"\n\n\t{item}")
            input()


if __name__=="__main__":
    main()

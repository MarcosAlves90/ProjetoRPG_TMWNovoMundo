import os
import sys
import time

from colorama import Fore


def color(c):
    print(getattr(Fore, c), end="")


def line(x):
    print("==" + "=" * len(x))
    print(" " + x + " ")
    print("==" + "=" * len(x))


def line_up(x):
    print("==" + "=" * len(x))
    print(" " + x + " ")


def line_down(x):
    print(" " + x + " ")
    print("==" + "=" * len(x))


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def exit_game(phrase):
    clear_screen()
    print(phrase)
    pause()
    force_exit()


def pause():
    input("\nPress Enter to continue...")


def invalid():
    print("Invalid input, please try again.")
    pause()


def print_text(texts, delay=0):
    for text in texts:
        print(text)
        time.sleep(delay)


def force_exit():
    sys.exit()

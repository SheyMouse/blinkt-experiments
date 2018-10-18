#!/usr/bin/env python

'''
A very basic script to take a user's input and display their chosen colour.
'''


import blinkt
import time


print("Hello. I'm Pi. What is your name?")
pers = input(">>> ")
time.sleep(1)
print("Nice to meet you " + pers + "!")

time.sleep(1)

print("I would like to display your chosen colours on my LEDs.")
print()
print("Please choose from red, green, blue, yellow, cyan, magenta, or pink.")
print("What should I display?")
ledcolour = input(">>> ").lower()


if ledcolour == "red":
    print("255, 0, 0")
    clear()
    set_all(255, 0, 0, 1.0)
    show()
elif ledcolour == "green":
    print("0, 255, 0")
    clear()
    set_all(0, 255, 0, 1.0)
    show()
elif ledcolour == "blue":
    print("0, 0, 255")
    clear()
    set_all(0, 0, 255, 1.0)
    show()
elif ledcolour == "yellow":
    print("255, 255, 0")
    clear()
    set_all(255, 255, 0, 1.0)
    show()
elif ledcolour == "cyan":
    print("0, 255, 255")
    clear()
    set_all(0, 255, 255, 1.0)
    show()
elif ledcolour == "magenta":
    print("255, 0, 255")
    clear()
    set_all(255, 0, 255, 1.0)
    show()
elif ledcolour == "pink":
    print("255, 0, 128")
    clear()
    set_all(255, 0, 128, 1.0)
    show()
else:
    print("I don't know that colour")

blinkt.set_clear_on_exit()



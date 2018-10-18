#!/usr/bin/env python

'''
A very basic script to take a user's input and display their chosen colour.
'''


import blinkt
import time

blinkt.clear()
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

while True:
    if ledcolour == "red":
        print("255, 0, 0")
        blinkt.clear()
        blinkt.set_all(255, 0, 0, 1.0)
        blinkt.show()
    elif ledcolour == "green":
        print("0, 255, 0")
        blinkt.clear()
        blinkt.set_all(0, 255, 0, 1.0)
        blinkt.show()
    elif ledcolour == "blue":
        print("0, 0, 255")
        blinkt.clear()
        blinkt.set_all(0, 0, 255, 1.0)
        blinkt.show()
    elif ledcolour == "yellow":
        print("255, 255, 0")
        blinkt.clear()
        blinkt.set_all(255, 255, 0, 1.0)
        blinkt.show()
    elif ledcolour == "cyan":
        print("0, 255, 255")
        blinkt.clear()
        blinkt.set_all(0, 255, 255, 1.0)
        blinkt.show()
    elif ledcolour == "magenta":
        print("255, 0, 255")
        blinkt.clear()
        blinkt.set_all(255, 0, 255, 1.0)
        blinkt.show()
    elif ledcolour == "pink":
        print("255, 0, 128")
        blinkt.clear()
        blinkt.set_all(255, 0, 128, 1.0)
        blinkt.show()
    else:
        print("I don't know that colour")

blinkt.set_clear_on_exit()




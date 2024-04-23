#!/usr/bin/env python

while True:
    i = input("Input the number(q: Quit) : ")
    if i == "q":
        break
    elif i.isalpha():
        print("Please enter a number")
    else:
        if int(i) > 0:
            print("positive")
        elif i < 0:
            print("negative")
        else:
            print("zero")



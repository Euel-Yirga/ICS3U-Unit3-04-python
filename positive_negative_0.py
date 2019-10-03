#!/usr/bin/env python3

# Created by: Euel Yirga
# Created on: Sept 2019
# This program says if a number is positive or negative


def main():
    # input
    number = int(input("Please enter a positive or negative number: "))

    # process
    if number < 0:
        # output
        print()
        print("-")

    # process
    elif number == 0:
        # output
        print()
        print("0")

    # process
    else:
        # output
        print()
        print("+")


if __name__ == "__main__":
    main()
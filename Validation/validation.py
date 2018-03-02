#!/usr/bin/env python3

def get_float(prompt, low, high):
    while True:
        number = float(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low, 
                    "and less than or equal to", high)

def get_int(prompt, low, high):
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low,
                    "and less than or equal to", high)

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input
        valid_number = get_float("Enter number: ", 0, 1000)
        print("Valid number = ", valid_number)
        print()
        valid_number = get_int("Enter integer: ", 0, 50)
        print("valid integer = ", valid_number)
        print()

        # see if the user wants to continue
        choice = input("Repeat? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__maine__":
    main()
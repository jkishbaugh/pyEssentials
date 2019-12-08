#!/usr/bin/env python3

def main():
    num1 = int(input("Choose a number..."))
    num2 = int(input("Choose a second number..."))
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
    print(num1 % num2)

    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 < num2:
        print(f"{num1} is less than {num2}")
    elif num1 == num2:
        print(f"{num2} is equal to {num2}")

    aList = list(range(100))
    if num1 in aList and num2 in aList:
        print("Both numbers are in the list")
    elif num1 in aList and num2 not in aList:
        print(f"{num1} is in the list but not {num2}")
    elif num2 in aList and num1 not in aList:
        print(f"{num2} is in the list but not {num1}")
    elif num1 not in aList and num2 not in aList:
        print(f"Neither number is in the list.")

if __name__ == '__main__': main()

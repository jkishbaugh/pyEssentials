#!/usr/bin/env python3

import platform


def main():
    # Create two variables and assign a number to one variable and a string to the other.
    num = 5
    typenum = type(num)
    hello = "this is variable named hello is a  "
    typehello = type(hello)
    # Print out both variables with the variable types.
    print("{} is a {}".format(num, typenum))
    print("{} {}".format(hello, typehello))
    # Create two more variables and assign a number to each variable.
    x = 7
    y = 7
    # Now write an if elif else control structure
    if x > y:
        print("x:{} > y:{}".format(x, y))
    elif x < y:
        print("x:{} < y:{}".format(x, y))
    elif x == y:
        print("x:{} == y:{}".format(x, y))
    else:
        print("Something unknown occurs")
    # Call this function twice from the main function.
    # Once using the values 1 and 10.
    number_printer(1, 10)
    # Once using any values you like.
    number_printer(35, 40)
    # Call this class from the main function and print the type of pet and the sound it makes.
    fav = housePet()
    fav.animal()
    fav.noise()

# Define a new function with:
# It needs to accept two arguments.
def number_printer(x, y):
    # It needs to print out all the numbers between the first number and the second number.
    if x < y:
        while x <= y:
            print(x)
            x += 1
    elif x >= y:
        while y < x:
            print(y)
            y += 1


# Define a simple class called housePet with:
class housePet:
    # Two variables:
    # One that sets the type of pet as your favorite type of pet.
    favoriteType = "sloth"
    # One that sets what sound that pet makes.
    sound = "squeal"

    # Two functions:
    # One to print what type of pet in the type variable.
    def animal(self):
        print(self.favoriteType)

    # One to print what sound that pet makes.
    def noise(self):
        print(self.sound)


if __name__ == '__main__': main()

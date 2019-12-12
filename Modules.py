#!usr/bin/env python3

import math

def main():
    rad = float(input("Please enter the length of the radius. "))
    volume = (4/3) * (math.pi * rad ** 3)
    surface_area = 4 * (math.pi * rad ** 3)
    print(f'Volume is {round(volume, 2)}')
    print(f'Surface area is {round(surface_area, 2)}')


if __name__ == "__main__": main()
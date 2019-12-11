#!/usr/bin/env python3

def main():
    temp = int(input("What is the temperature (in Fahrenheit)? "))
    wind_speed = int(input("What is the wind speed(mph) ?"))
    print(windChill(temp, wind_speed))


def windChill(temp, speed):
    chill = 35.74 + (0.6125 * temp) - (35.75 * speed ** 0.16) + (0.4275 * temp * speed ** 0.16)
    return chill

if __name__ == '__main__':main()
#!/usr/bin/env python3

temp = input("What is the weather like today?").lower()
inputString = 'You should wear {} today'
if temp == 'hot':
    print(inputString.format('sandals'))
elif temp == 'rain':
    print(inputString.format('galoshes'))
elif temp == 'snow':
    print(inputString.format('boots'))
else:
    print("I have no recommendation. Decide for yourself which shoes to wear.")

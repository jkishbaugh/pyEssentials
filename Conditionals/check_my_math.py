#! usr/bin/env python3

num1 = int(input("choose your first number"))
num2 = int(input('choose second number'))
operation = input("What operation are we performing( +, -, *, /)? ")
answer = int(input('What is the answer? '))

if operation == '+':
    sum = num2 + num1
    correct = answer == sum
    print('You are correct!') if correct else print('Incorrect. Please try again.')
elif operation == '-':
    diff = num1 - num2
    correct = answer == diff
    print('You are correct!') if correct else print('Incorrect. Please try again.')
elif operation == '*':
    prod = num1 * num2
    correct = answer == prod
    print('You are correct!') if correct else print('Incorrect. Please try again.')
elif operation =="/":
    quot = num1/num2
    correct = answer == quot
    print('You are correct!') if correct else print('Incorrect. Please try again.')

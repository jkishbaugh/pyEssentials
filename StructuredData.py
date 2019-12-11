#!/usr/bin/env python3


def main():
    fruit_list = ['Apples', 'Pears', 'Oranges', "Peaches"]
    print(fruit_list)
    # Ask the user for another fruit and add it to the end of the list.
    newFruit = input("What is your favorite fruit? ")
    fruit_list.append(newFruit)
    print(fruit_list)
    # Add another fruit to the beginning of the list using insert() and display the list.
    fruit_list.insert(0, "grapes")
    print(fruit_list)
    length_fruit_list = len(fruit_list)
    num = int(input(f"Please pick a number between  1 and {length_fruit_list} "))
    print(f"{num}: {fruit_list[num - 1]}")
    # Display all the fruits using a for loop.
    for fruit in fruit_list:
        print(fruit)
    # Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
    chris = dict(name= 'Chris', city= 'Seattle', cake= 'Chocolate')
    # Display the dictionary.
    print_dict(chris)
    # Delete the entry for “cake” by using the pop() method.
    chris.pop('cake')
    # Display the dictionary.
    print_dict(chris)
    # Add an entry for “fruit” with “Mango” and display the dictionary.
    chris['fruit'] = "Mango"
    # Display the dictionary keys.
    for k in chris.keys(): print(k)
    # Display the dictionary values.
    for v in chris.values(): print(v)
    # Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    print('cake' in chris.keys())
    # Display whether or not “Mango” is a value in the dictionary.
    print('Mango' in chris.values())
    # Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4,
    all_numbers = set(range(21))
    s2 = set(x for x in all_numbers if x % 2 == 0)
    s3 = set(x for x in all_numbers if x % 3 == 0)
    s4 = set(x for x in all_numbers if x% 4 == 0)
    # so that s2 contains numbers divisible by 2, s3 contains numbers divisible by 3,
    # and s4 contains numbers divisible by 4.
    # Display the sets.
    print_set(s2)
    print_set(s3)
    print_set(s4)
    # Display the union of s2 and s3, that is the numbers that are in either set.
    print_set(s2 | s3)
    # Display the intersection of s3 and s4, that is the numbers that are in both sets.
    print_set(s3 & s4)

def print_dict(obj):
    for k, v in obj.items(): print(f'{k}: {v}')


def print_set(obj):
    print('{', end='')
    for x in obj: print(x, end=' ')
    print('}')


if __name__ == '__main__': main()

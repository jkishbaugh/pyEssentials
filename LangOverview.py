#!/usr/bin/env python3

import platform


def main():
    num = 5
    hello = "this is a string {}".format(num)
    print(hello)


if __name__=='__main__':main()
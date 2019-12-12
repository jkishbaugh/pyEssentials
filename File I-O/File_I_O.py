#!usr/bin/env python3


def main():
    p1 = open("p1.txt", 'rt')
    p2 = open('p2.txt', 'rt')
    output = open('p3.txt', 'wt')

    for line_1, line_2 in zip(p1, p2):
        print(line_1.rstrip(), file=output)
        print("1", end="")
        print(line_2.rstrip(), file=output)
        print("2", end="")


if __name__ == '__main__': main()

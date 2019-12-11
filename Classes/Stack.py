#!/usr/bin/env python3


class Stack:
    # the three methods your class will need will be
    def __init__(self):
        self._stack = list()

    def push(self, val):
        if val: self._stack.append(val)
        print(self._stack)

    def pop(self):
        try:
            self._stack[0]
        except:
            print("All done. Pat yourself on the back.")
        else:
            print(self._stack.pop())


def main():
    stack = Stack()
    stack.push("Me First!!!")
    stack.push("No it's my turn.")
    stack.push(78)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()


if __name__ == '__main__': main()
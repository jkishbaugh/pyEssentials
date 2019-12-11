#!/usr/bin/env python3

class Queue:
    # init__: to initialize your Queue (think: how will you store the queue’s elements? You’ll need to initialize an appropriate object attribute in this method)
    def __init__(self):
        self._queue = list()

    # insert: inserts one element in your Queue
    def add(self, val):
        if val: self._queue.append(val)
        return self._queue

    # remove: removes one element from your Queue and returns it. If the queue is empty, return a message that says
    # it is empty.
    def remove(self):
        try:
            self._queue[0]
        except:
            return "All caught up. The queue is empty."
        else:
            return self._queue.pop(0)


def main():
    q = Queue()
    print(q.add(9))
    print(q.add("No not me"))
    print(q.add(54))
    print(q.remove())
    print(q.remove())
    print(q.remove())
    print(q.remove())

if __name__ == '__main__': main()

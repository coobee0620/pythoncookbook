#!/usr/bin/env python

# 怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次pop操作总是返回优先级最高的那个元素
# 利用元组比较大小
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def iterator(self):
        length = len(self._queue)
        counter = 0
        while True:
            yield self.pop()
            counter += 1
            if counter >= length:
                return


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

for x in q.iterator():
    print(x)

# 利用元祖比较大小
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
d = (4, 3, Item('spam'))

print(a > b)
print(d>a)
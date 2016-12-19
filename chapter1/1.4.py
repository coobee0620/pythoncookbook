#!/usr/bin/env python

# 怎样从一个集合中获得最大或者最小的N个元素列表？

import heapq

# 注意
# 当要查找的元素个数相对比较小的时候，函数 nlargest() 和 nsmallest() 是很合适的。
# 如果N的大小和集合大小接近的时候，通常先排序这个集合然后再使用切片操作会更快点 ( sorted(items)[:N] 或者是 sorted(items)[-N:] )。
# 需要在正确场合使用函数 nlargest() 和 nsmallest() 才能发挥它们的优势 (如果N快接近集合大小了，那么使用排序操作会更好些)。
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)

print(sorted(nums)[-3:])

def order(aaa):
    len1 = len(aaa)
    counter = 0
    while True:
        if counter == 0:
            heapq.heapify(aaa)
        a = heapq.heappop(aaa)
        yield a
        counter += 1
        if counter >= len1:
            return


o = order(nums)

for x in o:
    print(x)

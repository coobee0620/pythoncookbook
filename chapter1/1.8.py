#!/usr/bin/env python

# 怎样在数据字典中执行一些计算操作(比如求最小值、最大值、排序等等)？

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
    'CD': 10.75
}
# zip() 函数先将键和值反转过来
# zip() 函数创建的是一个只能访问一次的迭代器
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
print(max_price)

# 等效做法

min_key = min(prices, key=lambda k: prices[k])
min_value = prices[min_key]
max_key = max(prices, key=lambda k: prices[k])
max_value = prices[max_key]

print((min_key,min_value),(max_key,max_value))
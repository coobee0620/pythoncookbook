#!/usr/bin/env python

# 你的程序已经出现一大堆已无法直视的硬编码切片下标，然后你想清理下代码。

###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])

print(cost)

SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)


a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)
s = 'HelloWorld'
print(a.indices(len(s)))
print(range(*a.indices(len(s))))
for i in range(*a.indices(len(s))):
    print(s[i])
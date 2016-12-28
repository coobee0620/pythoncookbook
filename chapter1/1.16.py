#!/usr/bin/env python

# 过滤序列元素

mylist = [1, 4, -5, 10, -7, 2, 3, -1, 0]

# 简单方案，列表推导
# 使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量内存。
print([n for n in mylist if n > 0])

print([n for n in mylist if n < 0])

# 内存敏感，利用生成器迭代
f = (n for n in mylist if n > 0)
print(f)
for x in f:
    print(x)

f =(n for n in mylist if n < 0)
print(f)
for x in f:
    print(x)

# 使用内建的 filter() 函数
# 复杂过滤规则
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(values)
print(ivals)

# 过滤操作的一个变种：将不符合条件的值用新值代替，而非丢弃
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_neg)




addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
# compress返回一个迭代器，如果需要得到列表使用list()
f = list(compress(addresses, more5))
print(f)
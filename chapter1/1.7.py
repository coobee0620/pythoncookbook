#!/usr/bin/env python

# 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。

from collections import OrderedDict

# 一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。
# 所以如果你要构建一个需要大量 OrderedDict 实例的数据结构的时候(比如读取100,000行CSV数据到一个 OrderedDict 列表中去)
# 那么你就得仔细权衡一下是否使用 OrderedDict 带来的好处要大过额外内存消耗的影响。
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

print("--------")
dictionar = {'foo': 1, 'bar': 2, 'spam': 3, 'grok': 4}
for key in dictionar:
    print(key, d[key])

#!/usr/bin/env python

# 你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。

import operator

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=operator.itemgetter('fname'))
rows_by_uid = sorted(rows, key=operator.itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))
print(rows_by_fname)
print(rows_by_uid)



min(rows, key=operator.itemgetter('uid'))
max(rows, key=operator.itemgetter('uid'))
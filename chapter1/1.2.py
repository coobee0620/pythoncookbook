#!/usr/bin/env python

import math

# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才能从这个可迭代对象中解压出N个元素出来？
# 不确定参数

def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

def avg(nums):
    return sum(nums)/len(nums)

print(drop_first_last((1.1,2.2,3.3,4.4,5.5,6.6,7.7)))


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)


sales_record = [1,2,3,4,5,6,7,8]
*trailing_qtrs, current_qtr = sales_record
trailing_avg = avg(trailing_qtrs)
print(trailing_avg)
print(trailing_avg/current_qtr)


records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
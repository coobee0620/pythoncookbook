#!/usr/bin/env python

# 你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的代码难以阅读， 于是你想通过名称来访问元素。
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

sub1 = Subscriber('sub1@example.com', '2012-10-20')
sub2 = Subscriber('sub2@example.com', '2012-10-21')

dict()
#!/usr/bin/env python

# 你想排序类型相同的对象，但是他们不支持原生的比较操作。

import operator
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    # 原生方案
    print(sorted(users, key=lambda u: u.user_id))
    # attrgetter
    print(sorted(users, key=operator.attrgetter('user_id')))
    print(min(users, key=operator.attrgetter('user_id')))
    print(max(users, key=operator.attrgetter('user_id')))

sort_notcompare()


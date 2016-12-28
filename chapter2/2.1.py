#!/usr/bin/env python

# 你需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格)并不是固定的。

import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
fields = re.split(r'[;,\s]\s*', line)
print(fields)
fields =re.split(r'(;|,|\s)\s*', line)
print(fields)

values = fields[::2]
print(values)
delimiters = fields[1::2] + ['']
print(delimiters)

print(''.join(v+d for v,d in zip(values, delimiters)))
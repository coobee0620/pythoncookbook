#!/usr/bin/env python

# 你正在使用正则表达式处理文本，但是关注的是Unicode字符处理。

import re
num = re.compile('\d+')
print(num)
print(num.match('123'))

print(num.match('\u0661\u0662\u0663'))
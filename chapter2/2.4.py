#!/usr/bin/env python

# 你想匹配或者搜索特定模式的文本

text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
print(text == 'yeah')

# Match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))
# Search for the location of the first occurrence
print(text.find('no'))

import re
# 对于复杂的匹配需要使用正则表达式和 re 模块
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
# Simple matching: \d+ means match one or more digits

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))


# 在定义正则式的时候，通常会利用括号去捕获分组
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(0))
print(m.group(1))
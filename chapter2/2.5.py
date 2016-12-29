#!/usr/bin/env python

# 你想在字符串中搜索和匹配指定的文本模式

text = 'yeah, but no, but yeah, but no, but yeah'
text1 = text.replace('yeah', 'yep')
print(text1)

import re
# 对于复杂的模式，请使用 re 模块中的 sub() 函数
# sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字比如 \3 指向前面模式的捕获组号。
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
text1 = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text1)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
text1 = datepat.sub(r'\3-\1-\2', text)
print(text1)

#!/usr/bin/env python

# 你正在处理Unicode字符串，需要确保所有字符串在底层有相同的表示。
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1==s2)
print(len(s1))
print(len(s2))

# 以使用unicodedata模块先将文本标准化
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))
print(ascii(t2))

t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFD', s2)
print(t1 == t2)
print(ascii(t1))
print(ascii(t2))
# NFC表示字符应该是整体组成(比如可能的话就使用单一编码)，而NFD表示字符应该分解为多个组合字符表示
#!/usr/bin/env python

# 你需要以忽略大小写的方式搜索与替换文本字符串
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
# 一个小缺陷，替换字符串并不会自动跟被匹配字符串的大小写保持一致
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace


print(text)
print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

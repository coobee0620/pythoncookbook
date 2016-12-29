#!/usr/bin/env python

# 你想去掉文本字符串开头，结尾或者中间不想要的字符，比如空白。

# Whitespace stripping
s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))
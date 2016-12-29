#!/usr/bin/env python

# 你正在试着用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹配。 而你想修改它变成查找最短的可能匹配。
import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

# 在这个例子中，模式 r'\"(.*)\"' 的意图是匹配被双引号包含的文本。
# 但是在正则表达式中*操作符是贪婪的，因此匹配操作会查找最长的可能匹配。
# 于是在第二个例子中搜索 text2 的时候返回结果并不是我们想要的。
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

# 为了修正这个问题，可以在模式中的*操作符后面加上?
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
# 通过在 * 或者 + 这样的操作符后面添加一个 ? 可以强制匹配算法改成寻找最短的可能匹配。
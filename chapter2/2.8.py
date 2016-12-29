#!/usr/bin/env python

# 你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配。
import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
        multiline comment */
        '''
print(comment.findall(text1))

print(comment.findall(text2))
# 为了修正这个问题，你可以修改模式字符串，增加对换行的支持
# (?:.|\n) 指定了一个非捕获组 (也就是它定义了一个仅仅用来做匹配，而不能通过单独捕获或者编号的组)。
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))


# re.compile() 函数接受一个标志参数叫 re.DOTALL ，在这里非常有用。 它可以让正则表达式中的点(.)匹配包括换行符在内的任意字符
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2)) # 同样效果

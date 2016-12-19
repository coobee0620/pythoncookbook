#!/usr/bin/env python

# 现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N个变量？
p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)
print(date)

name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(data)
print(shares)
print(price)

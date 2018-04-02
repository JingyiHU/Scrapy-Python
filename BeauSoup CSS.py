#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:29:00 2018

@author: hujingyi
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has chinese, apply decode()

html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
print(html)

# 按照class匹配，找所有 class=month 的信息. 并打印出它们的 tag 内文字.

soup = BeautifulSoup(html, 'lxml')

# use class to de narrow search

month = soup.find_all('li',{"class": "month"})
for m in month:
    print(m.get_text())
    
# 找到 class=jan 的信息. 然后在 <ul> 下面继续找 <ul> 内部的 <li> 信息. 这样一层层嵌套的信息, 非常容易找到.
    
jan = soup.find('ul', {"class": "jan"})

# use jan as a parent
d_jan = jan.find_all('li')

for d in d_jan:
    print(d.get_text())

#单双引号无明显差别
#用get_text（）可以读来tag之间的内容
# find(‘这里是标签名’， {这里是标签的属性}) 只存在一个用find
# 存在多个用find_all
# 可以在前面的基础上再次用findall继续找结果
    

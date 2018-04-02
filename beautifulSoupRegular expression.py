#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:51:44 2018

@author: hujingyi
"""

# 读取网页，导入正则表达式模块

from bs4 import BeautifulSoup 
from urllib.request import urlopen

import re

html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')

print(html)

# 找到所有的图片 发现所有的图片的tag名都为img 只是可能图片的格式不同 jpg或者png

# 如果只挑选jpg形式的图片

soup = BeautifulSoup(html, 'lxml')

img_links = soup.find_all("img", {"src": re.compile(".*?.jpg")})

for link in img_links:
    print(link['src'])
    


#'.*?\.jpg' 这样写也是对的 在句号之前加了一个反向的slash
    
# 选一些课程的链接, 而这些链接都有统一的形式, 就是开头都会有 https://morvan.

course_links = soup.find_all("a", {"href": re.compile("https://morvanzhou.*")})
for link in course_links:
    print(link['href'])
    
# 总结：
# a = soup.find_all("这里写标签名",{"这里写属性名"：re.compile("这里写匹配的正则表达式")})
# for B in a:
#   print(B['属性名'])
    
    
    
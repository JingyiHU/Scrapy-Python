#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:18:06 2018

@author: hujingyi
"""

from bs4 import BeautifulSoup

from urllib.request import urlopen

# if has chinese, use decode()

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)

soup = BeautifulSoup(html, features = 'lxml')
print(soup.h1)

print("\n", soup.p)

# 找到所有的链接，能用像 Python 字典的形式, 用 key 来读取 l["href"].

all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print("\n", all_href)

#result:
#['https://morvanzhou.github.io/', 'https://morvanzhou.github.io/tutorials/data-manipulation/scraping/']
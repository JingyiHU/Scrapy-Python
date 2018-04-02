#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 17:32:45 2018

@author: hujingyi
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = "https://baike.baidu.com"

# 将 /item/... 的网页都放在 his 中, 做一个备案, 记录我们浏览过的网页.
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

# 先不用循环, 对一个网页进行处理, 走一遍流程, 然后加上循环, 让我们的爬虫能在很多网页中爬取

# 在屏幕上打印出来我们现在正在哪张网页上, 网页的名字叫什么.

url = base_url + his[-1]

html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, features = 'lxml')
print(soup.find('h1').get_text(), '     url: ', his[-1])

# =============================================================================
# 接下来我们开始在这个网页上找所有符合要求的 /item/ 网址. 
# 使用一个正则表达式(正则教程) 过滤掉不想要的网址形式. 
# 这样我们找到的网址都是 /item/%xx%xx%xx... 这样的格式了. 
# 之后我们在这些过滤后的网页中随机选一个, 当做下一个要爬的网页. 
# 不过有时候很不幸, 在 sub_urls 中并不能找到合适的网页, 我们就往回跳一个网页, 
# 回到之前的网页中再随机抽一个网页做同样的事.
# =============================================================================

# find valid urls

# exemple: <a target=_blank href="/item/%E8%9C%98%E8%9B%9B/8135707" data-lemmaid="8135707">
sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

if len(sub_urls) != 0:
    his.append(random.sample(sub_urls, 1)[0]["href"]) 
    #这句感觉像是从0位置开始放，随机找一个放进去？-1位置是一开始初始的那个网页
    #这里不管是单双引号最后结果都是 网址在单引号里面 包着
else:
    #no valid sub link found
    his.pop()
print(his)

# 接下来，有了上面这个操作，我们就可以把它放在一个for循环里，让它在不同的网页跳来跳去
















#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 15:57:52 2018

@author: hujingyi
"""

from urllib.request import urlopen

#if is chinese, apply decode()

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')

print(html)

# find the page title

import re

# =============================================================================
# res = re.findall(r"<title>(.+?)<\title>", html)
# print("\npage title is : ", res[0]) 这个错误是因为slash打反了
# =============================================================================

res = re.findall(r"<title>(.+?)</title>", html)
print("\npage title is: ", res[0])

##### find all the links 

res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)


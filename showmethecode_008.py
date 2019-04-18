#! /usr/bin/env python
# -*- Coding: utf-8 -*-
# 第 0008 题：一个HTML文件，找出里面的正文。
from goose import Goose
from goose.text import StopWordsChinese
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
url = "https://blog.csdn.net/huangxiongbiao/article/details/45871865"
def extract(url):
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=url)
    return article.cleaned_text
if __name__ == '__main__':
    print (extract(url))
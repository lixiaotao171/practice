#! /usr/bin/env python
# -*- Coding: utf-8 -*-
# 敏感词文本文件
# filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出Freedom，否则打印出HumanRights。
filtered_words = ["北京","程序员","公务员","领导","牛比","牛逼","你娘","你妈","love","sex","jiangge"]
s = input("输入:\n")
count = 0
for i in filtered_words:
    if i in s:
        print("Freedom")
    else:
        count += 1
if count == len(filtered_words):
    print("HumanRights")



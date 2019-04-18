#! /usr/bin/env python
# -*- Coding: utf-8 -*-
'''
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
思路：遍历给出目录下的图片，把大于iPhone5分辨率的图片都进行缩放。使用Python的PIL
库对图片进行处理，IPhone5屏幕分辨率为640 × 1136，将大于该分辨率的图片按照一定比例缩放至适合大小并保存。
'''
import image, os
MyPath = ""
OutPath = ""
#定义一个函数：输入图片，获取图片的长和宽与iphone5比较
def Picture_Compare(s):
    image.
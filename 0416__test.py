#coding=utf-8
'''
from time import sleep
import requests
s = input("请主人输入话题：")
while True:
 resp = requests.post("http://www.tuling123.com/openapi/api",data={"key":"4fede3c4384846b9a7d0456a5e1e2943", "info": s, })
 resp = resp.json()
 sleep(1)
 print('小鱼：', resp['text'])
 s = resp['text']
 resp = requests.get("http://api.qingyunke.com/api.php", {'key': 'free', 'appid': 0, 'msg': s})
 resp.encoding = 'utf8'
 resp = resp.json()
 sleep(1)
 print('菲菲：', resp['content'])

from PIL import Image
im = Image.open("d:/1.jpg")
images = []
images.append(Image.open('d:/2.jpg'))
images.append(Image.open('d:/3.jpg'))
im.save('gif.gif', save_all=True, append_images=images, loop=1, duration=1, comment=b"aaabb")

import requests
r = requests.get("http://www.baidu.com/")
print (r.text)

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格
def rm_str_blank():
    s = input("输入一串字符:")
    s1 = s         #输入字符
    for i in range(0,len(s)):
        if s[i] == " ":
            s1 = s[i+1:]
        else:
            break
    s2 = s1
    for i in range(len(s1)):
        if s1[len(s1)-i-1] == " ":
            s2 = s1[:len(s1)-i-1]
        else:
            break
    return s2
print (rm_str_blank())

#杨辉三角
def triangles():
    l = [1]
    for i in range(int):
        l.append(i)
'''
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def change_list_size(s):
    l=[]
    for i in s:
        i.title()
        l.append(i)
L = ['adam','LISA','barT']
map(change_list_size(),L)




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
'''
import requests
r = requests.get("http://www.baidu.com/")
print (r.text)
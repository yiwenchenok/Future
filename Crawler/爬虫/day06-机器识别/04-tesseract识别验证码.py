#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 04-tesseract识别验证码.py
import pytesseract
from PIL import Image

image = Image.open('img.png')

#灰化处理
lim = image.convert("L")
lim.save("lim.png")

#二值化处理
xx = 160
table = []
for i in range(256):
    if i < xx:
        table.append(0)
    else:
        table.append(1)

bim = lim.point(table,'1')
bim.save("bim.png")

text = pytesseract.image_to_string(image,"chi_sim")
print(text)
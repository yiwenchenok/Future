#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 03-tesseract识别中文.py
import pytesseract
from PIL import Image  # pip install pillow

image = Image.open("2.png")
text = pytesseract.image_to_string(image,'chi_sim')  #默认识别英文
print(text)

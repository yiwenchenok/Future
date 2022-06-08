#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 02-tesseract识别英文.py
import pytesseract
from PIL import Image  # pip install pillow

image = Image.open("this.png")
text = pytesseract.image_to_string(image)
print(text)

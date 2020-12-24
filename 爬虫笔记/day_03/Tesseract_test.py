#机器视觉
#将图片翻译成文字一般称为文字识别（OCR）
#Tesseract是一个OCR库

from pytesseract import *

#图片处理库
from PIL import Image

image=Image.open('1.png')

text=image_to_string(image)

print(text)
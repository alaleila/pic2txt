# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 17:17:52 2018

@author: YHF
"""

#作者微信：2501902696 
from PIL import Image 
import pytesseract 
#上面都是导包，只需要下面这一行就能实现图片文字识别 
text = pytesseract.image_to_string(Image.open('test_01.jpg'),lang='chi_sim') 
print(text)


#用于测试github有无更新
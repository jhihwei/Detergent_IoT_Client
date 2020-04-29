import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
with open(dir_path+'\.log', 'r', encoding='utf8') as f:
    text = f.readline()
    print(text)

from PIL import Image
import pytesseract
img = Image.open('rpiDesktop.jpg')
text = pytesseract.image_to_string(img, lang='eng')
print("123")
print(text)
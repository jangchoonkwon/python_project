# -*- encoding: utf8 -*-
import cv2
import os
import re

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# 설치한 tesseract 프로그램 경로 (64비트)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


# 32비트인 경우 => r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def imgtxt(img):
    image = cv2.imread(img)  # 이미지 불러오기
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Gray 프로세싱
    filename = '{}.png'.format(os.getpid())  # 글자 프로세싱을 위해 Gray 이미지 임시파일 형태로 저장.
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename), lang='kor')  # Simple image to string
    text = text.strip()
    text = text.replace(" ", "")
    os.remove(filename)
    print(text)
    with open("D:/FineTec/DailyLoss/ocr/test.txt", 'a') as f:
        f.write(text + '\n')

    cv2.imshow('Image', image)
    cv2.waitKey(0)


# 주간	2	3	4	5	7	8	9	10	16	17	18	19

trgImg = "d:/FineTec/DailyLoss/ocr/cs_name.png"
# trgImg = "d:/FineTec/DailyLoss/ocr/20220613-1.png"
# schImg =
imgtxt(trgImg)

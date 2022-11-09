# -*- coding: utf-8 -*-
import shutil

import re, os, time, cv2, csv
from typing import List, Any

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def name_list_roi(dir):
    file_list = os.listdir(dir)
    index = 0
    for f_name in file_list:
        img = os.path.join(dir, f_name)
        img = cv2.imread(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray', gray)
        cv2.waitKey(1000)
        height = img.shape[0]
        width = img.shape[1]
        mid_y = height / 2
        mid_x = width / 2
        offset_y = 304  #5월까지 296
        offset_x = -252
        y1 = int(mid_y + offset_y)
        x1 = int(mid_x + offset_x)
        rows = 108  #5월까지 106
        cols = 450
        y2 = y1 + rows
        x2 = x1 + cols
        roi = img[y1:y2, x1:x2]
        text = pytesseract.image_to_string(roi, lang='kor')
        time.sleep(2)
        roi1 = img[y1 + 4:y2 + 10, x1:x2 - 400]
        roi2 = img[y1 + 0:y2 + 10, x1 + 130:x2 - 264]
        roi3 = img[y1 + 4:y2 + 10, x2 - 186:x2 - 134]
        roi4 = img[y1 + 4:y2 + 10, x2 - 52:x2]

        n_list = []
        text1 = pytesseract.image_to_string(roi1, lang='kor')
        text1 = text1.replace(" ", "")
        text1 = re.findall('\w+', text1)
        cv2.imshow('Image', roi1)
        cv2.waitKey(1000)
        print(text1)
        n_list = n_list + text1

        text2 = pytesseract.image_to_string(roi2, lang='kor')
        text2 = text2.replace(" ", "")
        text2 = re.findall('\w+}', text2)
        cv2.imshow('Image', roi2)
        cv2.waitKey(1000)
        print(text2)
        n_list = n_list + text2

        text3 = pytesseract.image_to_string(roi3, lang='kor')
        text3 = text3.replace(" ", "")
        text3 = re.findall('\w+', text3)
        cv2.imshow('Image', roi3)
        cv2.waitKey(1000)
        print(text3)
        n_list = n_list + text3

        text4 = pytesseract.image_to_string(roi4, lang='kor')
        text4 = text4.replace(" ", "")
        text4 = re.findall('\w+', text4)
        cv2.imshow('Image', roi4)
        cv2.waitKey(1000)
        print(text4)
        n_list = n_list + text4
        print(n_list)

        # n_list: List[Any] = re.findall('[가-힣]{3}', text)
        # f_name = '{}'.format(f_name[:-4])
        # d_list = [f_name]
        # sum_list = d_list + n_list

        # time.sleep(1)
        # print(index)
        # print(sum_list)

        with open('d:/FineTec/ocr/CS_name_roi.csv', 'a', newline='', encoding='cp949') as f:
            writer = csv.writer(f)
            writer.writerow(n_list)

        # cv2.imshow('Image', roi)
        # cv2.waitKey(1000)
        index += 1

if __name__ == "__main__":
    scr_dir_path = 'd:/FineTec/ocr/20220607'
    name_list_roi(scr_dir_path)
else:
    print("---------- module is running ---------")

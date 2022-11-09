import csv, os, re, time, cv2
from typing import List, Any

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

def cs_get_names(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    cv2.waitKey(1000)

    roi = gray[708:794, 30:474]
    cv2.imshow(roi)
    cv2.waitKey(0)

    text = pytesseract.image_to_string(roi, lang='kor')
    time.sleep(2)
    text = text.strip()

    del_dic = {' ': '', '\ㅣ': '', '\n': '', '': '', '확인': '', 'ㅣ메주': ''}
    for word, replacement in del_dic.items():
        text = text.replace(word, replacement)

    name_dic = {'깅이쉐': '김인식', '지성힌': '지성현', '김미촉': '김미숙', '의미애': '황미애', '고도빈': '고도원', '이령서': '김형석', '이료론': '이효현'}
    name_dic = List.sort(name_dic)
    for word, replacement in name_dic.items():
        text = text.replace(word, replacement)

    n_list: List[Any] = re.findall('[ㄱ-힣]{3}', text)

    time.sleep(1)
    print(n_list)

    with open("d:/FineTec/DailyLoss/ocr/20220519.csv", 'a', newline='', encoding='cp949') as file:
        writer = csv.writer(file)
        writer.writerow(n_list)

    cv2.imshow('Image', img)
    cv2.waitKey(1000)



if __name__ == "__main__":
    path_dir = "d:/FineTec/DailyLoss/ocr/20220519"
    path_Img = "20220519-joju-2.png"
    path_file = "20220519.csv"
    scrImg = os.path.join(path_dir, path_Img)
    saveName = os.path.join(path_dir, path_file)

    cs_get_names(scrImg)

else:
    print("--------- module running ---------")
import pyautogui as pag
import time, cv2, os, re

import getRng

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def go_date(xdt: object) -> str:
    """

    :rtype: object
    """
    pag.moveTo(1224, 500)
    pag.click
    pag.scroll(-1)
    time.sleep(1)
    pag.scroll(-1)
    time.sleep(1)
    center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/cs_top.png", confidence=0.85,
                                      region=(672, 800, 554, 1080 - 800))
    time.sleep(1)
    pag.click(center)
    # center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/cs_cal1.png", confidence=0.85, region=(672, 0, 554, 300))
    # pag.click(center)
    time.sleep(1)
    pag.moveTo(1205, 130, 0.5)
    pag.click()
    # center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/cs_cal2.png", confidence=0.85, region=(672, 100, 554, 100))
    # pag.click(center)
    time.sleep(1)
    pag.moveTo(1194, 174, 0.5)
    pag.click()
    time.sleep(1)
    center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/cs_cal3.png", confidence=0.85,
                                      region=(672, 300, 554, 500))
    pag.click(center)
    time.sleep(1)
    pag.typewrite('{0}.{1}.{2}.'.format(xdt[:2], xdt[2:4], xdt[-2:]))
    time.sleep(1)
    center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/cs_cal_cnf.png", confidence=0.9,
                                      region=(672, 600, 554, 400))
    pag.click(center)
    time.sleep(1)
    center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/cs_cal_sch.png", confidence=0.9,
                                      region=(672, 800, 554, 1080 - 800))
    pag.click(center)
    time.sleep(1)


# for i in xdate_list:
#     go_CS_date(i)
#     pag.moveTo(3048, 441)
#     time.sleep(10)

# go_CS_date("211214")

# cs_top = "D:/FineTec/DailyLoss/Loss_img/cs_top.png"
# cal1 = "D:/FineTec/DailyLoss/Loss_img/cs_cal1.png"
# cal2 = "D:/FineTec/DailyLoss/Loss_img/cs_cal2.png"
# cal3 = "D:/FineTec/DailyLoss/Loss_img/cs_cal3.png"
# cal_cnf = "D:/FineTec/DailyLoss/Loss_img/cs_cal_cnf.png"
# cal_sch = "D:/FineTec/DailyLoss/Loss_img/cs_cal_sch.png"


def catch_scroll(img, sch_region):
    time.sleep(1)
    p_list = pag.locateAllOnScreen(img, confidence=0.9, region=sch_region)
    p_list = list(p_list)
    print(p_list)
    p_list = p_list[0][0] + 100, p_list[0][1] - 3, p_list[0][2] + 370, p_list[0][3] + 8  # 사용하는 코드
    print(p_list)
    pag.screenshot("d:/FineTec/DailyLoss/ocr/cs_name.png", region=p_list)
    tgrImg = "d:/FineTec/DailyLoss/ocr/cs_name.png"
    time.sleep(3)
    image = cv2.imread(tgrImg)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filename = '{}.png'.format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename), lang='kor')

    del_dic = {
        ' ': '', '\ㅣ': '', '\n': '', '': '', '확인': '', 'ㅣ메주': '', "연상": "연장", "조줄": "조출", "조술": "조출", \
        "소술": "조출", "소줄": "조출", "소출": "조출", "\/": "7", "]": "1", "/": "7"
    }

    for word, replacement in del_dic.items():
        text = text.replace(word, replacement)

    text = re.sub("\n\|\”\"\.\s", "", text)
    text = re.sub("([ㄱ-힣]+.*)(\d{8})", "\\2", text)
    text = re.sub("(\d{8})([ㄱ-힣]+)(\d+)", "\\1-\\2-\\3", text)
    text = re.sub("(\d{8})([ㄱ-힣]+)(\d+)", "\\1-\\3-\\2", text)

    text = text.replace("--", "-").replace(".", "")
    # text = re.sub(r"([ㄱ-힣])-$", "\\1", text)
    # assert isinstance(text, object)
    outname = '{}.png'.format(text)

    time.sleep(1)
    outpath = "D:/FineTec/DailyLoss/ocr/cs_dn/"
    out_full_name = outpath + outname
    print(text)
    # with open(outpath + '{0}.{1}'.format("csSheet", "txt"), 'a', encoding='cp949') as f:
    #     f.write(out_full_name + '\n')
    assert isinstance(image, object)
    cv2.imshow('Image', image)
    cv2.waitKey(1)

    time.sleep(1)
    # p_click = pag.locateAllOnScreen(img, confidence=0.9, region=(672, 0, 554, 800))
    # assert isinstance(p_click, object)
    # p_click = list(p_click)
    # p_click = pag.moveTo(p_click[0][0] + 240, p_click[0][1] + 176)
    p_click = pag.locateCenterOnScreen("d:/FineTec/DailyLoss/ocr/cs_sheet.png", confidence=0.8,
                                       region=(672, p_list[1], 600, 500))
    # p_click = pag.locateCenterOnScreen(p_click, confidence=0.9, region=(672, 0, 554, 800))
    pag.click(p_click)
    time.sleep(7)
    pag.screenshot(out_full_name, region=(672, 170, 554, 800))
    time.sleep(1)
    pag.hotkey('ctrl', 'shift', '2')
    time.sleep(0.5)
    pag.press('right', presses=2)
    time.sleep(0.5)
    pag.press('enter')
    pag.moveTo(1220, 500)
    pag.click

    time.sleep(0.5)

    print(out_full_name + "  --> 캡쳐에 성공했습니다.")
    os.remove(tgrImg)


def catch_top(img, sch_region):
    time.sleep(2)
    p_list = pag.locateAllOnScreen(img, confidence=0.9, region=sch_region)
    p_list = list(p_list)
    p_list = p_list[0][0] + 100, p_list[0][1], p_list[0][2] + 370, p_list[0][3] + 8  # 사용하는 코드
    print(p_list)
    # p_list = p_list[0][0] + 100, p_list[0][1], p_list[0][2] + 340, p_list[0][3] - 100
    pag.screenshot("d:/FineTec/DailyLoss/ocr/cs_name.png", region=p_list)
    tgrImg = "d:/FineTec/DailyLoss/ocr/cs_name.png"
    time.sleep(3)
    image = cv2.imread(tgrImg)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filename = '{}.png'.format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename), lang='kor')

    del_dic = {
        ' ': '', '\ㅣ': '', '\n': '', '': '', '확인': '', 'ㅣ메주': '', "연상": "연장", "조줄": "조출", "조술": "조출", \
        "소술": "조출", "소줄": "조출", "소출": "조출", "\/": "7", "]": "1", "/": "7"
    }
    for word, replacement in del_dic.items():
        text = text.replace(word, replacement)

    text = re.sub("\n\|\”\"\.\s", "", text)
    text = re.sub("([ㄱ-힣]+.*)(\d{8})", "\\2", text)
    text = re.sub("(\d{8})([ㄱ-힣]+)(\d+)", "\\1-\\2-\\3", text)
    text = re.sub("(\d{8})([ㄱ-힣]+)(\d+)", "\\1-\\3-\\2", text)

    text = text.replace("--", "-").replace(".", "")
    # text = re.sub(r"([ㄱ-힣])-$", "\\1", text)
    # assert isinstance(text, object)
    outname = '{}.png'.format(text)

    time.sleep(1)
    outpath = "D:/FineTec/DailyLoss/ocr/cs_dn/"
    out_full_name = outpath + outname
    print(text)
    # with open(outpath + '{0}.{1}'.format("csSheet", "txt"), 'a', encoding='cp949') as f:
    #     f.write(out_full_name + '\n')
    assert isinstance(image, object)
    cv2.imshow('Image', image)
    cv2.waitKey(1)

    time.sleep(2)
    # p_click = pag.locateAllOnScreen(img, confidence=0.9, region=(672, 0, 554, 800))
    # assert isinstance(p_click, object)
    # p_click = list(p_click)
    # p_click = pag.moveTo(p_click[1][0] + 240, p_click[1][1] + 176)
    p_click = pag.locateCenterOnScreen("d:/FineTec/DailyLoss/ocr/cs_sheet.png", confidence=0.8,
                                       region=(672, p_list[1], 554, 300))
    pag.click(p_click)
    time.sleep(8)
    pag.screenshot(out_full_name, region=(672, 170, 554, 800))
    time.sleep(2)
    pag.hotkey('ctrl', 'shift', '2')
    time.sleep(1)
    pag.press('right', presses=2)
    time.sleep(1)
    pag.press('enter')
    pag.moveTo(1220, 500)
    pag.click

    # for i in range(2):
    #     pag.scroll(-2, 1)
    #     i += 1

    # pag.press(['down', 'down'])
    print(out_full_name + "  --> 캡쳐에 성공했습니다.")


def catch_middle(img, sch_region):
    time.sleep(2)
    p_list = pag.locateAllOnScreen(img, confidence=0.9, region=sch_region)
    p_list = list(p_list)
    p_list = p_list[1][0] + 100, p_list[1][1], p_list[1][2] + 370, p_list[1][3] + 8  # 사용하는 코드
    print(p_list)
    # p_list = p_list[0][0] + 100, p_list[0][1], p_list[0][2] + 340, p_list[0][3] - 100
    pag.screenshot("d:/FineTec/DailyLoss/ocr/cs_name.png", region=p_list)
    tgrImg = "d:/FineTec/DailyLoss/ocr/cs_name.png"
    time.sleep(3)
    image = cv2.imread(tgrImg)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filename = '{}.png'.format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename), lang='kor')

    del_dic = {
        ' ': '', '\ㅣ': '', '\n': '', '': '', '확인': '', 'ㅣ메주': '', "연상": "연장", "조줄": "조출", "조술": "조출", \
        "소술": "조출", "소줄": "조출", "소출": "조출", "\/": "7", "]": "1", "/": "7"
    }
    for word, replacement in del_dic.items():
        text = text.replace(word, replacement)

    text = re.sub("\n\|\”\"\.\s", "", text)
    text = re.sub("([ㄱ-힣]+.*)(\d{8})", "\\2", text)
    text = re.sub("(\d{8})([ㄱ-힣]+)(\d+)", "\\1-\\2-\\3", text)
    text = re.sub("(\d{8})([ㄱ-힣]+)(\d+)", "\\1-\\3-\\2", text)

    text = text.replace("--", "-").replace(".", "")
    # text = re.sub(r"([ㄱ-힣])-$", "\\1", text)
    # assert isinstance(text, object)
    outname = '{}.png'.format(text)

    time.sleep(1)
    outpath = "D:/FineTec/DailyLoss/ocr/cs_dn/"
    out_full_name = outpath + outname
    print(text)
    # with open(outpath + '{0}.{1}'.format("csSheet", "txt"), 'a', encoding='cp949') as f:
    #     f.write(out_full_name + '\n')
    assert isinstance(image, object)
    cv2.imshow('Image', image)
    cv2.waitKey(1)

    time.sleep(2)
    # p_click = pag.locateAllOnScreen(img, confidence=0.9, region=(672, 0, 554, 800))
    # assert isinstance(p_click, object)
    # p_click = list(p_click)
    # p_click = pag.moveTo(p_click[1][0] + 240, p_click[1][1] + 176)
    p_click = pag.locateCenterOnScreen("d:/FineTec/DailyLoss/ocr/cs_sheet.png", confidence=0.8,
                                       region=(672, p_list[1], 554, 300))
    pag.click(p_click)
    time.sleep(8)
    pag.screenshot(out_full_name, region=(672, 170, 554, 800))
    time.sleep(2)
    pag.hotkey('ctrl', 'shift', '2')
    time.sleep(1)
    pag.press('right', presses=2)
    time.sleep(1)
    pag.press('enter')
    pag.moveTo(1220, 500)
    pag.click

    # for i in range(2):
    #     pag.scroll(-2, 1)
    #     i += 1

    # pag.press(['down', 'down'])
    print(out_full_name + "  --> 캡쳐에 성공했습니다.")


def catch_bottom(img, sch_region):
    time.sleep(2)
    p_list = pag.locateAllOnScreen(img, confidence=0.9, region=sch_region)
    p_list = list(p_list)
    p_list = p_list[2][0] + 100, p_list[2][1], p_list[2][2] + 370, p_list[2][3] + 8  # 사용하는 코드
    # p_list = p_list[0][0] + 100, p_list[0][1], p_list[0][2] + 340, p_list[0][3] - 100
    pag.screenshot("d:/FineTec/DailyLoss/ocr/cs_name.png", region=p_list)
    tgrImg = "d:/FineTec/DailyLoss/ocr/cs_name.png"
    time.sleep(3)
    image = cv2.imread(tgrImg)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filename = '{}.png'.format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename), lang='kor')

    del_dic = {
        ' ': '', '\ㅣ': '', '\n': '', '': '', '확인': '', 'ㅣ메주': '', "연상": "연장", "조줄": "조출", "조술": "조출", \
        "소술": "조출", "소줄": "조출", "소출": "조출", "\/": "7", "]": "1", "/": "7"
    }
    for word, replacement in del_dic.items():
        text = text.replace(word, replacement)

    text = re.sub("\n\|\”\"\.\s", "", text)
    text = re.sub("([ㄱ-힣]+.*)(\d{8})", "\\2", text)
    text = re.sub("(\d{8})([ㄱ-힣]+)(\d+)", "\\1-\\2-\\3", text)
    text = re.sub("(\d{8})([ㄱ-힣]+)(\d+)", "\\1-\\3-\\2", text)

    text = text.replace("--", "-").replace(".", "")
    # text = re.sub(r"([ㄱ-힣])-$", "\\1", text)
    # assert isinstance(text, object)
    outname = '{}.png'.format(text)

    time.sleep(1)
    outpath = "D:/FineTec/DailyLoss/ocr/cs_dn/"
    out_full_name = outpath + outname
    print(text)
    # with open(outpath + '{0}.{1}'.format("csSheet", "txt"), 'a', encoding='cp949') as f:
    #     f.write(out_full_name + '\n')
    assert isinstance(image, object)
    cv2.imshow('Image', image)
    cv2.waitKey(1)

    time.sleep(2)
    # p_click = pag.locateAllOnScreen(img, confidence=0.9, region=(672, 0, 554, 800))
    # assert isinstance(p_click, object)
    # p_click = list(p_click)
    # p_click = pag.moveTo(p_click[2][0] + 240, p_click[2][1] + 176)
    p_click = pag.locateCenterOnScreen("d:/FineTec/DailyLoss/ocr/cs_sheet.png", confidence=0.8,
                                       region=(672, p_list[1], 554, 1080 - p_list[1]))
    pag.click(p_click)
    time.sleep(8)
    pag.screenshot(out_full_name, region=(672, 170, 554, 800))
    time.sleep(2)
    pag.hotkey('ctrl', 'shift', '2')
    time.sleep(1)
    pag.press('right', presses=2)
    time.sleep(1)
    pag.press('enter')
    pag.moveTo(1220, 500)
    pag.click

    # for i in range(2):
    #     pag.scroll(-2, 1)
    #     i += 1

    # pag.press(['down', 'down'])
    print(out_full_name + "  --> 캡쳐에 성공했습니다.")


def catch_click(img, outfile, srchRigon):
    time.sleep(1)
    # region=(left, top, length, width)
    # center = pag.locateCenterOnScreen(img, confidence=0.8, region=(srchRigon))
    # center = pag.locateCenterOnScreen(img, confidence=0.8, region=(srchRigon))
    center = pag.locateCenterOnScreen(img, confidence=0.8, region=(srchRigon))
    pag.click(center)
    time.sleep(4)
    pag.screenshot(outfile, region=(672, 170, 554, 800))
    time.sleep(1)
    pag.hotkey('ctrl', 'shift', '2')
    time.sleep(1)
    pag.press('right', presses=2)
    time.sleep(1)
    pag.press('enter')
    time.sleep(3)
    pag.moveTo(1200, 268)
    pag.scroll(-20)
    time.sleep(0.5)
    pag.scroll(-20)
    time.sleep(0.5)
    pag.scroll(-20)
    pag.moveTo(2640, 365)
    print(outfile + " --> 캡쳐에 성공했습니다.")


def catch_cs(sch_region, fname):
    """

    :rtype: object
    """
    pag.moveTo(670 + 554, 570, duration=0.5)
    time.sleep(1)
    pag.click()
    outname = '/{}.png'.format(fname)
    outpath = "D:/FineTec/DailyLoss/ocr" + "/{}".format(fname[:8])
    out_full_name = outpath + outname
    pag.screenshot(out_full_name, region=(672, 170, 554, 800))
    time.sleep(1)
    pag.hotkey('ctrl', 'shift', '2')
    time.sleep(1)
    pag.press('right', presses=2)
    time.sleep(1)
    pag.press('enter')
    pag.moveTo(1220, 500)
    pag.click
    print(out_full_name + "  --> 캡쳐에 성공했습니다.")


def catch_file_name(img, sch_region):
    time.sleep(1)
    p_list = pag.locateAllOnScreen(img, confidence=0.9, region=sch_region)
    p_list = list(p_list)
    print(p_list)
    p_list = p_list[0][0] + 100, p_list[0][1] - 3, p_list[0][2] + 370, p_list[0][3] + 8  # 사용하는 코드
    print(p_list)
    pag.screenshot("d:/FineTec/DailyLoss/ocr/cs_name.png", region=p_list)
    tgrImg = "d:/FineTec/DailyLoss/ocr/cs_name.png"
    time.sleep(3)
    image = cv2.imread(tgrImg)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filename = '{}.png'.format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename), lang='kor')

    del_dic = {
        ' ': '', '\ㅣ': '', '\n': '', '': '', '확인': '', 'ㅣ메주': '', "연상": "연장", "조줄": "조출", "조술": "조출", \
        "소술": "조출", "소줄": "조출", "소출": "조출", "\/": "7", "]": "1", "/": "7"
    }

    for word, replacement in del_dic.items():
        text = text.replace(word, replacement)

    text = re.sub("\n\|\”\"\.\s", "", text)
    text = re.sub("([ㄱ-힣]+.*)(\d{8})", "\\2", text)
    text = re.sub("(\d{8})([ㄱ-힣]+)(\d+)", "\\1-\\2-\\3", text)
    text = re.sub("(\d{8})([ㄱ-힣]+)(\d+)", "\\1-\\3-\\2", text)
    text = text.replace("--", "-").replace(".", "")
    # text = re.sub(r"([ㄱ-힣])-$", "\\1", text)
    # assert isinstance(text, object)
    outname = '{}'.format(text)
    time.sleep(1)
    outpath = "D:/FineTec/DailyLoss/ocr/cs_dn/"
    print(text)
    with open(outpath + '{0}.{1}'.format("csSheet", "csv"), 'a', encoding='cp949') as f:
        f.write(outname + '\n')
    assert isinstance(image, object)
    cv2.imshow('Image', image)
    cv2.waitKey(1)
    print(outname + "  --> 캡쳐에 성공했습니다.")
    os.remove(tgrImg)


if __name__ == "__main__":
    # cs_img = "D:/FineTec/DailyLoss/Loss_img/cs_sheet.png"
    # cs_name = "D:/FineTec/DailyLoss/ocr/202112114-주간-10.png"
    # srch_Region1 = 672, 0, 554, 600 # 상영역
    # srch_Region2 = 672, 500, 554, 300 # 중영역
    # srch_Region3 = 672, 800, 554, 200 # 하영역
    # catch_scroll("d:/FineTec/DailyLoss/ocr/cs_drino.png", (srch_Region1))
    getRng.pressF4()
    catch_top("d:/FineTec/DailyLoss/ocr/cs_drino.png", (672, 0, 554, 800))
    # catch_middle("d:/FineTec/DailyLoss/ocr/cs_drino.png", (672, 0, 554, 800))
    # catch_bottom("d:/FineTec/DailyLoss/ocr/cs_drino.png", (672, 0, 554, 800))
    # catch_cs((672, 0, 554, 1080), "20220112-주간연장-7")
else:
    print("---------- module running ----------")

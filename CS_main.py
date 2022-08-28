import pyautogui as pag
import time
import getCS
import getRng

if __name__ == "__main__":

    # getCS.go_date("220523")
    # getCS.catch_cs((684, 0, 554, 800), "20220402-주간-11")  # 9.17.20.28.50.

    # xdate_list: object = [
    #     "220616", "220627", "220704"
    # ]
    #
    # xNum_list: object = [
    #     66, 34, 65
    # ]

    # 37

    # x_dic = dict(zip(xdate_list, xNum_list))

    #
    #
    # print(x_dic)
    #
    # for key, val in x_dic.items():
    #     getCS.go_date(key)
    #     for i in range(int(val)+6):
    #         print(i, "/", int(val)+6)
    #         getCS.catch_scroll("d:/FineTec/DailyLoss/ocr/cs_drino.png", (672, 0, 554, 600))  # 상영역
    #         time.sleep(1)
    #         pag.scroll(-1)
    #         time.sleep(1)
    #         pag.scroll(-1)
    #     try:
    #         getCS.catch_top("d:/FineTec/DailyLoss/ocr/cs_drino.png", (672, 320, 554, 400))  # 중영역
    #         time.sleep(1)
    #         pag.scroll(-1)
    #         time.sleep(1)
    #         pag.scroll(-1)
    #         getCS.catch_top("d:/FineTec/DailyLoss/ocr/cs_drino.png", (672, 660, 554, 300))  # 하영역
    #     except IndexError:
    #         pass

    n = 22
    for i in range(n):
        print(i, "/", n + 2)
        getCS.catch_scroll("d:/FineTec/DailyLoss/ocr/cs_drino.png", (672, 0, 554, 600))  # 상영역
        time.sleep(1)
        pag.click(1220, 900, duration = 0.5)
        pag.dragRel(0, -380, duration = 1)
        i += 1

    try:
        print(n + 1, "/", n + 2)
        getCS.catch_top("d:/FineTec/DailyLoss/ocr/cs_drino.png", (672, 420, 554, 400))  # 중영역
        time.sleep(1)
        pag.scroll(-1)
        time.sleep(1)
        pag.scroll(-1)
        print(n + 2, "/", n + 2)
        getCS.catch_top("d:/FineTec/DailyLoss/ocr/cs_drino.png", (672, 660, 554, 300))  # 하영역
    except IndexError:
        pass


else:
    print("---------- module is running ----------")

# Point(x=972, y=383)Point(x=1063, y=382)Point(x=1195, y=378)

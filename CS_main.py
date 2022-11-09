import pyautogui as pag
import time
import getCS
import getRng

# getCS.go_date("220523")
# getCS.catch_cs((684, 0, 554, 800), "20220708-조출주간-32")  # 9.17.20.28.50.

# n = 69
# for i in range(n+3):
#     print(i+1, "/", n+3)
#     getCS.catch_scroll("d:/FineTec/ocr/cs_drino.png", (672, 0, 554, 800))  # 상영역
#     time.sleep(1)
#     pag.click(1215, 900, duration=0.5)
#     pag.dragRel(0, -350, duration=1)
#     i += 1
# try:
#     print(n + 4, "/", n + 5)
#     getCS.catch_top("d:/FineTec/ocr/cs_drino.png", (672, 420, 554, 400))  # 중영역
#     time.sleep(1)
#     pag.scroll(-1)
#     time.sleep(1)
#     pag.scroll(-1)
#     print(n + 5, "/", n + 5)
#     getCS.catch_top("d:/FineTec/ocr/cs_drino.png", (672, 660, 554, 300))  # 하영역
# except IndexError:
#     pass


cs_date = [
           "220618"
            ]

for date in cs_date:
    getCS.go_date(date)
    getCS.get_gunsu()
    n = getCS.get_gunsu()
    for i in range(n+3):
        print(i+1, "/", n+3)
        getCS.catch_scroll("d:/FineTec/ocr/cs_drino.png", (672, 0, 554, 600))  # 상영역
        time.sleep(1)
        pag.click(1215, 900, duration=0.5)
        pag.dragRel(0, -350, duration=1)
        i += 1
    try:
        print(n + 4, "/", n + 5)
        getCS.catch_top("d:/FineTec/ocr/cs_drino.png", (672, 420, 554, 400))  # 중영역
        time.sleep(1)
        pag.scroll(-1)
        time.sleep(1)
        pag.scroll(-1)
        print(n + 5, "/", n + 5)
        getCS.catch_top("d:/FineTec/ocr/cs_drino.png", (672, 660, 554, 300))  # 하영역
    except IndexError:
        pass

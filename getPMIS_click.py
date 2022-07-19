import pyautogui as pag
import time


def xldn_img_click():
    time.sleep(0.5)
    center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/pmis_sch.png", confidence=0.9)
    pag.click(center)
    time.sleep(2)
    center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/pmis_exl.png", confidence=0.98)
    pag.click(center)
    time.sleep(2)
    center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/pmis_cnf.png", confidence=0.95)
    pag.click(center)


def xldn_click():
    time.sleep(0.5)
    pag.click(1650, 293)
    time.sleep(2)
    pag.click(1570, 912)
    time.sleep(2)
    pag.click(1130, 157)


if __name__ == "__main__":
    c = pag.position()
    print(c)

else:
    print("module running")

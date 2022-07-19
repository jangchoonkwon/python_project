import chromedriver_autoinstaller
import pyautogui as pag
import time, os
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# Check if chrome driver is installed or not
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'

if os.path.exists(driver_path):
    print(f"chrom driver is insatlled: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)

URL = 'http://www.spmportal.com/pjt/layout/mainLayout2.do'

driver: WebDriver = webdriver.Chrome(driver_path)
driver.get(URL)
driver.maximize_window()


def go_Web():
    # URL = 'http://www.spmportal.com/pjt/layout/mainLayout2.do'
    # driver: WebDriver = webdriver.Chrome(executable_path='chromedriver')
    # driver.get(URL)
    # driver.maximize_window()

    driver.implicitly_wait(3)
    time.sleep(0.5)
    parent = driver.current_window_handle
    print(f"This is parent window : {parent}")
    uselessWindows = driver.window_handles
    print(
        f"This has the parent window and also the two popup windows : {uselessWindows}")
    driver.switch_to.window(uselessWindows[-1])
    driver.close()
    driver.switch_to.window(uselessWindows[0])

    time.sleep(1)
    driver.implicitly_wait(3)
    driver.find_element(By.ID, "username_show").send_keys("sgas21")
    driver.implicitly_wait(3)
    driver.find_element(By.ID, "password_show").send_keys("fine1410!")
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "//*[@id='loginData']/fieldset/div/input").click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/ul/li[4]/a").click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "//*[@id='mainMenuWrapper']/li[4]/span/p[21]/a").click()
    time.sleep(1)
    driver.implicitly_wait(3)


# def xldn_click():
#     time.sleep(0.5)
#     center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/pmis_sch.png", confidence=0.9)
#     pag.click(center)
#     time.sleep(2)
#     center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/pmis_exl.png", confidence=0.98)
#     pag.click(center)
#     time.sleep(2)
#     center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/pmis_cnf.png", confidence=0.95)
#     pag.click(center)
#     return


if __name__ == "__main__":
    go_Web("D:/FineTec/DailyLoss/Loss_img/pmis_sch.png", 0, 0.9)
    # c_click("D:/FineTec/DailyLoss/Loss_img/pmis_exl.png", 2, 0.98)
    # c_click("D:/FineTec/DailyLoss/Loss_img/pmis_cnf.png", 2, 0.95)
    # def pm_login(ipt1, ipt2):
    #     driver.implicitly_wait(3)
    #     driver.find_element(By.ID, "username_show").send_keys(ipt1)
    #     driver.implicitly_wait(3)
    #     driver.find_element(By.ID, "password_show").send_keys(ipt2)
    #
    #
    # def pm_xp_click(img, slp):
    #     driver.implicitly_wait(slp)
    #     driver.find_element(By.XPATH, img).click()

    # popup_close()
    # pm_login("sgas21", "fine1410!")
    # pm_xp_click("//*[@id='loginData']/fieldset/div/input", 3)
    # pm_xp_click("/html/body/div[1]/div[3]/div[1]/div[2]/ul/li[4]/a", 3)
    # pm_xp_click("//*[@id='mainMenuWrapper']/li[4]/span/p[21]/a", 3)

    # center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/pmis_sch.png", confidence=0.9)
    # pag.click(center)
    # time.sleep(2)
    # center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/pmis_exl.png", confidence=0.98)
    # pag.click(center)
    # time.sleep(2)
    # center = pag.locateCenterOnScreen("D:/FineTec/DailyLoss/Loss_img/pmis_cnf.png", confidence=0.95)
    # pag.click(center)

else:
    print("모듈호출")

import pyautogui as pag
import keyboard, time


# def get_search_img(keypress: "F4", outpng: str) -> object:

def pressF4_1():
    """

    """
    while True:
        if keyboard.is_pressed("F4"):
            t1 = pag.position()
            time.sleep(0.5)
            break
            print(t1)
    print(t1)


def pressF4_2():
    while True:
        if keyboard.is_pressed("F4"):
            t1 = pag.position()
            print(t1)
            time.sleep(0.5)
            break
            print(t1)
    while True:
        if keyboard.is_pressed("F4"):
            t2 = pag.position()
            print(t2)
            time.sleep(0.5)
            break
            print(t2)
    region = (t1[0], t1[1], t2[0] - t1[0], t2[1] - t1[1])
    print(region)


if __name__ == "__main__":
    pressF4_1()

else:
    print("module running")

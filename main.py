import pyautogui
import time
import PIL
from PIL import Image

flag = 0
def get_food():
    # 截图获取食物数量 980 210 1120 250 左上角和右下角坐标为
    image = pyautogui.screenshot(region=(980,210,140,40))
    return find_core(image)
    # image.save("D:\Py_Program\knight\photos\\food.png")

#传入图片检测窗口是否在屏幕上 用食物数量作为检测标志
def find_core(image):
    if pyautogui.locateOnScreen(image):
        return 1;
    else:
        return 0;

#判断是否钓上鱼的函数(钓上杂物按钮在中间无法识别到还需采集样本)
def get_fish():
    global flag
    image_get_fish = Image.open("D:\Py_Program\knight\photos\\finish_get_fish.png")
    image_get_trash = Image.open("D:\Py_Program\knight\photos\\finish_get_trash.png")
    image_get_submit = Image.open("D:\Py_Program\knight\photos\\finish_get_submit.png")
    if pyautogui.locateOnScreen(image_get_fish):
        flag = 1
        return 1
    elif pyautogui.locateOnScreen(image_get_trash):
        flag = 2
        return 1
    elif pyautogui.locateOnScreen(image_get_submit):
        flag = 3
        return 1
    else:
        return 0

def click_true():
    image = Image.open("D:\Py_Program\knight\photos\\true.png")
    pos = pyautogui.center(pyautogui.locateOnScreen(image))
    pyautogui.click(pos)

if __name__ == '__main__':
    time.sleep(2)

    #钓鱼程序的主循环
    while get_food(): #1280 1025
        pyautogui.click(1280,1025)
        #等待钓鱼结果的循环
        while True:
            # image_get = pyautogui.screenshot(1073,1077,184,70)
            if get_fish():
                if flag == 1:
                    pos_fish = pyautogui.center(pyautogui.locateOnScreen("D:\Py_Program\knight\photos\\finish_get_fish.png"))
                    pyautogui.click(pos_fish)
                elif flag == 2:
                    pos_trash = pyautogui.center(pyautogui.locateOnScreen("D:\Py_Program\knight\photos\\finish_get_trash.png"))
                    pyautogui.click(pos_trash)
                elif flag == 3:
                    pos_submmit = pyautogui.center(pyautogui.locateOnScreen("D:\Py_Program\knight\photos\\finish_get_submit.png"))
                    pyautogui.click(pos_submmit)
                time.sleep(0.5)
                if pyautogui.locateOnScreen("D:\Py_Program\knight\photos\\true.png"):
                    click_true()
                break

    # 截图区域刚好为小程序未移动区域
    # im1 = pyautogui.screenshot(region=(1020,210,510,970))
    # # 保存截图到photos文件夹备用
    # im1.save("D:\Py_Program\knight\photos\\test.png")
    # im2 = pyautogui.screenshot(region=(1073,1077,184,70))
    # im2.save("D:\Py_Program\knight\photos\\finish.png")
    # print(get_fish())
    # if get_fish():
    #     pos = pyautogui.center(pyautogui.locateOnScreen("D:\Py_Program\knight\photos\\finish.png"))
    #     pyautogui.click(pos)



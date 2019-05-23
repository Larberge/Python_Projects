from PIL import ImageGrab as ig
import numpy as np
import cv2
from pynput import keyboard
from pynput.keyboard import Controller

kb = Controller()

def newImg(h):
    hoyde = h
    if(hoyde<=150):
        hoyde = 150
    screen_coords = [160, hoyde , 680, hoyde+1]
    screen_img = ig.grab(bbox=screen_coords)
    #screen_img.save("./img1.png", "png")
    pxl_array = np.array(screen_img)
    pxl_array = cv2.cvtColor(pxl_array, cv2.COLOR_BGR2GRAY)
    return pxl_array




go = False
last_pressed = None

def on_press(key):
    pass


def on_release(key):
    if key.char in 'asdf':
        global last_pressed
        last_pressed = key.char
        print("Start")
        global go
        go = True
        return False


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

def press_A():
    print("A")
    kb.release(last_pressed)
    kb.press('a')

def press_S():
    print("S")
    kb.release(last_pressed)
    kb.press('s')

def press_D():
    print("D")
    kb.release(last_pressed)
    kb.press('d')


def press_F():
    print("F")
    kb.release(last_pressed)
    kb.press('f')


print(last_pressed)
h = 400
pxls = newImg(h)
pxls = pxls.tolist()[0]
while(go):
    for i in range(len(pxls)):
        if pxls[i] > 50 and pxls[i] < 100:
            if i >= 0 and i <= 117 and last_pressed != 'a':
                press_A()
                last_pressed = 'a'
                break
            elif i >= 133 and i <= 253 and last_pressed != 's':
                press_S()
                last_pressed = 's'
                break
            elif i >= 270 and i <= 387 and last_pressed != 'd':
                press_D()
                last_pressed = 'd'
                break
            elif i >= 404 and i <= 519 and last_pressed != 'f':
                press_F()
                last_pressed = 'f'
                break
    pxls = newImg(h)
    pxls = pxls.tolist()[0]
    h = h-1






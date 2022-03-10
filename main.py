import os
import time
import pyautogui as pyag
import colorsys

BCK = 's'
FWD = 'w'
LFT = 'd'

def mouse_click():
    time.sleep(1)
    pyag.mouseDown(button='left')
    pyag.mouseUp(button='left')
    time.sleep(1)

def hsv(rgb):
    return colorsys.rgb_to_hsv(rgb[0]/255.,rgb[1]/255.,rgb[2]/255.)

def find_location(img, start, end, hue):
    found_x = []
    found_y = []
    for y in range(start[1], end[1]):
        for x in range(start[0], end[0]):
            if hsv(img.getpixel((x, y)))[0]*360 > hue:
                found_x.append(x)
                found_y.append(y)
    return (sum(found_x) // len(found_x), sum(found_y) // len(found_y))

def alt_f4():
    pyag.keyDown('alt')
    pyag.press('f4')
    pyag.keyUp('alt')

def moonshine_location(offset=0):
    screen = pyag.screenshot()
    x, y = find_location(screen, (1150, 170), (1800, 900), 280)
    pyag.moveTo(x, y)

def moonshine_claim():
    moonshine_location(offset=300)
    mouse_click()
    receive_location = pyag.locateOnScreenCenter('C:\Users\Korisnik\Desktop\Programming\Pyhton\TarkovScavCase\receive.png')
    pyag.moveTo(receive_location)
    mouse_click()

def moonshine_buy():
    moonshine_location()
    pyag.click(button = 'right')
    pyag.move(50,30)
    mouse_click()
    pyag.moveTo(1800, 975)
    mouse_click()
    pyag.press('y')

def moonshine_start():
    pyag.moveTo(960,20)
    mouse_click()
    pyag.moveTo(1895,800)
    mouse_click()
    moonshine_location(offset=270)
    pyag.move(270,0)
    mouse_click()

def game_start():
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Battlestate Games\Battlestate Games Launcher")
    time.sleep(15)
    pyag.moveTo(1380,800)
    mouse_click()

def enter_hideout():
    time.sleep(30)
    pyag.moveTo(960,20)
    mouse_click()

def movement():
    time.sleep(6)
    pyag.keyDown(BCK)
    time.sleep(2)
    pyag.keyUp(BCK)
    pyag.keyDown(LFT)
    time.sleep(1)
    pyag.keyUp(LFT)
    pyag.keyDown(FWD)
    time.sleep(0.75)
    pyag.keyUp(FWD)

def scav_case():
    time.sleep(3)
    pyag.press('f')
    time.sleep(0.5)
    pyag.moveTo(1895,800)
    mouse_click()

def moonshine():
    moonshine_claim()
    moonshine_buy()
    moonshine_start()

def hideout():
    time.sleep(50)
    pyag.moveTo(200,1070)
    mouse_click()
    enter_hideout()
    movement()
    scav_case()
    moonshine()

game_start()
hideout()
alt_f4()

from playerActions import *
from PIL import ImageGrab
import time
import pyautogui
import cv2
import argparse
from rgbValues import * 
from interfaceRegions import *
from playerActions import *

region1 = FISHING_WHEEL_REGION

baitCounter = 0

def setUpFreshwater():
    returnToSpawn()
    returnToBaitShopFromSpawn()
    buyAllBait()
    fromBaitShopToRiver()
    selectBait()

def setUpSaltwater():
    returnToSpawn()
    returnToBaitShopFromSpawn()
    buyAllBait()
    returnToSpawn()
    moveToOcean()
    selectBait()

def fish(string):
    counter = 50
    selectRod()
    time.sleep(.5)
    castRod()
    while True:
        time.sleep(.5)
        fishingWheelImage = ImageGrab.grab(bbox=region1)
        pixels = fishingWheelImage.getdata()

        if ROD_WHEEL_PIXEL_COLOR in pixels:
            print("Value is visible on the screen!")
            reelingFish()
            
        if counter == 0:
            if string == "F":
                setUpFreshwater()
            elif string == "S":
                setUpSaltwater()
            else:
                setUpFreshwater()
        
        del fishingWheelImage

def reelingFish():
    caughtTextBox = ImageGrab.grab(bbox=region1)
    pixelsAvaliable = caughtTextBox.getdata()

    while ROD_WHEEL_PIXEL_COLOR in pixelsAvaliable:
        pyautogui.mouseDown()
        time.sleep(.0001)
        pyautogui.mouseUp()
        # print('Not Found')
        caughtTextBox = ImageGrab.grab(bbox=region1)
        pixelsAvaliable = caughtTextBox.getdata()
        del caughtTextBox
    time.sleep(3)
    exitFishingDialog()
    castRod()

def __main__(arg):
    if arg == 'F':
        print("Freshwater location")
        setUpFreshwater()
        fish("F")


    elif arg == "S":
        print("Saltwater location")
        setUpSaltwater()
        fish("S")
    
    else:
        print('Default')
        fish("F")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fishing script")
    parser.add_argument('--f', action='store_true', help="Option for mode F")
    parser.add_argument('--s', action='store_true', help="Option for mode S")
    args = parser.parse_args()

    time.sleep(3)
    
    if args.f:
        __main__('F')
    elif args.s:
        __main__('S')
    else:
        __main__("Already at location")


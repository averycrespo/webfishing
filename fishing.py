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

baitCounter = 50

def setUpFreshwater():
    returnToSpawn()
    returnToBaitShopFromSpawn()
    buyAllBait()
    fromBaitShopToRiver()

def setUpSaltwater():
    returnToSpawn()
    returnToBaitShopFromSpawn()
    buyAllBait()
    returnToSpawn()
    moveToOcean()


# Counter issue present
def fish(string):
    counter = 50
    selectBait()
    drinkCola()
    selectRod()
    time.sleep(.5)
    castRod()
    print("Outside of true loop", counter)

    while True:
        time.sleep(.5)
        fishingWheelImage = ImageGrab.grab(bbox=region1)
        pixels = fishingWheelImage.getdata()

        # Reset 
        if counter <= 1:
            if string == "F":
                setUpFreshwater()
                fish(string)
            elif string == "S":
                setUpSaltwater()
                fish(string)
            else:
                setUpFreshwater()
                fish("F")

        if ROD_WHEEL_PIXEL_COLOR in pixels:
            reelingFish()
            counter -= 1
            print("After fishing: ", counter)
        
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


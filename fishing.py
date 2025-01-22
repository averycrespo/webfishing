from playerActions import interactAndExit, moveLeft, moveRight, init_setup, hold_m1, selectRod
from PIL import ImageGrab
import time
import cv2
import argparse
from playerActions import *

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

def __main__(arg):
    if arg == 'F':
        print("Freshwater location")
        setUpFreshwater()

    elif arg == "S":
        print("Saltwater location")
        setUpSaltwater()
    

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

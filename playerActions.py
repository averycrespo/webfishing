import pyautogui
import time
from interfaceRegions import *

# Binds: 
# 'e' interact
# 'tab' open backpack
# 'w-a-s-d movement 

# Interact with bucket and escape dialog
def interactAndExit():
    pyautogui.keyDown('e')
    pyautogui.keyUp('e')
    time.sleep(1.3)
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    time.sleep(1.2)

def interact():
    pyautogui.keyDown('e')
    pyautogui.keyUp('e')
    time.sleep(.5)

# Move player left
def moveLeft():
    pyautogui.keyDown('a')  
    time.sleep(.3) 
    pyautogui.keyUp('a')

# Move player right
def moveRight():
    pyautogui.keyDown('d') 
    time.sleep(.3)  
    pyautogui.keyUp('d')

def moveUp():
    pyautogui.keyDown('w') 
    time.sleep(.3)  
    pyautogui.keyUp('w')

def moveDown():
    pyautogui.keyDown('s') 
    time.sleep(.3)  
    pyautogui.keyUp('s')

def getUp():
    pyautogui.keyDown('space') 
    time.sleep(.1)  
    pyautogui.keyUp('space')

# Move player to align buckets properly
def init_setup():
    # Bucket
    pyautogui.keyDown('3') 
    time.sleep(.25)
    pyautogui.keyUp('3')

    # enable sprint
    shiftKey()

    # hit bench
    pyautogui.keyDown('s') 
    time.sleep(1.4)
    pyautogui.keyUp('s')
    
    # move towards wall 
    i = 0
    while i < 15:
        moveRight()
        i += 1

    pyautogui.keyDown('3') 
    time.sleep(.25)
    pyautogui.keyUp('3')

    time.sleep(1)
    # right bucket
    click()

    moveRight()
    shiftKey()
    moveLeft()

    pyautogui.keyDown('2') 
    time.sleep(.25)
    pyautogui.keyUp('2')

    time.sleep(1)

    click()
    pyautogui.keyDown('a')  
    time.sleep(.15) 
    pyautogui.keyUp('a')


def selectRod():
    pyautogui.keyDown('1') 
    time.sleep(.25)
    pyautogui.keyUp('1')

def shiftKey(): 
    # enable sprint
    pyautogui.keyDown('shift') 
    time.sleep(.2)
    pyautogui.keyUp('shift')


def click():
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()

def buy():
    pyautogui.mouseDown()
    pyautogui.mouseUp()

def drinkCola():
    pyautogui.keyDown('5') 
    time.sleep(0.5)
    pyautogui.keyUp('5')
    time.sleep(.3)
    hold_m1()
    time.sleep(1.2)

def hold_m1():
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

def returnToSpawn():
    pauseMenu()
    moveCursorRTS()
    click()
    pauseMenu()
    time.sleep(1.5)

def pauseMenu():
    pyautogui.keyDown('esc')
    time.sleep(.1)
    pyautogui.keyUp('esc')

def baitMenu():
    pyautogui.keyDown('b')
    pyautogui.keyUp('b')

def selectBait():
    baitMenu()
    time.sleep(.5)
    selectGildedWormBait()
    click()
    baitMenu()
    time.sleep(.5)

def moveCursorRTS():
    pyautogui.moveTo(*SPAWN_POSITION)

def moveCursorWorm():
    pyautogui.moveTo(*WORM_POSITION)

def moveCursorCricket():
    pyautogui.moveTo(*CRICKET_POSITION)

def moveCursorLeech():
    pyautogui.moveTo(*LEECH_POSITION)

def moveCursorMinn():
    pyautogui.moveTo(*MINN_POSITION)

def moveCursorSquid():
    pyautogui.moveTo(*SQUID_POSITION)

def moveCursorNaut():
    pyautogui.moveTo(*NAUT_POSITION)

def moveCursorGworm():
    pyautogui.moveTo(*GWORM_POSITION) 

def moveCursorSellAll():
    pyautogui.moveTo(*SELL_BUTTON_POSITION)

def selectWormBait():
    pyautogui.moveTo(*WORM_BAIT)

def selectCricketBait():
    pyautogui.moveTo(*CRICKET_BAIT)

def selectLeechBait():
    pyautogui.moveTo(*LEECH_BAIT)

def selectMinnBait():
    pyautogui.moveTo(*MINN_BAIT)

def selectSquidBait():
    pyautogui.moveTo(*SQUID_BAIT)

def selectNautBait():
    pyautogui.moveTo(*NAUT_BAIT)

def selectGildedWormBait():
    pyautogui.moveTo(*GWORM_BAIT)


def buyAllBait():
    interact()
    moveCursorWorm()
    buy()
    moveCursorCricket()
    buy()
    moveCursorLeech()
    buy()
    moveCursorMinn()
    buy()
    moveCursorSquid()
    buy()
    moveCursorNaut()
    buy()
    moveCursorGworm()
    buy()
    sellAll()
    pauseMenu() # Exit buy menu

# Function existing if player is already inside menu
def sellAll():
    moveCursorSellAll()
    buy()

def fromBaitShopToRiver():
    shiftKey()
    i = 0
    while i < 5:
        moveUp()
        i = i + 1
    shiftKey()
    selectRod()

def returnToBaitShopFromSpawn():
    shiftKey()
    i = 0
    while i < 6:
        moveLeft()
        i = i + 1
    i = 0
    moveDown()
    shiftKey()

def moveToOcean():
    shiftKey()

    pyautogui.keyDown('s') 
    time.sleep(1.4)
    pyautogui.keyUp('s')
    
    i = 0
    while i < 15:
        moveRight()
        i += 1

    pyautogui.keyDown('s') 
    time.sleep(1)
    pyautogui.keyUp('s')

    i = 0
    while i < 5:
        moveRight()
        i += 1

    pyautogui.keyDown('s') 
    time.sleep(1)
    pyautogui.keyUp('s')

    i = 0
    while i < 11:
        moveRight()
        i += 1
    time.sleep(.3)
    getUp()
    i = 0
    while i < 3:
        moveRight()
        i += 1
    shiftKey()
    selectRod()

def castRod():
    pyautogui.mouseDown()
    time.sleep(.40)
    pyautogui.mouseUp()
    
def exitFishingDialog():
    time.sleep(1)
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    time.sleep(1)
    castRod()


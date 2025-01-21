import pyautogui
import time

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

def hold_m1():
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
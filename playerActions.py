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
    time.sleep(1)

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
    pyautogui.keyDown('s') 
    time.sleep(1.4)
    pyautogui.keyUp('s')

    pyautogui.keyDown('d') 
    time.sleep(6)
    pyautogui.keyUp('d')

    pyautogui.keyDown('3') 
    time.sleep(.25)
    pyautogui.keyUp('3')

    time.sleep(1)

    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()

    pyautogui.keyDown('d') 
    time.sleep(.2)
    pyautogui.keyUp('d')

    moveRight()
    moveLeft()
    moveLeft()

    pyautogui.keyDown('2') 
    time.sleep(.25)
    pyautogui.keyUp('2')

    time.sleep(1)

    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()

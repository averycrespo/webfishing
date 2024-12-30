import pyautogui
import time

# Moving script for webfishing to automatically pickup fish from fishing buddies
# 
# 'a' is the key for right movement
# 'd' is the key for left movement
# 'e' is the key for interaction with the bucket
# 

# Move player left
def moveLeft():
    pyautogui.keyDown('a')  
    time.sleep(.5) 
    pyautogui.keyUp('a')

# Move player right
def moveRight():
    pyautogui.keyDown('d') 
    time.sleep(.5)  
    pyautogui.keyUp('d')
       
# Interact with fishing bucket and exit diaglog box
def interactAndExit():
    pyautogui.keyDown('e')
    pyautogui.keyUp('e')
    time.sleep(1.3)
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')

def init_wait():
    time.sleep(2)

def wait():
    time.sleep(70)

# Script begin
init_wait()
try:
    while True:
        moveLeft()
        interactAndExit()
        moveRight()
        interactAndExit()
    
       
       
except KeyboardInterrupt:
    print("Script stopped by user.")

    
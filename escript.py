import pyautogui
import time

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
    time.sleep(1) 
    pyautogui.keyUp('e')
    pyautogui.keyDown('e')
    time.sleep(1) 
    pyautogui.keyUp('e')

def init_wait():
    time.sleep(3)

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

    
from playerActions import interactAndExit, moveLeft, moveRight, init_setup
from PIL import ImageGrab
import time
import cv2

# Settings: 1920x1080 windowed
# Initial flag for running setup (should be True if origin is at spawn)
init_flag = True
logging = False
show_screenshots = False

# Regions for screenshots
region1 = (600, 300, 800, 450)
region2 = (1250, 300, 1450, 450)
subregion1 = (50, 50, 120, 120)
subregion2 = (50, 50, 120, 120)

# RBG color for 'caught fish' indicator
fish_pixel_white = (255, 238, 213)

def collectLeftBucket():
    moveLeft()
    time.sleep(.3) 
    interactAndExit()
    moveRight()

def collectRightBucket():
    moveRight()
    time.sleep(.3) 
    interactAndExit()
    moveLeft()
        
def __main__(init_flag):
    
    time.sleep(3) 

    # Fresh spawn in 
    if init_flag is True:
        init_setup()

    # Loop for auto collection
    while True:
        time.sleep(5)
        ################### Left Fishing bucket ########################
        leftBucketScreenshot = ImageGrab.grab(bbox=region1)

        if show_screenshots is True: 
            leftBucketScreenshot.show()

        leftFishPixelArea = leftBucketScreenshot.crop(subregion1)

        pixel_position1 = (5, 5)  
        rgb_value1 = leftFishPixelArea.getpixel(pixel_position1)

        if logging is True:
            print(f"Region 1 - RGB value at {pixel_position1}: {rgb_value1}")

        pixels1 = leftFishPixelArea.getdata()

        if fish_pixel_white in pixels1:
            collectLeftBucket()

        ################## Right Fishing bucket ########################
        rightBucketScreenshot = ImageGrab.grab(bbox=region2)
        rightFishPixelArea = rightBucketScreenshot.crop(subregion2)

        if show_screenshots is True: 
            rightBucketScreenshot.show()

        pixel_position2 = (10, 10) 
        rgb_value2 = rightFishPixelArea.getpixel(pixel_position2)

        if logging is True:
            print(f"Region 2 - RGB value at {pixel_position2}: {rgb_value2}")

        pixels2 = rightFishPixelArea.getdata()

        if fish_pixel_white in pixels2:
            collectRightBucket()
        
        ################## Reset screenshots ########################
        leftBucketScreenshot = None
        rightBucketScreenshot = None
        del leftBucketScreenshot
        del rightBucketScreenshot

        # Exit loop: 'q' 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

__main__(init_flag)
cv2.destroyAllWindows()


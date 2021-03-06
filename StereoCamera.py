# Prerequisite: OpenCV python library and Adafruit ServoKit Python library
# Check the camera detection   "vcgencmd get_camera"
# Check the adafruit board detection "sudo i2cdetect -y 1"

import cv2
from time import sleep
from adafruit_servokit import ServoKit

# cap = cv2.VideoCapture(0)
cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

servokit = [] 
for i in range(0,10):
    servokit.append(ServoKit(channels=16, address=0x40+i))
    
# Reset
numOfRow = 10
numOfCol = 10

arr = [90]*10

for i in range(0,numOfRow):
    arr[i] = [90]*numOfCol
        
for i in range(0,numOfRow):
    for j in range(0, numOfCol):
#         print(str(arr[i][j]), end = "  ")
        servokit[i].servo[j].angle = arr[i][j]
        
sleep(0.5)


while(True):
    # Capture frame-by-frame
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    stereo = cv2.createStereoBM(numDisparities=16, blockSize=15) # edit these
    depthmap = stereo.compute(frame1, frame2)
    # plt.imshow(depthmap,'gray')
    plt.show()

    # Convert color image to gray scale
    gray = cv2.cvtColor(depthmap, cv2.COLOR_BGR2GRAY)
    
    # Change the value of each pixel to the range of 0 and 255
    retval, dst = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    for i in range(200,255):
        gray[dst==i] = 255
    
    cv2.imshow('frame', gray)
    
    # resize the image to 10 pixel by 10 pixel
    dim = (10, 10)
    resized = cv2.resize(dst, dim, interpolation = cv2.INTER_AREA)

    for i in range(0,resized.shape[0]):
        for j in range(0,resized.shape[1]):
            pixel = resized.item(i, j)
            val = pixel / 256 * 180
            servokit[i].servo[9-j].angle = val
        print()
    print()
    print()
    print()

    sleep(0.1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#    sleep(0.2)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

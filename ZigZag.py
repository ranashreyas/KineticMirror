# Prerequisite: OpenCV python library and Adafruit ServoKit Python library
# Check the adafruit board detection "sudo i2cdetect -y 1"


import time
from adafruit_servokit import ServoKit

servokit = [] 
for i in range(0,10):
    servokit.append(ServoKit(channels=16, address=0x40+i))

numOfRow = 10
numOfCol = 10

arr = [90]*10

for i in range(0,numOfRow):
    arr[i] = [90]*numOfCol
        
for i in range(0,numOfRow):
    for j in range(0, numOfCol):
#         print(str(arr[i][j]), end = "  ")
        servokit[i].servo[j].angle = arr[i][j]
#     print()
# print()

time.sleep(0.5)


for i in range(0,numOfRow):
    for j in range(0, numOfCol):
        if i%2 == 0:
            arr[i][j] = 180
            servokit[i].servo[j].angle = 180
        else:
            arr[i][9-j] = 180
            servokit[i].servo[9-j].angle = 180
          
#         for k in range(0,numOfRow):
#             for l in range(0, numOfCol):
#                 print(str(arr[k][l]), end = "  ")
#             print()
#         print()
        
        time.sleep(0.1)
    
    


    


# Prerequisite: OpenCV python library and Adafruit ServoKit Python library
# Check the adafruit board detection "sudo i2cdetect -y 1"


import time
#from adafruit_servokit import ServoKit

# servokit = [] 
# for i in range(0,10):
#     servokit.append(ServoKit(channels=16, address=0x40+i))

numOfRow = 10
numOfCol = 10

arr = [0]*10

for i in range(0,numOfRow):
    arr[i] = [0]*numOfCol
        
for i in range(0,numOfRow):
    for j in range(0, numOfCol):
        print(str(arr[i][j]), end = "  ")
#         servokit[i].servo[j].angle = arr[i][j]
    print()
print()

time.sleep(0.5)


xArray = [0] * 100
yArray = [0] * 100

T = 0
B = numOfRow-1
L = 0
R = numOfCol-1
index = 0
direction = 0

while(T<=B and L<=R):
    if(direction==0):
        for i in range(L, R+1):
            xArray[index] = T
            yArray[index] = i
            index += 1
        T += 1
    elif(direction==1):
        for i in range(T, B+1):
            xArray[index] = i
            yArray[index] = R
            index += 1
        R -= 1
    elif(direction==2):
        for i in range(R, L-1, -1):
            xArray[index] = B
            yArray[index] = i
            index += 1
        B -= 1
    elif(direction==3):
        for i in range(B, T-1, -1):
            xArray[index] = i
            yArray[index] = L
            index += 1
        L += 1
    direction = (direction+1)%4


for idx_spiral in range (0,100):  
    arr[xArray[idx_spiral]][yArray[idx_spiral]] = 180
    
    i = xArray[idx_spiral]
    j = yArray[idx_spiral]
    
    #print(str(i) + " " + str(j))

    for i in range(0,numOfRow):
        for j in range(0, numOfCol):
            print(str(arr[i][j]), end = "  ")
        print()
    print()
    
#     servokit[i].servo[j].angle = 180
    
    time.sleep(0.1)
    
    
for idx_spiral in range (99,-1,-1):    
    arr[xArray[idx_spiral]][yArray[idx_spiral]] = 0
    
    i = xArray[idx_spiral]
    j = yArray[idx_spiral]
    
    #print(str(i) + " " + str(j))

    for i in range(0,numOfRow):
        for j in range(0, numOfCol):
            print(str(arr[i][j]), end = "  ")
        print()
    print()
    
#     servokit[i].servo[j].angle = 0
    
    time.sleep(0.1)    

import pygame
from DriveClass import Drive
import serial
import numpy as np

def getNumCam():
    num = 0
    while True:
        cp = cv2.VideoCapture(num)
        if cp.isOpened():
            # working capture
            num += 1
        else:
            break
    return num
currCam = 0;
cap = cv2.VideoCapture(currCam)
cap.set(3,1920)
cap.set(4,1080)
capNum = 0
rollspeed = 0.75
t = Drive()
size = [1,1]
ser = serial.Serial("COM4", baudrate=9600,  timeout=0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()
pygame.joystick.init()
pilotInput = [0 for i in range(0,6)]
joystick = pygame.joystick.Joystick(0)
joystick.init()
clock.tick(10)
t.updatecoefficents()
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done=True
    pilotInput[0] = joystick.get_axis(0)
    pilotInput[1] = joystick.get_axis(1)
    pilotInput[2] = joystick.get_axis(2) #Right is up
    pilotInput[3] = joystick.get_axis(3)
    pilotInput[4] = joystick.get_axis(4) 
    pilotInput[5] = joystick.get_hat(0)[0] * rollspeed
    motorv = t.getsolution(pilotInput)
    motorvs = ""
    for i in range(0,5):
        motorvs += str(motorv[i]) + ","
    motorvs += str(motorv[5]) + ";"
    ser.write(motorvs.encode("utf-8"))
    #print(motorvs)
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if joystick.get_button(0) == 1:
        done = False
    if joystick.get_button(1) == 1:
        cv2.imwrite("frame%d.jpg" % capNum, frame)
        capNum += 1;
    if joystick.get_button(2) == 1:
        cap.release()
        currCam += 1
        if currCam >= getNumCam():
            currCam = 0
        cap = cv2.VideoCapture(currCam)
        cap.set(3,1920)
        cap.set(4,1080)
    #print(serB.readline())
    #pygame.display.flip()
pygame.quit()
cv2.destroyAllWindows()

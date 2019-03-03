import numpy as np
import cv2

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

while(True):
    
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k & 0xFF == ord('q'):
        break
    if k & 0xFF == ord('c'):
        cv2.imwrite("frame%d.jpg" % capNum, frame)
        capNum += 1;
    if k & 0xFF == ord('n'):
        cap.release()
        currCam += 1
        if currCam >= getNumCam():
            currCam = 0
        cap = cv2.VideoCapture(currCam)
        cap.set(3,1920)
        cap.set(4,1080)

# When everything done, release the capture
cv2.destroyAllWindows()

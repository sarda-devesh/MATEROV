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

frontCam = 0
rearCam = 1
cap = cv2.VideoCapture(frontCam)
cap.set(3,1920)
cap.set(4,1080)
cop = cv2.VideoCapture(rearCam)
cop.set(3,1920)
cop.set(4,1080)

sc = 0.4

while(True):
    
    # Capture frame-by-frame
    met, img1 = cap.read()
    mot, img2 = cop.read()

    # Our operations on the frame come here
    #frame = cv2.resize(frame, (0, 0), None, .5, .5)
    img2 = cv2.resize(img2, (0, 0), None, sc, sc)

    rows,cols,channels = img1.shape
    y = cols/2
    x = 0    
    rows,cols,channels = img2.shape
    y = int(y - cols/2)
    roi = img1[x:x+rows, y:y+cols]
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
    dst = cv2.add(img1_bg,img2_fg)
    img1[x:x+rows, y:y+cols] = dst
    
    # Display the resulting frame
    #numpy_horizontal = np.hstack((frame, frome))
    
    cv2.imshow('Numpy Horizontal', img1)
    k = cv2.waitKey(1)
    if k & 0xFF == ord('q'):
        break
    if k & 0xFF == ord('c'):
        cv2.imwrite("frame%d.jpg" % capNum, img1)
        capNum += 1;
    if k & 0xFF == ord('a'):
        sc += 0.01
    if k & 0xFF == ord('d'):
        sc -= 0.01
    if k & 0xFF == ord('p'):
        print(sc)
    if k & 0xFF == ord('n'):
        frontCam = 1 - frontCam
        rearCam = 1 - rearCam
        cap = cv2.VideoCapture(frontCam)
        cap.set(3,1920)
        cap.set(4,1080)
        cop = cv2.VideoCapture(rearCam)
        cop.set(3,1920)
        cop.set(4,1080)

# When everything done, release the capture
cv2.destroyAllWindows()

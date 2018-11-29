import numpy as np
import cv2



def camcap():
    global value
    cap = cv2.VideoCapture(0)
    threshhold=90
    ret, frame = cap.read()
    if cap.isOpened() == 0:
        cap.open(0)

    greyframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    scaleing = 50

    height = int(greyframe.shape[0]*scaleing / 100)
    width = int(greyframe.shape[1]*scaleing / 100)

    dim=(width, height)

    greyframe = cv2.resize(greyframe, dim, interpolation = cv2.INTER_AREA)

    blackframe = cv2.threshold(greyframe, threshhold, 255, cv2.THRESH_BINARY)[1]

    mid = sum(blackframe[:,int(width/2)])

    left = sum(blackframe[:,int(width/3)])

    right = sum(blackframe[:,int((width/3)*2)])

    #print("middle: ",mid)
    #print("left: ", left)
    #print("right: ", right)

    #nonze = np.where(blackframe[int(height/2),:]==0)

#    cv2.imshow('frame',blackframe)

        #print(nonze)

    value=[left, mid, right]

    return value

##    if cv2.waitKey(1) == ord('q'):
##        cap.release()
##        cv2.destroyAllWindows()

while True:
    camcap()



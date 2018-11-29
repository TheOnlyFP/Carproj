import numpy as np
import cv2
from threading import Thread



def camcap():
    global value
    cap = cv2.VideoCapture(0)
    threshhold=90
    width=80
    height=40
    ret = cap.set(3,80)
    ret = cap.set(4,40)
    ret, frame = cap.read()
    if cap.isOpened() == 0:
        cap.open(0)

    greyframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blackframe = cv2.threshold(greyframe, threshhold, 255, cv2.THRESH_BINARY)[1]

    mid = sum(blackframe[:,40])

    left = sum(blackframe[:,26])

    right = sum(blackframe[:,53])

    #print("middle: ",mid)
    #print("left: ", left)
    #print("right: ", right)

    #nonze = np.where(blackframe[int(height/2),:]==0)

    cv2.imshow('frame',blackframe)

        #print(nonze)

    if cv2.waitKey(1) == ord('q'):
        cap.release()
        cv2.destroyAllWindows()

    value=[left, mid, right]

    print(value)

    return value


camcap()



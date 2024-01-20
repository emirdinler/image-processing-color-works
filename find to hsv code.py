import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0 ,cv.CAP_DSHOW)
cv.namedWindow("frame")
cv.resizeWindow("frame", 300, 300)
def nothing(x):
    pass
cv.createTrackbar("lowerh", "frame", 0, 180, nothing)
cv.createTrackbar("lowers", "frame", 0, 255, nothing)
cv.createTrackbar("lowerv", "frame", 0, 255, nothing)

cv.createTrackbar("upperh", "frame", 0, 180, nothing)
cv.createTrackbar("uppers", "frame", 0, 180, nothing)
cv.createTrackbar("upperv", "frame", 0, 180, nothing)

cv.setTrackbarPos("upperh", "frame", 180)
cv.setTrackbarPos("uppers", "frame", 255)
cv.setTrackbarPos("upperv", "frame", 255)

while True:
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)

    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowerh = cv.getTrackbarPos("lowerh", "frame")
    lowers = cv.getTrackbarPos("lowers", "frame")
    lowerv = cv.getTrackbarPos("lowerv", "frame")

    upperh = cv.getTrackbarPos("upperh", "frame")
    uppers = cv.getTrackbarPos("uppers", "frame")
    upperv = cv.getTrackbarPos("upperv", "frame")

    lower_value = np.array([lowerh, lowers, lowerv])
    upper_value = np.array([upperh, uppers, upperv])

    mask = cv.inRange(frame_hsv, lower_value, upper_value)
    mask_result = cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow("original", frame)
    cv.imshow("mask", mask_result)
    if cv.waitKey(20) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
import cv2 as cv
import numpy as np

lowerb = np.array([75, 100, 100])
upperb = np.array([130, 255, 255])

video = cv.VideoCapture("")#The location of the video should be here
cv.namedWindow("frame", cv.WINDOW_AUTOSIZE)
while video.isOpened():
    ret, image = video.read()
    if ret:
        image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        img_inrange = cv.inRange(image_hsv, lowerb, upperb)
        img_mask = cv.bitwise_and(image, image, mask=img_inrange)
    if not ret:
        break
    cv.imshow("original", image)
    cv.imshow("frame", img_mask)
    if cv.waitKey(20) == ord('q'):
        break
cv.destroyAllWindows()

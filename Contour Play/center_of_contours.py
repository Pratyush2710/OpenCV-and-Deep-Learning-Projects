'''import cv2
import imutils



image = cv2.imread('tetris_blocks.png')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (4,4),0)

thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

'''

import imutils
import cv2

#load image as a grayscale
image = cv2.imread('puzzle.jpg',0)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', image)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('blurred', blurred)
thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('blurred', thresh)

# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

for c in cnts:
    M = cv2.moments(c)
    # to get center of contour

    # to check if m00 is zero or not to avoid DivisionByZero error
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0


    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.circle(image, (cX, cY), 5, (255, 255, 255), -1)
    cv2.putText(image, "center", (cX - 30, cY - 30),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    git
    cv2.imshow("Image", image)
    cv2.waitKey(0)


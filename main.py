import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "SUN",(130,50), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=2, color=(255,255,255))

cv2.putText(img, "MERCURY",(110,250), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "VENUS",(190,170), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "EARTH",(290,260), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "MARS",(380,170), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "JUPITER",(570,380), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "SATURN",(720,120), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "URANUS",(970,300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5, color=(255,255,255))

cv2.putText(img, "NEPTUNE",(1070,150), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=0.5, color=(255,255,255))

img = cv2.imshow("output",img)
cv2.waitKey(0)
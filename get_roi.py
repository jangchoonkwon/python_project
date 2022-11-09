import cv2
import numpy as np

scr_img = "d:/FineTec/DailyLoss/ocr/2022-06-02/20220602-joju-34.png"

img = cv2.imread(scr_img)

# x=320; y=150; w=50; h=50        # roi 좌표
# roi = img[y:y+h, x:x+w]
#
# x=320; y=150; w=50; h=50        # roi 좌표
# roi = img[710:790, 60:520]

cv2.imshow(img)
cv2.waitKey(0)

# print(roi.shape)                # roi shape, (50,50,3)
# cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0)) # roi 전체에 사각형 그리기 ---②
# cv2.imshow('img', img)
#
# key = cv2.waitKey(0)
# print(key)
# # cv2.destroyAllWindows()

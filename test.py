import numpy as np
# import cv2

# img = cv2.imread('edge-detect.png')
# imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(imgray,127,255,0)
# image ,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# #绘制独立轮廓，如第四个轮廓
# #imag = cv2.drawContour(img,contours,-1,(0,255,0),3)
# #但是大多数时候，下面方法更有用
# imag = cv2.drawContours(img,contours,3,(0,255,0),3)

# while(1):
#     cv2.imshow('img',img)
#     cv2.imshow('imgray',imgray)
#     cv2.imshow('image',image)
#     cv2.imshow('imag',imag)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cv2.destroyAllWindows()

area = np.array([[ 1., 0., 0.],
 [ 0., 1., 2.],[ 1., 0., 0.]])

print(area.ndim)
import pytesseract
import numpy as np
import cv2

def getImageMask(mask,area):
	for top,left,right,bottom in area:
		mask[top:bottom,left:right] = [0,0,0]
	return mask;

def presetMask(mask):
	return getImageMask(mask,[(0,0,160,100),(0,420,645,110),(457,0,645,510),(165,480,645,200)])

def dectDst(img):
	dstArea = img[(426-250):(463-250),(1115-633):(1275-633)]
	Lower = np.array([0, 0, 250])
	Upper = np.array([0, 0, 255])
	mask = cv2.inRange(dstArea, Lower, Upper)
	dstArea = cv2.bitwise_and(dstArea, dstArea, mask=mask)
	code = pytesseract.image_to_string(dstArea,lang="chi_sim")
	return code

def matchTemplate(img,template,threshold = 0.6):
	tempStr = "./template/%s.png" % (template)
	templ = cv2.imread(tempStr,0)
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	w, h = templ.shape[::-1]
	res = cv2.matchTemplate(img_gray,templ,cv2.TM_CCOEFF_NORMED)
	threshold = threshold
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	print(max_val)
	if(max_val < threshold):
		return None
	top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)
	cv2.rectangle(img, top_left, bottom_right, 0, 3)
	cv2.imshow(template,img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return (int(top_left[0] + w/2), int(top_left[1] + h/2))


if __name__=='__main__':
	img = cv2.imread('./image/c1.png')
	dstArea = matchTemplate(img,"current")
	img = cv2.imread('./image/c2.png')
	dstArea = matchTemplate(img,"current")
	img = cv2.imread('./image/c3.png')
	dstArea = matchTemplate(img,"current")
	img = cv2.imread('./image/c4.png')
	dstArea = matchTemplate(img,"current")
	img = cv2.imread('./image/c5.png')
	dstArea = matchTemplate(img,"current")
	img = cv2.imread('./image/c6.png')
	dstArea = matchTemplate(img,"current")
	img = cv2.imread('./image/c7.png')
	dstArea = matchTemplate(img,"current")
	if(dectDst):
		print(dstArea)
	cv2.destroyAllWindows()
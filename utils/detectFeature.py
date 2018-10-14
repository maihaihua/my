import pytesseract
import numpy as np
import cv2


def dectDst(img):
    dstArea = img[(426 - 250):(463 - 250), (1115 - 633):(1275 - 633)]
    Lower = np.array([0, 0, 250])
    Upper = np.array([0, 0, 255])
    mask = cv2.inRange(dstArea, Lower, Upper)
    dstArea = cv2.bitwise_and(dstArea, dstArea, mask=mask)
    code = pytesseract.image_to_string(dstArea, lang="chi_sim")
    return code

def getTargetFeature(image):
    result = cv2.absdiff(image,image)
    pass;

def getSamePossibility(image,target):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(image,target)
    unmatch = cv2.countNonZero(diff)
    h,w = image.shape[:2]
    size = w * h
    return unmatch/size

def dectFeature(image,target):
    th,tw = target.shape[:2]
    targetPoint = target[th//2,tw//2]
    h,w = image.shape[:2]
    results = []
    for i in range(h):
        for j in range(w):
            diff = cv2.absdiff(image[i,j],targetPoint)
            if(diff[0][0] == 0 and diff[1][0] == 0 and diff[2][0] == 0):
                # image[i,j] = (0,0,0)
                probality = getSamePossibility(image[(i-5):(i+5),(j-5):(j+5)],target[(th//2-5):(th//2+5),(tw//2-5):(tw//2+5)]);
                results.append((probality,i,j));
    probality = 1
    posX=0
    posY=0
    for i in range(len(results)):
        if(results[i][0] < probality):
            probality = results[i][0]
            posY = results[i][1]
            posX = results[i][2]
    print(posX,posY)
    cv2.rectangle(image,(posX - tw//2,posY-th//2),(posX + (tw - tw//2),posY++ (th - th//2)),(255,255,255),1)
    return image  

if __name__ == "__main__":    
    target = cv2.imread('./template/bjlb.png')
    # for i in range(1,8):
    #     tempStr = "./image/c%d.png" % (i)
    #     image = cv2.imread(tempStr)
    #     image = dectFeature(image,target)
    #     cv2.imshow(tempStr,image)
    image = cv2.imread('./image/dect-test.png')
    image = dectFeature(image,target)
    cv2.imshow('tempStr',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


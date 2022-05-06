
import cv2
from cvzone.PoseModule import PoseDetector


capture=cv2.VideoCapture(r'C:\Users\samsa\Downloads\Video\source.mp4')
detector=PoseDetector()
posList=[]
while True:
    success ,img=capture.read()
    cv2.imshow("image",img)
    img=detector.findPose(img)
    lmlist,boxinfo=detector.findPosition(img)
    if boxinfo:
        lmString= ''
        for lm in lmlist:
            lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[3]},'
        posList.append(lmString)
    

    cv2.imshow('image',img)
    key=cv2.waitKey(1)
    if key==ord('s'):
        with open('AnimationFile.txt','w') as f:
            f.writelines(['%s\n' % item for item in posList])
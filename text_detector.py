import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame',(800,800))
cv2.namedWindow('frame2',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame2',(800,800))

cv2.namedWindow('frame3',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame3',(800,800))
cv2.namedWindow('frame4',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame4',(800,800))



count = 0

cropped_folder="/home/ieshaan/Desktop/Python/Misc/FINAL_CROPPED2/"



dest = "/home/ieshaan/Desktop/Python/Misc/Text_Detect/"
masked = "/home/ieshaan/Desktop/Python/Misc/Masked_Data/"

for i in os.listdir(cropped_folder):
	img = cv2.imread(cropped_folder+str(i))
	gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	mser = cv2.MSER_create()
	im = img.copy()

	regions,_ = mser.detectRegions(gray_img)

	hulls = [cv2.convexHull(p.reshape(-1,1,2))for p in regions]
	
	cv2.polylines(im, hulls,1,(0,255,0),2)
	
	fname = dest + i[:-4] + '-t.png'

	mask = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8)

	for contour in hulls:
		cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)
	text_only = cv2.bitwise_and(im, im, mask=mask)

	print(count)
	if count == 10:
		cv2.imshow('frame',mask)
		cv2.imshow('frame2',gray_img)
		cv2.imshow('frame3',text_only)
		cv2.imshow('frame4',im)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	fn = masked+ i[:-4]+'-m.png'

	#cv2.imwrite(fn,text_only,[int(cv2.IMWRITE_PNG_COMPRESSION), 9])
	#cv2.imwrite(fname,im,[int(cv2.IMWRITE_PNG_COMPRESSION), 9])
	count +=1
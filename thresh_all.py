import cv2
import numpy as np
import os
import time
start_time = time.time()

src="/home/ieshaan/Desktop/Python/Misc/JpgCvt/"
dest="/home/ieshaan/Desktop/Python/Misc/Thresh/"



for i in os.listdir(src):
	if i.endswith('.png'):
		img = cv2.imread(src+i)
		img2 = img
		#print(i)
		
		rows,cols,_ = img.shape

		img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		_,mask = cv2.threshold(img2gray,200,255,cv2.THRESH_BINARY_INV)
		_,white = cv2.threshold(img2,255,255,cv2.THRESH_BINARY_INV)
		
		mask_inv = cv2.bitwise_not(mask)
		img1_fg = cv2.bitwise_and(white,white,mask=mask_inv)
		img2_bg = cv2.bitwise_and(img2,img2,mask=mask)

		dst = cv2.add(img2_bg,img1_fg)
		fname=dest+i[:-4]+'-thresh.png'
		cv2.imwrite(fname,dst)

print("--- %s seconds ---" % (time.time() - start_time))
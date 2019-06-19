import cv2
import os
import numpy as np

src_jpg = "/home/ieshaan/Desktop/Python/Misc/Document Classification Exercise/comm_jpg/"

cropped_jpg = "/home/ieshaan/Desktop/Python/Misc/Document Classification Exercise/crop_jpg/"

for i in os.listdir(src_jpg):
	img = cv2.imread(src_jpg + str(i))
	gray_seg = cv2.Canny(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),0,25)
	pts = np.argwhere(gray_seg>0)
	try:
		y1,x1 = pts.min(axis = 0)
		y2,x2 = pts.max(axis = 0)
		cropped = img[y1:y2, x1:x2]
		fname = cropped_jpg + i[:-4] + '-c.png'

		cv2.imwrite(fname,cropped, [int(cv2.IMWRITE_PNG_COMPRESSION),9])

	except ValueError:
		fname = cropped_jpg + i[:-4] + '-nc.png'
		cv2.imwrite(fname,img,[int(cv2.IMWRITE_PNG_COMPRESSION),9])


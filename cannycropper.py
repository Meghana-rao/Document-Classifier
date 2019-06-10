import cv2 
import numpy as np
import os
import time
start_time=time.time()

# Source folder
src="/home/ieshaan/Desktop/Python/Misc/JpgCvt/"
# Destination folder for Canny_cropper
tagged="/home/ieshaan/Desktop/Python/Misc/Canny_cropper/"
# Destination folder for non Canny
desn="/home/ieshaan/Desktop/Python/Misc/Blank_Pages/"
# Final Cropped pictures without data loss
cropped_folder="/home/ieshaan/Desktop/Python/Misc/FINAL_CROPPED/"

for i in os.listdir(src):
	img=cv2.imread(src+str(i))
	gray_seg = cv2.Canny(img,0,25)
	pts = np.argwhere(gray_seg>0)
	try:
		y1,x1 = pts.min(axis=0)
		y2,x2 = pts.max(axis=0)
		cropped = img[y1:y2, x1:x2]
		fname=cropped_folder+i[:-4]+'-C'+'.png'

		#tagged = cv2.rectangle(img.copy(), (x1,y1), (x2,y2), (0,255,0), 3, cv2.LINE_AA)
		#f_name=tagged+i[:-4]+'-Canny'+'.png'
		
		'''
		print(i)
		print('\t',	end='')
		print('x1: '+str(x1)+' y1: '+str(y1)+' x2: '+str(x2)+' y2: '+str(y2))
		print('\t',	end='')
		print(img.shape)
		print('\t',	end='')
		print(tagged.shape)
		print('\t',	end='')
		percentage=(y2-y1)*(x2-x1)*100/(img.shape[0]*img.shape[1])
		print('\t',	end='')
		print(percentage)
		print('\t',	end='')
		print(cropped.shape)
		'''

		cv2.imwrite(fname,cropped)
		#c2.imwrite(f_name,tagged)
	except ValueError:
		'''
		print(i)
		print("\tThis gives ValueError")
		'''
		fn=desn+i[:-4]+'-ncanny'+'.png'
		cv2.imwrite(fn,img)

print("--- %s seconds ---" % (time.time() - start_time))
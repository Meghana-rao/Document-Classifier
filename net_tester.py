#! python3
'''
net_tester.py

Running crop_split.py, cropper.py, tester.py

Please make sure you have these directories ready - 

cwd - This folder will contain all the subfolders which will contain the pdfs themselves 

dest - This folder will contain all the pdfs that have been divided into single pages

dest_jpg,src_jpg - This folder will contain all single pages pngs

cropped_png,folder_name - This folder will contain all the cropped pngs

src_label -  This will the path to label_image.py

src_graph - This will be the path to your graph that is produced after training your data

csv_file - This is the path of the csv_file if your data is already labelled and you want to test your model

'''
import subprocess

command_1 = "python3 -W ignore crop_split.py"
command_2 = "python3 -W ignore cropper.py"
command_3 = "python3 -W ignore tester.py"

test1 = subprocess.Popen(command_1,shell = True)

test2 = subprocess.Popen(command_2,shell = True)

test3 = subprocess.Popen(command_3,shell = True)
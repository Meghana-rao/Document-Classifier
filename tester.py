#! python3
# Purpose is to create a classification report and a confusion matrix

import csv,os
from sklearn.metrics import classification_report,confusion_matrix
import numpy as np
import subprocess

Encoder = {
"a":"Aadhar","b":"Community and Birth Certificate","c":"Marksheet","d":"Bonafide/Study and Conduct",
"e":"Income Certificate","f":"National Food Security Card","g":"Others","h":"Caste Certificate",
"i":"Blank Document","j":"EBC Certificate","k":"EBC application"}

csv_file = "/home/ieshaan/Desktop/Python/Misc/DocumentClassificationExercise/f26/data.csv"


src_label = "/home/ieshaan/Desktop/Python/Misc/DocumentClassificationExercise/CSV_Folder/tensorflow-for-poets-2/scripts/label_image.py"

src_graph = "/home/ieshaan/Desktop/Python/Misc/DocumentClassificationExercise/CSV_Folder/tensorflow-for-poets-2/tf_files/retrained_graph.pb"

folder_name = "/home/ieshaan/Desktop/Python/Misc/DocumentClassificationExercise/f26/"

class_list = []
file_list = []
count = 0
y_true = []
net_csv = []
files = []

for i in os.listdir(folder_name):
	files.append(i)

files.sort()

for i in range(len(files)):
	if files[i].endswith('.png'):
		print(i)
		file_path = os.path.join(folder_name,files[i])
		command = "python3 {} --graph={} --image={}".format(src_label,src_graph,file_path)

		test = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE)
		output, err = test.communicate()
		output = output.decode('utf-8')
		output = output.split('\n')

		file_list.append(file_path)
		class_list.append(output[3].split()[0])
		temp = []
		temp.append(file_path)
		temp.append(output[3].split()[0])
		net_csv.append(temp)

with open(csv_file) as fp:
	line = fp.readlines()

for i in range(len(line)):
	y_true.append(line[i][-2:-1])

with open(folder_name+'pred.csv') as fp1:
	writer = csv.writer(fp1)
	writer.writerows(net_csv)

'''
print("LineType")
print(type(line))
print("ClassType")
print(type(class_list))
print("True")
print(line[0][-2:-1])
print("File List")
print(file_list)
print("Class List")
print(class_list[0])
'''
print('\n Predictions \n')
print(class_list)
print('\n True Values \n')
print(y_true)

print(classification_report(y_true,class_list))
print(confusion_matrix(y_true,class_list))


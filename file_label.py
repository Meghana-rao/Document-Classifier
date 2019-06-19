import csv
import os
import shutil
count = 0
cwd = "/home/ieshaan/Desktop/Python/Misc/Document Classification Exercise/crop_jpg/"
f1 = "/home/ieshaan/Desktop/Python/Misc/Document Classification Exercise/f1/"
f2 = "/home/ieshaan/Desktop/Python/Misc/Document Classification Exercise/f2/"
f3 = "/home/ieshaan/Desktop/Python/Misc/Document Classification Exercise/f3/"
f4 = "/home/ieshaan/Desktop/Python/Misc/Document Classification Exercise/f4/"
f5 = "/home/ieshaan/Desktop/Python/Misc/Document Classification Exercise/f5/"
f6 = "/home/ieshaan/Desktop/Python/Misc/Document Classification Exercise/f6/"

all_files = []
for i in os.listdir(cwd):
	all_files.append(i)

all_files.sort()
var = 'label'

f1_data = []
for i in range(500):
	path_of_file = cwd + all_files[i]
	new_loc_of_file = f1 + all_files[i]
	shutil.move(path_of_file,new_loc_of_file)
	temp = []
	temp.append(all_files[i])
	temp.append(var)
	f1_data.append(temp)

with open(f1+'data.csv','w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(f1_data)
csvFile.close()


f2_data = []
for i in range(500,1000):
	path_of_file = cwd + all_files[i]
	new_loc_of_file = f2 + all_files[i]
	shutil.move(path_of_file,new_loc_of_file)
	temp = []
	temp.append(all_files[i])
	temp.append(var)
	f2_data.append(temp)

with open(f2+'data.csv','w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(f2_data)
csvFile.close()


f3_data = []
for i in range(1000,1500):
	path_of_file = cwd + all_files[i]
	new_loc_of_file = f3 + all_files[i]
	shutil.move(path_of_file,new_loc_of_file)
	temp = []
	temp.append(all_files[i])
	temp.append(var)
	f3_data.append(temp)

with open(f3+'data.csv','w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(f3_data)
csvFile.close()


f4_data = []
for i in range(1500,2000):
	path_of_file = cwd + all_files[i]
	new_loc_of_file = f4 + all_files[i]
	shutil.move(path_of_file,new_loc_of_file)
	temp = []
	temp.append(all_files[i])
	temp.append(var)
	f4_data.append(temp)

with open(f4+'data.csv','w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(f4_data)
csvFile.close()


f5_data = []
for i in range(2000,2500):
	path_of_file = cwd + all_files[i]
	new_loc_of_file = f5 + all_files[i]
	shutil.move(path_of_file,new_loc_of_file)
	temp = []
	temp.append(all_files[i])
	temp.append(var)
	f5_data.append(temp)

with open(f5+'data.csv','w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(f5_data)
csvFile.close()


f6_data = []
for i in range(2500,3000):
	path_of_file = cwd + all_files[i]
	new_loc_of_file = f6 + all_files[i]
	shutil.move(path_of_file,new_loc_of_file)
	temp = []
	temp.append(all_files[i])
	temp.append(var)
	f6_data.append(temp)

with open(f6+'data.csv','w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(f6_data)
csvFile.close()
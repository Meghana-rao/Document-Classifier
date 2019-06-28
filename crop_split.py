from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path
import os,csv
import time

start_time=time.time()
TOTAL_FILES = 0
folder=[]

#Edit source document folder here
cwd="/home/ieshaan/Desktop/Python/Misc/DocumentClassificationExercise/income/"

#Edit destination document folder here 
dest="/home/ieshaan/Desktop/Python/Misc/DocumentClassificationExercise/income_sorted/"

#Edit jpg destination folder here
dest_jpg="/home/ieshaan/Desktop/Python/Misc/DocumentClassificationExercise/income_png/"

errors = []

png_count = 0

for i in os.listdir(cwd):
	folder.append(i)

for j in range(len(folder)):
    count=0
    print(folder[j])
    for t in os.listdir(cwd+folder[j]+"/"):
        if t.endswith('.pdf') or t.endswith('.PDF'):
            count += 1
            TOTAL_FILES += 1
            print('\t',t)
            try:
                inputpdf = PdfFileReader(open(cwd+folder[j]+"/"+t, "rb"),strict=False)
                for k in range(inputpdf.numPages):
                    output = PdfFileWriter()
                    output.addPage(inputpdf.getPage(k))
                    f_name=str(folder[j])+"-f"+str(count)+"-p"+str(k+1)+".pdf"
                    with open(dest+f_name, "wb") as outputStream:
                        output.write(outputStream)
                    page=convert_from_path(dest + f_name,dpi=100);
                    fname=f_name[:-4]+ ".png";
                    page[0].save(dest_jpg+fname,'PNG');
                    png_count +=1
            except Exception as e:
                print(e)
                temp = []
                temp.append(t)
                temp.append(str(e))
                errors.append(temp)
path = "/home/ieshaan/Desktop/Python/Misc/DocumentClassificationExercise/"

with open(path+'data.csv','w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(errors)
csvFile.close()

print(TOTAL_FILES)
time_taken = time.time() - start_time
print("--- %s seconds ---" % (time_taken))

timer = ["Time"]
timer.append(str(time_taken))

files = ["TOTAL_FILES(PDF)"]
files.append(str(TOTAL_FILES))

no_of_png = ["PNG COUNT"]
no_of_png.append(str(png_count))

print(timer)
print(files)
print(no_of_png)


with open(path+'stats.csv','w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(timer)
    writer.writerows(files)
    writer.writerows(no_of_png)
csvFile.close()

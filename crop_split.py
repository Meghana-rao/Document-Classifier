from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path
import os,csv
import time

start_time=time.time()
TOTAL_FILES = 0
folder=[]

#Edit source document folder here
cwd="/home/ieshaan/Desktop/Python/Misc/Document Classification Exercise/community/"

#Edit destination document folder here 
dest="/home/ieshaan/Desktop/Python/Misc/Document Classification Exercise/Commmunity_Sorted/"

#Edit jpg destination folder here
dest_jpg="/home/ieshaan/Desktop/Python/Misc/Document Classification Exercise/comm_jpg/"

errors = []

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
            except Exception as e:
                print(e)
                errors.append(str(e))
path = "/home/ieshaan/Desktop/Python/Misc/Document Classification Exercise/"

with open(path+'data.csv','w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(errors)
csvFile.close()

print(TOTAL_FILES)
print("--- %s seconds ---" % (time.time() - start_time))
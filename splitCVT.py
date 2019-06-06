from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path
import os

count=0
folder=[]

#Edit source document folder here
cwd="/home/ieshaan/Desktop/Python/Misc/Documents/"
#Edit destination document folder here 
dest="/home/ieshaan/Desktop/Python/Misc/Doc_ind/"
#Edit jpg destination folder here
dest_jpg="/home/ieshaan/Desktop/Python/Misc/JpgCvt/"


#For all the document subfloders, splitting and storing them in a seperate file
for i in os.listdir(cwd):
	#print("/home/ieshaan/Desktop/Python/Misc/Documents/"+i+":")
	folder.append(i)
#Alphabetical folder sort
folder.sort()

#Dividing it into individual pdf files. 
for j in range(len(folder)):
	#print(folder[j])
	for t in os.listdir(cwd+folder[j]+"/"):
		if t.endswith('.pdf'):
			count+=1;
			
			inputpdf = PdfFileReader(open(cwd+folder[j]+"/"+t, "rb"),strict=False)
			for k in range(inputpdf.numPages):
    				output = PdfFileWriter()
    				output.addPage(inputpdf.getPage(k))
    				f_name=dest+"file-"+str(count)+"-"+t[:-4]+"-page"+str(k+1)+".pdf"
    				# Dividing PDF into one page PDF
    				with open(f_name, "wb") as outputStream:
    					output.write(outputStream)
    				# Converting PDF to JPEG
    				page=convert_from_path(f_name,dpi=300);
    				fname="file-"+str(count)+"-"+t[:-4]+"-page"+str(k+1)+".jpg";
    				page[0].save(dest_jpg+fname,'JPEG');
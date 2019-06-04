from PyPDF2 import PdfFileWriter, PdfFileReader

import os

count=0
folder=[]

#Edit source document folder here
cwd="/home/ieshaan/Desktop/Python/Misc/Documents/"
#Edit destination document folder here 
dest="/home/ieshaan/Desktop/Python/Misc/Doc_ind/"

#For all the document subfloders, splitting and storing them in a seperate file
for i in os.listdir(cwd):
	#print("/home/ieshaan/Desktop/Python/Misc/Documents/"+i+":")
	folder.append(i)
#Alphabetical folder sort
folder.sort()

#Dividing it into individual pdf files. 
for j in range(len(folder)):
	print(folder[j])
	for t in os.listdir(cwd+folder[j]+"/"):
		if t.endswith('.pdf'):
			count+=1;
			
			inputpdf = PdfFileReader(open(cwd+folder[j]+"/"+t, "rb"),strict=False)
			for k in range(inputpdf.numPages):
    				output = PdfFileWriter()
    				output.addPage(inputpdf.getPage(k))
    				with open(dest+"file-%d-%s-page%d-.pdf"%(count,t,k+1), "wb") as outputStream:		
        				output.write(outputStream)
	


# We are using tesseract python and numpy packages for this program for OCR

#import io
# We are importing and calling a number of packages or libraries
# Import tesseract (for python) - 'pip install pytesseract' in the terminal 
# Import numpy -"pip install numpy"

# We first called the package Tesseract- this is popular python package for OCR
# We also called numpy- this python package is used to calculating numerical value. 
# numpy is used for manuplating amd analyzing big datasets and numberical values for text
# Tesseract package refers code from numbpy

from PIL import Image
import pytesseract

# Using numpy instead of wand.image library 

import numpy as np

# Beloow is the old code
	# from wand.image import Image as wi
		# wand.image library is used to read and write images of various format
		# wand is also used to convert images from one form to anoother 

	#pdf = wi(filename = "sample2.pdf", resolution = 300)
	#pdfImage = pdf.convert('jpeg')

 	# imageBlobs = []

	# for img in pdfImage.sequence:
	# imgPage = wi(image = img)
	# imageBlobs.append(imgPage.make_blob('jpeg'))

 	# recognized_text = []

	# for imgBlob in imageBlobs:
	# im = Image.open(io.BytesIO(imgBlob))
	# text = pytesseract.image_to_string(im, lang = 'eng')
	# recognized_text.append(text)

	# print(recognized_text)

# using numpy package for image recognition insatead
# We are locating where we are in the path - assigning the working directory. 
# Driecting the code to find all the necessary files and folders. 
# It is better that you organize all the project related file. 

import os, sys
from os import path
os.chdir('C:\\Users\\nkhan29\\Documents\\GitHub\\pythonteachingcode\\')
 

# We downloaded the image and saved in the same directory as python VS code folder
filename = '1_python-ocr.jpg' #calling the input image to test Tesseract
img1 = np.array(Image.open(filename)) #assigning a new function 

# call tesseract form my loacl machine
# Had issue/error messages with Tessercat import 
# To resolve the issues, calling tesseractt via machine - by giving its path 

pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\nkhan29\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

#Assigning new function to read teh image we uploaded
text = pytesseract.image_to_string(img1)

#Printing the image
print (image)

from PIL import Image
import pytesseract
#import numpy as np

# Setting the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\nkhan29\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Loading the image
filename = '1_python-ocr.jpg'
img1 = Image.open(filename)

# Performing OCR on the image
text = pytesseract.image_to_string(img1, lang='eng')  # Language set to English

# Printing the extracted text
print(text)
if 'specific_keyword' in text:
    # Do something when the specific keyword is found
    print('Found the keyword!')
else:

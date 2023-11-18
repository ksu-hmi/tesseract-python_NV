from PIL import Image
import pytesseract

# Setting the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\nkhan29\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Loading the image for OCR
filename = '1_python-ocr.jpg'
img1 = Image.open(filename)

# Performing OCR on the image
text = pytesseract.image_to_string(img1, lang='eng')  # Extracting text from the image

# Printing the extracted text
print(text)

# Function to check for a specific keyword in the extracted text
def check_keyword(text, keyword):
    return keyword in text

# Defining the specific keyword to search for
specific_keyword = 'example_keyword'

# Checking for the specific keyword in the extracted text
if check_keyword(text, specific_keyword):
    print(f'Found the "{specific_keyword}" keyword!')
else:
    print(f'"{specific_keyword}" keyword not found.')

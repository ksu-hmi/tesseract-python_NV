# Python-OCR-Space
- OCR Document Scanning: To describe what the project is attempting to achieve, OCR is the technology used to convert images or scanned documents into machine-readable text. With this technology, we can write code to read the scanned text/images or by using APIs, to process what is written in the text or image. An OCR engine works by storing many different font and text image patterns as templates. The OCR software uses pattern-matching algorithms to compare text images, by going through each character, to its internal database. If the characters are recognized, it is called optical word recognition. Modern OCR systems use intelligent character recognition (ICR) technology to read the text in the same way humans do. Primarily there are two major steps for the image/text to be identified and then transmitted to OCR engine. We can also utilize this with APIs, where we send the text or image to an external server and the server will return the image. There are many online resources for that. one main one that we explored during our search was The free OCR API. It offers multiple langauages that are connected to the smae endpoint, and have option to work with diiferent programming langauges including python. The ocrspace package is designed to be a Python wrapper for the OCR SapceAPI which provides Optical Character Recognition (OCR) capabilities. The use case for the ocrspace package would be any scenario where there is a need to extract text from images or scanned documents programmatically.
- For the overall usefulness, benefits and expected value, project is useful in any scenarios or for any usecase where there is a need to extract the information from images and scanned documents. In sitautions and settings where there is a need to upload scanned documents or paper pdfs, transfering data into electronic systems, requires a lot of manual work. Similarly, usecases where large documents require scanning and extraction of relevant information can be very time consuming, redundant and error prone. This solution aims to transform manual workflows and processes into automated and digitalized workflows, with high precision. Overall objective is to improve efficiency, and enhance data timeliness, completeness, and quality. Also, support automation and minimize manual review and proceses. This can be especially useful and applicable to public health settings that receive paper fax on case reports on a regular basis. Delays or errors in the review and uploading on this information into electronic surveillance systems, can delay the disease response activities and put communities at risk of increased mortality and morbidity. Automated, digitalized processes leads to efficiency and improved data use for healthcare/public health agencies. There are also some limitations to be considered for any such project.  
I.	Best work in situations with high-resolution input, where foreground text is neatly segmented from the background.
II.	For text localization and detection, there are several parameters that may be adjusted and managed for high acuity

# Getting Started

To get started with the project, follow these steps:

# Installation:
- Install tesserct-ocr using this command:
    - On Ubuntu
      ```
      sudo apt-get install tesseract-ocr
      ```
    - On Mac
      ```
      brew install tesseract
      ```
    - On Windows, download installer from [here](https://github.com/UB-Mannheim/tesseract/wiki)


- Install python binding for tesseract, pytesseract, using this pip command:
  ```
  pip install pytesseract
  ```

- Install image processing library in python, pillow using this pip command:
  ```
  pip install pillow
  ```
  
**For working with pdf files:**
- Install imagemagick using this command:
    - On Ubuntu
      ```
      sudo apt-get install imagemagick
      ```
    - For other platforms, download installer from [here](https://imagemagick.org/script/download.php)


- Install python binding for imagemagick, wand, using this pip command:
  ```
  pip install wand
  ```
# Getting Help

If you need help with this project or have any questions, you can:

Check the project's documentation in the docs folder.

Open an issue in the GitHub repository.

Contact the project maintainers (see the "Maintainers" section below).

# Maintainers and Contributors

This project is actively maintained and contributions are welcome. 

The primary maintainers of the project are: Vivian Chima vchima and Nomana Khan NomKh

Feel free to reach out for project-related inquiries, contributions, or collaboration opportunities.

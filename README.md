# Find-Names-Inside-Your-PDF-Folder-Fast-and-Easy
Easily search for names or text inside a folder full of PDFs—even scanned ones. This tool uses OCR to read each PDF page and finds your search term, then copies matching PDFs to a separate folder for quick review. Perfect for handling lots of documents without manual searching.
# PDF OCR Name Search Tool

This Python tool scans PDF files using Optical Character Recognition (OCR) to detect if a specific name appears in their content. If a match is found, the corresponding PDF is copied to a designated folder.

---

##  Features

-  Converts PDF pages to images using `pdf2image`
-  Extracts text from images using `pytesseract` (Tesseract OCR)
-  Utilizes multiprocessing (`ProcessPoolExecutor`) for faster processing
-  Performs case-insensitive text search
-  Copies matched PDFs into the `matched_pdfs` folder
-  Cleans up temporary image files after processing

---

##  Requirements

- Python 3.6 or newer
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases) (required for `pdf2image`)

### Python Dependencies

Install the required packages:

pip install pytesseract pdf2image Pillow tqdm

### Output

![222](https://github.com/user-attachments/assets/6b24925e-74be-408c-a945-a3148780b7d0)
![Project](https://github.com/user-attachments/assets/3af5ca23-798a-4aa8-80fe-16697450eeaa)

import fitz
import pdb

from fitz._fitz import PDF_ENCRYPT_KEEP

input_file = "ExifTool.pdf"
barcode_file = "Chris_Hemsworth_Signature.png"
image_rectangle = fitz.Rect(450,20,550,120)
file_handle = fitz.open(input_file)
first_page = file_handle[0]
first_page.insertImage(image_rectangle, filename = barcode_file)
file_handle.save(file_handle.name, incremental=True, encryption=PDF_ENCRYPT_KEEP)
file_handle.close()
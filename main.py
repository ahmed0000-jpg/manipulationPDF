import os
from os import listdir
from PyPDF2 import PdfFileReader, PdfFileWriter
import fitz
from os.path import isfile, join
import pdb
from fitz._fitz import PDF_ENCRYPT_KEEP
pdf_file_path = 'python3-exiv2-readthedocs-io-en-latest.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')
output_folder_path = os.path.join(os.getcwd(), 'output')

pdf = PdfFileReader(pdf_file_path)

for page_num in range(pdf.numPages):
    pdfWriter = PdfFileWriter()
    pdfWriter.addPage(pdf.getPage(page_num))

    with open(os.path.join(output_folder_path, '{0}_Page{1}.pdf'.format(file_base_name, page_num+1)), 'wb') as f:
        pdfWriter.write(f)
        f.close()
output_folder_path = os.path.join(os.getcwd(), 'output')
barcode_file = "Chris_Hemsworth_Signature.png"
image_rectangle = fitz.Rect(450,20,550,120)
fichiers = [f for f in listdir("output") if isfile(join("output", f))]
for fichier in fichiers:
    input_file = os.path.join(output_folder_path,fichier)
    file_handle = fitz.open(input_file)
    first_page = file_handle[0]
    first_page.insertImage(image_rectangle, filename=barcode_file)
    file_handle.save(file_handle.name, incremental=True, encryption=PDF_ENCRYPT_KEEP)
    file_handle.close()
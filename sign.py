import os
from os import listdir
from os.path import isfile, join
import fitz
from fitz._fitz import PDF_ENCRYPT_KEEP
output_folder_path = os.path.join(os.getcwd(), 'output')
barcode_file = "signatures/Chris_Hemsworth_Signature.png"
image_rectangle = fitz.Rect(450,20,550,120)
fichiers = [f for f in listdir("output") if isfile(join("output", f))]
for fichier in fichiers:
    input_file = os.path.join(output_folder_path,fichier)
    file_handle = fitz.open(input_file)
    first_page = file_handle[0]
    first_page.insertImage(image_rectangle, filename=barcode_file)
    file_handle.save(file_handle.name, incremental=True, encryption=PDF_ENCRYPT_KEEP)
    file_handle.close()
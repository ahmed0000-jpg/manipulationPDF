import os
from os import listdir
from PyPDF2 import PdfFileReader, PdfFileWriter
import fitz
from os.path import isfile, join
import argparse
import pdb
from fitz._fitz import PDF_ENCRYPT_KEEP
from configparser import ConfigParser
def file_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise FileNotFoundError(string)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=file_path)

    parsed_args = parser.parse_args()

    pdf_file_path = parsed_args.path
    file_base_name = pdf_file_path.replace('.pdf', '')
    file_name = file_base_name.split("/")[1]
    file_name_extension = file_name + ".pdf"
    output_folder_path = os.path.join(os.getcwd(), 'output',file_name)
    if not os.path.isdir(output_folder_path):
        os.makedirs(output_folder_path)
    #pdb.set_trace()
    pdf_file_path = os.path.join(os.getcwd(), 'input', file_name_extension)
    pdf = PdfFileReader(pdf_file_path)
    #pdb.set_trace()

    for page_num in range(pdf.numPages):
        pdfWriter = PdfFileWriter()
        pdfWriter.addPage(pdf.getPage(page_num))

        with open(os.path.join(output_folder_path, '{0}_Page{1}.pdf'.format(file_name_extension, page_num+1)), 'wb') as f:
            pdfWriter.write(f)
            f.close()
    #pdb.set_trace()
    # problème 2
    file = 'config.ini'
    config = ConfigParser()
    config.read(file)
    path = config['file']['path']
    barcode_file = path
    image_rectangle = fitz.Rect(450,20,550,120)
    fichiers = [f for f in listdir(join("output",file_name)) if isfile(join("output",file_name, f))]
    for fichier in fichiers:
        input_file = os.path.join(output_folder_path,fichier)
        file_handle = fitz.open(input_file)
        first_page = file_handle[0]
        first_page.insertImage(image_rectangle, filename=barcode_file)
        file_handle.save(file_handle.name, incremental=True, encryption=PDF_ENCRYPT_KEEP)
        file_handle.close()
if __name__ == '__main__':
    main()
import pdfplumber, os, sys

from collections import OrderedDict
from typing import List, Dict, Tuple, Any, NewType
from PyPDF2 import PdfFileReader

PDF = NewType('PDF', str)
pdf_Files: List[PDF] = []

#path_to_pdf = os.chdir("../Data/")
path_to_pdf = os.path.normpath(os.getcwd() + os.sep + os.pardir)
'''
for dirpath, dirnames, filenames in os.walk(path):
    for filename in [f for f in filenames if f.endswith('.pdf')]:
        pdfFiles.append(os.path.join(dirpath, filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(filename)
'''
def look_for_fields_in_pdf(pdf_files):
    with pdfplumber.open(pdf_files) as pdf:
        first_page_of_pdf = pdf.pages[0]
        return dict(first_page_of_pdf.extract_text(x_tolerance=3, y_tolerance=3))

def create_ini_files(pdf_files):
    #print((pdf_files))
    file_path = os.path.abspath(pdf_files)
    #print(os.path.dirname(file_path))
    directory = os.path.dirname(file_path)
    ini_file = os.path.join(directory, os.path.splitext(os.path.basename(pdf_files))[0] + '.ini')
    with open(ini_file, 'w+') as ini:
        ini.write('test' + '\n')
    #print(os.path.splitext(os.path.basename(pdf_files))[0])
    #open(file_path, '%s.ini' ,'w') % ini_file
    #for pdf_file in pdf_files:
    #    print(pdf_files)
    #    for dirpath, dirnames, filenames in os.walk(path):
    #        for filename in [f for f in filenames if f.endswith(".pdf")]:
    #            pass
                #print(pdf_file)
                #print(os.path.splitext(os.path.basename(pdf_file))[0])
                #open(os.path.join(dirpath, '%s.ini' ) % (os.path.basename(pdf_file)[0],),'w')
        #for dirpath, dirnames, filenames in os.walk(pdf_file):
        #    base=os.path.basename(pdf_file)
        #    open(os.path.join(path,'Data/%s.ini') % (os.path.splitext(base))[0], 'w')

def look_for_pdf(path, pdf_files):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith(".pdf")]:
            #print(filename)
            pdf_file = os.path.join(dirpath, filename)
            #print(pdf_file)
            create_ini_files(pdf_file)
            pdf_files.append(os.path.join(dirpath, filename))
    #pdf_files
    #create_ini_files(path,pdf_files)




def main():
    look_for_pdf(path_to_pdf, pdf_Files)
    #for pdf_file in pdf_Files:
    #    print(pdf_file)

if __name__ == "__main__":
    main()

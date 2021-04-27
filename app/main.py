from typing import List, Dict, Tuple, Any, NewType
import PyPDF2, os, sys

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
def create_ini_files(path,pdf_files):
    for pdf_file in pdf_files:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in [f for f in filenames if f.endswith(".pdf")]:
                print(os.path.splitext(os.path.basename(pdf_file))[0])
                open(os.path.join(dirpath, '%s.ini' ) % (os.path.splitext(os.path.basename(pdf_file))[0],),'w')
        #for dirpath, dirnames, filenames in os.walk(pdf_file):
        #    base=os.path.basename(pdf_file)
        #    open(os.path.join(path,'Data/%s.ini') % (os.path.splitext(base))[0], 'w')

def look_for_pdf(path, pdf_files):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith(".pdf")]:
            #print(filename)
            pdf_files.append(os.path.join(dirpath, filename))
    #pdf_files
    create_ini_files(path,pdf_files)




def main():
    look_for_pdf(path_to_pdf, pdf_Files)
    #for pdf_file in pdf_Files:
    #    print(pdf_file)

if __name__ == "__main__":
    main()

import os

# clearing the screen
def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# take input pdf name
def takeInput(nopdf):
    return (input('Please enter the {} pdf full path with name = '.format(nopdf)))

# cheking input pdf extension
def checkInput(pdf):
    if pdf[-4:] == ('.pdf' or '.PDF'):
        return True
    else:
        return False

#page number function
def pageNumbers(pdf1, pdf1reader, pdf2, pdf2reader):
    print(" Total number of pages in the {} file is {}. ".format(pdf1, len(pdf1reader.pages)))
    print(" Total number of pages in the {} file is {}. ".format(pdf2, len(pdf2reader.pages)))
    input('')

# extracting text from pdf
def printPDFextract(pdfreader, pdf):
    total_page = len(pdfreader.pages)
    i = 0
    while(i < total_page):
        pageObj = pdfreader.pages[i]
        print("********** Page number {} from file {}. **********".format(i+1, pdf))
        print(pageObj.extract_text())
        i += 1
        if i >= total_page:
            print("**************************************************")
    input()

# comparing pdfs 
def comparePdfs(pdf1, pdf1reader, pdf2, pdf2reader):
    pdf1len = len(pdf1reader.pages)
    pdf2len = len(pdf2reader.pages)
    i = 0
    match = False
    while(i < pdf1len):
        page1obj = pdf1reader.pages[i]
        j = 0
        while(j < pdf2len):
            page2obj = pdf2reader.pages[j]
            if page1obj.extract_text() == page2obj.extract_text():
                if (not match):
                    match = True
                print("**************************************************************************************************************")
                print("***** Page number {} of file {} is matching with page number {} of file {}. ******".format(i + 1, pdf1, j + 1, pdf2))
                print("**************************************************************************************************************")
            j += 1
        i += 1
    if (not match):
        print("There are no matching pages between the files.")
    input()
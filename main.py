import PyPDF2
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
def pageNumbers(pdf1reader, pdf2reader):
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

print("This program is developed to do operations on two pdf files.")
pdf = takeInput('first')
correctname = checkInput(pdf)
while(not correctname):
    print("You have entered wrong format of file.")
    pdf = takeInput('first')
    correctname = checkInput(pdf)
    
if correctname:
    pdf1 = pdf

pdf = takeInput('second')
correctname = checkInput(pdf)
while(not correctname):
    print("You have entered wrong format of file.")
    pdf = takeInput('second')
    correctname = checkInput(pdf)

if correctname:
    pdf2 = pdf

pdf1obj = open(pdf1, 'rb') # pdf in binary object
pdf2obj = open(pdf2, 'rb') # pdf in binary object

pdf1reader = PyPDF2.PdfReader(pdf1obj) # reading pdf file
pdf2reader = PyPDF2.PdfReader(pdf2obj) # reading pdf file

loop_condition = True
while(loop_condition):
    clearScreen()
    
    print("Please choose your options from given below:--")
    print("   1. Know the page number in both the pdfs.")
    print("   2. Print the text from {} (Sometime it may not show the correct text due to different encoding formats).".format(pdf1))
    print("   3. Print the text from {} (Sometime it may not show the correct text due to different encoding formats).".format(pdf2))
    print("   4. Compare {} and {} files page wise.".format(pdf1, pdf2))
    print("   5. Exit from the program.")

    choice = input('      Enter your option number = ')
    if choice.isdigit():
        next_process = True
        choice = int(choice)
    else:
        next_process = False
    
    clearScreen()
    
    if  next_process and choice == 5:
        loop_condition = False
    elif next_process and choice == 1:
        pageNumbers(pdf1reader, pdf2reader)
    elif next_process and choice == 2:
        printPDFextract(pdf1reader, pdf1)
    elif next_process and choice == 3:
        printPDFextract(pdf2reader, pdf2)
    elif next_process and choice == 4:
        comparePdfs(pdf1, pdf1reader, pdf2, pdf2reader)
    else:
        print('==========================================')
        print('Wrong input. Please hit enter to continue.')
        input('==========================================')

clearScreen()

pdf1obj.close()
pdf2obj.close()
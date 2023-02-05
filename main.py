import PyPDF2
from functions import clearScreen, takeInput, checkInput, pageNumbers, printPDFextract, comparePdfs

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
        pageNumbers(pdf1, pdf1reader, pdf2, pdf2reader)
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